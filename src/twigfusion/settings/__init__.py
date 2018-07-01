import defusedxml.ElementTree as xml
import os.path
from apps.utils.functions import str_to_bool, get_unique_xml_element
from apps.utils.exceptions import XmlElementNotFound
from .base import *

class ConfigurationNotFound(Exception):
    '''The exception that is raised when configuration is not found.'''

class ConfigurationError(Exception):
    '''The exception that is raised when there is an error in configuration.'''

def configuration_bool_error(tag: str, value: str, attribute: str='enabled') -> str:
    '''Returns the error message when a boolean in the configuration file is invalid.
    
    Arguments:

        tag: The XML tag name.

        value: The value the boolean attribute was set to.

        attribute: The XML attribute name.

    '''

    return (
        f'The <{tag}> element has attribute enabled="{value}" in the configuration file. '
        f'Expected enabled="true" or enabled="false".'
    )

# Iterates through the list of possible file paths until the file is found.
# The first file that is found is used.
# The config_file variable is set only when a file is found.
for path in CONFIGURATION_FILE_PATHS:
    if os.path.isfile(path):
        config_path = path
        break

# Reads the configuration file.
# Raises an error if the file could not be found.
try:
    # Parse the XML file with defusedxml.
    config_file = xml.parse(config_path)
except NameError:
    # If no files were found in the paths specified, raise an error.
    paths = ''
    for path in CONFIGURATION_FILE_PATHS:
        paths += '\n\t' + path
    raise ConfigurationNotFound(
        'The configuration file could not be found '
        'in the paths specified:' + paths
    )

# Parse the XML root.
# This will serve as the config file variable.
config = config_file.getroot()

# If the root element isn't <website>, raise an error.
if config.tag != 'website':
    raise ConfigurationError('The XML root element is <{config.tag}>, expected <website>.')

try:
    # If the 'name' attribute is not the website name, raise an error.
    if config.get('name') != WEBSITE_NAME:
        raise ConfigurationError(
            f'The website name is \'{config.attrib['name']}\', '
            f'expected \'{WEBSITE_NAME}\'.'
        )
except NameError:
    # If WEBSITE_NAME is not defined, raise an error.
    raise ConfigurationError('The WEBSITE_NAME variable is not defined in the Django settings.')
except KeyError:
    # If there is no website name, raise an error.
    raise ConfigurationError('A website name was not specified in the configuration file.')

# Find the current website mode
# If the website mode is empty, raise an error.
mode_name = get_unique_xml_element(config, 'current-mode').text
if not mode_name:
    raise ConfigurationError('The current website mode was not specified.')

# Parse the modes list and find the current mode.
mode = None
for m in get_unique_xml_element(config, 'modes').findall('mode'):
    # Search the mode name attributes for the current mode
    if m.get('name') == mode_name:
        # Check that the current mode is unique. Raise an error if it isn't.
        # This is required to avoid confusion regarding which mode is used.
        if mode is None:
            mode = m
        else:
            raise ConfigurationError(
                'There is more than one mode with '
                f'the name \'{mode_name}\'.'
            )

# Import the settings file corresponding to the selected mode if it exists.
try:
    exec(f'from .{mode_name} import *')
except ModuleNotFoundError:
    pass

# Apply the DEBUG setting.
# If the current mode does not specify this setting, raise an error.
try:
    DEBUG = str_to_bool(get_unique_xml_element(mode, 'debug').get('enabled'))
except ValueError:
    raise ConfigurationError(configuration_bool_error('debug', get_unique_xml_element(mode, 'debug').get('enabled')))

# Apply the SECRET_KEY setting.
# If the current mode does not specify this setting, raise an error.
SECRET_KEY = get_unique_xml_element(mode, 'secret-key').text
if not SECRET_KEY:
    raise ConfigurationError(
        f'The <secret-key> element in the configuration '
        'file consists of an empty string.'
    )

# Apply database configurations if applicable.
database = get_unique_xml_element(mode, 'database')
database_keys = [
    # The accepted database configuration data.
    'engine',
    'name',
    'user',
    'password',
    'host',
    'port',
]
for key in database_keys:
    try:
        DATABASES['default'][key] = get_unique_xml_element(database, key).text
    except XmlElementNotFound:
        pass

# Applies Google services configuration data if applicable
try:
    google = get_unique_xml_element(mode, 'google')

    try:
        GOOGLE_SITE_VERIFICATION = get_unique_xml_element(google, 'site-verification').text
    except XmlElementNotFound:
        
    # TODO: Implement reCAPTCHA support.
    try:
        recaptcha = get_unique_xml_element(google, 'recaptcha')

        try:
            recaptcha_enabled = str_to_bool(recaptcha.get('enabled'))
        except XmlElementNotFound:
            recaptcha_enabled = False

        if recaptcha_enabled:
            try:
                RECAPTCHA_PUBLIC_KEY = get_unique_xml_element(recaptcha, 'public-key').text
            except XmlElementNotFound:
                raise ConfigurationError('The reCAPTCHA public key is required when reCAPTCHA is enabled.')
                        try:
                RECAPTCHA_PRIVATE_KEY = get_unique_xml_element(recaptcha, 'private-key').text
            except XmlElementNotFound:
                raise ConfigurationError('The reCAPTCHA private key is required when reCAPTCHA is enabled.')

        del recaptcha

    except XmlElementNotFound:
        pass

    del google

except XmlElementNotFound:
    pass

# Applies analytics configurations if applicable.
try:
    analytics = get_unique_xml_element(mode, 'analytics')

    try:
        ANALYTICAL_INTERNAL_IPS = []

        for ip in get_unique_xml_element(analytics, 'internal-ips'):
            # Iterate through the list of IP addresses.
            if ip.tag = 'address':
                # Only use IP addresses in the <address> tags.
                ANALYTICAL_INTERNAL_IPS.append(ip)

        del analytics
    except XmlElementNotFound:
        pass
    try:
        ANALYTICAL_AUTO_IDENTIFY = str_to_bool(
            get_unique_xml_element(analytics, 'auto-identify').get('enabled')
        )
    except XmlElementNotFound:
        pass

    # Applies Google Analytics configurations if applicable
    try:
        google_analytics = get_unique_xml_element(analytics, 'google')

        if str_to_bool(google_analytics.get('enabled')):
            try:
                GOOGLE_ANALYTICS_PROPERTY_ID = get_unique_xml_element(google_analytics, 'id').text
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_SITE_SPEED = get_unique_xml_element(google_analytics, 'sample-rate').text
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = str_to_bool(
                    get_unique_xml_element(google_analytics, 'display-advertising').get('enabled')
                )
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_SITE_SPEED = str_to_bool(
                    get_unique_xml_element(google_analytics, 'site-speed').get('enabled')
                )
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE = get_unique_xml_element(google_analytics, 'site-speed').get('sample-rate')
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_ANONYMIZE_IP = str_to_bool(
                    get_unique_xml_element(google_analytics, 'anonymize-ip').get('enabled')
                )
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_SESSION_COOKIE_TIMEOUT = get_unique_xml_element(google_analytics, 'cookie-timeout').get('session')
            except XmlElementNotFound:
                pass
            try:
                GOOGLE_ANALYTICS_VISITOR_COOKIE_TIMEOUT = get_unique_xml_element(google_analytics, 'cookie-timeout').get('visitor')
            except XmlElementNotFound:
                pass
            except

        del google_analytics

    except XmlElementNotFound:
        pass

    # Applies Matomo (Piwik) configurations if applicable
    try:
        matomo = get_unique_xml_element(analytics, 'matomo')

        if str_to_bool(matomo.get('enabled')):
            try:
                PIWIK_SITE_ID  = get_unique_xml_element(matomo, 'id').text
            except XmlElementNotFound:
                pass
            try:
                PIWIK_DOMAIN_PATH  = get_unique_xml_element(matomo, 'server').text
            except XmlElementNotFound:
                pass

        del matomo

    except XmlElementNotFound:
        pass

del analytics

except XmlElementNotFound:
    pass

# Delete non-settings variables
del config_file
del config
del mode_name
del mode
del database
del database_keys

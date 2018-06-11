import configparser
import os.path
from .base import *

class ConfigurationNotFound(Exception):
    '''The exception that is raised when configuration is not found.'''

class ConfigurationError(Exception):
    '''The exception that is raised when there is an error in configuration.'''

config_file = configparser.ConfigParser()

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
    config_file.read(config_path)
except NameError:
    paths = ''
    for path in CONFIGURATION_FILE_PATHS:
        paths += '\n\t' + path
    raise ConfigurationNotFound('The '+ WEBSITE_NAME +'.ini file could not be found in the paths specified:' + paths)

# Applies the website mode.
try:
    MODE = config_file[WEBSITE_NAME]['mode']
except KeyError:
    raise ConfigurationError('The \''+ WEBSITE_NAME +'\' section or website mode is undefined.')

# Creates the 'config' variable conataining 
# the INI section corresponding to the website mode.
config = config_file['mode.{0}'.format(MODE)]

# Applies the required configuration data.
try:
    DEBUG = bool(int(config['debug']))
    SECRET_KEY = config['secret_key']
except KeyError:
    raise ConfigurationError(
        'The mode \'{0}\' is undefined or is missing required keys.'.format(MODE))

# Applies database configurations if applicable
db_config_keys = [
    'ENGINE',
    'NAME',
    'USER',
    'PASSWORD',
    'HOST',
    'PORT',
]
for key in db_config_keys:
    try:
        DATABASES['default'][key] = config['db.{0}'.format(key.lower())]
    except KeyError:
        pass

# Applies analytics configurations if applicable
try:
    ANALYTICAL_INTERNAL_IPS = config['analytics.meta.internal_ips'].split(',')
except KeyError:
    pass
try:
    ANALYTICAL_AUTO_IDENTIFY = bool(int(config['analytics.meta.auto_identify']))
except KeyError:
    pass

try:
    if bool(int(config['analytics.google.enabled'])):
        try:
            GOOGLE_ANALYTICS_PROPERTY_ID = config['analytics.google.id']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = config['analytics.google.display_advertising']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_SITE_SPEED = config['analytics.google.site_speed']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_ANONYMIZE_IP = config['analytics.google.anonymize_ip']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_SAMPLE_RATE = config['analytics.google.sample_rate']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE = config['analytics.google.site_speed_sample_rate']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_SESSION_COOKIE_TIMEOUT = config['analytics.google.session_cookie_timeout']
        except KeyError:
            pass
        try:
            GOOGLE_ANALYTICS_VISITOR_COOKIE_TIMEOUT = config['analytics.google.visitor_cookie_timeout']
        except KeyError:
            pass
except KeyError:
    pass

try:
    if bool(int(config['analytics.matomo.enabled'])):
        try:
            PIWIK_DOMAIN_PATH = config['analytics.matomo.id']
        except KeyError:
            pass
        try:
            PIWIK_DOMAIN_PATH = config['analytics.matomo.server']
        except KeyError:
            pass
except KeyError:
    pass

# Applies additional configuration data if applicable
try:
    GOOGLE_SITE_VERIFICATION = config['google.site_verification']
except KeyError:
    GOOGLE_SITE_VERIFICATION = ''

try:
    exec('from .{0} import *'.format(MODE))
except ImportError:
    raise ConfigurationError('Could not import settings file for the mode \'{0}\'.'.format(MODE))

# Delete non-settings variables
del config_path
del config_file
del config
del db_config_keys

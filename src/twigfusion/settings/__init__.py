import defusedxml.ElementTree as xml
import os.path
from apps.utils.functions import str_to_bool, get_unique_xml_element
from .base import *

class ConfigurationNotFound(Exception):
    '''The exception that is raised when configuration is not found.'''

class ConfigurationError(Exception):
    '''The exception that is raised when there is an error in configuration.'''

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
    raise ConfigurationError(
        'The <debug> element consists of '
        f'<debug enabled="{get_unique_xml_element(mode, 'debug').get('enabled')}" />'
        'in the configuration file. '
        'Expected <debug enabled="true" /> or <debug enabled="false" />'
    )

# Apply the SECRET_KEY setting.
# If the current mode does not specify this setting, raise an error.
SECRET_KEY = get_unique_xml_element(mode, 'secret-key').text
if not SECRET_KEY:
    raise ConfigurationError(
        f'The <secret-key> element in the configuration '
        'file consists of an empty string.'
    )

# Delete non-settings variables
del config_file
del config
del mode_name
del mode

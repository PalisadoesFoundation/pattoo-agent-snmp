"""Configures snmp agent."""
import os
from pattoo_shared.installation import configure, shared
from pattoo_shared import files


def install(daemon_list):
    """Start configuration process.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    if os.environ.get('PATTOO_CONFIGDIR') is None:
        os.environ['PATTOO_CONFIGDIR'] = '{0}etc{0}pattoo'.format(os.sep)
    config_directory = os.environ.get('PATTOO_CONFIGDIR')

    snmp_agent_dict = {
            'polling_interval': 300,
    }

    # Attempt to create configuration directory
    files.mkdir(config_directory)

    # Create the pattoo user and group
    configure.create_user('pattoo', '/nonexistent', ' /bin/false', True)

    # Attempt to change the ownership of the configuration directory
    shared.chown(config_directory)

    for daemon in daemon_list:
        config_file = configure.pattoo_config(
                                            daemon,
                                            config_directory,
                                            snmp_agent_dict)

        configure.check_config(config_file, snmp_agent_dict)
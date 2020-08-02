"""Install necesary packages to run the snmp agent."""
from pattoo_shared.installation import configure, shared, packages

# Since distro is a dependency for pattoo shared, its safe to import
import distro


def install_dependencies():
    """Install the necessary system dependencies for the snmp agent.

    Args:
        None

    Returns:
        None
    """
    # Initialize key variables
    distribution = distro.id()

    if distribution == 'debian' or distribution == 'ubuntu':
        # Say what we are doing
        print('Installing easy snmp dependencies...')

        # Install net-snmp with package manager
        shared.run_script(
                    'sudo apt-get install libsnmp-dev snmp-mibs-downloader')

        # Install easy snmp dependencies
        shared.run_script(
            'sudo apt-get install gcc python-dev')

    elif distribution == 'rhel' or distribution == 'centos':
        # Install net-snmp with package manager
        shared.run_script(
            'sudo yum install net-snmp-devel')

        # Install easy snmp dependencies
        shared.run_script(
            'sudo yum install gcc python-devel')

    # Die if distribution isn't debian or rhel based
    else:
        shared.log('''\
Your operating system does not support Net-SNMP 5.7.x \n \
Please follow this guide to build and install Net-SNMP 5.7.x on your system \
        http://www.net-snmp.org/docs/INSTALL.html''')


def install(requirements_dir):
    """Ensure packages necessary for starting the snmp agent are installed.

    Args:
        requirements_dir: The directory with the pip_requirements.txt file

    Returns:
        None
    """
    # Install easysnmp dependencies
    install_dependencies()

    # Install pip packages
    packages.install(requirements_dir)

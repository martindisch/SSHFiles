from setuptools import setup

setup(
    name="sshfiles",
    version="1.0.0",
    description="Recursively list files and their SFTP URLs from a directory",
    packages=['sshfiles'],
    include_package_data=True,
    install_requires=['flask', 'gunicorn']
)

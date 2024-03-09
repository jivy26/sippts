"""Setup script for SIPPTS - a toolset for various network tasks."""

from setuptools import setup, find_packages

# Define your package's metadata here.
PACKAGE_NAME = "SIPPTS"
VERSION = "0.1.0"  # Update this with your current version
AUTHOR = "Your Name"  # Replace with your name
AUTHOR_EMAIL = "your.email@example.com"  # Replace with your email
DESCRIPTION = "Forked SIPPTS for PyPi Publishing "
URL = "https://github.com/jivy26/sippts/"
LICENSE = "MIT"  # Update this according to your package's license
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
INSTALL_REQUIRES = [
    # Add your package dependencies here, if any.
]

scripts=[
    "bin/arpspoof",
    "bin/rtcpbleed",
    "bin/rtpbleed",
    "bin/rtpbleedflood",
    "bin/rtpbleedinject",
    "bin/sipdigestcrack",
    "bin/sipdigestleak",
    "bin/sippcapdump",
    "bin/sipenumerate",
    "bin/sipexten",
    "bin/sipflood",
    "bin/sipfuzzer",
    "bin/sipinvite",
    "bin/sipping",
    "bin/siprcrack",
    "bin/sipscan",
    "bin/sipsend",
    "bin/sipsniff",
    "bin/siptshark",
    "bin/wssend",
]

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url=URL,
        license=LICENSE,
        classifiers=CLASSIFIERS,
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES,
        scripts=scripts,
        python_requires='>=3.6',
    )

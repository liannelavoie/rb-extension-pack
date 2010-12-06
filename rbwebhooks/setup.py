from setuptools import setup, find_packages

PACKAGE="RB-WEBHOOKS"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Webhooks extension for Review Board""",
    author="Lianne Lavoie",
    packages=["rbwebhooks"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbwebhooks.extension:WebhooksExtension' % PACKAGE,
    },
    package_data={
        'rbwebhooks': [
            'templates/rbwebhooks/*.html',
        ],
    }
)

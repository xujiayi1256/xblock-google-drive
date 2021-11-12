"""Setup for my_google_drive XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock-google-drive',
    version='0.1',
    description='An XBlock which allows embedding of Google documents and calendar within an edX course',
    packages=[
        'google_drive',
    ],
    install_requires=[
        'mako',
        'XBlock',
        'xblock-utils',
    ],
    dependency_links=[
        'git+https://github.com/Learningtribes/xblock-utils.git@hawthorn#egg=xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'google-document = google_drive:GoogleDocumentBlock',
            'google-calendar = google_drive:GoogleCalendarBlock'
        ]
    },
    package_data=package_data("google_drive", ["static", "templates", "public"]),
)

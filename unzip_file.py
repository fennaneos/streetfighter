#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Download and unzip a ZIP file
Version: 1.0
Python 3.7+
Date created: May 12th, 2021
Date modified: -
"""

import requests
import zipfile

# link to split ryu gif to frames
URL = 'https://ezgif.com/zip/ezgif-3-ee7612dc67-gif-im'


def fetch_zip_file():
    # Try to get the ZIP file
    try:
        response = requests.get(URL)
    except OSError:
        print('No connection to the server!')
        return None

    # check if the request is succesful
    if response.status_code == 200:
        # Save dataset to file
        print('Status 200, OK')
        open('sources-csv.zip', 'wb').write(response.content)
    else:
        print('ZIP file request not successful!.')
        return None


def main():
    # Get the ZIP file
    fetch_zip_file()

    # Unzip
    with zipfile.ZipFile('sources-csv.zip', 'r') as zip_ref:
        zip_ref.extractall('assets/ryu')


if __name__ == '__main__':
    main()
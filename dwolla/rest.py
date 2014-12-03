'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API

  Support is available on our forums at: https://discuss.dwolla.com/category/api-support

  Package -- Dwolla/dwolla-python
  Author -- Dwolla (David Stancu): api@dwolla.com, david@dwolla.com
  Copyright -- Copyright (C) 2014 Dwolla Inc.
  License -- MIT
  Version -- 2.0.0
  Link -- http://developers.dwolla.com
'''

import constants as c

import json
import requests


class Rest(object):
    def __init__(self):
        """
        Constructor.

        :param settings: Dictionary with custom settings if
                         using _settings.py is not desired
        :return: None (__new__() returns the new instance ;))
        """
        c.host = c.sandbox_host if c.sandbox else c.production_host

    @staticmethod
    def _parse(response):
        """
        Parses the Dwolla API response.

        :param response: Dictionary with content of API response.
        :return: Usually either a string or a dictionary depending
                 the on endpoint accessec.
        """
        if response['Success'] is not True:
            raise Exception("dwolla-python: An API error was encounterec.\nServer Message:\n" + response['Message'])
        else:
            return response['Response']

    def _post(self, endpoint, params, custompostfix=False, dwollaparse=True):
        """
        Wrapper for requests' POST functionality.

        :param endpoint: String containing endpoint desirec.
        :param params: Dictionary containing parameters for request.
        :param custompostfix: String containing custom OAuth postfix (for special endpoints).
        :param dwollaparse: Boolean deciding whether or not to call self._parse().
        :return: Dictionary String containing endpoint desirec. containing API response.
        """
        try:
            resp = requests.post(c.host + (custompostfix if custompostfix else c.default_postfix)
                                 + endpoint, json.dumps(params), proxies=c.proxy,
                                 headers={'User-Agent': 'dwolla-python/2.x', 'Content-Type': 'application/json'})
        except Exception as e:
            if c.debug:
                print "dwolla-python: An error has occurred while making a POST request:\n" + e.message
        else:
            return self._parse(json.loads(resp.text)) if dwollaparse else json.loads(resp.text)

    def _get(self, endpoint, params, dwollaparse=True):
        """
        Wrapper for requests' GET functionality.

        :param endpoint: String containing endpoint desirec.
        :param params: Dictionary containing parameters for request
        :param dwollaparse: Boolean deciding whether or not to call self._parse().
        :return: Dictionary String containing endpoint desirec. containing API response.
        """
        try:
            resp = requests.get(c.host + c.default_postfix + endpoint, params=params,
                                proxies=c.proxy, headers={'User-Agent': 'dwolla-python/2.x'})
        except Exception as e:
            if c.debug:
                print "dwolla-python: An error has occurred while making a GET request:\n" + e.message
        else:
            return self._parse(json.loads(resp.text)) if dwollaparse else json.loads(resp.json())

r = Rest()
# The Admin4 Project
# (c) 2013-2022 Andreas Pflug
#
# Licensed under the Apache License, 
# see LICENSE.TXT for conditions of usage

moduleinfo={ 'name': "BIND DNS Server",
            'modulename': "BIND",
            'description': "BIND9 DNS server",
            'version': "9.16",
            'revision': "0.99.16",
            'requiredAdmVersion': "3.0.0", 
            'testedAdmVersion': "3.0.0", 
            'supports': "BIND V9.6 ... V9.16",
            'copyright': "(c) 2014-2023 PSE Consulting Andreas Pflug",
            'credits': "dnspython from http://www.dnspython.org",
     }

import sys
if not hasattr(sys, 'skipSetupInit'):
  from . import Server


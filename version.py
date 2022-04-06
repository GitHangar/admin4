# The Admin4 Project
# (c) 2013-2022 Andreas Pflug
#
# Licensed under the Apache License, 
# see LICENSE.TXT for conditions of usage


import sys
if not hasattr(sys, 'frozen'):
  import wx
  if wx.VERSION < (4,1,1):
    raise Exception("wx Version too old")  
try:
  from __version import *  # @UnusedWildImport
except:
  version="3.x-nightly"
  modDate=None
  revDate=None
  tagDate=None
  revLocalChange=True
  revDirty=True
  revOriginChange=True
  requiredAdmVersion="3.0"


class Version:
  def __init__(self, version):
    self.version=str(version)
    
  def str(self):
    return self.version

  def __str__(self):
    return self.version
  
  def fullver(self):
    ver=[]
    if self.version:
      for v in self.version.split('.'):
        ver.append("%03d" % int(v))
    return ".".join(ver)
  
  def __lt__(self, cmp):
    return self.fullver() < cmp.fullver()

  def __le__(self, cmp):
    return self.fullver() <= cmp.fullver()

  def __gt__(self, cmp):
    return self.fullver() > cmp.fullver()
  
  def __ge__(self, cmp):
    return self.fullver() >= cmp.fullver()
  
  def __eq__(self, cmp):
    return self.fullver() == cmp.fullver()
  
  def __ne__(self, cmp):
    return self.fullver() != cmp.fullver()
  
version=Version(version)



requiredAdmVersion=Version(requiredAdmVersion)
libVersion=Version("3.0.0")

appName="Admin4"
description="4th generation\nAdministration Tool\n\nHelp and manual: http://www.admin4.org/docs"
vendor="PSE"
vendorDisplay="PSE Consulting"
copyright="(c) 2013-2022 PSE Consulting Andreas Pflug"
license="Apache License V2.0"
author="PSE Consulting Andreas Pflug"

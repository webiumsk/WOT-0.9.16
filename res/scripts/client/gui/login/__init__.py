# 2016.10.11 22:10:03 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/login/__init__.py
from gui import GUI_SETTINGS
if GUI_SETTINGS.socialNetworkLogin['enabled']:
    from social_networks import Manager, SOCIAL_NETWORKS
    g_loginManager = Manager()
else:
    from Manager import Manager
    g_loginManager = Manager()
__all__ = ['g_loginManager']
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\login\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:03 St�edn� Evropa (letn� �as)

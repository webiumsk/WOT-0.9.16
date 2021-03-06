# 2016.10.11 22:11:10 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/crewOperations/__init__.py
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.crewOperations.CrewOperationsPopOver import CrewOperationsPopOver
    from gui.Scaleform.daapi.view.lobby.crewOperations.RetrainCrewWindow import RetrainCrewWindow
    return (GroupedViewSettings(VIEW_ALIAS.CREW_OPERATIONS_POPOVER, CrewOperationsPopOver, 'crewOperationsPopOver.swf', ViewTypes.WINDOW, 'crewOperationsPopOver', VIEW_ALIAS.CREW_OPERATIONS_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE), GroupedViewSettings(VIEW_ALIAS.RETRAIN_CREW, RetrainCrewWindow, 'retrainCrewWindow.swf', ViewTypes.TOP_WINDOW, 'retrainCrewWindow', None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (CrewOpsBusinessHandler(),)


class CrewOpsBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.CREW_OPERATIONS_POPOVER, self.loadViewByCtxEvent), (VIEW_ALIAS.RETRAIN_CREW, self.loadViewByCtxEvent))
        super(CrewOpsBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\crewoperations\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:11:10 St�edn� Evropa (letn� �as)

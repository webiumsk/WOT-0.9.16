# 2016.10.11 22:11:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/MotiveQuestsDetails.py
from gui.Scaleform.daapi.view.meta.TutorialHangarQuestDetailsMeta import TutorialHangarQuestDetailsMeta
from gui.server_events import settings, g_eventsCache
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers

class MotiveQuestDetails(TutorialHangarQuestDetailsMeta):

    def getSortedTableData(self, tableData):
        return events_helpers.getSortedTableData(tableData)

    def requestQuestInfo(self, questID):
        svrEvents = g_eventsCache.getMotiveQuests()
        event = svrEvents.get(questID)
        settings.visitEventGUI(event)
        info = None
        if event is not None:
            info = events_helpers.getEventDetails(event, svrEvents)
        self.as_updateQuestInfoS(info)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\server_events\motivequestsdetails.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:11:58 St�edn� Evropa (letn� �as)

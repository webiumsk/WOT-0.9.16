# 2016.10.11 22:13:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/fortifications/fort_helpers.py
import calendar
import datetime
import time
from adisp import process
from account_helpers.AccountSettings import AccountSettings
from constants import PREBATTLE_TYPE
from FortifiedRegionBase import NOT_ACTIVATED
from gui import DialogsInterface, SystemMessages
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.daapi.view.dialogs.rally_dialog_meta import UnitConfirmDialogMeta
from gui.shared.fortifications.context import CreateOrJoinFortBattleCtx
from gui.shared.fortifications.settings import ROSTER_INTRO_WINDOW
from helpers import time_utils

def adjustDefenceHourToUTC(defenceHour):
    date = datetime.datetime.now()
    currentDefenceHourStart = datetime.datetime(date.year, date.month, date.day, defenceHour)
    localTime = time.mktime(currentDefenceHourStart.timetuple())
    return time.gmtime(localTime).tm_hour


def adjustDefenceHourToLocal(defenceHour, timestamp = None):
    timestamp = timestamp or time_utils.getCurrentTimestamp()
    localtime = time.localtime(time_utils.getTimeForUTC(timestamp, defenceHour))
    return (localtime.tm_hour, localtime.tm_min)


def adjustDefenceHoursListToLocal(hList):
    result = []
    for defH in hList:
        result.append(adjustDefenceHourToLocal(defH)[0])

    return result


def adjustVacationToUTC(vacationStart, vacationDuration):
    vacationStart, _ = time_utils.getDayTimeBoundsForUTC(vacationStart)
    return (vacationStart, vacationDuration)


def adjustOffDayToUTC(offDay, defenceHour):
    return __adjustOffDay(offDay, defenceHour)


def adjustOffDayToLocal(offDay, defenceHour):
    return __adjustOffDay(offDay, defenceHour, False)


def __adjustOffDay(offDay, defenceHour, toUTC = True):
    if offDay != NOT_ACTIVATED and time.timezone:
        weekDays = tuple(calendar.Calendar().iterweekdays())
        timezoneHourOffset = abs(getTimeZoneOffset())
        isPositiveOffset = getTimeZoneOffset() < 0
        if isPositiveOffset:
            if defenceHour < timezoneHourOffset:
                if toUTC:
                    offDay -= 1
                else:
                    offDay += 1
        elif defenceHour + timezoneHourOffset >= 24:
            if toUTC:
                offDay += 1
            else:
                offDay -= 1
        if offDay == len(weekDays):
            offDay = weekDays[0]
        elif offDay == -1:
            offDay = weekDays[-1]
    return offDay


def getTimeZoneOffset():
    return float(time.timezone) / time_utils.ONE_HOUR


@process
def tryToConnectFortBattle(battleID, peripheryID):
    from gui.prb_control.dispatcher import g_prbLoader
    yield lambda callback: callback(None)
    if g_lobbyContext.isAnotherPeriphery(peripheryID):
        if g_lobbyContext.isPeripheryAvailable(peripheryID):
            result = yield DialogsInterface.showDialog(UnitConfirmDialogMeta(PREBATTLE_TYPE.FORT_BATTLE, 'changePeriphery', messageCtx={'host': g_lobbyContext.getPeripheryName(peripheryID)}))
            if result:
                g_prbLoader.getPeripheriesHandler().join(peripheryID, CreateOrJoinFortBattleCtx(battleID, waitingID='fort/fortBattle/createOrJoin'))
        else:
            SystemMessages.pushI18nMessage('#system_messages:periphery/errors/isNotAvailable', type=SystemMessages.SM_TYPE.Error)
    else:
        yield g_prbLoader.getDispatcher().join(CreateOrJoinFortBattleCtx(battleID, waitingID='fort/fortBattle/createOrJoin'))


def getRosterIntroWindowSetting(type):
    settings = dict(AccountSettings.getSettings('fortSettings'))
    if ROSTER_INTRO_WINDOW not in settings:
        settings[ROSTER_INTRO_WINDOW] = {}
        AccountSettings.setSettings('fortSettings', settings)
    return settings[ROSTER_INTRO_WINDOW].get(type)


def setRosterIntroWindowSetting(type, value = True):
    settings = dict(AccountSettings.getSettings('fortSettings'))
    if ROSTER_INTRO_WINDOW not in settings:
        settings[ROSTER_INTRO_WINDOW] = {}
    settings[ROSTER_INTRO_WINDOW][type] = value
    AccountSettings.setSettings('fortSettings', settings)


@process
def showFortDisabledDialog():
    yield DialogsInterface.showI18nInfoDialog('fortDisabled')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\fortifications\fort_helpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:41 St�edn� Evropa (letn� �as)

# 2016.10.11 22:09:24 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/awards/event_dispatcher.py
import gui.awards.special_achievement_awards as specialAwards
from gui.shared.event_dispatcher import showAwardWindow

def showResearchAward(vehiclesCount, messageNumber):
    showAwardWindow(specialAwards.ResearchAward(vehiclesCount, messageNumber))


def showVictoryAward(victoriesCount, messageNumber):
    showAwardWindow(specialAwards.VictoryAward(victoriesCount, messageNumber))


def showBattleAward(battlesCount, messageNumber):
    showAwardWindow(specialAwards.BattleAward(battlesCount, messageNumber))


def showPveBattleAward(battlesCount, messageNumber):
    showAwardWindow(specialAwards.PvEBattleAward(battlesCount, messageNumber))


def showBoosterAward(booster):
    showAwardWindow(specialAwards.BoosterAward(booster))


def showFalloutAward(lvls, isRequiredVehicle = False):
    showAwardWindow(specialAwards.FalloutAwardWindow(lvls, isRequiredVehicle))


def showClanJoinAward(clanAbbrev, clanName, clanDbID):
    showAwardWindow(specialAwards.ClanJoinAward(clanAbbrev, clanName, clanDbID))


def showTelecomAward(vehicleDesrs, hasCrew, hasBrotherhood):
    showAwardWindow(specialAwards.TelecomAward(vehicleDesrs, hasCrew, hasBrotherhood))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\awards\event_dispatcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:09:24 St�edn� Evropa (letn� �as)

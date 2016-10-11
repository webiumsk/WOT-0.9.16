# 2016.10.11 22:14:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/tooltips/fortifications.py
from gui.shared.formatters import icons, text_styles
from gui.shared.items_parameters import params_helper, formatters as params_formatters, NO_DATA
from gui.shared.tooltips import TOOLTIP_TYPE
from gui.shared.tooltips import formatters
from gui.shared.tooltips.common import BlocksTooltipData
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from helpers.i18n import makeString as _ms

def _packTimeLimitsBlock(block, limits):
    textOffset = 30
    for limit in limits:
        text = _ms(TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_TIMELIMITFORMAT, startTime=limit.startTime, endTime=limit.endTime)
        block.append(formatters.packImageTextBlockData(title=text_styles.error(text), txtOffset=textOffset))


class FortPopoverDefResTooltipData(BlocksTooltipData):

    def __init__(self, context):
        super(FortPopoverDefResTooltipData, self).__init__(context, TOOLTIP_TYPE.FORTIFICATIONS)
        self._setContentMargin(top=15, left=19, bottom=21, right=22)
        self._setMargins(afterBlock=14)
        self._setWidth(380)
        self._descr = TOOLTIPS.FORTIFICATION_POPOVER_DEFRESPROGRESS_BODY

    def _packBlocks(self, compensationValue):
        title = TOOLTIPS.FORTIFICATION_POPOVER_DEFRESPROGRESS_HEADER
        items = super(FortPopoverDefResTooltipData, self)._packBlocks()
        items.append(formatters.packTitleDescBlock(text_styles.highTitle(title), desc=text_styles.main(self._descr)))
        if compensationValue is not None:
            blocksGap = 12
            compensationHeader = text_styles.main(TOOLTIPS.FORTIFICATION_POPOVER_DEFRESPROGRESS_COMPENSATION_HEADER) + text_styles.alert('+' + compensationValue) + icons.nut()
            compensationBody = text_styles.standard(TOOLTIPS.FORTIFICATION_POPOVER_DEFRESPROGRESS_COMPENSATION_BODY)
            items.append(formatters.packBuildUpBlockData([formatters.packTextBlockData(text_styles.concatStylesToMultiLine(compensationHeader, compensationBody))], blocksGap, BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE))
        return items


class FortListViewTooltipData(BlocksTooltipData):

    def __init__(self, context):
        super(FortListViewTooltipData, self).__init__(context, TOOLTIP_TYPE.FORTIFICATIONS)
        self._setContentMargin(top=15, left=19, bottom=21, right=22)
        self._setMargins(afterBlock=14)
        self._setWidth(380)
        self._descr = None
        return

    def _packBlocks(self, isCurfewEnabled, timeLimits, serverName = None):
        title = TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_HEADER_CURFEW if isCurfewEnabled else TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_HEADER_INFO
        items = super(FortListViewTooltipData, self)._packBlocks()
        items.append(formatters.packTitleDescBlock(text_styles.highTitle(title), desc=text_styles.main(self._descr) if self._descr else None))
        blocksGap = 2
        mainBlock = self._packMainBlock(serverName, timeLimits)
        limits = timeLimits
        timeBlock = []
        _packTimeLimitsBlock(timeBlock, limits)
        if len(timeBlock) > 0:
            mainBlock.append(formatters.packBuildUpBlockData(timeBlock, 0))
        items.append(formatters.packBuildUpBlockData(mainBlock, blocksGap, BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE))
        items.append(formatters.packBuildUpBlockData([formatters.packImageTextBlockData(title=text_styles.main(TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_FOOTER))], blocksGap))
        return items

    def _packMainBlock(self, serverName, timeLimits):
        pass


class SortiesTimeLimitPacker(FortListViewTooltipData):

    def __init__(self, context):
        super(SortiesTimeLimitPacker, self).__init__(context)

    def _packMainBlock(self, serverName, timeLimits):
        if serverName or timeLimits:
            key = TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_TIMEDESCR
        else:
            key = TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_NONE
        return [formatters.packImageTextBlockData(title=text_styles.main(key))]


class SortiesServerLimitPacker(FortListViewTooltipData):

    def __init__(self, context):
        super(SortiesServerLimitPacker, self).__init__(context)

    def _packMainBlock(self, serverName, timeLimits):
        blocksGap = 20
        blocksList = [formatters.packImageTextBlockData(title=text_styles.main(_ms(TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_SERVERLIMIT, server=text_styles.error(serverName))))]
        if timeLimits:
            blocksList.append(formatters.packImageTextBlockData(title=text_styles.main(TOOLTIPS.FORTIFICATION_SORTIE_LISTROOM_REGULATION_SERVERLIMITTIMEDESCR)))
        mainBlock = [formatters.packBuildUpBlockData(blocksList, blocksGap)]
        return mainBlock


class FortConsumableOrderTooltipData(BlocksTooltipData):

    def __init__(self, context):
        super(FortConsumableOrderTooltipData, self).__init__(context, TOOLTIP_TYPE.EQUIPMENT)
        self.item = None
        self._setContentMargin(top=0, left=0, bottom=20, right=20)
        self._setMargins(10, 15)
        self._setWidth(400)
        return

    def _packBlocks(self, *args, **kwargs):
        self.item = self.context.buildItem(*args, **kwargs)
        items = super(FortConsumableOrderTooltipData, self)._packBlocks()
        item = self.item
        statsConfig = self.context.getStatsConfiguration(item)
        paramsConfig = self.context.getParamsConfiguration(item)
        leftPadding = 20
        rightPadding = 20
        topPadding = 20
        textGap = -2
        items.append(formatters.packBuildUpBlockData(HeaderBlockConstructor(item, statsConfig, leftPadding, rightPadding).construct(), padding=formatters.packPadding(left=leftPadding, right=rightPadding, top=topPadding)))
        items.append(formatters.packBuildUpBlockData(CommonStatsBlockConstructor(item, paramsConfig, 80, leftPadding, rightPadding).construct(), padding=formatters.packPadding(left=leftPadding, right=rightPadding), gap=textGap))
        return items


class ConsumableOrderTooltipBlockConstructor(object):

    def __init__(self, item, configuration, leftPadding = 20, rightPadding = 20):
        self.item = item
        self.configuration = configuration
        self.leftPadding = leftPadding
        self.rightPadding = rightPadding

    def construct(self):
        return None


class HeaderBlockConstructor(ConsumableOrderTooltipBlockConstructor):

    def __init__(self, item, configuration, leftPadding, rightPadding):
        super(HeaderBlockConstructor, self).__init__(item, configuration, leftPadding, rightPadding)

    def construct(self):
        item = self.item
        block = []
        title = item.userName
        desc = item.getUserType()
        block.append(formatters.packImageTextBlockData(title=text_styles.highTitle(title), desc=text_styles.main(desc), img=item.icon, imgPadding=formatters.packPadding(left=12), txtGap=-4, txtOffset=100 - self.leftPadding))
        return block


class CommonStatsBlockConstructor(ConsumableOrderTooltipBlockConstructor):

    def __init__(self, item, configuration, valueWidth, leftPadding, rightPadding):
        super(CommonStatsBlockConstructor, self).__init__(item, configuration, leftPadding, rightPadding)
        self._valueWidth = valueWidth

    def construct(self):
        block = []
        item = self.item
        block.append(formatters.packTitleDescBlock(title=text_styles.middleTitle(_ms(TOOLTIPS.TANKCARUSEL_MAINPROPERTY)), padding=formatters.packPadding(bottom=8)))
        params = item.getParams()
        for paramName, paramValue in params:
            block.append(self.__packParameterBloc(_ms('#menu:moduleInfo/params/' + paramName), paramValue, params_formatters.measureUnitsForParameter(paramName)))

        return block

    def __packParameterBloc(self, name, value, measureUnits):
        return formatters.packTextParameterBlockData(name=text_styles.main(name) + text_styles.standard(measureUnits), value=text_styles.stats(value), valueWidth=self._valueWidth, padding=formatters.packPadding(left=-5))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\tooltips\fortifications.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:14:09 St�edn� Evropa (letn� �as)

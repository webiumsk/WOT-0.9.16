# 2016.10.11 22:16:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/Util.py
import BigWorld

def entitiesFromChunk(sectionName):
    import ResMgr
    sects = ResMgr.openSection(sectionName)
    if sects != None:
        for sect in sects.values():
            if sect.name == 'entity':
                type = sect.readString('type')
                pos = sect.readVector3('transform/row3')
                dict = {}
                for props in sect['properties'].values():
                    try:
                        dict[str(props.name)] = eval(props.asString)
                    except:
                        dict[str(props.name)] = props.asString

                BigWorld.createEntity(type, BigWorld.player().spaceID, 0, pos, (0, 0, 0), dict)

    return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\util.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:16:55 St�edn� Evropa (letn� �as)

############################################################################
############################################################################

import Game_Scripts.tileMap

tileMapper = Game_Scripts.tileMap

#dictionary of stages
#dictionary key for assets
#.ie "dusk_city_roof_1 = stage of dusk city roof
stages = {
    "bridge_1" : {
        "background": {
            "img" : None,
            "position" : None,
            "scale" : (1,0.6),
        },
        "middle_ground": {
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "stage_floor": {
            "img" : "Stage_Assets/stage_floors/bridge_1.png",
            "position" : (1400,100),
            "scale" : (2,1),
        },
        "foreground": {
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "bgm" : {
            "name" : "Mob_Battle",
            "volume" : 0.2,
            "source" : 'Stage_Assets/bgm/NO_EX01.mp3',
        },
        "map" : {
            'tile_set' : tileMapper.tileSet2D(20,9,0,0,-15,2),
        },
        "spawns" : [
            (36,8),
            (4,8),
        ],
    },
    "blank" : {
        "background": {
            "img" : None,
            "position" : None,
            "scale" : (1,0.6),
        },
        "middle_ground": {
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "stage_floor": {
            "img" : None,
            "position" : (700,125),
            "scale" : (1.5,1),
        },
        "foreground": {
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "bgm" : {
            "name" : "NO.EX01",
            "volume" : 0.2,
            "source" : 'Stage_Assets/bgm/NO_EX01.mp3',
        },
        "map" : {
            'tile_set' : tileMapper.tileSet2D(40,9,0,0,-15,2),
        },
        "spawns" : [
            (36,8),
            (4,8),
        ],
    }
}

def returnAsset(stage):
    # check if stage exists
    if not stage in stages:
        # This makes sure even if we can't find the file it does not crash the engine.
        print("key error:"+stage)
        return(False)
    # return the stage
    return stages[stage]


############################################################################
############################################################################
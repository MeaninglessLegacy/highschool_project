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
            "visible" : True,
            "img" : 'Stage_Assets/backgrounds/sunset_2.png',
            "position" : (3000,0),
            "scale" : (3,1),
        },
        "middle_ground": {
            "visible" : False,
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "stage_floor": {
            "visible" : True,
            "img" : 'Stage_Assets/stage_floors/bridge_2.png',
            "position" : (70,21),
            "scale" : (100,26),
        },
        "foreground": {
            "visible" : True,
            "img" : 'Stage_Assets/foregrounds/bridge_under_1.png',
            "position" : (70,-2),
            "scale" : (100,24),
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
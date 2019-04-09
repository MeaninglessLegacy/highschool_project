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
            "img" : 'Stage_Assets/backgrounds/sunset_3.png',
            "position" : (1200,0),
            "scale" : (2,1),
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
        "on_floor": {
            "visible" : False,
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "foreground": {
            "visible" : True,
            "img" : 'Stage_Assets/foregrounds/bridge_under_4.png',
            "position" : (70,2),
            "scale" : (100,30),
        },
        "bgm" : {
            "name" : "Final Encounter",
            "volume" : 0.5,
            "fade_in_time" : 50,
            "source" : 'Stage_Assets/bgm/The Last Encounter Collection/TLE Digital Loop Medium.wav',
        },
        "map" : {
            'tile_set' : tileMapper.tileSet2D(20,10,0,-2,-15,2),
        },
        "spawns" : [
            (36,8),
            (4,8),
        ],
        "camera_spawn" : (20,-10,15)
    },
    "blank" : {
        "background": {
            "visible" : False,
            "img" : None,
            "position" : None,
            "scale" : (1,0.6),
        },
        "middle_ground": {
            "visible" : False,
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "stage_floor": {
            "visible" : False,
            "img" : None,
            "position" : (700,125),
            "scale" : (1.5,1),
        },
        "foreground": {
            "visible" : False,
            "img" : None,
            "position" : None,
            "scale" : None,
        },
        "bgm" : {
            "name" : "NO.EX01",
            "volume" : 0.2,
            "fade_in_time" : 50,
            "source" : 'Stage_Assets/bgm/NO_EX01.mp3',
        },
        "map" : {
            'tile_set' : tileMapper.tileSet2D(40,9,0,0,-15,2),
        },
        "spawns" : [
            (36,8),
            (4,8),
        ],
        "camera_spawn" : (20,-50,15)
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
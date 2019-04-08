############################################################################
############################################################################

fps = 60

#dictionary of animations
#dictionary key for animation = animation set
#.ie "tank" = tank animations
#delay is how many frames pass before next animation is played
#animations with higher priority get played over those with lower
animations = {
    "tank" : {
        "combat_walk" : {
            "animation_priority" : 1,
            "name" : 'combat_walk',
            "looped" : False,
            "delay" : fps/fps,
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/0-0.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/0-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/0-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/0-3.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/0-4.png",
            ],
            "sounds" : {
            },
        },
        "combat_basic_attack_1" : {
            "animation_priority" : 4,
            "name" : 'meleeAtk',
            "looped" : False,
            "delay" : fps/fps,
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/0-0-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/0-0-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/0-0-3.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/0-0-4.png",
            ],
            "sounds" : {
                "swing" : {
                    "frame" : 1,
                    "volume" : 1,
                    "source" : "Sound_Assets/melee_2.wav"
                },
                "battle_cry" : {
                    "frame" : 0,
                    "volume" : 1,
                    "source" : "Sound_Assets/female_battlecry_short_3.wav"
                },
            },
        },
        "combat_basic_attack_2" : {
            "animation_priority" : 4,
            "name" : 'meleeAtk',
            "looped" : False,
            "delay" : fps/fps,
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/1-1-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/1-1-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/1-1-3.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Basic/1-1-4.png",
            ],
            "sounds" : {
                "swing" : {
                    "frame" : 1,
                    "volume" : 1,
                    "source" : "Sound_Assets/melee_3.wav"
                },
                "battle_cry" : {
                    "frame" : 0,
                    "volume" : 1,
                    "source" : "Sound_Assets/female_battlecry_short_4.wav"
                },
            },
        },
        "combat_shield" : {
            "animation_priority" : 6,
            "name" : 'shield',
            "looped" : True,
            "delay" : fps/fps,
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Shield/1.png",
            ],
            "sounds" : {
            },
        },
        "combat_stagger" : {
            "animation_priority": 5,
            "name" : 'stagger',
            "looped" : False,
            "delay" : fps/(2/3*fps),
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Stagger/0-0.png",
            ],
            "sounds":{
            },
        },
        "combat_knocked_down" : {
            "animation_priority": 9,
            "name" : 'knockedDown',
            "looped" : False,
            "delay" : fps/(2/3*fps),
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-0.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-3.png",
                #"Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-4.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-5.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-6.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-7.png",
            ],
            "sounds" : {
                "hit" : {
                    "frame" : 0,
                    "volume" : 0.4,
                    "source" : "Sound_Assets/heavy_hit_1.wav"
                },
                "hurt" : {
                    "frame" : 0,
                    "volume" : 1,
                    "source" : "Sound_Assets/female_hurt_heavy_4.wav"
                },
            },
        },
        "combat_knocked_out" : {
            "animation_priority": 7,
            "name" : 'knockedOut',
            "looped" : True,
            "delay" : fps/(fps/2),
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Knock_Down/0-7.png",
            ],
            "sounds" : {
            },
        },
        "combat_recover" : {
            "animation_priority": 8,
            "name" : 'recover',
            "looped" : False,
            "delay" : fps/(fps*5/6),
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-0.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-3.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-4.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Recovery/0-5.png",
            ],
            "sounds" : {
            },
        },
        "combat_idle" : {
            "animation_priority": 0,
            "name" : 'idle',
            "looped" : True,
            "delay" : fps/(2/3*fps),
            "frames" : [
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-0.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-1.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-2.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-3.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-4.png",
                "Sprite_Assets/Sprites/Tank_Sprites/Combat_Idle/0-5.png",
            ],
            "sounds" : {
            },
        },
    }
}

def returnAnimation(animationSet):
    # check if animations exists
    if not animationSet in animations:
        # This makes sure even if we can't find the file it does not crash the engine.
        print("key error:"+animationSet)
        return(False)
    # return the image in cache
    return animations[animationSet]

def update_fps(new_fps):

    global fps

    fps = new_fps

############################################################################
############################################################################
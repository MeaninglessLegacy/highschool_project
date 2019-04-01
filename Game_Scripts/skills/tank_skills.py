############################################################################
############################################################################


#Tank Skills
#Skills are called from control no need to call control from here

import Game_Scripts.animator, Game_Scripts.actions_manager, math, Game_Scripts.attackMapper

animator = Game_Scripts.animator
action_manager = Game_Scripts.actions_manager
attackMapper = Game_Scripts.attackMapper

############################################################################
############################################################################

#Skills

#Tank ability 1
'''
8 frames 2 hits
hits on frame 2 and 6
light strike + medium strike
'''

def ability1(chr):

    #spr obj
    spr = chr.spriteObject

    #actions
    pAction = chr.stats.previous_action
    #previous action
    if not pAction == []:
        pAction = chr.stats.previous_action[0]

    #queue
    qAction = chr.stats.queued_actions

    #cooldown
    cooldown = math.ceil(spr.animationSet['combat_basic_attack_1']['delay'] * math.fabs(1 / chr.stats.rate)) * len(spr.animationSet['combat_basic_attack_1']['frames']) + 2

    #damage
    damage = chr.stats.atk * 0.5

    knockback = 250 * 1

    #determine animation
    animations = {
        str(spr.animationSet['combat_basic_attack_1']) : 0,
        str(spr.animationSet['combat_basic_attack_2']) : 1,
    }

    #animation to play
    animation = spr.animationSet['combat_basic_attack_1']

    #tiles that are hit
    attackMap = attackMapper.attackMap(
        center = (0,0),
        forward = 3,
        backwards = 0,
        up = 2,
        down = 0,
        up_forward = 2,
        up_backwards = 0,
        down_forward = 0,
        down_backwards = 0,
    )

    #if previous action was a melee attack
    if isinstance(pAction, action_manager.meleeaction) == True :
        #if previous action was one of the basic melee attacks
        if str(pAction.animation) in animations:
            key = animations[str(pAction.animation)]
            if key == 0:
                animation = spr.animationSet['combat_basic_attack_2']
                damage = chr.stats.atk*1
                knockback = 250 * 50
                cooldown = math.ceil((animation['delay']*math.fabs(1/chr.stats.rate))*len(animation['frames'])+(6*math.fabs(1/chr.stats.rate)))
                #different tiles hit
                attackMap = attackMapper.attackMap(
                    center=(0, 0),
                    forward=3,
                    backwards=0,
                    up=0,
                    down=2,
                    up_forward=0,
                    up_backwards=0,
                    down_forward=2,
                    down_backwards=0,
                )
            elif key == 1:
                animation = spr.animationSet['combat_basic_attack_1']
                cooldown = math.ceil((animation['delay']*math.fabs(1/chr.stats.rate))*len(animation['frames'])+(2*math.fabs(1/chr.stats.rate)))
                knockback = 250 * 1.5
                damage = chr.stats.atk * 0.5

    #check if there is a melee action
    atkAction = False

    for i in range(0, len(qAction)-1):
        if qAction[i].type == 'meleeAtk':
            atkAction = True
            return cooldown
            break

    #Create a melee attack
    if atkAction == False:
        action = action_manager.meleeaction(
            type='meleeAtk',
            animation=animation,
            #total amount of frames is delay frame of each frame * total number of frames
            frames=math.ceil(animation['delay']*math.fabs(1/chr.stats.rate))*len(animation['frames']),
            priority=2,
            hitframe=3*math.ceil(animation['delay']*math.fabs(1/chr.stats.rate)),
            initiator=chr,
            damage = damage,
            momentum = 1,
            ticks = 1,
            attackMap = attackMap,
            knockback= knockback,
        )
        #add action
        action_manager.addAction(chr, action)

        return cooldown
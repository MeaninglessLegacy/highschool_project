############################################################################
############################################################################


#Tank Skills
#Skills are called from control no need to call control from here

import Game_Scripts.animator, Game_Scripts.actions_manager, math, Game_Scripts.attackMapper, threading

animator = Game_Scripts.animator
action_manager = Game_Scripts.actions_manager
attackMapper = Game_Scripts.attackMapper

############################################################################
############################################################################

#Skills

held_skills = {
    'ability1' : {
        'type' : False,
    },
    'ability2' : {
        'type' : True,
    },
}

#Tank ability 1
'''
8 frames 2 hits
hits on frame 2 and 6
light strike + medium strike
'''

def ability1(chr, player):

    #spr obj
    spr = chr.spriteObject

    #actions
    pAction = None
    action = chr.stats.previous_action
    if not action == []:
        pAction = action[0]

    #queue
    qAction = chr.stats.queued_actions
    #previous

    knB_mod = 1

    #cooldown
    cooldown = math.ceil((spr.animationSet['combat_basic_attack_1']['delay']*math.fabs(1/chr.stats.rate))*(len(spr.animationSet['combat_basic_attack_1']['frames'])+2)+(math.fabs(1/chr.stats.rate)))

	#dash attack
    if not pAction == None:
        #print(pAction)
        if pAction.type == 'walk':
            knB_mod = 5
            cooldown = math.ceil(spr.animationSet['combat_basic_attack_1']['delay'] * (2 * math.fabs(1 / chr.stats.rate))) * (len(spr.animationSet['combat_basic_attack_1']['frames']) + 3)

    #damage
    damage = chr.stats.atk * 0.5

    knockback = 250 * 1 * knB_mod

    #determine animation
    animations = {
        str(spr.animationSet['combat_basic_attack_1']) : 0,
        str(spr.animationSet['combat_basic_attack_2']) : 1,
    }

    #animation to play
    animation = spr.animationSet['combat_basic_attack_1']

    #tiles that are hit
    attackMap = attackMapper.attackMap(
        center = (1,0),
        forward = 3,
        backwards = 1,
        up = 3,
        down = 3,
        up_forward = 2,
        up_backwards = 2,
        down_forward = 2,
        down_backwards = 2,
    )

    #if previous action was a melee attack
    if isinstance(pAction, action_manager.meleeaction) == True :
        #if previous action was one of the basic melee attacks
        if str(pAction.animation) in animations:
            key = animations[str(pAction.animation)]
            if key == 0:
                animation = spr.animationSet['combat_basic_attack_2']
                damage = chr.stats.atk*1
                knockback = 250 * 50 * knB_mod
                cooldown = math.ceil((animation['delay']*math.fabs(1/chr.stats.rate))*(len(animation['frames'])+8)+(math.fabs(1/chr.stats.rate)))
                #different tiles hit
                attackMap = attackMapper.attackMap(
                    center=(1, 0),
                    forward=3,
                    backwards=1,
                    up=2,
                    down=2,
                    up_forward=1,
                    up_backwards=1,
                    down_forward=1,
                    down_backwards=1,
                )
            elif key == 1:
                animation = spr.animationSet['combat_basic_attack_1']
                cooldown = math.ceil((animation['delay']*math.fabs(1/chr.stats.rate))*(len(animation['frames'])+2)+(math.fabs(1/chr.stats.rate)))
                knockback = 250 * 1.5 * knB_mod
                damage = chr.stats.atk * 0.5

    #check if there is a melee action
    atkAction = False

    for i in range(0, len(qAction)):
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
            frames=math.floor(animation['delay']*math.fabs(1/chr.stats.rate))*(len(animation['frames'])+2),
            priority=2,
            hitframe=4*math.floor(animation['delay']*math.fabs(1/chr.stats.rate)),
            initiator=chr,
            damage = damage,
            momentum = 1.5,
            ticks = 1,
            attackMap = attackMap,
            knockback= knockback,
        )
        #add action
        action_manager.addAction(chr, action)

        return cooldown

#Tank ability 2
'''
80% block
'''
def ability2(chr, player):

    spr = chr.spriteObject

    exempt_actions = []
    for i, o in enumerate(chr.stats.queued_actions):
        if not isinstance(o, action_manager.walkaction):
            exempt_actions.append(o)

    #toggle
    if player['abilities_held']['2'] == True and exempt_actions == []:
        spr.animationList = []
        stats = chr.stats
        stats.shield_strength = 0.80
        stats.shielding = True
        stats.weight += 3000

        animator.addAnimation(chr, spr.animationSet['combat_shield'])

    elif player['abilities_held']['2'] == False:
        # this chr's stats
        stats = chr.stats
        stats.shielding = False
        stats.shield_strength = 0
        stats.weight = stats.base_weight

        animator.removeAnimation(chr, spr.animationSet['combat_shield'])


    return 12 *math.fabs(1/chr.stats.rate)



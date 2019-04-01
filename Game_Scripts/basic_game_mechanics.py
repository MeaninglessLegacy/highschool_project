############################################################################
############################################################################

#Basic Game Mechanics

import Game_Scripts.animator, math, Game_Scripts.functions

functions = Game_Scripts.functions
animator = Game_Scripts.animator



############################################################################
############################################################################



#Movement
def moveChr(ch):
    #get momementum
    spr_momentum = ch.stats.momentum
    spr = ch.spriteObject
    #get borders
    border = functions.get_Borders()
    #if we have borders
    if border != []:

        topCorner = border[0]
        bottomCorner = border[1]

        xMomentum = spr_momentum[0]
        yMomentum = spr_momentum[1]

        #for knockdowns so this doesn't impede on movespeed
        if ch.stats.canMove == False:
            if xMomentum > 1.4:
                xMomentum = 1.4
            if yMomentum> 1.4:
                yMomentum = 1.4
            if xMomentum < -1.4:
                xMomentum = -1.4
            if yMomentum < -1.4:
                yMomentum = -1.4

        #change in pos
        xChange = spr.x + xMomentum
        yChange = spr.y + yMomentum

        if xChange > spr.x:
            if xChange < bottomCorner[0]:
                spr.x += xMomentum
            elif xChange >= bottomCorner[0]:
                spr.x = bottomCorner[0]
        elif xChange < spr.x:
            if xChange > topCorner[0]:
                spr.x += xMomentum
            elif xChange <= topCorner[0]:
                spr.x = topCorner[0]

        if yChange > spr.y:
            if yChange < bottomCorner[1]:
                spr.y += yMomentum
            else:
                spr.y = bottomCorner[1]
        elif yChange < spr.y:
            if yChange > topCorner[1]:
                spr.y += yMomentum
            else:
                spr.y = topCorner[1]

        ch.stats.momentum = (spr_momentum[0]-xMomentum, spr_momentum[1] - yMomentum,)

#Damage target
def damageTarget(initiator, target, attack):

    #Attack Stats
    damage = attack.damage
    knockback = attack.knockback

    #targets
    initSpr = initiator.spriteObject
    tarSpr = target.spriteObject
    initStats = initiator.stats
    tarStats = target.stats

    knockback_modifier = 1

    #damage target
    if tarStats.currentHP - damage <= 0:
        knockback_modifier = (80*tarStats.weight/2)/knockback
        tarStats.currentHP = 0
    else:
        tarStats.currentHP -= damage

    #knockback formula 10 is the scaling ratio, so this formula returns pixel / frame knocked back
    knockbackStrength = math.sqrt(2*(knockback*knockback_modifier)/tarStats.weight)

    #knockback
    if tarSpr.x > initSpr.x:
        tarSpr.heading = '+'
        tarStats.momentum = (knockbackStrength, 0)
    else:
        tarSpr.heading = '-'
        tarStats.momentum = (-knockbackStrength, 0)

    #stagger or knockdown
    #the threshhold force is the force need to knock a unit back 6 units
    #since -> 8^2*mass/2 = threshhold force
    threshhold_force = 64*tarStats.weight/2
    if (knockback*knockback_modifier) > threshhold_force:
        tarStats.canMove = False
        if tarStats.knockedOut == False:
            tarStats.knockedOut = True
            tarStats.stunTimer = math.ceil(knockbackStrength*2)
            animator.addAnimation(target, tarSpr.animationSet['combat_knocked_down'])
        pass
    else:
        #play sound
        hit_sound = functions.get_sound("Sound_Assets/light_hit_2.wav")
        hit_sound.set_volume(0.8)
        hit_sound.play()

        tarStats.canMove = False
        if tarStats.knockedOut == False:
            tarStats.stunTimer = math.ceil(knockbackStrength*2)
            animator.addAnimation(target, tarSpr.animationSet['combat_stagger'])

#Stuns
def manageStun(ch):
    #character
    chr = ch
    stats = chr.stats
    spr = chr.spriteObject

    #if is knocked out on the ground
    if stats.knockedOut == True or stats.currentHP == 0:
        animator.addAnimation(chr, spr.animationSet['combat_knocked_out'])
        animator.removeAnimation(chr, spr.animationSet['combat_recover'])
    else:
        animator.removeAnimation(chr, spr.animationSet['combat_knocked_out'])

    #Very sketchy
    if stats.stunTimer > 0:
        #reduce stun tiemr by one
        stats.stunTimer -= 1
    #zero stun timer
    elif stats.stunTimer <= 0:
        #check if knocked out
        if stats.knockedOut == True and stats.currentHP != 0:
            #if knocked out recover
            stats.knockedOut = False
            stats.stunTimer = math.ceil(len(spr.animationSet['combat_recover']['frames'])*spr.animationSet['combat_recover']['delay'])
            animator.addAnimation(chr, spr.animationSet['combat_recover'])
        #if not knocked out
        elif stats.knockedOut == False:
            #resume normal control
            stats.canMove = True
            animator.removeAnimation(chr, spr.animationSet['combat_stagger'])
            animator.removeAnimation(chr, spr.animationSet['combat_knocked_out'])


############################################################################
############################################################################

#update all the basic mechanics
def updateBasicMechanics(ch):
    for key in ch:
        moveChr(ch[key])
        manageStun(ch[key])
    pass
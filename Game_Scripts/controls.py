############################################################################
############################################################################


import pygame, math

import Game_Scripts.animator, Game_Scripts.actions_manager, Game_Scripts.character_skills

animator = Game_Scripts.animator
action_manager = Game_Scripts.actions_manager
character_skills = Game_Scripts.character_skills


############################################################################
############################################################################

#selected Character
def sC(ch):
    for key in ch:
        if ch[key].isSelected:
            return key

def change_sC(players, player_key, o, ch):

    k = ""

    player = players[player_key]

    for key in ch:
        if ch[key] == o:
            k=key
            ch[key].isSelected = True
            player['sC'] = ch[key]

    #get all characters controlled by players
    player_chr = {}
    for ply in players:
        if players[ply]['sC'] != None:
            player_chr[players[ply]['sC']] = players[ply]['sC']

    for key in ch:
        if key != k and not ch[key] in player_chr:
            ch[key].isSelected = False

def find_player(players, chr):

    for ply in players:
        if players[ply]['sC'] != None:
            if players[ply]['sC'] == chr:
                return players[ply]

    return None

############################################################################
############################################################################

#3D Controls


#Key pressed event

def keyPress3D(ch, cam):
    p = pygame.key.get_pressed()

    global fps

    if not ch[sC(ch)] is None:
        animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_idle'])

        #that list is what no keys pressed looks list
        if p == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) :
            animator.removeAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])
            pass

    if p[pygame.K_d]:
        if not ch[sC(ch)] is None:
            ch[sC(ch)].spriteObject.x-=0.1
            ch[sC(ch)].spriteObject.heading = "+"
            ch[sC(ch)].spriteObject.direction = "East"
            animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])

    if p[pygame.K_a]:
        if not ch[sC(ch)] is None:
            ch[sC(ch)].spriteObject.x+=0.1
            ch[sC(ch)].spriteObject.heading = "-"
            ch[sC(ch)].spriteObject.direction = "West"
            animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])

    if p[pygame.K_w]:
        if not ch[sC(ch)] is None:
            ch[sC(ch)].spriteObject.z-=0.1
            ch[sC(ch)].spriteObject.direction = "North"
            animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])

    if p[pygame.K_s]:
        if not ch[sC(ch)] is None:
            ch[sC(ch)].spriteObject.z+=0.1
            ch[sC(ch)].spriteObject.direction = "South"
            animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])

    #print(ch[sC(ch)].spriteObject.x, ch[sC(ch)].spriteObject.y, ch[sC(ch)].spriteObject.z)
    if p[pygame.K_q]:
        cam.x+=1
    if p[pygame.K_e]:
        cam.x-=1
    if p[pygame.K_z]:
        cam.z -= 1
    if p[pygame.K_c]:
        cam.z += 1

def mouseMove(e, cam, s):
    x, y = e.rel
    x /= s.get_width()
    y /= s.get_height()

    cam.xRot += x
    cam.yRot += y



############################################################################
############################################################################

#2D Controls

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

controls = {
    "player_1" : {
        "left" : pygame.K_a,
        "right" : pygame.K_d,
        "up" : pygame.K_w,
        "down" : pygame.K_s,
        "changeChr" : pygame.K_q,
        "ability1" : pygame.K_j,
        "ability2" : pygame.K_k,
    },
    "player_2" : {
        "left" : pygame.K_KP4,
        "right" : pygame.K_KP6,
        "up" : pygame.K_KP8,
        "down" : pygame.K_KP5,
        "changeChr" : pygame.K_KP7,
        "ability1" : pygame.K_KP0,
        "ability2" : pygame.K_KP1,
    },
    "controller_1" : {
        "left" : (1,0),
        "right" : (-1,0),
        "up" : (0,1),
        "down" : (0,-1),
        "aleft" : [-1],
        "aright" : [1],
        "aup" : [1],
        "adown" : [-1],
        "changeChr" : pygame.K_y,
        "ability1" : pygame.K_x,
    },
        "cleft" : pygame.K_u,
        "cright" : pygame.K_i,
        "cup" : pygame.K_o,
        "cdown" : pygame.K_p,
        'blank' : (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
}

def keyBinding_check(player):
    try:
        controls[player]
    except:
        return None
    else:
        return controls[player]

############################################################################
############################################################################

def controllerPress2D(ch, borders, cam, players, player):

    joystick = joysticks[0]
    joystick.init()

    chr = players[player]['sC']

    player_characters = []
    for key in ch:
        if ch[key].playerCharacter == True:
            player_characters.append(ch[key])
    change_sC(players, player, player_characters[0], ch)

    if chr == None:
        return False

    key_map = controls['controller_1']

    name = joystick.get_name()

    axes = joystick.get_numaxes()

    for i in range(axes):
        axis = joystick.get_axis(i)
        walkspeed = chr.stats.walkspeed * chr.stats.rate
        if axis < -0.5 and i == 0:
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
            action = action_manager.walkaction(
                type='walk',
                animation=chr.spriteObject.animationSet['combat_walk'],
                frames=0,
                priority=1,
                direction='west',
                walkspeed=walkspeed,
                borders=borders,
            )
            action_manager.addAction(chr, action)
        if axis > 0.5 and i == 0:
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
            action = action_manager.walkaction(
                type='walk',
                animation=chr.spriteObject.animationSet['combat_walk'],
                frames=0,
                priority=1,
                direction='east',
                walkspeed=walkspeed,
                borders=borders,
            )
            action_manager.addAction(chr, action)
        if axis < -0.5 and i == 1:
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
            action = action_manager.walkaction(
                type='walk',
                animation=chr.spriteObject.animationSet['combat_walk'],
                frames=0,
                priority=1,
                direction='north',
                walkspeed=walkspeed,
                borders=borders,
            )
            action_manager.addAction(chr, action)
        if axis > 0.5 and i == 1:
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
            action = action_manager.walkaction(
                type='walk',
                animation=chr.spriteObject.animationSet['combat_walk'],
                frames=0,
                priority=1,
                direction='south',
                walkspeed=walkspeed,
                borders=borders,
            )
            action_manager.addAction(chr, action)

    buttons = joystick.get_numbuttons()

    for i in range(buttons):
        button = joystick.get_button(i)

    hats = joystick.get_numhats()

    for i in range(hats):
        hat = joystick.get_hat(i)

#For abilities that are tapped once
def use_ability(p, keyBindings, chr, players, player, ability, cd):
    if not p[keyBindings['left']] and not p[keyBindings['right']] and not p[keyBindings['up']] and not p[keyBindings['down']]:
        for i, o in enumerate(chr.stats.previous_action):
            if isinstance(o, action_manager.walkaction):
                del chr.stats.previous_action[i]
    if p[keyBindings[ability]] and character_skills.checkHeldSkill(chr, ability)['type'] == False:
        animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
        skill = character_skills.useSkill(chr, ability, players[player])
        if skill != False:
            players[player]['ability_cd'][cd] = skill[0]
    # if the ability is a held type ability
    if p[keyBindings[ability]] and character_skills.checkHeldSkill(chr, ability)['type'] == True:
        if players[player]['abilities_held'][cd] == False:
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
            players[player]['abilities_held'][cd] = True
            skill = character_skills.useSkill(chr, ability, players[player])

#main control for 2d
def keyPress2D(ch, borders, cam, players, player):
    #Return keys pressed
    p = pygame.key.get_pressed()

    chr = players[player]['sC']
    keyBindings = keyBinding_check(players[player]['player'])

    #cds
    ability_1_cd = players[player]['ability_cd']['1']
    ability_2_cd = players[player]['ability_cd']['2']
    sdebounce = players[player]['ability_cd']['chr_swap']

    if not chr == None and keyBindings != None:
        # set walkspeed
        walkspeed = chr.stats.walkspeed*chr.stats.rate
        #Idle Animation, move to events later
        animator.addAnimation(chr, chr.spriteObject.animationSet['combat_idle'])

        if p==controls['blank'] or (not p[keyBindings['left']] and not p[keyBindings['right']] and not p[keyBindings['up']] and not p[keyBindings['down']]):
            #Remove Walk Animations
            animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
            pass

        action = None
        #Walk Key Bindings
        if chr.stats.canMove == True:
            if p[keyBindings['left']]:
                animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
                action = action_manager.walkaction(
                    type = 'walk',
                    animation = chr.spriteObject.animationSet['combat_walk'],
                    frames = 0,
                    priority = 1,
                    direction = 'west',
                    walkspeed = walkspeed,
                    borders = borders,
                )
                action_manager.addAction(chr, action)
                pass
            if p[keyBindings['right']]:
                animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
                action = action_manager.walkaction(
                    type='walk',
                    animation=chr.spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='east',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(chr,action)
                pass
            if p[keyBindings['up']]:
                animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
                action = action_manager.walkaction(
                    type='walk',
                    animation=chr.spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='north',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(chr, action)
                pass
            if p[keyBindings['down']]:
                animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_recover'])
                action = action_manager.walkaction(
                    type='walk',
                    animation=chr.spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='south',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(chr, action)
                pass

        #Ability Key Bindings
        #use skills
        if chr.stats.canMove == True and chr.stats.shielding == False:
            #ability 1
            if ability_1_cd == 0:
                #if the ability is a tap type ability
                if (character_skills.checkHeldSkill(chr, 'ability1')) != False:
                    use_ability(p, keyBindings, chr, players, player, 'ability1', '1')
            else:
                players[player]['ability_cd']['1'] -= 1
            #ability_2
            if ability_2_cd == 0:
                #if the ability is a tap type ability
                if (character_skills.checkHeldSkill(chr, 'ability2')) != False:
                    use_ability(p, keyBindings, chr, players, player, 'ability2', '2')
            else:
                players[player]['ability_cd']['2'] -= 1

        #toggle held skills
        if(character_skills.checkHeldSkill(chr, 'ability1')) != False and (character_skills.checkHeldSkill(chr, 'ability2')) != False:
            if not p[keyBindings['ability1']] and character_skills.checkHeldSkill(chr, 'ability1')['type'] == True:
                if players[player]['abilities_held']['1'] == True:
                    animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
                    players[player]['abilities_held']['1'] = False
                    skill = character_skills.useSkill(chr, 'ability1', players[player])
                    players[player]['ability_cd']['1'] = skill[0]
            if not p[keyBindings['ability2']] and character_skills.checkHeldSkill(chr, 'ability2')['type'] == True:
                if players[player]['abilities_held']['2'] == True:
                    animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
                    players[player]['abilities_held']['2'] = False
                    skill = character_skills.useSkill(chr, 'ability2', players[player])
                    players[player]['ability_cd']['2'] = skill[0]

        #if you get knocked out while shielding or holding an ability down
        if chr.stats.knockedOut == True:
            if (character_skills.checkHeldSkill(chr, 'ability1')) != False and (character_skills.checkHeldSkill(chr, 'ability2')) != False:
                if character_skills.checkHeldSkill(chr, 'ability1')['type'] == True:
                    if players[player]['abilities_held']['1'] == True:
                        animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
                        players[player]['abilities_held']['1'] = False
                        skill = character_skills.useSkill(chr, 'ability1', players[player])
                        players[player]['ability_cd']['1'] = skill[0]
                if character_skills.checkHeldSkill(chr, 'ability2')['type'] == True:
                    if players[player]['abilities_held']['2'] == True:
                        animator.removeAnimation(chr, chr.spriteObject.animationSet['combat_walk'])
                        players[player]['abilities_held']['2'] = False
                        skill = character_skills.useSkill(chr, 'ability2', players[player])
                        players[player]['ability_cd']['2'] = skill[0]

        if p[controls['cleft']]:
            cam.x += 5
        if p[controls['cright']]:
            cam.x -= 5
        if p[controls['cup']]:
            cam.z += 1
        if p[controls['cdown']]:
            cam.z -= 1

    # Swap between characters temp
    if sdebounce == 0 and keyBindings != None:
        if p[keyBindings['changeChr']]:
            players[player]['ability_cd']['chr_swap'] = 3
            # first we need to draw the area that each object is going to be
            # no of player character
            player_characters = []
            for key in ch:
                if ch[key].playerCharacter == True:
                    player_characters.append(ch[key])

            # change chr to next chr in dic
            current_chr = chr

            for i in range(0, len(player_characters)):
                if current_chr == None:
                    change_sC(players, player, player_characters[0], ch)
                if player_characters[i] == current_chr and i != len(player_characters) - 1:
                    change_sC(players, player, player_characters[i + 1], ch)
                    break
                elif player_characters[i] == current_chr and i == len(player_characters) - 1:
                    change_sC(players, player, player_characters[0], ch)
                    break
    else:
        players[player]['ability_cd']['chr_swap'] -= 1



def mouseClick2D(ch, player):
    ev = pygame.event.get()

    chr = player.sC

############################################################################
############################################################################
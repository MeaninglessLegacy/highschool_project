############################################################################
############################################################################


import pygame

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

def change_sC(o, ch):
    k = ""

    for key in ch:
        if ch[key] == o:
            k=key
            ch[key].isSelected = True

    for key in ch:
        if key != k:
            ch[key].isSelected = False



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

keyBindings = {
    "left" : pygame.K_a,
    "right" : pygame.K_d,
    "up" : pygame.K_w,
    "down" : pygame.K_s,
    "changeChr" : pygame.K_q,
    "ability1" : pygame.K_j,
    "cleft" : pygame.K_u,
    "cright" : pygame.K_i,
    "cup" : pygame.K_o,
    "cdown" : pygame.K_p,
    'blank' : (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
}


#ability delay timer
ability_1_cd = 0

#swap delay timer
sdebounce = 0

############################################################################
############################################################################
def keyPress2D(ch, borders, cam):
    #Return keys pressed
    p = pygame.key.get_pressed()

    topCorner = borders[0]
    bottomCorner = borders[1]

    if not sC(ch) == None:
        # set walkspeed
        walkspeed = ch[sC(ch)].stats.walkspeed*ch[sC(ch)].stats.rate
        #Idle Animation, move to events later
        animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_idle'])

        if p==keyBindings['blank']:
            #Remove Walk Animations
            animator.removeAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_walk'])
            pass

        action = None
        #Walk Key Bindings
        if ch[sC(ch)].stats.canMove == True:
            if p[keyBindings['left']]:
                #temp move camera
                #if ch[sC(ch)].spriteObject.x + walkspeed <= bottomCorner[0]:
                    #cam.x += walkspeed
                action = action_manager.walkaction(
                    type = 'walk',
                    animation = ch[sC(ch)].spriteObject.animationSet['combat_walk'],
                    frames = 0,
                    priority = 1,
                    direction = 'west',
                    walkspeed = walkspeed,
                    borders = borders,
                )
                action_manager.addAction(ch[sC(ch)], action)
                pass
            if p[keyBindings['right']]:
                #temp move camera
                #if ch[sC(ch)].spriteObject.x - walkspeed >= topCorner[0]:
                    #cam.x -= walkspeed
                action = action_manager.walkaction(
                    type='walk',
                    animation=ch[sC(ch)].spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='east',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(ch[sC(ch)],action)
                pass
            if p[keyBindings['up']]:
                action = action_manager.walkaction(
                    type='walk',
                    animation=ch[sC(ch)].spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='north',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(ch[sC(ch)], action)
                pass
            if p[keyBindings['down']]:
                action = action_manager.walkaction(
                    type='walk',
                    animation=ch[sC(ch)].spriteObject.animationSet['combat_walk'],
                    frames=0,
                    priority=1,
                    direction='south',
                    walkspeed=walkspeed,
                    borders=borders,
                )
                action_manager.addAction(ch[sC(ch)], action)
                pass

        global ability_1_cd
        global sdebounce

        #Swap between characters temp
        if sdebounce == 0:
            if p[keyBindings['changeChr']]:
                sdebounce = 3
                # first we need to draw the area that each object is going to be
                # no of player character
                player_characters = []
                for key in ch:
                    if ch[key].playerCharacter == True:
                        player_characters.append(ch[key])

                #change chr to next chr in dic
                current_chr = ch[sC(ch)]

                for i in range(0, len(player_characters)):
                    if player_characters[i] == current_chr and i != len(player_characters)-1:
                        change_sC(player_characters[i+1], ch)
                        break
                    elif player_characters[i] == current_chr and i == len(player_characters)-1:
                        change_sC(player_characters[0], ch)
                        break
        else:
            sdebounce -= 1


        #Ability Key Bindings
        if ch[sC(ch)].stats.canMove == True:
            if ability_1_cd == 0:
                if p[keyBindings['ability1']]:
                    skill = character_skills.useSkill(ch[sC(ch)], 'ability1')
                    ability_1_cd = skill
            else:
                ability_1_cd -= 1

        if p[keyBindings['cleft']]:
            cam.x += 5
        if p[keyBindings['cright']]:
            cam.x -= 5
        if p[keyBindings['cup']]:
            cam.z += 1
        if p[keyBindings['cdown']]:
            cam.z -= 1

def mouseClick2D(ch):
    ev = pygame.event.get()

    for event in ev:

        # mousebutton Up
        if event.type == pygame.MOUSEBUTTONDOWN:

            if not ch[sC(ch)] is None:

                animator.addAnimation(ch[sC(ch)], ch[sC(ch)].spriteObject.animationSet['combat_basic_attack_1'])

############################################################################
############################################################################
############################################################################
############################################################################


#Stage Manager set stage backgrounds, music etc.

import pygame, math, Game_Scripts.stages, Game_Scripts.functions


functions = Game_Scripts.functions

stages = Game_Scripts.stages

############################################################################
############################################################################

stage_bgm = None

############################################################################
############################################################################

def drawBackground(background_img, screen, cam):
    # Load the image
    img = functions.get_image(background_img['img'])
    img_pos = background_img['position']
    img = pygame.transform.scale(img, (math.floor(screen.get_width() * background_img['scale'][0]),math.floor(screen.get_height() * background_img['scale'][1])))
    # If a position is specified otherwise it is fixed
    if img_pos != None:
        xPos = cam.x - img_pos[0]
        yPos = cam.y - img_pos[1]
        screen.blit(img, (xPos, yPos))
    else:
        screen.blit(img, (0, 0))

#main function
def renderStage2D(stage, screen, cam):

    global stage_bgm

    background_screen = screen
    #Background
    if stage['background']['img'] != None:
        drawBackground(stage['background'], background_screen, cam)
    #Mid ground
    if stage['middle_ground']['img'] != None:
        drawBackground(stage['middle_ground'], background_screen, cam)
    #Floor
    if stage['stage_floor']['img'] != None:
        drawBackground(stage['stage_floor'], background_screen, cam)
    #Foreground
    if stage['foreground']['img'] != None:
        drawBackground(stage['foreground'], background_screen, cam)

    #Background music
    if stage['bgm']['source'] != None:
        get_bgm = stage['bgm']['source']
        #if the stage bgm is not the current bgm
        if stage_bgm != get_bgm:
            stage_bgm = get_bgm
            pygame.mixer.music.stop()
            pygame.mixer.music.load(stage['bgm']['source'])
            pygame.mixer.music.set_volume(stage['bgm']['volume'])
            pygame.mixer.music.play(-1)


    return background_screen

def set_bgm(bgm):

    global stage_bgm

    if stage_bgm != bgm:
        stage_bgm = bgm
        pygame.mixer.music.stop()
        pygame.mixer.music.load(bgm)

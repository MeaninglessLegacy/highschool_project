############################################################################
############################################################################


#Stage Manager set stage backgrounds, music etc.

import pygame, math, Game_Scripts.stages, Game_Scripts.functions


functions = Game_Scripts.functions

stages = Game_Scripts.stages

############################################################################
############################################################################

stage_bgm = None

music_inc = 0

############################################################################
############################################################################

def drawBackground(background_img, screen, cam):
    # Load the image
    img = functions.get_image(background_img['img'], False)
    img_pos = background_img['position']
    img = pygame.transform.scale(img, (math.floor(screen.get_width() * background_img['scale'][0]),math.floor(screen.get_height() * background_img['scale'][1])))
    # If a position is specified otherwise it is fixed
    if img_pos != None:
        xPos = cam.x*10 - img_pos[0]
        yPos = cam.y - img_pos[1]
        screen.blit(img, (xPos, 0))
    else:
        screen.blit(img, (0, 0))


def determine_regions(layer, cam, s):

    start_pos = layer['position']
    scale = layer['scale']
    image = layer['img']

    '''
    start_pos --------------------------------------- start_pos x - scale x
    |                                                                   |
    |                                                                   |
    |                                                                   |
    start_pos y - scale y --start_pos x - scale x , start_pos y - scale y
    '''

    vt = []
    vt.append([start_pos[0], start_pos[1], -15])
    vt.append([start_pos[0] - scale[0], start_pos[1], -15])
    vt.append([start_pos[0], start_pos[1] - scale[1], -15])
    vt.append([start_pos[0] - scale[0], start_pos[1] - scale[1], -15])

    segments = [[0, 3], [2, 1], [0, 2], [3, 1]]
    edges = []
    dC = []

    for i in range(0, len(vt)):
        x = vt[i][0]
        y = vt[i][1]
        z = vt[i][2]

        # dC.append(distort2DCamera(x,y,cam,s))
        dC.append(functions.distortPoint(x, y, z, cam, s))

    #pygame.draw.polygon(s, (25, 25, 25), [dC[1], dC[3], dC[2], dC[0]], 0)

    space = pygame.Rect(dC[0], (dC[1][0]-dC[0][0], dC[2][1]-dC[0][1]))

    if image != None:

        image = functions.get_image(layer['img'], True)

        if space.width < 5000 or space.height < 5000:

            image = pygame.transform.scale(image, (space.width, space.height))

        s.blit(image, space)

#main function
def renderStage2D(stage, screen, cam, layer):

    background_screen = screen
    #Background
    if stage['background']['visible'] != False and layer == 2:
        drawBackground(stage['background'], background_screen, cam)
    #Mid ground
    if stage['middle_ground']['visible'] != False and layer == 2:
        determine_regions(stage['middle_ground'], cam, screen)
    #Floor- stage floor is special boit it is behind yet still needs alpha
    if stage['stage_floor']['visible'] != False and layer == 2:
        determine_regions(stage['stage_floor'], cam, screen)
    #On Floor
    if stage['on_floor']['visible'] != False and layer == 1:
        determine_regions(stage['on_floor'], cam, screen)
    #Foreground
    if stage['foreground']['visible'] != False and layer == 1:
        determine_regions(stage['foreground'], cam, screen)

    return background_screen
	
def music_stage(stage, level):

    global stage_bgm, music_inc
	
    #Background music
    if stage['bgm']['source'] != None and level == 0:
        get_bgm = stage['bgm']['source']
        #if the stage bgm is not the current bgm
        if stage_bgm != get_bgm:
            stage_bgm = get_bgm
            pygame.mixer.music.stop()
            pygame.mixer.music.load(stage['bgm']['source'])
            pygame.mixer.music.set_volume(0)
            music_inc = 1
            pygame.mixer.music.play(-1)

    if stage['bgm']['source'] != None and level == 0:
        if music_inc < stage['bgm']['fade_in_time']:
            music_inc += 1
            pygame.mixer.music.set_volume(stage['bgm']['volume']*(music_inc/stage['bgm']['fade_in_time']))
			
    if stage['bgm']['source'] != None and level == 1:
        if music_inc > 0:
            music_inc -= 1
            pygame.mixer.music.set_volume(stage['bgm']['volume'] * (music_inc / stage['bgm']['fade_in_time']))
        if music_inc <= 0:
            if stage_bgm != None:
                stage_bgm = None
                pygame.mixer.music.stop()
            return True

    return False


def set_bgm(bgm):

    global stage_bgm

    if stage_bgm != bgm:
        stage_bgm = bgm
        pygame.mixer.music.stop()
        pygame.mixer.music.load(bgm)
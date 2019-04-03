import pygame, sys, math, os.path

#Tkinter stuff
pygame.init()

pygame.mixer.pre_init(44100,-16,6, 1024)

#screen
w = 1600
h = 900
#clock
t = pygame.time.Clock()

fps = 24

#At the end replace all file paths with this
filepath = os.path.dirname(__file__)

#Temp
icon = pygame.image.load('Sprite_Assets\Icon\icon.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('untitled')


############################################################################
############################################################################

#Screens
#Main Screen that the game is drawn on
s = pygame.display.set_mode((w,h))

combat_UI = pygame.Surface((w,h), pygame.SRCALPHA)

title_screen = pygame.Surface((w,h))

background_screen = pygame.Surface((w,h))

loading_screen = pygame.Surface((w,h), pygame.SRCALPHA)

generic_screen = pygame.Surface((w,h), pygame.SRCALPHA)

############################################################################
############################################################################

#Importing Other Scripts

import Game_Scripts.functions, Game_Scripts.sprites, Game_Scripts.animations, Game_Scripts.controls, Game_Scripts.renderer, Game_Scripts.tileMap, Game_Scripts.animator, Game_Scripts.combat_UI, Game_Scripts.actions_manager, Game_Scripts.basic_game_mechanics, Game_Scripts.stage_Manager, Game_Scripts.stages, Game_Scripts.ui_elements, Game_Scripts.screen_layouts

#Extraenous functions such as copying arrays
functions = Game_Scripts.functions

#sprites
#sprites.sprite(self, name, x, y, z, w, h, imgUrl, animationSet, animated) is class object of sprite
#sprites.character() is class object of all characters
sprites = Game_Scripts.sprites

#animations list
#animations.animations['key'] is the list of animations
#animations.returnAnimation('string') is used to return an animation and prevent errors if animation doesn't exist
animations = Game_Scripts.animations

#controls
#controls.sC(ch) selected character returns key of the character in the dicitonary so to use, use ch[sC(ch)]
#controls.change_sC(character, ch) change selected character
#controls.keyPress(ch, cam, borders) key press event
controls = Game_Scripts.controls

#renderer
#renderer.camera2D(x,y,z) 2D camera class
#(renderList, cam, screen, borders) - 2D render main function, cam is what cam to render from but most likely going to be flat 2d cam, screen is screen where everything is
renderer = Game_Scripts.renderer

#3dTileMap
tileMapper = Game_Scripts.tileMap

#animate the animations
#animationManager(objects_to_animate, ch)
#animationPlayer(sprite, animation, ch)
#addAnimation(character, animation)
#removeAnimation(character, animation)
animator = Game_Scripts.animator

#ui_elements
ui_elements = Game_Scripts.ui_elements

#combat_UI manager
combat_UI_manager = Game_Scripts.combat_UI

#actions manager
actions_manager = Game_Scripts.actions_manager

#movement mechanics, damage mechanics, knock down, recover mechanics
basic_game_mechanics = Game_Scripts.basic_game_mechanics

#stage manager, set stage, begin battles, end battles, set backgrounds
stage_manager = Game_Scripts.stage_Manager

#stages
stages_list = Game_Scripts.stages

#screen layouts UI related
screen_layouts = Game_Scripts.screen_layouts

############################################################################
############################################################################

#Game Variables

run = True

game_fps = animations.fps

fps = animations.fps

#characters
ch = {}

#render type 3d cam can also be used for 2.5D
#cam = renderer.camera2D(550, 100, 0)
cam=renderer.camera3D(15, 8, 15, 0, 0)

#animate objects
objects_to_animate = []

#ojbects to update movement
objects_to_manage = []

#Map-Temporary
#tile_set = tileMapper.tileSet3D(15, 1, 10, 0, 0, -15, 0.5)
tile_set = tileMapper.tileSet2D(20,8,0,0,-15,2)
borders = tileMapper.borders2D(tile_set)

#Stage
current_stage = stages_list.stages['bridge_1']

#ui_elements on screen
ui_elements_list = []

############################################################################
############################################################################

#Game Logic Variables

#what screen we are at
screen = "title"

#the last screen
previous_screen = ""

#change screen
change_screen = ""

############################################################################
############################################################################

ch["tank"] = sprites.character(
    spriteObject=sprites.sprite(
        name = "tank",
        x=1056,
        y=-72,
        z=-14,
        w=400,
        h=300,
        heading="+",
        imgUrl="Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/Tank_Walk_Combat_Frame_1.png",
        animationSet = animations.animations["tank"],
        animated = True
    ),
    stats = sprites.stats(
        name = "dummy 2",
        chrClass = "tank",
        team = '1',
        maxHP = 300,
        lvl= 10,
        weight=200,
        rate = 1,
        walkspeed = 0.6,
        atk = 8,
    ),
    isSelected=True,
    playerCharacter = True,
)

ch["dummy"] = sprites.character(
    spriteObject=sprites.sprite(
        name = "dummy",
        x=72,
        y=-72,
        z=-14,
        w=400,
        h=300,
        heading="-",
        imgUrl="Sprite_Assets/Sprites/Tank_Sprites/Combat_Walk/Tank_Walk_Combat_Frame_1.png",
        animationSet = animations.animations["tank"],
        animated = True
    ),
    stats = sprites.stats(
        name = "dummy",
        chrClass = "tank",
        team = '2',
        maxHP = 150,
        lvl=5,
        weight=100,
        rate = 2,
        walkspeed = 0.7,
        atk = 60,
    ),
    isSelected=False,
    playerCharacter = True,
)

############################################################################
############################################################################

load_screen_elements = []
load_transition = 0
delay = 0

#functions switching between screens

def changeScreen(new_screen):

    global load_transition, change_screen, screen

    change_screen = new_screen

    screen = 'load'


def load():

    global load_transition, loading_screen, load_screen_elements, delay, screen, change_screen

    if load_transition <= fps * 1:

        load_transition += 1

    elif load_transition >= fps*1:

        load_transition = 0

        screen = change_screen

    pygame.draw.rect(loading_screen, (0, 0, 0), (0, 0, loading_screen.get_width(), loading_screen.get_height()), 0)

    if len(load_screen_elements) > 0:
        for i in range(0, len(load_screen_elements)):
            if load_screen_elements[i].name == 'loading_label':

                if delay == 0:
                    delay = math.floor(fps/4)
                    if load_screen_elements[i].text == 'Loading':
                        load_screen_elements[i].text = 'Loading.'
                    elif load_screen_elements[i].text == 'Loading.':
                        load_screen_elements[i].text = 'Loading..'
                    elif load_screen_elements[i].text == 'Loading..':
                        load_screen_elements[i].text = 'Loading...'
                    elif load_screen_elements[i].text == 'Loading...':
                        load_screen_elements[i].text = 'Loading'
                else:
                    delay -= 1

            ui_elements.draw_ui_element(load_screen_elements[i], loading_screen)

    s.blit(loading_screen, (0, 0))

############################################################################
############################################################################

#Game Logic

#combat win comditions = 1 team has zero participants remains
def returnTeams(list_chrs):
    #first lets make a team dictionary
    teams = {}

    for chr in list_chrs:
        #get team of chr
        team_key = list_chrs[chr].stats.team
        #if the team is already in the list
        if team_key in teams:
            teams[team_key][chr] = list_chrs[chr]
        elif not team_key in teams:
            teams[team_key] = {}
            teams[team_key][chr] = list_chrs[chr]

    return teams

#how many live team members there are
def return_alive_members(teams):

    live_count = {}

    for team in teams:
        live_count[team] = 0
        for chr in teams[team]:
            if teams[team][chr].stats.currentHP > 0:
                live_count[team] += 1

    return  live_count

#win conditions
def win_conditions(win_conditions):

    for i in range(0, len(win_conditions)):
        #the win condition we are checking
        win_condition = win_conditions[i]
        #elimate win condition
        if win_condition == 'eliminate':
            teams = returnTeams(ch)
            alive_members = return_alive_members(teams)
            for team in alive_members:
                if alive_members[team] == 0:
                    return True
    return False

############################################################################
############################################################################


#Run Game
pygame.event.get()

while run:

    # fps at top of engine
    t.tick(game_fps)

    #this handles pygame dying
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False

    #What to run on title screen
    if screen == "title":

        if previous_screen != "title":

            #first time we arrive on this screen
            ui_elements_list = []
            previous_screen = "title"

            #add all the buttons and stuff
            ui_elements_list = screen_layouts.return_screen_elements('title_screen')

            stage_manager.set_bgm('Stage_Assets/bgm/Uncontrollable.mp3')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

        elif previous_screen == "title":

            #we need mouse position
            mouse_pos = pygame.mouse.get_pos()

            # draw animated background and stuff


            # draw ui_stuff
            if len(ui_elements_list) > 0:

                for i in range(0, len(ui_elements_list)):
                    ui_elements.draw_ui_element(ui_elements_list[i], title_screen)
                    ui_elements.mouseHover(ui_elements_list[i], title_screen, mouse_pos)

                    #Button Interactivity
                    if hasattr(ui_elements_list[i], 'mouseOver'):
                        if ui_elements_list[i].mouseOver == True:
                            ui_elements_list[i].text_color = (0,255,255)
                            ui_elements_list[i].x_position = 0.85
                            ui_elements_list[i].width = 0.3
                        elif ui_elements_list[i].mouseOver == False:
                            ui_elements_list[i].text_color = (255, 255, 255)
                            ui_elements_list[i].x_position = 0.9
                            ui_elements_list[i].width = 0.2
                        if event.type == pygame.MOUSEBUTTONUP  and ui_elements_list[i].mouseOver == True:
                            if ui_elements_list[i].name == "duel_button":
                                #should bring us to a stage and character selection menu
                                for chr in ch:
                                    ch[chr].stats.currentHP = ch[chr].stats.maxHP
                                changeScreen("combat")
                            elif ui_elements_list[i].name == "quit_button":
                                run = False

            #draw the screen
            s.blit(title_screen, (0, 0))

    #What to run if screen is combat
    if screen == "combat":

        #first time on this screen
        if previous_screen != "combat":

            animations.update_fps(game_fps)

            #first time we arrive on this screen
            ui_elements_list = []
            previous_screen = "combat"

            #we need to load everything right?
            '''
            1.add characters to ch
            2.load stage
            3.load character animations
            4.add characters to manager and animator
            5.1 load the map <---
            5.move characters to spawn locations
            6.countdown battle
            '''
            #set the proper fps tick
            game_fps = fps
            #temporary already added characters to ch thus
            load()
            #clear old slates
            objects_to_manage = []
            objects_to_animate = []
            #loading the characters
            for chr in ch:
                load_thread = functions.loadThread(1, "Load-Thread", animations.animations[ch[chr].stats.chrClass])
                load_thread.start()
                #check to see if our threads have loaded
                while load_thread.loaded == False:
                    load()
                    t.tick(game_fps)
                    pygame.display.flip()
                objects_to_animate.append(ch[chr])
                objects_to_manage.append(ch[chr])
            #setting up the map
            tile_set = current_stage['map']['tile_set']
            borders = tileMapper.borders2D(tile_set)
            #spawning the characters
            teams = returnTeams(ch)
            spawn_locations = current_stage['spawns']
            #first we need to assign each team a slot for spawning
            slots_assigned = {}
            for team in teams:
                if not team in slots_assigned:
                    slots_assigned[team] = None
                    i = list(slots_assigned.keys()).index(team)
                    try:
                        spawn_locations[i]
                    except:
                        pass
                    else:
                        slots_assigned[team] = spawn_locations[i]
                    for chr in teams[team]:
                        ch[chr].spriteObject.x = slots_assigned[team][0]
                        ch[chr].spriteObject.y = slots_assigned[team][1]



        if win_conditions(['eliminate']) == False:

            #Controls
            #if event.type == pygame.MOUSEMOTION:
            #controls.mouseMove(event, cam, s)
            #mouse event

            #key press events
            #controls.keyPress3D(ch, cam)
            controls.keyPress2D(ch, borders, cam)

        #update tiles
        tileMapper.updateTileSet(tile_set)
        # Update Sprite Locations on Grid Pos
        tileMapper.updateSpriteTiles(tile_set, ch)
        # Update Tile Effects
        tileMapper.updateTileEffects(tile_set, ch)

        #update borders
        functions.updateBorders(borders)

        #screen fill
        s.fill((65, 65, 65))
        background_screen.fill((65, 65, 65))

        #ch[controls.sC(ch)].stats.currentHP -= 1

        # what to update actions for
        actions_manager.action_manager(objects_to_manage, ch)
        # What to animate
        animator.animationManager(objects_to_animate, ch)

        # update the basic mechanics
        basic_game_mechanics.updateBasicMechanics(ch)

        #What to render
        drawList = []
        #Add Stuff to Render
        drawList.append(ch["tank"].spriteObject)
        drawList.append(ch["dummy"].spriteObject)
        drawList.extend(tile_set)

        #Render Options
        renderer.flatRender(drawList, cam, borders, s, current_stage, background_screen, ch)
        #renderer.render3D(drawList, cam, s)

        # Draw UIs below renderer because renderer clears our screen
        combat_UI_manager.draw_combat_UI(s, combat_UI, w, h, ch)

        #win conditions
        if win_conditions(['eliminate']) == True:
            pass
            #game_fps=1
            #battle end animations before leaving
            #changeScreen('title')

    if screen =='load':
        if previous_screen != "load":
            previous_screen = "load"
            game_fps = fps
            pygame.mixer.stop()
            functions.clearCaches()
            load_screen_elements = screen_layouts.return_screen_elements('loading_screen')
        elif previous_screen == "load":
            load()

    #.diplay.flip = update screen with new stuff
    pygame.display.flip()



#pygame.quit()
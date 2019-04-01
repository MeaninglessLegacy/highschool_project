############################################################################
############################################################################

#Combat_UI

import pygame, math

from pygame import font

import Game_Scripts.controls, Game_Scripts.ui_assets, Game_Scripts.functions

functions = Game_Scripts.functions
controls = Game_Scripts.controls
ui_assets = Game_Scripts.ui_assets

############################################################################
############################################################################



#Draw the health bar of the selected character
def drawHealthBar(UI_surface, w, h, ch):

    #Size of Health Bar
    sizeX = math.floor(w*0.45)
    sizeY = h

    #Position of Health Bar
    positionX = math.floor(w*0.15)
    positionY = 0

    #Set Character
    character = ch
    #Get HP Stats
    maxHP = character.stats.maxHP
    currentHP = character.stats.currentHP

    #HpBar filled percent
    filledPercent = currentHP/maxHP

    #final size, floored because it takes an interger value
    fSizeX = math.floor(sizeX*filledPercent)

    #Draw rect on UI_Surface
    pygame.draw.rect(UI_surface, (53, 61, 22), (positionX, positionY, sizeX, sizeY), 0)
    pygame.draw.rect(UI_surface, (183, 255, 151), (positionX, positionY, fSizeX, sizeY), 0)

    #text surface
    f = font.Font(None, math.ceil(sizeY*1.5))
    #hp text littearly just HP
    hp_text = f.render("HP", True, [255, 255, 255])
    hp_text_rect = hp_text.get_rect(center=(math.ceil(w * 0.075), math.ceil(h * 0.55)))
    UI_surface.blit(hp_text, hp_text_rect)
    #hp label text
    text_Surface = f.render((str(int(currentHP))+"/"+str(maxHP)), True, [255, 255, 255])
    text_rect = text_Surface.get_rect(center=(math.ceil(w*0.8), math.ceil(h*0.55)))
    UI_surface.blit(text_Surface, text_rect)


#the ui along the bottom
def drawCharacterBoxs(primaryScreen, UI_surface, w, h, ch):
    #character boxes along the bottom
    #top half is character image/portrait sprite

    #first we need to draw the area that each object is going to be
    #no of player character
    player_characters = {}
    for key in ch:
        if ch[key].playerCharacter == True:
            player_characters[key] = ch[key]

    no_characters = len(player_characters)

    ui_elements = {}

    #for each character create a box
    for chr in player_characters:
        #size of the gui
        i = list(player_characters.keys()).index(chr)
        #how many indents there are each indent is 0.05 of the screen width, the number of indents is always one more than the no of characters
        indents_size = 0.05*(no_characters+1)
        #therefore the size of each character box should be the remaining width/no_characters
        char_guiX = (1-indents_size)/no_characters
        #we will scale down the char_guiX if it is greater than a portion of the screen
        if char_guiX > 0.14:
            char_guiX = 0.14
        #now we need to determine an indentation size
        indent_size = (1-(char_guiX*no_characters))/(no_characters+1)
        #y scale is arbituary
        char_guiY = 0.175
        #screen that is the box
        gui_main = pygame.Surface((math.floor(char_guiX*w),math.floor(char_guiY*h)), pygame.SRCALPHA)
        #debug
        #gui_main.fill((255,255,255))
        #final step blit the gui onto the game
        #x pos is the indents + previous guis so
        char_guiX_pos = char_guiX*i*w + indent_size*(i+1)*w
        char_guiY_pos = h*0.95 - char_guiY*h
        # Now we need to to draw the gui itself onto our surface



        # first thing we need to do is draw the character portrait
        ui_chr = player_characters[chr]
        #the entire background will be the portrait we will draw ontop of it
        ui_portrait = ui_assets.returnAsset(ui_chr.stats.chrClass)["portrait"]
        #we have a portrait
        if not ui_portrait is None:
            #Return the asset in image
            key = ui_portrait["image"]
            asset = functions.get_image(key)
            asset = pygame.transform.scale(asset, (math.floor(char_guiX*w), math.floor(char_guiY*h)))
            gui_main.blit(asset, (0, 0))

        #now that the portrait is drawn if it is selected draw selected box
        if ui_chr.isSelected == True:
            ui_selected = ui_assets.returnAsset("universal")["portrait_select"]
            asset = functions.get_image(ui_selected["image"])
            asset = pygame.transform.scale(asset, (math.floor(char_guiX * w), math.floor(char_guiY * h)))
            gui_main.blit(asset, (0, 0))

        #define a region for the rest of the ui to be drawn on

        stat_displaysX = math.floor(char_guiX*w)
        stat_displaysY = math.floor(char_guiY*h*0.33)

        stat_displaysX_pos = 0
        stat_displaysY_pos = char_guiY*h-stat_displaysY-char_guiY*h*0.1

        stat_displays = pygame.Surface((stat_displaysX,stat_displaysY), pygame.SRCALPHA)
        stat_displays.fill((50,50,50, 150))

        #draw the health bar
        hpBarX=math.floor(stat_displaysX)
        hpBarY=math.floor(stat_displaysY*0.3)
        hp_bar = pygame.Surface((hpBarX, hpBarY), pygame.SRCALPHA)
        drawHealthBar(hp_bar, hpBarX, hpBarY, ui_chr)
        stat_displays.blit(hp_bar, (0, stat_displaysY-hpBarY-stat_displaysY*0.1))

        #name label and level and stuff
        f = font.Font(None, math.ceil(stat_displaysY * 0.5))
        # name label
        name_text = f.render(ui_chr.stats.name, True, [255, 255, 255])
        name_text_rect = name_text.get_rect(center=(math.ceil(stat_displaysX * 0.2), math.ceil(stat_displaysY * 0.3)))
        stat_displays.blit(name_text, name_text_rect)
        # level label
        level_text = f.render((str(ui_chr.stats.lvl)), True, [255, 255, 255])
        level_rect = level_text.get_rect(center=(math.ceil(stat_displaysX * 0.8), math.ceil(stat_displaysY * 0.3)))
        stat_displays.blit(level_text, level_rect)



        #The next thing we need to be able to draw is the top left and top right sections for currently playing music and entering map


        #blit statdisplays
        gui_main.blit(stat_displays, (stat_displaysX_pos, stat_displaysY_pos))
        gui_main.convert()
        UI_surface.blit(gui_main, (char_guiX_pos, char_guiY_pos))

    #blit entire gui onto screen
    primaryScreen.blit(UI_surface, (0, 0))



############################################################################
############################################################################

blankSurface = None

#Main function
def draw_combat_UI(primaryScreen, UI_surface, w, h, ch):

    #Blank Surface/Redraw the UI
    if globals()['blankSurface'] is None:
        globals()['blankSurface'] = pygame.Surface((w, h), pygame.SRCALPHA)
    elif UI_surface is not blankSurface:
        UI_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    #draw Ui
    drawCharacterBoxs(primaryScreen, UI_surface, w, h, ch)

    pass



############################################################################
############################################################################
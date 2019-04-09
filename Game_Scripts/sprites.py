############################################################################
############################################################################

#SPRITES
import pygame, math, Game_Scripts.functions

functions = Game_Scripts.functions



############################################################################
############################################################################

#sprite class
class sprite(pygame.sprite.Sprite):
    def __init__(self, name, x, y, z, w, h, imgUrl, animationSet, animated, heading):
        #Basic Variables
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.imgUrl = imgUrl

        #Load Image
        self.img = pygame.image.load(imgUrl)
        self.img = pygame.transform.scale(self.img, (w, h))

        #direction facing
        self.heading = heading
        #direction travel
        self.direction = "east"

        # spriteBox
        self.spriteBox = spriteBox(self)

        #animations
        self.animationSet = animationSet
        self.animated = animated

        self.animationList = [animationSet["combat_idle"]]
        self.animationCounter = 0

        self.moving = False
        self.combat = True

    def changeImage(self, imgUrl):
        self.imgUrl = imgUrl

        self.img = functions.get_image(self.imgUrl, True)
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

    def resetWH(self, w, h):
        self.w = w
        self.h = h
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

#Stats
class stats():
    def __init__(self, name, chrClass, lvl, team, maxHP, rate, weight, walkspeed, atk):

        self.name = name
        self.lvl = lvl
        self.xp = 0
        self.chrClass = chrClass
        self.team = team
        self.rate = rate

        self.atk = atk
        self.shield_strength = 0
        self.shielding = False

        self.maxHP = maxHP
        self.currentHP = maxHP

        self.walkspeed = walkspeed
        self.base_weight = weight
        self.weight = weight
        self.momentum = (0,0)
        self.current_Tile = (0,0)

        self.queued_actions = []
        self.previous_action = []

        self.canMove = True
        self.knockedOut = False
        self.stunTimer = 0

#character itself
class character():
    #Add other stuff later
    def __init__(self, spriteObject, isSelected, playerCharacter, stats):
        self.spriteObject = spriteObject
        self.stats = stats
        self.isSelected = isSelected
        self.playerCharacter = playerCharacter

############################################################################
############################################################################

#3D Sprites

#Generate A Box For the Sprite for 3D Rendering
class spriteBox():

    def __init__(self, sprite):

        self.w = sprite.w
        self.h = sprite.h

        self.x = sprite.x
        self.y = sprite.y
        self.z = sprite.z

    def updateSpriteBox(self, sprite, cam, s):
        self.w = sprite.w
        self.h = sprite.h

        self.x = sprite.x
        self.y = sprite.y
        self.z = sprite.z

        """
            Sprite Box
            1-------0
            |       |
            |       |
            |       |
            3-------2
        """

        # vt vertices of the sprite box
        vt = []

        vt.append([self.x - 7, self.y + 10, self.z])
        vt.append([self.x + 7, self.y + 10, self.z])
        vt.append([self.x + 7, self.y - 0.5, self.z])
        vt.append([self.x - 7, self.y - 0.5, self.z])

        dC = []
        # Draw Coordinates = dt

        for i in range(0, len(vt)):
            x = vt[i][0]
            y = vt[i][1]
            z = vt[i][2]

            dC.append(functions.distortPoint(x, y, z, cam, s))

        #scale of the spritebox to scale sprite
        self.xScale = math.floor(math.fabs(dC[1][0]-dC[0][0]))
        self.yScale = math.floor(math.fabs(dC[1][1]-dC[3][1]))

        self.rect = pygame.Rect(dC[1], (self.xScale, self.yScale))

############################################################################
############################################################################
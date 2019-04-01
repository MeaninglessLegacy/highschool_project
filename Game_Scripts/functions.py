############################################################################
############################################################################

import threading, pygame, math, time

#Loaded Images
image_cache = {}

#loaded sounds
sound_cache = {}

#global borders
borders = []

############################################################################
############################################################################

class loadThread(threading.Thread):
    def __init__(self, threadID, name, load):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.load = load
        self.loaded = False
    def run(self):
        start_time = time.time()
        print("Starting " + self.name + " " + str(time.ctime(start_time)))
        preloadAnimationSet(self.load)
        self.loaded = True
        print("Exiting " + self.name + " " + str(time.ctime(time.time())) + " Time taken " + str(time.time()-start_time))

############################################################################
############################################################################

#copies and returns an array
def copyArray(input):
    returnArray = []

    for i in range(0, len(input)):
        returnArray.append(input[i])

    return returnArray

#Checking if image is loaded and loading images that need to be loaded
def get_image(key):
    #if loaded image is not in the cache then load the image once
    if not key in image_cache:
        # This makes sure even if we can't find the file it does not crash the engine.
        try:
            fh = open(key, 'r')
        except FileNotFoundError:
            print('missing sprite:'+key)
            pass
        else:
            #change back to .convert_alpha() later
            '''if " Stage_Assets" in key:
                image_cache[key] = pygame.image.load(key).convert()
            else:
                image_cache[key] = pygame.image.load(key).convert_alpha()'''
            image_cache[key] = pygame.image.load(key).convert_alpha()
    #return the image in cache
    return image_cache[key]

#clear loaded images
def clearCaches():

    global image_cache
    global sound_cache

    image_cache = {}
    sound_cache = {}

#update global borders
def updateBorders(newBorders):

    global borders

    borders = newBorders

#return borders
def get_Borders():

    return  borders

#Checking if sound is loaded and loading sound that need to be loaded
def get_sound(key):
    if not key in sound_cache:
        try:
            fh = open(key, 'r')
        except FileNotFoundError:
            print('missing sprite:'+key)
            pass
        else:
            sound_cache[key] = pygame.mixer.Sound(key)
    #return the image in cache
    return sound_cache[key]

############################################################################
############################################################################

#3D Functions

#rotatees a point
def rotatePoint(x, y, theta):
    si = math.sin(theta)
    co = math.cos(theta)

    #0,1  - 1,0 +cos +sin
    #1,0  -  0,-1 +cos -sin
    #0,-1  -  -1,0 -cos -sin
    #-1,0 - 0,1 -cos +sin

    #x = y*si + x*co
    #y = y*co - x*si
    #Reverse Because ccs,sin graph is counter clockwise invert sin
    x = x*co-y*si
    y = y*co+x*si

    return [x,y]

#Description: Distorts a singular point. Useful for drawing images
def distortPoint(x,y,z, cam, s):
    x -= cam.x
    y -= cam.y
    z -= cam.z

    xzR = rotatePoint(x, z, cam.xRot)
    x = xzR[0]
    z = xzR[1]
    yzR = rotatePoint(y, z, cam.yRot)
    y = yzR[0]
    z = yzR[1]

    """
    xr = cam.xRot
    yr = cam.yRot

    si = math.sin(xr)
    co = math.cos(xr)

    x = x * co - z * si
    z = z * co - x * si
    """

    # Distort XY by INV Z DIFFERENCE
    # LARGER DIFFERENCE = SMALLER
    # SMALLER DIFFERENCE = BIGGER

    if (z == 0):
        z = 0.00000000001

    zDistort = (s.get_width() / 2) / z

    x *= zDistort
    y *= zDistort

    x += s.get_width() / 2
    y += s.get_height() / 2

    return [x,y]



############################################################################
############################################################################


# preloader give animations as a array of the url
def preload(animations):
    for i in range(0, len(animations)):
        for o in range(0, len(animations[i]["frames"])):
            if not animations[i]["frames"][o] in image_cache:
                # This makes sure even if we can't find the file it does not crash the engine.
                try:
                    fh = open(animations[i]["frames"][o], 'r')
                except FileNotFoundError:
                    print('missing sprite' + animations[i]["frames"][o])
                    pass
                else:
                    image_cache[animations[i]["frames"][o]] = pygame.image.load(animations[i]["frames"][o])
                    #print(str("loaded "+animations[i]["frames"][o]))
                    if animations[i]['sounds'] != {}:
                        for sound in animations[i]['sounds']:
                            get_sound(animations[i]['sounds'][sound]['source'])

# preloader feed this a set of animations eg animations.animations['tank']
def preloadAnimationSet(animation_set):
    for key in animation_set:
        for o in range(0, len(animation_set[key]["frames"])):
            if not animation_set[key]["frames"][o] in image_cache:
                # This makes sure even if we can't find the file it does not crash the engine.
                try:
                    fh = open(animation_set[key]["frames"][o], 'r')
                except FileNotFoundError:
                    print('missing sprite' + animation_set[key]["frames"][o])
                    pass
                else:
                    image_cache[animation_set[key]["frames"][o]] = pygame.image.load(animation_set[key]["frames"][o])
                    #print(str("loaded " + animation_set[key]["frames"][o]))
                    if animation_set[key]['sounds'] != {}:
                        for sound in animation_set[key]['sounds']:
                            get_sound(animation_set[key]['sounds'][sound]['source'])
                            #print(str("loaded" + animation_set[key]['sounds'][sound]['source']))


############################################################################
############################################################################
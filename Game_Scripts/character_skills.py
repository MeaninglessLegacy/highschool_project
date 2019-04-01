############################################################################
############################################################################

#Character Skills

import pygame, math

import Game_Scripts.functions

functions = Game_Scripts.functions

############################################################################
############################################################################

#skills
import Game_Scripts.skills.tank_skills

#import the skills
skills_folder = Game_Scripts.skills

tank_skills = skills_folder.tank_skills


#put skills into dictionary
#class of chr is called and returns skills
abilities = {
    'tank' : tank_skills,
}

############################################################################
############################################################################

#returns the skills of the character
def returnSkills(chr):
    chrClass = chr.stats.chrClass
    if chrClass in abilities:
        return abilities[chrClass]


#Main useSkillFunction
def useSkill(chr, skill):
    #return skill set
    skill_set = returnSkills(chr)

    #if our skill set exists
    if not skill_set is None:
        #first skill is activated
        if skill == 'ability1':
            #checks to see if the chr has a skill in slot 1
            if hasattr(skill_set, 'ability1') == True:
                #use ability and get cooldown
                cooldown = skill_set.ability1(chr)
                #return cooldown
                return  cooldown
    pass
from string import ascii_uppercase
import random

robot_name_list=[]

class Robot(object):
    name=''
    def generate_name(self):
        return random.choice(ascii_uppercase)+random.choice(ascii_uppercase)+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    def set_name(self):
        newName=self.generate_name()
        while newName in robot_name_list:
            newName=self.generate_name()
        robot_name_list.append(newName)
        return newName
    def reset(self):
        self.name=self.set_name()
    def __init__(self):
        self.name=self.set_name()
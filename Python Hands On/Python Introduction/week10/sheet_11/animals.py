#############################
# UTILITIES                 #
#############################

'''
e.g. a function that reads in the images
'''


#############################
# ANIMALS                   #
#############################

'''
The classes representing animals.
First, define the class hierarchy.
Then think of what the classes have in common,
this functionality goes in the superclass.
Then think of what is special about the subclass,
this goes into the subclass.

Hints: Some methods can be applied to all animals
(e.g., visit(), eat()), some only apply to a particular
animal (e.g., swim()).

Which attributes do the objects have?
--> Design your __init__ methods accordingly.



'''



class read_image:#Base Klass

    def __init__(self,pathpicture):
        self.pathpicture=pathpicture
        

    
    def display_zoo(self):
        
        with open(self.pathpicture) as f:
            for line in f:
                print(line)

    def visiting(self):
        
        
        print('Visting',self.name)
        

    def __str__(self):

        print ('Name:' + str(self.name)+
               'Information: Animal <can eat(), sleep()>')

    def eating(self):

        print('I am a ',self.name,'I am ^^^^^^^^^Eating^^^^^')

    def sleeping(self):

        print('I am a', self.name,'I am !!!!SleepingZZZZZZ')

     def __str__(self):
         return "hey there'


        
        

                
class Mammal(read_image):

    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)#derives the read_image
        read_image.__str__(self)
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)
        

class Rodent(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)#derives the read_image
        read_image.__str__(self)
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)
    

class LandBird(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)#derives the read_image
        read_image.__str__(self)
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)


class WaterBird(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)#derives the read_image
        read_image.__str__(self)
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)


class Fish(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)#derives the read_image
        read_image.__str__(self)
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)


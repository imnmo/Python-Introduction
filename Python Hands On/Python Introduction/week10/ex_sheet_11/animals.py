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

    
    def visit(self):
        print('Visting',self.name)
        with open(self.pathpicture) as f:
            for line in f:
                print(line)
        print ('NAME:',self.name)
        print ('INFORMATION:')
        print ('\tAnimal <can eat(), sleep()>')
        
    def __str__(self):
        return self.name

    def eat(self):

        print('I am a ',self.name,'I am ^^^^^^^^^Eating^^^^^')

    def sleep(self):

        print('I am a', self.name,'I am !!!!SleepingZZZZZZ')

class Mammal(read_image):

    def __init__(self,name,pathpicture):#Extends the read_image
            read_image.__init__(self,pathpicture)
            self.name=name
       


class Rodent(read_image):
    
    def __init__(self,name,pathpicture):#Extends the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self)
        print ( '\t|' )
        print ('\t---- Mammal\n\t\t|\n\t\t----Rodent <can gnaw()>')
    def gnaw(self):
        print(' I am a', self.name, 'Gnawing****')
   
  
class LandBird(read_image):

    def __init__(self,name,pathpicture):#Extends the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
        
    def visit(self):
        read_image.visit(self)
        print ( '\t|' )
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Land Bird')
    def fly(self):

        print(' here I am', self.name, '))flying Higher)))')

class WaterBird(read_image):
    
    def __init__(self,name,pathpicture):#Extends the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self)
        print ( '\t|' )
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Water Bird <can swim() ')
    def fly(self):

        print(' here I am', self.name, '))flying Higher)))')
    def swim(self):

        print('I am a',self.name,'I am >>>>>>>Swimming------')
    
class Fish(read_image):
    def __init__(self,name,pathpicture):#Extends the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self)
        print ( '\t|' )
        print ('\t---- Fish <can swim()')
    def swim(self):

        print('I am a',self.name,'I am >>>>>>>Swimming------')

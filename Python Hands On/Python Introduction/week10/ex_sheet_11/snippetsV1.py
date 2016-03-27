
#Just to read and print:


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
        print ( '\t|' )
    def __str__(self):
        return self.name

    def eat(self):

        print('I am a ',self.name,'I am ^^^^^^^^^Eating^^^^^')

    def sleep(self):

        print('I am a', self.name,'I am !!!!SleepingZZZZZZ')

    
    

    

        
        

                
class Mammal(read_image):

    def __init__(self,name,pathpicture):#over riddes the read_image
            read_image.__init__(self,pathpicture)
            self.name=name
       


class Rodent(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self)
        print ('\t---- Mammal\n\t\t|\n\t\t----Rodent <can gnaw()>')
    def gnaw(self):
        print(' I am a', self.name, 'Gnawing****')

  
class LandBird(read_image):

    def __init__(self,name,pathpicture):#over riddes the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
        
    def visit(self):
        read_image.visit(self)
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Land Bird')
    def fly(self):

        print(' here I am', self.name, '))flying Higher)))')
        

class WaterBird(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self)
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Water Bird <can swim() ')
    def fly(self):

        print(' here I am', self.name, '))flying Higher)))')
    def swim(self):

        print('I am a',self.name,'I am >>>>>>>Swimming------')

        
class Fish(read_image):
    def __init__(self,name,pathpicture):#over riddes the read_image
        read_image.__init__(self,pathpicture)
        self.name=name
    def visit(self):
        read_image.visit(self) 
        print ('\t---- Fish <can swim()')
    def swim(self):

        print('I am a',self.name,'I am >>>>>>>Swimming------')

        
      
                

IMG_PATH = "ascii-art/"

zoo_img = ""
zoo_animals = []

def display_zoo():
    with open(IMG_PATH + "zoo.txt") as zoo_img:
        for line in zoo_img:
            print(line)
    print('Animals')           
    for animal in zoo_animals:
        # Hint: the __str__ method of animal
        # will be called from here.
        print("*", animal)
        
        

         
        
    

if __name__ == "__main__":
    #Read Image blah blah
    zoo_img = read_image(IMG_PATH + "zoo.txt")
    # Create the zoo animals
    bear = Mammal("bear", IMG_PATH + "bear.txt")
    zoo_animals.append(bear)
    beaver = Rodent("beaver", IMG_PATH + "beaver.txt")
    zoo_animals.append(beaver) 
    cockatoo = LandBird("cockatoo", IMG_PATH + "cockatoo.txt")
    zoo_animals.append(cockatoo)
    duck = WaterBird("duck", IMG_PATH + "duck.txt")
    zoo_animals.append(duck)
    elephant = Mammal("elephant", IMG_PATH + "elephant.txt")
    zoo_animals.append(elephant)
    fish = Fish("fish", IMG_PATH + "fish.txt")
    zoo_animals.append(fish)
    gorilla = Mammal("gorilla", IMG_PATH + "gorilla.txt")
    zoo_animals.append(gorilla)
    rabbit = Rodent("rabbit", IMG_PATH + "rabbit.txt")
    zoo_animals.append(rabbit)
    stork = WaterBird("stork", IMG_PATH + "stork.txt")
    zoo_animals.append(stork)
    vulture = LandBird("vulture", IMG_PATH + "vulture.txt")
    zoo_animals.append(vulture)


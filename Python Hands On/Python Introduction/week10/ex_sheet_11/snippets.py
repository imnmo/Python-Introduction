
#Just to read and print:


class read_image:#Base Klass

    def __init__(self,pathpicture):
        self.pathpicture=pathpicture

    
    def visiting(self):
        print('Visting',self.name)
    
    def display_zoo(self):

        with open(self.pathpicture) as f:
            for line in f:
                print(line)
    def __str__(self):
        return self.name

    def animal_info(self):

        print ('NAME:',self.name)
        print ('INFORMATION:')
        print ('\tAnimal <can eat(), sleep()>')
        print ( '\t|' )
       


    def eating(self):

        print('I am a ',self.name,'I am ^^^^^^^^^Eating^^^^^')

    def sleeping(self):

        print('I am a', self.name,'I am !!!!SleepingZZZZZZ')

    def swimming(self):

        print('I am a',self.name,'I am >>>>>>>Swimming------')

    def gnawning(self):
        print(' I am a', self.name, 'Gnawing****')

    def flying(self):

        print(' here I am', self.name, '))flying Higher)))')
        

        
        

                
class Mammal(read_image):

    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)
        read_image.animal_info(self)#derives the read_image
        print ('\t----Mammal')
        
        
        
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
        read_image.display_zoo(self)
        read_image.animal_info(self)#derives the read_image
        print ('\t---- Mammal\n\t\t|\n\t\t----Rodent <can gnaw()>')
        
        
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)

        
    def gnaw(self):
        read_image.gnawning(self)
  

class LandBird(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        read_image.visiting(self)
        read_image.display_zoo(self)
        read_image.animal_info(self)#derives the read_image
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Land Bird')
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)

    def fly(self):

        read_image.flying(self)


class WaterBird(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):

        read_image.visiting(self)
        read_image.display_zoo(self)
        read_image.animal_info(self)#derives the read_image
        print ('\t---- Bird <can fly()>\n\t\t|\n\t\t----Water Bird <can swim() ')
        
    def eat(self):
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)
        
    def fly(self):
        
        read_image.flying(self)
        
    def swim(self):

        read_image.swimming(self)


class Fish(read_image):
    
    def __init__(self,name,pathpicture):#over riddes the read_image

        self.name=name
        self.pathpicture=pathpicture

    def visit(self):
        
        read_image.visiting(self)
        read_image.display_zoo(self)
        read_image.animal_info(self)#derives the read_image
        print ('\t---- Fish <can swim()')
        
       
        
        
        
        
    def eat(self):
        
        read_image.eating(self)
        
    def sleep(self):

        read_image.sleeping(self)

    def swim(self):

        read_image.swimming(self)


       

                

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
    

                

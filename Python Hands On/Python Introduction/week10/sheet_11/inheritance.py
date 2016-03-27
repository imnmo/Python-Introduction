class hello:

    def mother(self,name):
        self.name=name
        print('Is program working')


class son(hello):


    def son1(self):
        print('Hello I am the son of',self.name)





if __name__=='___main__':



    welcome=hello()
    welcome=son()

    welcome.mother('Anne')
    welcome.son1()

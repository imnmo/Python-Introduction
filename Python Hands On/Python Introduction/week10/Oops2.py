class Robot:
    typeofrobot1="Humanoid"
    typeofrobot2="diasterHumanoidrobot"
    numberofrobots=0

    def classification(self,creator):
        self.creator=creator
        Robot.numberofrobots+=1
        
        if self.creator =='Vasi':
            
            print(Robot.typeofrobot1,'-',self.creator)
        else:
            
            print(Robot.typeofrobot2,'-',self.creator)


    @staticmethod
    def printinfo():
        print(Robot.numberofrobots)




if __name__ == '__main__':
    chittiv1=Robot()
    chittiv2=Robot()
    chittiv1.classification('Vasi')
    chittiv2.classification('Bora')
    Robot.printinfo()

    
        
        

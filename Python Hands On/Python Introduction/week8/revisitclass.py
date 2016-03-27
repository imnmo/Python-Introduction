class player:
    def blast(self,enemy):
        enemy.die()

class invader:
    def die(self):
        print('I owe much for my death')













if __name__ =='__main___':
    hero=player()
    enemy=invader()
    hero.blast(invader)
                                  

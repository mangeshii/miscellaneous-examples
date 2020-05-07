class Centaur:
    def __init__(self):
        self.shoot=0
        self.run=30
        self.standing=False
        self.sleeping=True

    def shooting(self):
        if self.sleeping:
            if self.standing:  
                if self.shoot < 3:
                    print('twag twag')
                    self.shoot +=1
                else:
                    return self.cranky()

    def running(self):
        if self.sleeping:
            if self.standing:
                if self.run > 0:
                    print('clip clop clip clop')
                    self.run -= 10
                else:
                    print('tired')
    def cranky(self):
        print('NO!')


    def stand(self):
        if self.sleeping:
            print('standing')
            self.standing = True

    def sleep(self):
        print('sleeping')
        self.sleeping=False





c=Centaur()
c.sleep()
c.stand()
c.shooting()
c.shooting()
c.shooting()
c.shooting()
c.running()
c.running()
c.running()
c.running()

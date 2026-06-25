import time
class MobilePhone ():
    def __init__(self, model, battery):
        self.model=model
        self.battery=battery
    def use_phone (self):
            if self.battery <= 4:
                self.battery = 0
                print ("Your phone is out of battery!")
            elif self.battery >=5:
                self.battery -= 5
                print ("Your phone is being used!")
                time.sleep (5)
my_phone = MobilePhone ("iPhone",88)

my_phone.use_phone()
print ("Battery left:",my_phone.battery)
class Cab:

    def __init__(self):

        self.number_of_drivers = 1
        self.cabtype = 'Regular'

    
    def sharing_ride(self):
        return "Cab Sharing Not Available" 

    def startRide():
        return "Ride start"

    def endTrip(self):
        return "End Trip Now"  

    def wifi(self):
        return "Wifi switch on/of"

    def safetyAlert(self):
        return "Please wear seat belt"
        



if __name__ == "__main__":

    driver = Cab()
    print(driver.sharing_ride())
    print(driver.endTrip())
    print(driver.fuel())
    



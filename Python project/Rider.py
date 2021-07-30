class Rider:
    
    def __init__(self, name, mobile, location):
        
        self.name = name
        self.mobile = mobile
        self.location = 'Banglore'

    # """rider can login"""
    def rider_login(self):
        return "Click Login"

    # """Rider can select destination to travel"""
    def destination_To_Travel(self):
        return "Location set"

    #Rider can book a book to Travel selected destination"
    def book_Cab(self):
         return "Cab booked"

    #Ride End after reaching the destination
    def end_ride(self, end):
        return "Ride End at", end

    #Payment after ride end
    def pay_money(self):
        return "Paid"


if __name__ == "__main__":
    
    cab_rider = Rider('Venkat sundeep', 99999, 'banglore') #Inputs to the arguments and calling function
    print(cab_rider.name)
    print(cab_rider.end_ride('Banglore'))



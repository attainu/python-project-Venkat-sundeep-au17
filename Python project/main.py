# from Driver import *
# from Rider import *
# from Cab import *
import math

class Mycab:
    def __init__(self):

        self.Drivers_list  = list()
        self.Riders_list   = list()
        self.services      = ['Banglore', 'Chennai', 'Mumbai', 'Goa', 'hyderabad']
        self.driver_status = 'Active'
        self.current_rides = list()
        self.fare          = 2
        self.wif           = 'ON'
        

    #Drive Login Function 
    def driver_login(self, name, password, otp , status): 

      if status == 'on' or 'ON':
          self.driver_status = 'Active' #updating driver status attribute 
          print('hey',name +',', "Your now", self.driver_status) 
          print('Accept rides now')
      else: 
          self.driver_status = 'Not Active' #updating driver status attribute 
          print('hey',"'"+name+"'" + ',', "Your", self.driver_status) 

    #Rider Login Function
    def rider_login(self, username, password):
      print("")
      print('Hello,', username)
      print("------------")
      print('Book a ride now!')


    #Current location setup 
    def select_current_location(self, currentlocation):

        for city in range(len(self.services)):
            if currentLocation == city:
                print('Your current Location updated to',self.services[city]+'.')
                break
            else: 
                print("Sorry, Your location has not servceble, we will expand soon. Thank you!")
            
                
    #Ride Destination setupby rider
    def choose_destination(self, destination):
      
      for cities in range (len(self.services)):
          if destination == cities:
            print("")
            print('Your Destination set to',self.services[cities]+'.')
            break
          elif destination == destination:
            print("")
            print('Destination and current location should not be the same, Please select your destination Again')
            break
      else:
        print("")
        print( 'oops, No services in',self.services[cities]+'.' )

    #ride booking confirmation
    def book_ride(self):
      rideconfirm = int(input("Press 1 to confirm ride: "))
      if rideconfirm == 1:
        ride = 1
        self.current_rides.append(ride) #updating current rides attribute 
        print('Your Ride Booked')
      else:
        print("Please confirm your ride")
      # print('List of rides booked',self.current_rides)
    
    #Driver ride accept
    def accept_ride(self):
        ride = '0'
        self.current_rides.append(ride) #updating current ride  attribute 
        self.current_rides.pop()
        self.current_rides.append(ride)
        # print('No rides',self.current_rides)

    #Driver pickup
    def pickup(self):
      picup = int(input("press 1 to confirm pickup: "))
      if picup == 1:
        print("Driver has started, Please wait a moment")
      else: 
        print('enter: correct input')
        
    
    #wife on/of
    def wifi(self, wif):
      if wif == 1:
        print('Wifi connected')
      else: 
        print("Wifi not connected")
        self.wif = 'OFF'   

    #safety nofitication
    def safety(self):
      safe = input('Type "yes" if you wear sitbelt: ')
      if safe == 'yes' or 'Yes':
        print('Thank you')
      else: print('Please wear seatbelt')

    #destination alert
    def reached(self):
      reach = input('press 1 to check your status: ')
      if reach == 1:
        print("You are at destination.")
      else: print('you will reach soon,')  

    #Distance Travelled
    def distance(self):

       location1  = input("enter distance: ")
       X1 = location1.split(",")
       location2  =  input("enter second distance: ")
       X2 = location2.split(",")
       distance = math.sqrt( ((int(X1[0])-int(X2[0]))**2)+((int(X1[1])-int(X2[1]))**2) )
       print("Total Distance Travelled :", distance)
       fare = distance * 2
       print("Total fare", round(fare))

    def payment(self, confirmation):
        print('Payment succesfully')

    def end(self):
      end = int(input('Please 1 to close the ride: '))
      if end == 1:
        print('Thank you! Have a Nice Day.')
      else: print('Please relogin to book return ride') 

if __name__=='__main__':
      #Driver portal
     print(input('Driver Login - Press Enter'))
     print("<<<--------------------------------Driver Login Portal-------------------------------->>>")
     name = input('Enter your ID: ')
     password = input('Enter your Password: ')
     print('Your One time password 2345')
     print("")
     otp = input('Enter OTP: ')
     status = input('Enter ON/OFF: ') 
     driver_login = Mycab()
     driver_login.driver_login(name, password, otp, status)
  #Driver login end
  #Rider Login Start
     print('----------------------------------------------------MyCabs----------------------------------------------------')
     rider = Mycab()
     driver = Mycab()
     print("Rider Login")
     print("")
     username = input('Enter your Name: ')
     password = input('Enter Your Password : ')
     rider.rider_login(username, password)
     print(input('Press "'"Enter"'" to setup your current location.'))
     print("")
     print('Services Availble cities:')
     print('------------------------ ')
     print('Press 0 - Banglore')
     print('Press 1 - Chennai')
     print('Press 2 - Munbai')
     print('Press 3 - Goa')
     print('Press 4 - Hyderabad')
     print('------------------------ ')

     
     currentLocation = int(input('Enter your location here: '))
     print('------------------------ ')
     rider.select_current_location(currentLocation)
     print("")

     print('Services Availble cities:')
     print('------------------------ ')
     print('Press 0 - Banglore')
     print('Press 1 - Chennai')
     print('Press 2 - Munbai')
     print('Press 3 - Goa')
     print('Press 4 - Hyderabad')
     print('--------------------------- ')

     Destination = int(input('Enter your Destination here: '))
     rider.choose_destination(Destination)
     print("")
     rider.book_ride()
     driver.accept_ride()
     print("")
     driver.pickup()
     print("")
     driver.safety()
     print("")
     wif = int(input('Enter 1 to ON WIFI: '))
     driver.wifi(wif)
     print('Wifi',driver.wif)
     print("")
     driver.reached()
     print("")
     rider.distance()
     confirmation = input('Types "yes" if you paid: ')
     print("")
     rider.payment(confirmation)
     print(' _________________')
     print("//////////////////")
     print("")
     driver.end()
     

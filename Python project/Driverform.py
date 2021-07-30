class DriverRegistration:
    
    def __init__(self, fullname, age, licence,experience, email, mobile, password):

        self.fullname = fullname
        self.age = age
        self.drivinglicence = licence
        self.experience = experience
        self.email  = email
        self.mobile = mobile
        self.__createpassword = password
    def createAccount(self):
        
        return " Account Created "
         

if __name__ == "__main__":
    
    # Input for registration
    create  = int(input('Press 1 to create account: '))
    drivername = input('Enter Your name')
    driverage = input('Enter your age: ')
    licence = int(input('Press 5 to confirm Licence: '))
    driverexperience = int(input('How much Experience do you have : '))
    emails = input("Enter your email login id: ")
    phone = int(input("Enter your contact number: "))
    passwords = input('Create your login password: ')

    driver   = DriverRegistration(drivername, driverage, licence, driverexperience, emails, phone, passwords)
    # if create == 1:
    #     print(driver.createAccount())
    # else: 
    #     print('Failed, Please Register again') 
    if licence == 5:                                                          
        print("Awesome! Your Licence approved.")
    else:
        print('You are not eligible to register, please come back with licence.')

    signup = input('Press enter to confirm and login')

    print("hello",driver.fullname, "Welcome to  MyCABS")
   


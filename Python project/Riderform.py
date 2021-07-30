class RiderRegistration:
    
    def __init__(self, fullname, age, email, mobile, password):

        self.fullname = fullname
        self.age = age
        self.email  = email
        self.mobile = mobile
        self.__createpassword = password
    
    def createAccount(self):

        return " Account Created "
         

if __name__ == "__main__":


    rider   = RiderRegistration('Venkat sundeep', 'age', 'email', 'mobile', 'password')
    create  = int(input('Press 1 to create account: '))

    if create == 1:
        print(rider.createAccount())
    else: 
        print('Exit')

    print("Welcome to OLA Cabs", "'"+rider.fullname+"'")
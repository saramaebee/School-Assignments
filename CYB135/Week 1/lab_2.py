# class Login
class Login():
    #Constructor
    def __init__(self):
        # setsid, password to default values
        self.simLogin="Test"
        self.simpass="test1234"
        
        
    # check_credentials() method accepts user id, password
    # as function arguments and checks it with default values
    def check_credentials(self,Id,Pass):
        #if userId,Password both are correct,login success
        if(self.simLogin==Id and self.simpass==Pass):
            print("Successful login!")
            return True
        #if userId is correct and wrong password
        elif(self.simLogin==Id and self.simpass!=Pass):
            print("Login name is correct, incorrect password!")
            return False
        #if userId wrong and valid password
        elif(self.simLogin!=Id and self.simpass==Pass):
            print("Login name is incorrect, password accepted!")
            return False
         #If both userId and password are wrong
        else:
            return False

if __name__=="__main__":
    # creating a Login class object user1
    user1= Login()
    # Declaring a variable count keep
    # track of login attempts
    count = 0
    max_count = 5
    # credentials or user enter invalid details 5times
    
    while (count < max_count):
        # read user_id and password from user
        user_id = input()
        password = input()
        # using user1 object of class Login
        # access check_credentials() methd of Login class
        # store the funtion return boolean in check variable
        Login_check=user1.check_credentials(user_id,password)
        # if check==True then user entered valid details
        # break the while loop
        if(Login_check==True):
            break
        # if check==False then user entered invalid details
        # increment number of tries by 1
        if(Login_check==False):
            count = count + 1
            print(user_id, password)
            print('Unsuccessful login attempt!')
            print('Try again - you have ', 5 - count, 'attempts left!')
    if count >= 5:
        if (Login_check==False):
            print(user_id, password)
            print('Unsuccessful login attempt!')

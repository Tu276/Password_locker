import unittest
from locker import User
from locker import Credentials

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the User class behaviours


    Args:
    
     unittest.TestCase: TestCase class that helps in creating test cases

    '''
    def tearDown(self):
        '''
        tear down method that cleans up after each test case is run
        '''
        User.user_List = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("tu276","nathan") #create user object

    def test_init(self):
         
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login_username,"tu276")
        self.assertEqual(self.new_user.user_password,"nathan")

    def test_save_user(self):
        '''
        test case to see if user ogject is saved into 

        '''
        self.new_user.save_user() #save user
        self.assertEqual(len(User.user_List),1)

    def test_save_multiple_user(self):

        self.new_user.save_user()
        test_user = User("Test_user","password")#new user

        test_user.save_user()
        self.assertEqual(len(User.user_List),2)

    

    
        

# if __name__ == '__main__':#######################################################
#     unittest.main()####################################3

class TestCredentials(unittest.TestCase):
    '''
    test class that defines test cases for the Credentials class behaviours


    Args:
    
     unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def tearDown(self):
        
        Credentials.credentials_List = []

        
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_crendentials = Credentials("facebook","tu276","nathan") # create credentials object
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_crendentials.account_name,"facebook")
        self.assertEqual(self.new_crendentials.account_username,"tu276")
        self.assertEqual(self.new_crendentials.account_password,"nathan")

    def test_save_credentials(self):
        '''
        test case to see if user ogject is saved into 

        '''
        self.new_crendentials.save_credentials() #save user
        self.assertEqual(len(Credentials.credentials_List),1)

    def test_save_multiple_credentials(self):
        
        self.new_crendentials.save_credentials()
        test_credentials = Credentials("test","testusername","testpassword")# new cerdentials 

        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_List),2)


if __name__ == '__main__':
    unittest.main()
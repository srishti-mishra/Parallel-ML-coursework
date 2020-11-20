import re 
from time import sleep   
# Make a regular expression 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
      
# Define a function for 
# for validating an Email 
def check(email):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        print("Valid Email:", email)  
          
    else:  
        print("Invalid Email:", email)  
        
        
      
  
# Driver Code  
if __name__ == '__main__' :  
      
    # Enter the email  
    email = "srishtimishra101295@gmail.com"
      
    # calling run function  
    check(email) 
  
    email = "mishra.sr@northeastern.edu"
    check(email) 
  
    email = "srishtimishra.xyz"
    check(email) 
    sleep(5)
    print('End of Process 2')     
   
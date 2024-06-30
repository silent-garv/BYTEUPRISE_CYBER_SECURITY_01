#Password strength checker 
import re   # importing regular expressions 

password = input("Enter your password :")
if len(password) < 8:   # condition to check length of password 
    print("Password must be at least 8 character long.")
elif not re.search("[A-Z]",password):  # condition to add Uppercase in password 
    print("Password must contain at least one uppercase letter")
elif not re.search("[a-z]",password):   # condition to add Lowercase in password 
    print("Password must contain at least one lowercase letter")
elif not re.search("[0-9]",password):  # condition to add number in password 
    print("Password must contain one number")
elif not re.search("[@,!,#,$,%,^,&,*]",password):   # conditionto add special character in password 
    print("Password must contain at least one special character")    
else:
    print("password is strong")        

email  = input("enter your Email:-")
if len(email)>=6:
    pass
else:
    print("wrong Email")
if email[0].isalpha():
   pass
else:
    print("wrong Email")
if email[0].islower():
    pass
else:
    print("error")
if email.count("@")==1 and ("@" in email):
    pass
else:
    print("wrong")
if (email[-4]==".") or (email[-3]=="."):
    pass
else:
    print("wrong email2")

s=input("Enter a phone no. of 10-digits and 2 dashes like -> 017-555-1212")
l=len(s)
if(l==12):
    print("THe entered phone no. is correct")
    if (s[3]=='-'and s[7]=='-'):
            print(" Yes, Entered phone no. is in valid format")
    else:
            print("No, Entered phone no. is not valid format")
else:
    print("Invaid, Please check the instruction and enter correctly")



while True:
    s=input("Please enter a sentence or q to quit")
    if(s=='q'):
        break;
    else:
        new_str = ""
        for i in range(0,len(s)):
            if s[i].isupper():
                #print(s[i])
                new_str= new_str+s[i].lower()
            if s[i].islower():
                new_str = new_str + s[i].upper()
            if s[i]== ' ':
                new_str = new_str + s[i]
        print(new_str)
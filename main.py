import string
import random

if __name__=="__main__":
    s1=string.ascii_lowercase
    print(s1)
    s2=string.ascii_uppercase
    print(s2)
    s3=string.digits
    print(s3)
    s4=string.punctuation
    print(s4)
    plen=int(input("Enter Password length\n"))
    s=[]
    s=s.extend(list(s1))
    s=s.extend(list(s2))
    s=s.extend(list(s3))
    s=s.extend(list(s4))
    print(s)
    random.shuffle(s)
    print(s)
    print("Your Password is:")
    print(random.sample(s,4))
    print("".join(s[0:plen]))
    
#///////////////////////////////////////Fors And Loops

def Number():
    for x in range(1,101):
        print(x)
def sumNumber():
    sum=0
    for x in range(1,50):
        sum=sum+x
    print(sum)
def TableZ():
    number=int(input("Enter Number : "))
    num2=0
    for x in range(1,10):
        num2=number * x
        print (num2)
def sumEvenNumbers():
    sum1=0
    for x in range(1,100):
        if(x%2==0):
            sum1=sum1+x
    print(sum1)
    
def EvenNumbers():
   
    for x in range(1,100):
        if(x%2==0):
            print(x)
def fors():
    while(True):
        print(" Chose one : \n [1] Number \n [2]SumNumber \n [3]Jadval Zarb \n [4]Sum Even Numbers \n [5] Show Even Numbers \n [0] Exit")
        number=input()
        if(number=="1"):
            Number()
        elif(number=="2"):
            sumNumber()
        elif(number=="3"):
            TableZ()
        elif(number=="4"):
            sumEvenNumbers()
        elif(number=="5"):
            EvenNumbers()
        elif(number=="0"):
            break
#///////////////////////////////////////////////////////// Tuple And Lists

def AddUser():
    mylist=["ali","hasan","reza"]
    print(mylist)
    name=""
    count=int(input("how many you have name to add list: "))
    for x in range(count):
        name=input("Enter Name: ")
        mylist.append(name)
    print(mylist)
def DeleteName():
    mylist=["ali","Reza","hasan","mohsen"]
    print (mylist)
    remove=input("What you want delete : ")
    mylist.remove(remove)
    print(mylist)
def mergelist():
    numberlist=[1,2,3,4,5,6]
    charlist=["a","b","c","d"]
    print(numberlist)
    print(charlist)
    charlist.extend(numberlist)
    print (charlist)
def reverse():
    
    numberlist=[6,5,4,3,2,1]
    print(numberlist[::-1])
def randomnumbers():
    import random
    mylist=[]
    mylist2=[]
    for x in range(4):
        mylist.append(random.randint(0,10))
    print (mylist)
    for x in range(4):
        mylist2.append(random.randint(0,10))
    print (mylist2)
    a=random.randint(0,3)
    print(a)
    print(mylist2[a] in mylist)
#///////////////////////////////////////////////////////Tuple founction is Down

def ShowfavoritColors():
    tp=("Red","Blue","Green","Black","Pink")
    print(tp)
def Numbers():
    tp=(1,2,3,4,5,6,7,8,9,10)
    print("List Is : ",tp)
    print(tp.count(5))
def Month():
    month=("farvardin","ordibehesht","khordad","tir","mordad","shahrivar","mehr","aban","azar","day","bahman","esfand")
    x=input("Enter Your Month: ")
    if(x in month):
        print("Founded")
    else:
        print("Not Found")
def AVG():
    scoreAVG=0
    rezult=()
    score1=0
    number1=int(input("How many you have Student To enter : "))
    number2=int(input("How many you have score to enter : "))
    r=list(rezult)
    for i in range(number1):
        name=input("Enter name: ")
        r.append(name)
        for f in range(number2):
            score1=int(input("Enter Score : "))
            scoreAVG=scoreAVG+score1
            if(f==number2-1):
                scoreAVG=scoreAVG/number2
                x="{:.2f}".format(scoreAVG)
                r.append(x)
                scoreAVG=0
    rezult=tuple(r)
    print(rezult)
def Dfrendbetween():
    mylist=["a","b","c","d"]
    mytuble=("A","B","C","D")
    mydec={"A","B","C","D"}
    print(mylist)
    print(mytuble)
    print(mydec)
def showtupls():
    while(True):
        print(" [1] show my Favorti Color\n [2] Numbers \n [3] Month \n [4] AVG \n [5] show Defrend between list Tuple and Decsionry \n [0] Exit")
        number=input()
        if(number=="0"):
            break
        elif(number=="1"):
            ShowfavoritColors()
        elif(number=="2"):
            Numbers()
        elif(number=="3"):
            Month()
        elif(number=="4"):
            AVG()
        elif(number=="5"):
            Dfrendbetween()
        else:
            print("Your Chose not in List")
def ListandTuple():
    while(True):
        print("List exercise")
        print(" Chose One \n [1]Add User \n [2] Delete Name From List \n [3] Marge List \n [4]Reverse List \n [5]Random Number \n [*]Show Tuple exercise \n [0] Exit")
        EntersNumber=input()
        if(EntersNumber=="1"):
            AddUser()
        elif(EntersNumber=="2"):
            DeleteName()
        elif(EntersNumber=="3"):
            mergelist()
        elif(EntersNumber=="4"):
            reverse()
        elif(EntersNumber=="5"):
            randomnumbers()
        elif(EntersNumber=="*"):
            showtupls()
        elif(EntersNumber=="0"):
            break
        else:
            print("Your Chose not In list ")
#///////////////////////////////////////////////////////////////////////// Ifs

def EvenAndodd():
    number=input("Enter Your Number: ")
    number=int(number)
    if(number%2==0):
      print ("Your number is Even")
    else:
       print("your number is Odd")
def HotOrCold():
   temperature=input("Enter Temperature Your Room: ")
   temperature=int(temperature)
   if(temperature >15):
     print("Your room is Hot")
   else:
      print("Your Room is Cold")
def Register():
   username=input("Enter your User Name : ")
   Password=input("Enter Your Passwprd: ")
   if(username=="User"and Password=="1234"):
      print("User Name and Password Is True")
   else:
      print("User name or Password is Wrong")
def Vote():
   print ("Plase answer questions whit \"YES\" OR \"NO\"")
   citizen=input("Are you citizen ? :")
   Age=input("How old are you ? : ")
   Age=int(Age)
   if(citizen=="yes" and Age>=18):
      print("You can Vote")
   elif(citizen=="yes" and Age<18):
      print ("You are not of legal age")
   else:
      print ("You must be citizen this country")
def Off():
   User=input("Are you User? :")
   Mony=input("how many use chashe ?: ")
   Mony=int(Mony)
   if(User=="yes" and Mony>100):
      print("You can use discounts")
   else:
      print("You Can't Use Discounts!!")      
def showifs():
    while(True):
        print ("Chose One: \n [1] Even or Odd number \n [2] Hot or Cold \n [3] Login \n [4] Can you Vote ?  \n [5] Can i Use Discounts? \n [0] Exit")
        numberchose=input()
        if(numberchose=="1"):
            EvenAndodd()
        elif(numberchose=="2"):
            HotOrCold()
        elif(numberchose=="3"):
            Register()
        elif(numberchose=="4"):
            Vote()
        elif(numberchose=="5"):
            Off()
        elif(numberchose=="0"):
            break
        else:
            print("Your Enters not In list")
while(True):
    print("Chose one: \n [1]Loop \n [2]List And Tuple \n [3]if")
    number1=input()
    if(number1=="1"):
        fors()
    elif(number1=="2"):
        ListandTuple()
    elif (number1=="3"):
        showifs()
    else:
        print("Your Chose not in list Try Again")


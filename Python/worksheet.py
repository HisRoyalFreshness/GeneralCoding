import statistics
import random
def mode(nums):
    print("The mode is {0}".format(statistics.mode(nums)))
          
def median(nums):
    
    print("The mean is {0}".format(nums[(len(nums)//2)]))

def mean(nums):
    b=0
    for count in nums:
        b+=nums[count]
    b=b/len(nums)
    print("The mean is {0}".format(b))

def displayq2menu():
    print()
    print("------Question 2------")
    print()
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Birthday Generator")
    print("0. Quit")
    
def birthdaygen():
    month=[["January",31],["Feburary",28],["March",31],["April",30],["May",31],["June",30],["July",31],["August",31],["September",30],["October",31],["November",30],["December",31]]
    genmonth=month[random.randint(0,11)]
    while True:
        gendate=random.randint(1,31)
        if gendate<genmonth[1]:
            break
    if gendate in [1,21,31]:
        suffix="st"
    elif gendate in [2,22]:
        suffix="nd"
    elif gendate in [3,23]:
        suffix="rd"
    else:
        suffix="th"
    print("Your random birthday is {0} {1}{2}!".format(genmonth[0],gendate,suffix))

    
def q2():
    while True:
        displayq2menu()
        nums=[1,2,3,3,3,4,4,5,6,7,8,9,10]
        while True:
            try:  
                choice=int(input("What would you like to do? "))
                print()
                if choice in [1,2,3,4,0]:
                    break
                else:
                    print("That's not a valid input!") 
            except:
                print("That's not even a number!")      
        if choice==1:
            mean(nums)
        elif choice==2:
            median(nums)
        elif choice==3:
            mode(nums)
        elif choice==4:
            birthdaygen()
        elif choice==0:
            break
        
def money():
    amount=100
    while True:
        while True:
                try:  
                    choice=float(input("How much did you spend? £"))
                    print()
                    if choice>0:
                        break
                    else:
                        print("That's not a valid input!") 
                except:
                    print("That's not even a number!")
        amount-=choice
        if amount<=0:
            print("You've gone over 100 pounds, you can't buy that!")
            break
        
def hottea():
    while True:
            try:  
                teatemp=float(input("What tempreture is your tea? "))
                target=float(input("What tempreture would you like your tea at? "))
                print()
                if 10000>teatemp>0 and 0<=target<teatemp:
                    break
                else:
                    print("That's not a valid input!") 
            except:
                print("That's not even a number!")
    count=0
    while teatemp>target:
        count+=1
        teatemp=teatemp*0.9
    print("It took {0} blows to cool it below {1}*c!".format(count,int(target)))
        
        
def q3():
    while True:   
        print()
        print("------Question 3------")
        print()
        print("1. £100 to spend")
        print("2. Hot Tea")
        print("0. Quit")
        while True:
            try:  
                choice=int(input("What would you like to do? "))
                print()
                if choice in [1,2,0]:
                    break
                else:
                    print("That's not a valid input!") 
            except:
                print("That's not even a number!")      
        if choice==1:
            money()
        elif choice==2:
            hottea()
        elif choice==0:
            break

def timestable():
    while True:
        try:  
            choice=int(input("What times table do you want? "))
            print()
            if choice in range(1,20):
                break
            else:
                print("That's not a valid input!") 
        except:
            print("That's not even a number!")
        
    topline="| x |"
    for count in range(0,choice):
        num=str(count+1)
        if len(num)==1:
            box=" "
            box+=num
            box+=" |"
        elif len(num)==2:
            box=" "
            box+=num
            box+="|"
        elif len(num)==3:
            box=""
            box+=num
            box+="|"
        topline+=box
    print("-"*(len(topline)))
    print(topline)
    print("-"*(len(topline)))
    for count in range(0,choice):
            #first line
            line="|"
            if len(str(count+1))==1:
                box=" "
                box+=str(count+1)
                box+=" |"
            elif len(str(count+1))==2:
                box=" "
                box+=str(count+1)
                box+="|"
            elif len(str(count+1))==3:
                box=""
                box+=str(count+1)
                box+="|"
                
            line+=str(box)
            for count2 in range(0,choice):
                num=str((count+1)*(count2+1))
                if len(num)==1:
                    box=" "
                    box+=num
                    box+=" |"
                elif len(num)==2:
                    box=" "
                    box+=num
                    box+="|"
                elif len(num)==3:
                    box=""
                    box+=num
                    box+="|"
                line+=box
            
            print(line)
            print("-"*(len(topline)))
def table():
    while True:
        try:  
            choice=int(input("What times table do you want? "))
            print()
            choice2=int(input("What would you like to know up to? "))
            if choice in range(0,20) and choice2>0:
                break
            else:
                print("That's not a valid input!") 
        except:
            print("That's not even a number!")

    for count in range(0,choice2):
        print("{0} * {1} = {2}".format(count+1,choice,(count+1)*choice))
    
def q4():
    while True:   
        print()
        print("------Question 4------")
        print()
        print("1. Full Times Table")
        print("2. Times Table")
        print("0. Quit")
        while True:
            try:  
                choice=int(input("What would you like to do? "))
                print()
                if choice in [1,2,0]:
                    break
                else:
                    print("That's not a valid input!") 
            except:
                print("That's not even a number!")      
        if choice==1:
            timestable()
        elif choice==2:
            table()
        elif choice==0:
            break

def main():
    print("2. Question 2")
    print("3. Question 3")
    print("4. Question 4")
    choice=int(input())
    if choice==2:
        q2()
    elif choice==3:
        q3()  
    elif choice==4:
        q4()
   
if __name__=="__main__":
        main()
    

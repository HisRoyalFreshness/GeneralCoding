import time
import random
def vinput():
    return input()
def function(inv):
    print("You're driving in your car when suddenly")
    for count in range(0,3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("OPTIMUS PRIME RIDING A WHALE EMERGES FROM THE EARTH")
    time.sleep(1)
    print("You have little time to react, you must get these Pi's to the")
    time.sleep(1)
    print("electronically starved students, but you have no time, you must fight!")
    time.sleep(1)
    print("You realise you have 3 options (pattern here ain't there wink emoticon)")
    print()
    time.sleep(2)
    
    print("You can A:")
    print("Run down the street like a little girl screaming, throwing babies at")
    print("the monster trying to get rid of it")
    print()
    
    time.sleep(2)
    print("You can B:")
    print("Using your mega rasberry pi abilites you can create a giant mecha robot")
    print("of doom and do battle with Optimus Whale Lord which will look super cool")
    print()
    
    time.sleep(2)
    print("You can C:")
    print("Scowl angrily at your new robot/whale overlord and attempt to drive past")
    print()
    
    time.sleep(3)
    print("What are you going to do? ")
    inp=vinput()

    if inp=="a":
        print("As you flee down the street like a little schoolgirl late for class Optimus Whale")
        time.sleep(1)
        print("turns round and let's out a mighty whimper, you feel his fishy, mechanical breath")
        time.sleep(1)
        print("hot on your ankles, what do you do?")
        
        time.sleep(2)
        print("You can A:")
        print("keep running down the street and hide in the disabled orphan kids hospital")
        print("and hope it accepts your offering of sacrifice")
        print()
        
        time.sleep(2)
        print("You can B:")
        print("grow a backbone and turn and kick the giant mechamammel in its titanium balls")
        print()
        
        time.sleep(2)
        print("You can C:")
        print("Give up and give in to the sweet relief only death can bring")
        print()
        
        inp2=vinput()

        if inp =="a":
            print("you are the worst kind of person, however the giant fish robot thing accepts")
            time.sleep(2)
            print("your offering of helpless children, you wipe the sweat off your brow and continue")
            time.sleep(2)
            print("on your way to university, with a guilt free mind, you horrible person")
            timetaken=5
                
        elif inp=="b":
            print("you turn round to face the beast, you are immediately stood on and")
            time.sleep(2)
            print("smeared along the pavement, thankfully, the robophibian thing has ")
            time.sleep(2)
            print("the ability to bring you back to life for some reason and then it just ")
            time.sleep(2)
            print("leaves and walks off for some reason, its best if you dont think about it")
            time.sleep(2)
            print("it takes ten minutes for you to come back to life because it does ok")
            timetaken=10
            
        elif inp=="c":
            print("You give in to CyborgWhaleManThing but as you wait for your fate to arrive")
            time.sleep(2)
            print("Jackie Chan turns up and kicks you so hard you fly into the sky Team Rocket")
            time.sleep(2)
            print("You land it what appears to be an identical alternate universe where everything")
            time.sleep(2)
            print("is identical except for the giant whale robot thing thats fading from your memory")
            time.sleep(2)
            print("you shake your head and you have no recollection of the last event, so you just keep")
            time.sleep(2)
            print("walking in a really convinient way, wondering where the last 7 minutes went...")
            timetaken=7
        else:
            print("You've broken the universe good job")
            timetaken=0
            
    elif inp=="b":
        print("You engage in a mighty battle with the RoboWhale and it looks super sweet,")
        time.sleep(2)
        print("like, imagine a michael bay film mixed with avatar and some other cool visual shit")
        time.sleep(2)
        print("it looks super sweet, I've never seen anything so cool in my life, i'm just going ")
        time.sleep(2)
        print("to stop talking so I can watch this amazing, epic, once in a lifetime moment")
        time.sleep(3)
        print("Oooo")
        time.sleep(5)
        print("AhhhH")
        time.sleep(2)
        print("Woaahhh")
        time.sleep(9)
        print("Wow didn't that look amazing, that was a great fight, I guess you can continue on with")
        time.sleep(2)
        print("your day, authough you might be around 14 minutes late now..")
        timetaken=14
        
    elif inp=="c":
        print("surprisingly you drive past really easy and continue, you don't lose any time")
        time.sleep(2)
        print("That took like no time, but that was really boring that could of been something epic...")
        timetaken=0
    else:
        print("You've broke the game good job")
        timetaken=0
    
    return timetaken

function(1)

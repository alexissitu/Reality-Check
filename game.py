import time
import random

#class Game(object):
#	def __init__(self, newName):
#		self.name = newName
#		print(self.name)
		
#myGame = Game(newName='hello')

#STARTING SCREEN------------------------------------*
print("Welcome to your \"REALITY CHECK\"!")
print("A simulation of a virtual life")
print()
time.sleep(1)

#VARIABLES--------------------------------------------*
answer =""

#FUNCTIONS--------------------------------------------*
def testYesOrNo(answer):
	answer = answer.upper()
	while answer != "YES" and answer != "NO":
		print("whoops! try entering yes or no")
		answer = input()
		answer = answer.upper()
	return answer

		

	
#MENU-----------------------------------------------*
chosenOption = "ya"
print("--WELCOME TO THE MENU--")

while chosenOption != "1":
	print("Please pick one")
	print("1: Start Game")
	print("2: Commands")
	print("3: About game")

	chosenOption = input()

	while chosenOption !="1" and chosenOption !="2" and chosenOption != "3":
		print("whoops! please try again. Enter one of the option numbers")
		chosenOption = input()

	if chosenOption != "1":
		if chosenOption == "2":
			print("Use the keywords \"yes\" and \"no\" or option varaiables (ex: A, B, C, 1, 2, 3...etc) to progress through the game")
			print("only use custom responses when implied (ex: please type character name")
		
	

		if chosenOption == "3":
			print("(PROTOTYPE/ROUGH OUTLINE OF GAME--NOT FINAL PRODUCT!!) Reality check  is about a character you customize who goes through the stages of life. You can choose the beginning difficulty through your living situation. There will be 5 levels: childhood, young adult, your prime, mid-life crisis and road to afterlife. There will be multiple different endings all depending on the choices you make. Your choices range from what your relationships you make to general life choices, so choose wisely! You will choose life objectives at the beginning of the game in order to complete throughout the game. If you complete your life goals, you win at life! :) However, be careful! Like real life, \"Reality Check\" contains random curveballs at any point in the game, so be prepared. How will you live your life? What does happiness mean to you? And remember, where you begin may not be where you end.")
			print()
			print("Also, the random dempgraphics and levels are apart of the game! It is not a bug. In life, we don't get to choose where we are born and who we are born as. This game wanted to capture this idea and show you (the player) an important life lesson about differences in human beings.")
			print()
			print ("**Disclaimer: the game will include mild violence, harsh languages, mental health topics (depression, etc.), angst, unpredictability, intense themes surrounding life, death, happiness and success. Overall a very intense game questioning beliefs, faith, destiny, and the existential dread surrounding your choices in life.**")
			print()
			print("would you like to hear about the developers?")
			answer = input()
			if answer == "yes":
				testYesOrNo(answer)
				print()
				print()
				print("Reality check was developed by 4 girls from the Girls Who Code Foster City Branch.")
				print()
				print("-----------")
				print("MEET:")
				print()
				print("ALEXIS: Alexis is a sophomore at Mills High School. She has attended several computer science internships over her freshman year summer and is a part of the non profit organization Girls Who Code. She is not only driven and inspired by computer science but also psychology. She believes life is about experiencing new things and stepping out of your comfort zone. She wanted to help develop this game for teens to realize that it does not matter where you start in life but where you end up.")
				print()
				print("KRISTEN: ")
				print()
				print("MANDY: ")
				print()
				print("TAYLOR: Taylor is a senior at Mills High School and joined Girls Who Code for the years 2017 to 2018. She aspires to one day make more video games with companies like Nintendo! Taylor enjoys animations, drawing, various TV shows and, of course, computer science. She was inspired by the fact that many feel inadequet with the choices in their lives. She wants to help show peope that things are sometimes just meant to be and you cannot control life all the time, so just live it to the fullest.")

		print()
		print("would you like to return to menu?")
		chosenOption = input()
		testYesOrNo(chosenOption)
		while chosenOption == "no":
			print("okay, you're just stuck on this page then...")
			time.sleep(1)
			print("...")
			time.sleep(1)
			print("...")
			time.sleep(1)
			print("...")
			time.sleep(1)
			print("...would you like to return to the menu now?")
			chosenOption = input()
			print()
			



#GAME STARTS ---------------------------------------*
#CHARACTER NAME***
print("Please type your character's name")
name = input()
name = name.upper()
print()
print("Would you like to name your character " + name + "?")
answer = input()
answer = testYesOrNo(answer)

while answer == "no":
	print()
	print("Please input character name")
	name = input()
	name = name.upper()
	print()
	print("Would you like to name your character " + name + "?")
	answer = input()
	answer = testYesOrNo(answer)

print()
print("Perfect! Welcome " + name + "!")
print("Time to pick your demographics")
time.sleep(1)
print()
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait")
time.sleep(2)
print()

#DEMOGRAPHICS***
def sexPicker():
	sexes = ["boy", "girl"]
	return random.choice(sexes)
sex = sexPicker().upper()

def racePicker():
	races = ["Caucasian", "African", "Asian", "Spanish", "Pacific Islander"]
	return random.choice(races)
race = racePicker().upper()
print ("You were born as a(n) " + race + " " + sex)
print()

def levelPicker():
	levels = ["easy", "normal", "hard"]
	return random.choice(levels)
level = levelPicker().upper()
print("By society's standards, your life will start off on " + level + " mode")
richness = ""
if level == "EASY":
	richness = "RICH"

if level == "NORMAL":
	richness = "MIDDLE CLASS"
	
if level == "HARD":
	richness = "POOR"
	

print()
time.sleep(2)

#PLAYER PROFILE***
print("PLAYER PROFILE:")
print("Name: " + name)
print("Gender: " + sex)
print("Ethnicity: " + race)
print("Economic background: " + richness)
print()
time.sleep(1)
print("Ready? Let's begin!")

#CHAPTER 1: CHILDHOOD ------------------------------*
time.sleep(1)
print()
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait")
time.sleep(2)
print("Processing... Please wait")
time.sleep(2)
print()

print(name)
time.sleep(1)
print("7 YEARS OLD.")
time.sleep(1)
print("Welcome to your childhood!")
time.sleep(2)
print()
print("Today is your first day of 2nd grade :)")
time.sleep(5)
print("When you walk into a class, what do you do?")
time.sleep(2)
A = "smile brightly and walk up to all the kids in class and introduce yourself"
B = "reluctant to let go of your mom's hand and hide your face behind her"
C = "calmly walk into class and sit down"
print("A: " + A)
time.sleep(1)
print("B: " + B)
time.sleep(1)
print("C: " + C)
action = input().upper()
nature = ""
if action == "A":
	print("You gleefully greet all the children and make many new friends!")
	nature = "outgoing"
if action == "B":
	print("you shield your eyes as you walk into the class and don't make eye contact with anyone")
	nature = "timid"
if action == "C":
	print("you sit there patiently, ready to learn :)")
	nature = "calm"
time.sleep(2)
print()
print("Your teacher walks in and begins the lesson")
time.sleep(2)
print("...")
time.sleep(1)
print("...")
print("a couple of hours pass and it's time for a break~")
print ()
time.sleep(1)
print("Who will you play with at recess?")
A = "Only your best friend"
B = "A whole group of friends"
C = "Watch the other kids play"
time.sleep(1)
print("A: " + A)
time.sleep(1)
print("B: " + B)
time.sleep(1)
print("C: " + C)
action = input().upper()
if action == "A":
  print ("You and your best friend play on the swings everyday. You're usually the one pushing them.")
if action == "B":
  print ("You all play \"house\" or \"family\" together")
if action == "C":
  print("you stare at the other kids as you sit on the swing alone")
print()
print()
time.sleep(2)
print ("~~fast forward some years~~")
time.sleep(2)
#CHAPTER 2:
print(name)
print("14 YEARS OLD.")
time.sleep(1)
print("Welcome to freshman year at Mc High School!")
#friends
print("Choose your group of friends: popular, quiet, artistic, athletic, or smart")
Group = input()
print ("You will be friends with the " + Group + " kids")
print ("Are you okay with this group of friends? ")
answer = input().upper()

while answer == "NO":
	print("Please choose your group of friends : popular, quiet, artistic, athletic")
	Group = input()
	print()
	print("Are you okay with this group of friends?")
	answer = input()
if answer == "YES":
  print ("Now onto your next important part of freshman year!")
print()
time.sleep(1)
print ("You see a cute person that is in 3 of your classes")
print ()
time.sleep(1)
print ("Will you...")
print ()
time.sleep(1)
A = "develop a crush and talk to them"
B = "ignore them"
C = "friendzone them"
print("A: " + A)
time.sleep(1)
print("B: " + B)
time.sleep(1)
print("C: " + C)
action = input().upper()
if action == "A":
  print ("Your crush officially thinks you are a creep")
if action == "B":
  print ("You turn out to be great friends with this person")
if action == "C":
  print("This person is deeply obsessed with you and is now your stalker")
print ()
def schoolratingResult():
	schoolratings = ["amazing", "alright", "terrible", "horrific", "life changing"]
	schoolrating = schoolratings[random.randint(0, 4)]
	return schoolrating
time.sleep(1)
print ( "Your freshman year was... let's say " + schoolratingResult() )
#sophomore year
time.sleep(1)
print("Time has passed by and it is sophomore year already!")
print ()
time.sleep(1)
print ("It is time to build up our high school experience to build our college applications")
time.sleep(1)
print ()
print ("The first thing is, which club are you going to join?")
time.sleep(1)
A = "Leadership"
B = "Community Service"
C = "Debate"
D = "Mock trial"
E = "Art and Crafts"
F = "Culinary Arts"
print("A:" + A)
print("B:" + B)
print("C:" + C)
print("D:" + D)
print("E:" + E)
print("F:" + F)
action = input().upper()
if action == "A":
  print("You are growing as a leader and now a part of the ASB")
if action == "B":
  print("You are loaded with community hours enough for 10 people! You are an environmentalist")
if action == "C":
  print("You are in honors English class, you like to stand up for what you believe in.")
if action == "D":
  print("You are a future lawyer and have a way to twist everyone's words to benefit you")
if action == "E":
  print("You are an aspiring artist who specializes in drawing stick figures")
if action == "F":
  print("You can cook better than Gordon Ramsey!! Why are you in high school?!")
print()
time.sleep(1)
print("Anyways, moving on....")
time.sleep(1)
print("Are you going to participate in any sports this year?")
answer = input().lower()
while answer == "no":
	print("It is okay. Not everyone is an athlete. You are a musician")
	answer = input()
def sportResult():
	sports = ["Volleyball", "Tennis", "Swimming", "Basketball", "Soccer"]
	sport = sports[random.randint(0, 4)]
	return sport
if answer == "yes":
	print("The sport you will be joining is " + sportResult())
	print("You will be a team player throughout the rest of high school and so forth")
time.sleep(3)
print("Months go by as slow as a turtle... 2 more years of high school left!!")
print()
time.sleep(4)
print("The worst year of your life has come. The dreadful junior year. You must step it up for the sake of college.")
print()
time.sleep(3)
print("What classes are you planning to take this year?")
A = "AP courses"
B = "regular same old classes"
print ("A:" + A)
print ("B:" + B)
print ()
answer = input().upper()
if answer == "A":
  print ("why do you do that to yourself? oh well,rest in peace.")
  time.sleep(5)
if answer == "B":
  print ("best of luck to you. you won't die like those taking AP courses")
  time.sleep(5)
print ("days are slowly passing by.... ")
time.sleep(3)
print ("work load is piling quickly...")
time.sleep(3)
print ("will you ever survive junior year?")
answer = input().lower()
if answer == "no":
  print("Of course you will! Don't worry.")
print()
if answer == "yes":
  print("you are probably wrong and you will be the last to survive")
print()
time.sleep(2)
print("loading life...")
time.sleep(2)
print("loading life...")
time.sleep(2)
print("loading life...")
time.sleep(2)
print ("It is finally time to graduate out of this prison.")
time.sleep(1)
print ("WHERE ARE YOU PLANNING TO GO TO COLLEGE?!")
time.sleep(1)
A = "UC"
B = "Private university"
C = "CSU"
D = "Community College"
E = "I have to go to college ??"
print ("A:" + A)
print ("B:" + B)
print ("C:"  + C)
print ("D:" + D)
print ("E:" + E)
action = input().upper()
print ()
if action == "A":
  print( "you can have fun living the rest of your life in student debt. ")
if action == "B":
  print("are you super rich or did you recently win the lottery??")
if action == "C":
  print("you have a bright future ahead of you")
if action == "D":
  print("you are saving a lot of money... smart")
if action == "E":
  print("bro?? are you on drugs? just kidding, you control your own life. Don't let anyone pressure you.")
print()
print ("Well... the time for high school has reached an end.")
time.sleep(5)
print("Up next is.... College!! or whatever you are planning to do in your 20's")



#COLLEGE
time.sleep(1)
print(name)
time.sleep(1)
print("18 YEARS OLD.")
time.sleep(1)
print("I see that you have changed your mind about which college you want to go to...")
time.sleep(1)
collegeList = ["Yale", "Stanford", "Community College"]
college = random.choice(collegeList)
print("Well congrats! You graduated high school and are now attending " + college + "!")
print("What major do you want to pursue?")
major = input()

#make list of extraCurriculars
print("Now what clubs/sororities do you want to join?")
club = input()
print("How many classes are you taking?")
numClasses = int(input())
print("How many of those classes are you actually attending?")
numActualClasses = int(input())
print("With classes come tests...so how many hours do you study for those tests?")
studyHours = int(input())
print("How many all-nighters do you pull?")
allNighters = int(input())
print("Do you go to parties?")
parties = input()
print("Do you apply for internships/workstudy?")
internships = input()
print("Do you spend more time in the 1)library or passed out in someone’s 2)lawn?")
location = input()
print("These choices make up your four years of college")
print("Are your choices correct? I shall refrain from judgement...")
print("However these choices do determine your success in college and based on these choices you...")

#Do you graduate?
graduate = True

if("History" in major):
  print("You graduated with honors! Good luck on Your fuure career...")
  graduate = True
elif(studyHours > 5):
  print("You graduated with a 4.0 GPA!")
  graduate = True
elif(location == "lawn"):
  print("You're a college dropout.")
  graduate = False
  
print()
time.sleep(2)
print("time passes...")


#MID LIFE CRISIS ----------------------------------*  
time.sleep(5)
print(name)
time.sleep(1)
print("50 YEARS OLD.")
time.sleep(1)
print("It's time for a midlife crisis.")
time.sleep(1.5)
print("You were fired from your job recently. You are absolutely devasted. To add salt to the wound, you recently got scammed and lost 10,000 dollars.")
time.sleep(2.3)
print("You and your spouse are growing more emotionally distant by the day...")


# Choose your path of downward spiral
print("Do you choose 1) crippling depression, or 2) alcohol addiction?")
badChoice = input()

# choosing crippling depression
if badChoice == 1:
  print("Everyday, you feel tired and uninterested with things with what you once thought were your main hobbies.")
  time.sleep(2)
  print("Well, at least you have your spouse.")
  time.sleep(1)
  print("Do you want to talk to your spouse? 1) yes or 2) no?")
  talkChoice = input()
  while badChoice != 1 and badChoice != 2:
    print("Do you want to talk to your spouse? 1) yes or 2) no?")
    talkChoice = input()
  
  # Talk to spouse
  print(" ")
  if talkChoice == 1:
    print("You tried talking to your spouse about your worsening depression.")
    time.sleep(2)
    print("But right when you reach to the topic, your spouse tells you to suck it up.")
    time.sleep(2)
    print("Eventually, you both descend into constantly heated arguments, from once a week to almost every hour")
    time.sleep(2)
    print("with subjects varying from past mistakes to just plain insulting each other.")
  
  # refuse to talk to spouse
  
  elif talkChoice  == 2:
    print("You decided against talking to your spouse about your progressive depression.")
    time.sleep(1)
    print("For a while, you tried to hide your depression, but as the recession worsens and your money starts drifting away, you can't keep it inside anymore.")
    
# choosing alcoholism    
elif badChoice == 2:
  print("You go to a nearby liquor store.")
  time.sleep(2)
  print("You purchase a crap ton of alcohol. A crap ton.")
  time.sleep(2)
  print("You drink all day and all night. Your spouse is tired of your excessive drinking and tells you to go see a therapist.")
  time.sleep(2)
  print("You slam your wine bottle at a nearby table and refuse.")
  time.sleep(3)
  print("This continues for about 2 months, with patience from both sides wearing thin.")

time.sleep(4)

print(" ")
print("The time has come for divorce.")
time.sleep(2)
print("Your spouse starts filing the papers.")
time.sleep(2)


print("You try to convince them that it's not worth it to fill out those divorce papers,")
time.sleep(2)
print("that there is still hope.")

print("Do you save your marriage? 1 for yes, 2 for no")
marital = int(input())
while marital != 1 and marital != 2:
  print("Do you save your marriage? 1 for yes, 2 for no")
  marital = int(input())

time.sleep(3)
if marital == 1:
  print("As luck would have it, you manage to work out communication and save your spouse from completing the papers.")
  time.sleep(2)
  print("It took a while, but you did it.")
  print("...")
  time.sleep(3)
  print("...sike.")
  time.sleep(2)
  print("You return to your vicious cycle of verbal assault.")
  time.sleep(2)
  print("And in this case, the universe...")
  dealWith = random.randint(1, 2)
  if dealWith == 1:
    time.sleep(2)
    print("...decided that you eventually regain your sanity back from the waking abuse.")
    time.sleep(2)
    print("You and your spouse eventually came to terms with the fact that your union was not a good one.")
    time.sleep(1)
    print("")
  elif dealWith == 2:
    time.sleep(2)
    print("...decided that you stay together longer.")
    time.sleep(2)
    print("It actually too bad, but you both eventually drift far apart.")		
    print("Emotionally and physically.")
    
print("To be continued...")
time.sleep(1)
print("Thank you for playing this rough outline! A cleaner version will be out one day :)")
	

"""
MadLibs
Author: Hope Baer
Period/Core: 3


"""
import time
from termcolor import colored 

#Begins game!
print(colored("Let's " + "play" + " Silly Sentences!", 'red'))
time.sleep(2)
print (colored("There are a few rules.", 'yellow'))
time.sleep(1)
print(colored("...", 'green'))
time.sleep(1)
print(colored("*All verbs MUST be past tense, unless ending in -ing, -ed, etc.*", 'cyan'))
print(colored("*Only appropriate body parts can be chosen.*",'blue'))
time.sleep(1)
print(colored("*And lastly, enjoy the game!*",'magenta'))
time.sleep(1)
print(colored("...", 'red'))
time.sleep(2)

#variables for user input
person = input("Enter a friend's name:")
adjectiveone = input("Enter an adjective:")
place = input("Enter a store/restaurant name:")
verbone = input("Enter a verb:")
nounone = input("Enter a noun:")
verbtwo = input("Enter a verb ending in -ing:")
bpartone = input("Enter a body part:")
adjectivetwo = input("Enter an adjective ending in -ly:")
objectone = input("Enter an object:")
bparttwo =input("Enter a body part:")
verbthree = input("Enter a verb:")
nountwo = input("Enter a noun:")
family  = input("Enter a person (father, mother, grandparent, etc.):")
caps = input("Enter a word in ALL CAPS:")
verbfour = input("Enter a verb:")
facebody = input("Enter a body part of the face:")
bpartthree = input("Enter a body part:")
verbfive = input("Enter a verb:")
adjectivethree = input("Enter an adjective:")
emotionone = input("Enter an emotion:")
adjectivefour = input("Enter an adjective:")
nounthree = input("Enter a noun:")
objecttwo = input("Enter an object:")
objectthree = input("Enter an object:")
expressionone = input("Enter an expression ending in -ed:")
adjectivefour = input("Enter an adjective:")
verbsix = input("Enter a verb ending with -ed:\n")

print("Great!" + " Now let's move on.")
print("Generating...\n")
time.sleep(3)


#generated story
print(f"Today I went to the mall. At the mall, I saw {person}.")
print(f"{person} and we gave each other a {adjectiveone} high-five and walked over to {place}.\n At {place}, {person} almost immediately {verbone} over to the {nounone}. “Wait!” I said, {verbtwo} over to {person}. I grabbed their {bpartone} and pulled them over to the door. “What are you doing?” I said {adjectivetwo}.\n  “  I was looking for a/an {objectone} and I found it,” {person} said, pointing their {bparttwo} to the {objectone}. “O.K. Go get it, then!” I let go of their {bpartone} and they {verbthree} to the {nountwo}. I watched them as they barreled into the {nounone} as they tripped and knocked over a {family}. “{caps}!!!!” The {family} yelled, and whacked Dave with the {objectone}. They had gotten up and left as I {verbfour} to help {person} up. “Oops,” {person} replied, rubbing their {facebody}. I reached out to {person} with my {bpartthree} and they got up.\n  “What is all this?!” The store manager said, who {verbfive} over to us. She pointed her {adjectivethree} finger at me and {person}. “Clean it up! And get out!” She yelled, disturbing all of the customers around us. I felt {emotionone}. {person} looked at me and opened their mouth to speak, but paused as the lady walked {adjectivefour} to us. She picked up the {objectone} that {person} wanted! “Hurry it up! And pay for everything you broke!” She swatted her hands around to queue us to begin cleaning the messy floor. I grabbed a {nounthree} and swept with it. {person} picked up a {objecttwo} and a {objectthree} and started scrubbing the floors. After we finished cleaning, we handed over our leftover money we were going to use to buy the {objectone} with. She {expressionone} and pointed her {adjectivefour} finger to the door. I {verbsix} {person} on the back. “We’ll get it Amazon I guess.” I told them. We headed back into the mall and didn’t enter {place} again.")

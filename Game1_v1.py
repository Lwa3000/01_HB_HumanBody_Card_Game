#Game1 Summary
#Game title: HumanBody Card Game

#Dictionary that stores all the facts
card_list=[
	{ 'card_no':'1',
	  'question':['question 1','question 2','question 3'],
	  'answer':['answer 1','answer 2','answer 3'],
	  'explanation':['explanation1','explanation2','explanation3'],
	  'category': 'category1',
	  'facts':['Fact 1', 'Fact 2', 'Fact 3'],
	  'viewed':[False, False, False],
	  'answered_correctly':False
	},
	{ 'card_no':'2',
	  'question':['question 1','question 2','question 3'],
	  'answer':['answer 1','answer 2','answer 3'],
	  'explanation':['explanation1','explanation2','explanation3'],
	  'category': 'category1',
	  'facts':['Fact 1', 'Fact 2', 'Fact 3'],
	  'viewed':[False, False, False],
	  'answered_correctly':False
	},
	{ 'card_no':'3',
	  'question':['question 1','question 2','question 3'],
	  'answer':['answer 1','answer 2','answer 3'],
	  'explanation':['explanation1','explanation2','explanation3'],
	  'category': 'category1',
	  'facts':['Fact 1', 'Fact 2', 'Fact 3'],
	  'viewed':[False, False, False],
	  'answered_correctly':False
	},
	{ 'card_no':'4',
	  'question':['question 1','question 2','question 3'],
	  'answer':['answer 1','answer 2','answer 3'],
	  'explanation':['explanation1','explanation2','explanation3'],
	  'category': 'category1',
	  'facts':['Fact 1', 'Fact 2', 'Fact 3'],
	  'viewed':[False, False, False],
	  'answered_correctly':False
	},
]

#Functions used to run the game

def display_card(card_list):
	#Randomly selects a card to display and to browse through. 
	#This is only if the card has not been answered_correctly.
	#Input: Takes the encyclopedia of a list of cards.
	#Output: True if the whole card is browsed through. 
	#		 False if the card is not browsed through.

	Round=[1,2,3,4]
	for item in Round:
		print "Card: "+item+"/4"
		print "What do you want to find out?"

		card=card_list.pop()
		while card1[answered_correctly]==True:
			card=card_list.pop()

		display_questions_on_card(card)

		selection=int(raw_input("Please select an option"))
		if selection==4:
			break
		elif selection in [1,2,3]:
			while False in card[viewed]:
				display_questions_on_card(card)
				card[viewed][selection]=True
			run_quiz(card)
		else:
			print "Please enter one of the options."
		
def display_questions_on_card(card):
		print "1. "+ card["question"][0]
		print "2. "+ card["question"][1]
		print "3. "+ card["question"][2]
		print "4. Nothing Today."

def run_quiz(card):
	#Runs the quiz on the card if the card is browsed through
	#Input: the card of facts
	#Output: True if the user answered_correctly. False otherwise.
	pass

def count_remaining_cards(card_list):
	#Counts the number remaining cards that is not answered correctly.
	#Input: takes a list of cards
	#Output: the count as an integer.
	pass


#Main Function to play the game 
def main():
	#step1: Display 1 out of 4 card of facts for the user to browse through.
	#step2: Once the user has browsed through all of the facts, run the quiz on the card.
	#step3: Once all of the cards have been answered, display the number of cards won.
	#step4: Check to see if there are anymore cards in the list. If there is, ask to play again.
	pass

main()
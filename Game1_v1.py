#Game1 Summary
#Game title: HumanBody Card Game

from random import choice

#Dictionary that stores all the facts
card_list=[
    { 'card_no':'1',
      'question':['What is the most powerful muscles you have?',
                  'Where is smallest bone in your body?',
                  'Most animals have a ackbone are called vertebrates. What are animals with no spine called?'],
      'answer':['Your legs','ears','invertebrates'],
      'explanation':['The most powerful muscles are in your legs.',
                     'The smallest bone in your body is lies deep inside your ear. It is around the same length as a grain of rice.',
                     'Animals with no spine are called invertebrates, like spiders and bugs.'],
      'category': 'category1',
      'facts':['Fact 1', 'Fact 2', 'Fact 3'],
      'viewed':[False, False, False],
      'answered_correctly':False
    },
    { 'card_no':'2',
      'question':['question 1 on card2','question 2 on card2','question 3 on card2'],
      'answer':['answer 1','answer 2','answer 3'],
      'explanation':['explanation1','explanation2','explanation3'],
      'category': 'category1',
      'facts':['Fact 1', 'Fact 2', 'Fact 3'],
      'viewed':[False, False, False],
      'answered_correctly':False
    },
    { 'card_no':'3',
      'question':['question 1 on card3','question 2 on card3','question 3 on card3'],
      'answer':['answer 1','answer 2','answer 3'],
      'explanation':['explanation1','explanation2','explanation3'],
      'category': 'category1',
      'facts':['Fact 1', 'Fact 2', 'Fact 3'],
      'viewed':[False, False, False],
      'answered_correctly':False
    },
    { 'card_no':'4',
      'question':['question 1 on card4','question 2 on card4','question 3 on card4'],
      'answer':['answer 1','answer 2','answer 3'],
      'explanation':['explanation1','explanation2','explanation3'],
      'category': 'category1',
      'facts':['Fact 1', 'Fact 2', 'Fact 3'],
      'viewed':[False, False, False],
      'answered_correctly':False
    },
]
count_num_of_cards_correct=0

#Functions used to run the game

def display_card(card_list):
#Randomly selects a card to display and to browse through.
#This is only if the card has not been answered_correctly.
#Input: Takes the encyclopedia of a list of cards.
#Return: True if the whole card is browsed through.
#        False if the card is not browsed through.
    global count_num_of_cards_correct
    Round=[1,2,3,4]
    for item in Round:
        card=card_list.pop()
        # while card["answered_correctly"]==True:
        #     card=card_list.pop()

        selection=display_questions_on_card(card, item)
        card["viewed"][selection-1]=True
        if selection==4:
            break
        elif selection in [1,2,3]:
            while False in card["viewed"]:
                selection=display_questions_on_card(card, item)
                card["viewed"][selection-1]=True
                print card["viewed"]
            count_num_of_cards_correct += 1
            run_quiz(card, item)
        else:
            print "Please enter one of the options."

def display_questions_on_card(card, item):
    print "---------"
    print "Card: "+str(item)+"/4"
    print "What do you want to find out?"
    print "1. "+ card["question"][0]
    print "2. "+ card["question"][1]
    print "3. "+ card["question"][2]
    print "4. Nothing Today."
    print "---------"
    selection=int(raw_input("Please select an option: "))
    print "Question: " + str(selection)
    print "  " + card["question"][selection-1]
    print "  " + card["answer"][selection-1]
    print "  " + card["explanation"][selection-1]
    raw_input("Press Enter if done viewing>>")
    print "---------"
    return selection


def run_quiz(card, item):
#Runs the quiz on the card if the card is browsed through
#Input: the card of facts
#Return: True if the user answered_correctly. False otherwise.
    print "---------"
    print "Quiz Time for card:"+str(item)+"/4"
    quiz_question_index=choice([0,1,2])
    print "  Question:" + card["question"][quiz_question_index]
    print "  "
    user_answer="wrong answer"
    while user_answer not in card["answer"][quiz_question_index]:
        user_answer=raw_input("Please enter the answer, or q to quit the game: ")
        if user_answer.lower() in card["answer"][quiz_question_index].lower():
            print card["explanation"][quiz_question_index]
            print "You have answered this question correctly! You got "+ str(count_num_of_cards_correct) +" jewel(s) out of 4!"
            display_jewels(count_num_of_cards_correct)
            card["answered_correctly"] = True
            return True
        elif user_answer == 'q':
            return False
        else:
            print "Please try again."

def count_remaining_cards(card_list):
#Counts the number remaining cards that is not answered correctly.
#Input: takes a list of cards
#Return: the count as an integer.
    pass

def display_rules():
#Displays the rules of the game.
#Input: None
#Return: None
    print '''
        The Human Body Game!
        How to play: You have 4 cards to play with. Each card will have three facts to browse through.
                     After you have browsed through all the cards. You will be asked to answer one random
                     question. You will get 1 jewel for each card you answer correctly.

    '''

def display_jewels(num_of_jewels):
#Displays number of jewels
    count = 0
    while num_of_jewels != count:
        display_one_jewel()
        count +=1

def display_one_jewel():
    print '''
      .     '     ,
        _________
     _ /_|_____|_\ _
       '. \   / .'
         '.\ /.'
           '.'
    '''

#Main Function to play the game
def main():
#step1: Display 1 out of 4 card of facts for the user to browse through.
#step2: Once the user has browsed through all of the facts, run the quiz on the card.
#step3: Once all of the cards have been answered, display the number of cards won.
#step4: Check to see if there are anymore cards in the list. If there is, ask to play again.
    display_rules()
    display_card(card_list)

main()

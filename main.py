"""
Copywrite Adam Morris

A very simple half-written card game, written with beginner programmers in mind.
Your task is to get the computer to play with you.

The Game:
This card game simulates a game of "Spit" or "Speed".
The real game is not turn-taking, but this program is not (yet)

Definitions:
• Player and computer receives half the deck (26/52 cards)
• A hand begins play
• Players place five cards face-up, and one face-up in the pit
• Their "hand" has 15 cards (5 face-up and 10 face-down)
• Each iteration of play stops when neither the computer or player have a play
• New interation of play begins with "spitting" -- placing a card face-up in the pit
• Players can only play cards that are +1 or -1 difference from cards in the pit

Improvements:
This program does not simulate every aspect of the game, including, but not limited to:
• Being able to move cards in your pile in order to make room for another
• Wraparound: Placing an Ace on a King, or a King on an Ace does not currently work
• Fix bug that makes it fail when the human player runs out of cards!

"""

# First thing is to define our class structure. 
# ... In this case, we will use the "Deck" class defined outside of this file
# ... Python is an object-oriented language, and classes are often considered an advanced topic
# ... but all a beginner has to understand is that the next line basically 
# ... just like copying and pasting the code that someone else wrote into this file
# ... that way we can use their code
from pydealer import Deck

# Second, we make our own class that we will use and control exclusively
# ... this class keeps all our code organized
class App:
	"""
	This is the Application class. It holds all the code in one place for our game.
	There is only one App class, and it is created in the main function, defined below. 
	"""

	# Inside this App class, we need constants
 	# ... in python we can define constants that classes use here, with simple
 	# ... "constant = value" statement
 	# ... and then inside our functions we can use it by typing "self.constant"
	num_cards_to_deal_to_each = 26     # half the deck
	num_face_up = 5

	# Inside this App class, we need functions that take actions
	# ... the first one is the "constructor" action, which gets called automatically
	# ... when the class is created on program start-up
	def __init__(self):
		"""
		This function will be called first, when the application starts up, see the main function below
		"""

		# Let's init the deck of cards
		# ... so that we have two players (your_hand, computer_hand) 
		# ... the pydealer package that we have imported actually contains these functions
		# ... you can see the code in there, not in this file
		# ... but all we have to understand is that this code "makes" the deck of cards
		# ... shuffles them
		# ... and then deals them 
		self.deck = Deck()
		self.deck.shuffle()
		self.human_hand = self.deck.deal(self.num_cards_to_deal_to_each)
		self.computer_hand = self.deck.deal(self.num_cards_to_deal_to_each)
		# ...okay, so now we have the cards delt to the players

		# Now let's put cards in the pit, which is called "spitting" in this game
		# ... we we use the word "spit"
		# ... this function we CAN see the code for below
		# ... it is defined below where it says "def spit(self):"
		self.spit()

		# So now that we have initialized our setup, let's begin
		self.start()

	def start(self):
		"""
		Starts the action, and allows the computer to keep looping over and over until finished
		This is our main program loop
		"""

		# Here is where the game output starts at the beginning of the game
		# It just takes the first five from the human and computer, then calls the loop function
		self.yours = self.human_hand.deal(self.num_face_up)
		self.computer = self.computer_hand.deal(self.num_face_up)
		self.loop()

	def loop(self):
		"""
		Keep going until cannot play anymore, or the user types Cntrl-C 
		"""

		# Each time in the loop we will output the cards
		# It clears the screen each time and prints the computer hand, the pit, and then the human hand
		self.output_cards()

		# Now we have to ask the human to input their selection in the menu
		human_selection = self.ask_human()
		# ... got it, and it is guaranteed to be a valid selection

		# Let's check what the human selected
		if human_selection is None:
			# ... this means "no play", but there isn't anything to do in that case
			# ... so we just use the "pass" keyword that means "do nothing"
			pass

		else:
			# ... human made a valid selection and wasn't "no play"
			# ... so let's the card the human has selected
			which = self.yours.get(human_selection)[0]

			# ... now we have to look through each card in the pit
			# ... and see if there is a match
			# ... so set up a match variable to be False by default
			match = False

			# ... now loop through
			# ... the first time through it is a 0
			# ... and the second time through it is a 1 
			# ... i.e. the "first" and "second" card
			for pit_index in [0, 1]:

				# ...... why check match now?
				# ...... there is a good reason, but if you don't know try to figure it out
				if match is True:
					continue   # "continue" keyword makes the loop move to the next one, does not go to the below code

				# ...... set "pit_card" to the actual card, either he 0 or 1 one
				pit_card = self.pit[pit_index]

				# ...... now use our function "determine_value" to get the value of the card
				pit_item_value = self.determine_value(pit_card)
				which_item_value = self.determine_value(which)

				# ...... do some math that let's us know if this is a legal play
				if abs(pit_item_value - which_item_value) == 1:
					# .......... legal play, so now we put the card on top of that, and set match to True
					self.pit[pit_index] = which
					match = True

			# ... outside of the loop now
			# ... now we check if we found a match
			if match:
				# ....... match!, so we need to add a card to our hand
				self.yours.add( self.human_hand.deal(1) )
			else:
				# ....... no match!, so now we need to put the card back where we got it from
				self.yours.insert(which, human_selection)

		# Okay, done checking what the human did, it's the computer's turn
		# ... but we haven't implemented this properly yet
		# ... just the skeleten!

		# Calls "ask_computer" function, which you should write
		# ... we are looking for it to return None or an integer
		computer_selection = self.ask_computer()

		# Check to see if this is case where both sides say "no play"
		# ... which means we have to spit
		if computer_selection is None and human_selection is None:
			# ... both the human and computer reported no play
			self.spit()

		elif computer_selection:
			# ... computer says they can play, so play it!
			# ... at the moment, this does nothing!
			# ... but can you write something that works?
			pass 

		self.loop()

	# These functions are defined below implement various features of the program:

	def your_card_size(self):
		"""
		Returns how many cards you have as an integer
		"""
		return len(self.yours) + 1

	def spit(self):
		self.pit = [self.human_hand.get(0)[0], self.computer_hand.get(0)[0]]

	def output_cards(self):
		print("\033c")  # clears screen
		print()     # blank line
		print("    COMPUTER:")
		for computer_card in self.computer.cards:
			print('    ', end="")   # four spaces and no newline chr
			print(computer_card.name)
		print()
		print("    PIT:")
		for pit_item in self.pit:
			print("    ", end="")   # four spaces and no newline chr
			print(pit_item.name)
		print()
		print("    YOU")
		
		for card_index in range(1, self.your_card_size()):
			# This line uses the string.format method
			print('{}:  {}'.format(card_index, self.yours.cards[card_index-1].name))
		print()
		print('-'*20)   # prints out 20 hyphens
		print()

	def ask_human(self):
		"""
		Prompts the human to enter a number
		Validates that it is a number, by keep asking until we got a good value
		Must return the index of the card that the human wants played
		Or None if the human wants to say "no play"
		"""

		# The input function is a python built-in function that displays the string and waits for return
		selection = input('Play which card? (or "no" for "no play"): ')
		# ...okay, now selection variable equals what the user just entered on the keyboard

		# Check to see if the user entered "no" or "NO" or "nO" or "No"
		if selection.lower() == "no":
			# ... they did, so end early, return None as the documentation above says
			return None

		# Check that selection is a digit, and that this digit is within the range of cards that the human has
		while not selection.isdigit() or not (int(selection) in range(1, self.your_card_size())):
			# ... it isn't, so remind the human what we are expecting
			selection = input('Enter a number between {} and {}: '.format(1, self.your_card_size()))

		# Now we have to adjust selection variable so that it is an integer instead of a string
		# and also minus 1 because computers count things with 0 = "the first" but humans count 1 = "the first"
		selection = int(selection) - 1
		# ...okay, it's an integer now, and appropriately offset

		return selection

	def ask_computer(self):
		"""
		The function that lets the computer play
		It needs to return the index of the card that it wants to play
		Or return None if there is no play

		There are a few ways to tackle this little problem
		"""
		return None

	# This is an advanced method that uses a few concepts that is not described here
	@classmethod
	def determine_value(cls, card):
		"""
		Looks at the value of the card and determines the appropriate numerical value
		"""
		return int({'Jack':11, 'Queen':12, 'King':13, 'Ace': 1}.get(card.value, card.value))

def main():
	app = App()   # Python creates the object and automatically calls __init__

if __name__ == "__main__":
	# Whenever this game is run, it calls the main function
	main()
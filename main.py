import random
from time import sleep

def start():
	class Card:

		def sort_cards(self, mas): # bubble-sort

			for i in range(len(mas)):

				for j in range(len(mas) - i - 1):

					if mas[j] > mas[j + 1]:

						mas[j], mas[j + 1] = mas[j + 1], mas[j]


		def show_cards(self, mas): # print-cards

			global current_card, master_card

			self.sort_cards(mas)

			print("The current card is: ")

			sleep(1)

			print(' ---\n' +
					'|   |\n' +
					'| ' + current_card + ' |\n' +
					'|   |\n' +
					 ' ---\n')

			print("The master card is: ")

			sleep(1)

			print(' ---\n' +
					'|   |\n' +
					'| ' + master_card + ' |\n' +
					'|   |\n' +
					 ' ---\n')


			sleep(1)

			print('Your cards are:')

			sleep(1)

			for i in range(len(mas)):

				print(' ---\n' +
					'|   |\n' +
					'| ' + mas[i] + ' |\n' +
					'|   |\n' +
					 ' ---\n') # , end=" "

				sleep(1)


		def logic(self, mas): # game-logic

			global current_card, master_card, cards_list, cheatcodes, lenght

			x = 0

			if lenght == 10:

				while len(mas) != 5:

					mas.append(cards_list[i])
					x += 1

				if x == 1:

					print(str(x) + " card was added in your deck!")
				else:

					print(str(x) + "cards were added in your deck!")
				x = 0
				lenght = 1

			self.show_cards(mas)

			#for i in mas:
			#	if i < current_card and i != master_card:
			#		self.no_cards(mas)
			#		break

			ans = raw_input('Do you want to use any? ')

			sleep(1)

			if ans.isdigit():

				if not ans in mas and not ans in cheatcodes:
					print("Sorry, but there's no such card in your deck!")
					self.use_cards(mas)

				else:

					ans = str(ans)

					if ans in cheatcodes:

						print("You used the cheatcode card!\n" + 
	'''+--------------+
	|              |
	| ''' + ans + ''' |
	|              |
	+--------------+''')

						sleep(1)

						if ans == cheatcodes[0]:

							print("Cheatcode activated: 0 is the master card.")

							master_card = "0"

						elif ans == cheatcodes[1]:

							print("Cheatcode activated: 0 is the current card.")

							current_card = "0"

						elif ans == cheatcodes[2]:

							print("Cheatcode activated: you have 3 cards.")

							for i in range(len(mas) - 3):
								mas.remove(mas[i])

						elif ans == cheatcodes[3]:

							print("Cheatcode activated: you have 1 card.")

							try:

								mas = [str(random.randint(0, len(mas)))]

							except IndexError:

								print("- A wild IndexError appeared! -")

								sleep(1)

								print("Sorry, we can't activate your cheatcode card, probably because you have card with number 1 in your deck.")

						elif ans == cheatcodes[4]:

							print("Cheatcode activated: Russia was disconnected from SWIFT.")

						print("")

						self.logic(mas)

					elif current_card > ans and ans != master_card:

						print("You can't use that card!")
						self.logic(mas)

					else:

						current_card = ans
						mas.remove(ans)
						lenght += 1
						cards_list.append(ans)

						print('You used card: ')

						sleep(1)

						print(' ---\n' +
							'|   |\n' +
							'| ' + ans + ' |\n' +
							'|   |\n' +
							 ' ---\n')

						print(mas)

			else:
				mas = []
				self.goodbye(mas, True)
			

		def use_cards(self, mas): # repeat-game-logic

			for i in range(len(mas)):

				self.logic(mas)
				self.goodbye(mas, False)


		def goodbye(self, mas, give_up): # no-cards-in-deck

			sleep(1)

			if not mas:

				print("...")

				if not give_up:

					sleep(1)

					print("Oh! You actually won the game! Congratulations, and goodbye!")

					exit()

				else:

					sleep(1)

					print("It was a nice game. Goodbye!")

					exit() 

			else:
				self.use_cards(mas)


		def no_cards(self, mas): # no-useful-cards (needs fix)
			print("It seems that you don't have any cards that you can use.")

			sleep(1)

			print("3 cards were added in your deck!")

			for i in range(3):

				mas.append(str(random.randint(0, 7)))

			self.use_cards(mas)


	list1 = []
	cards_list = []
	cheatcodes = ["061916396836", # 0 is the master card
				  "970144313397", # 0 is the current card
				  "787992333303", # Player has 3 cards
				  "787992111101", # Player has 1 card (restarts the game)
				  "993304906842"] # Russia was disconnected from SWIFT

	for i in range(7):
		list1.append(str(random.randint(0, 9)))

	current_card = str(random.randint(0, 9))

	cards_list.append(current_card)

	master_card = current_card
	lenght = 1

	card1 = Card()

	card1.use_cards(list1)

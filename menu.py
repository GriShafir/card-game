from time import sleep
from msvcrt import getch
from main import start
import sys


def get():
	global x

	while True:
		key = ord(getch())

		if key == 27: #ESC
			break

		elif key == 13 and x == 0: #Enter
			start()
			
		elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
			key = ord(getch())

			if key == 80: #Down arrow
				return "down"

			elif key == 72: #Up arrow
				return "up"

# this is the menu example

def startupmenu():
	global x
	print(
'''          _____              _  _____                      \n    /\\   / ____|            | |/ ____|                     \n   /  \\ | |     __ _ _ __ __| | |  __  __ _ _ __ ___   ___ \n  / /\\ \\| |    / _` | '__/ _` | | |_ |/ _` | '_ ` _ \\ / _ \\  \n / ____ \\ |___| (_| | | | (_| | |__| | (_| | | | | | |  __/ \n/_/    \\_\\_____\\__,_|_|  \\__,_|\\_____|\\__,_|_| |_| |_|\\___| \n''')
	print("> Play\n  Exit")

	while True:

		if get() == "down" and x == 0:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")

			print("  Play\n> Exit")

			x = 1

		elif get() == "up" and x == 1:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")

			print("> Play\n  Exit")

			x = 0

list1 = ["|", "/", "-", "\\"]
x = 0

print("Mining some diamonds...")

for j in range(10):
	for i in range(len(list1)):
		print(list1[i])
		sys.stdout.write("\033[F")
		sys.stdout.write("\033[K")
		sleep(0.1)

print("Done!")

get2()
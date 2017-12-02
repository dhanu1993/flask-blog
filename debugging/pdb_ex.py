import sys
from random import choice
import pdb


random1	= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]	
random2	= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]	

while True:
	print("to exit this game type 'exit'")

	pdb.set_trace()
	ans = input("what is {} times {} ? ".format(choice(random2), choice(random1)))

	if ans == "exit":
		print("you were exit from game")
		sys.exit()
	elif ans == choice(random1) * choice(random2):
		print("correct")
	else:
		print("wrong")

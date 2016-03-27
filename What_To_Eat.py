from random import randint
from time import sleep
from sys import exit

print 'The choices are...\n'

Places = {1:'IHOP', 2:'Steak n Shake', 3:'Taco Bell', 4:'McDonalds', 5:'Dennys', 6:'Chinese', 7:'Find Something at Home', 8:'Burger King'}

for values in Places:
		print Places[values]
	
def main(dict):

	print '\nChoosing...\n'
	sleep(2)

	Eatery = randint(1, len(dict))

	print dict[Eatery]
	sleep(3)
	
	agree = raw_input('\nYes or No? ')
	if (agree.lower() == 'y') or (agree.lower() == 'yes'):
		print '\n-------> Thank you; come again!'
		sleep(2)
		exit()
		
	elif (agree.lower() == 'n') or (agree.lower() == 'no'):
		print '\n\n\n\n\n'
		print 'Recalculating...\n'
		main(dict)

		
main(Places)
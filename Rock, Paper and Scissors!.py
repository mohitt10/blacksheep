import random
def get_choices():
	player_choice=input('\n Enter your choice(rock,paper,scissors): ').strip()
	options=['rock','paper','scissors']
	computer_choice=random.choice(options)
	selected={'player':player_choice,'computer':computer_choice}
	return selected
def check_win(player,computer):
	print(f' you chose {player},computer chose {computer}')
	if player==computer:
		print("\n it's a tie!")
	elif player=='rock':
		if computer=='scissors':
			print('\n rock smashes scissors!! You Win!!')
		elif computer=='paper':
			print('\n paper covers rock!! You lose.')
	elif player=='paper':
		if computer=='rock':
			print('\n paper covers rock!! You Win!!')
		elif computer=='scissors':
			print('\n scissors cut paper!! You lose.')
	elif paper=='scissors':
		if computer=='rock':
			print('\nrock destroys scissors!! You lose.')
		elif computer=='paper':
			print('\n scissors cut paper!! You Win!!')
treat=True
while treat:			
	selected=get_choices()
	check_win(selected['player'],selected['computer'])
	confirmation=input('\n Do you want to play again?(if yes then press Y): ')
	if confirmation.strip()!='Y':
		treat=False







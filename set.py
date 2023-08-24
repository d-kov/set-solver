

def check_valid(cards):
	card_1 = cards[0]
	card_2 = cards[1]
	card_3 = cards[2]

	conditions = {}
	#check for same or different colours
	conditions['diff_colours'] = (card_1['colour'] != card_2['colour'] and card_1['colour'] != card_3['colour'] and card_2['colour'] != card_3['colour'])
	conditions['same_colours'] = (card_1['colour'] == card_2['colour'] and card_1['colour'] == card_3['colour'] and card_2['colour'] == card_3['colour'])

	#check for same or different shapes
	conditions['diff_shapes'] = (card_1['shape'] != card_2['shape'] and card_1['shape'] != card_3['shape'] and card_2['shape'] != card_3['shape'])
	conditions['same_shapes'] = (card_1['shape'] == card_2['shape'] and card_1['shape'] == card_3['shape'] and card_2['shape'] == card_3['shape'])

	#check for same or different shades
	conditions['diff_shades'] = (card_1['shade'] != card_2['shade'] and card_1['shade'] != card_3['shade'] and card_2['shade'] != card_3['shade'])
	conditions['same_shades'] = (card_1['shade'] == card_2['shade'] and card_1['shade'] == card_3['shade'] and card_2['shade'] == card_3['shade'])

	#check for same or different amount
	conditions['diff_amount'] = (card_1['amount'] != card_2['amount'] and card_1['amount'] != card_3['amount'] and card_2['amount'] != card_3['amount'])
	conditions['same_amount'] = (card_1['amount'] == card_2['amount'] and card_1['amount'] == card_3['amount'] and card_2['amount'] == card_3['amount'])

	#evaluate whether its valid or not
	print(cards)
	print((conditions['diff_colours'] or conditions['same_colours']) and (conditions['diff_shapes'] or conditions['same_shapes']) and (conditions['diff_shades'] or conditions['same_shades']) and (conditions['diff_amount'] or conditions['same_amount']))
	return (conditions['diff_colours'] or conditions['same_colours']) and (conditions['diff_shapes'] or conditions['same_shapes']) and (conditions['diff_shades'] or conditions['same_shades']) and (conditions['diff_amount'] or conditions['same_amount'])
def find_set(cards, previous_cards):
	for card in cards:
		if not card in previous_cards:
			previous_cards.append(card)
			if len(previous_cards) == 3:
				#base case
				#check for all the possible conditions
				if check_valid(previous_cards):
					print(f'Possible combination! {previous_cards}')
					return previous_cards
				else:
					previous_cards.pop()
					return previous_cards

			else:
				find_set(cards, previous_cards)
				previous_cards.pop()
		else:
			continue





def main():
	#informing user of input
	colours = ['Orange', 'Green', 'Pink']
	shapes = ['Round', 'Diamond', 'Squiggle']
	shades = ['Clear', 'Partial', 'Filled']

	print('Enter each of the 12 cards on screen.')
	print('Format: Card <num>: <colour> <shape> <shading> <amount>')
	print('Colour format:\n1 - Orange\n2 - Green\n3 - Pink')
	print('Shape format:\n1 - Round\n2 - Diamond\n3 - Squiggle')
	print('Shading format:\n1 - Clear\n2 - Partial\n3 - Filled')
	print('Amount format: 1 or 2 or 3')

	#set up the initial 12 cards
	cards = []
	for x in range(12):
		card = {}
		data = input(f'Card {x}: ')
		data = data.split()
		card['colour'] = colours[int(data[0]) - 1]
		card['shape'] = shapes[int(data[1]) - 1]
		card['shade'] = shades[int(data[2]) - 1]
		card['amount'] = int(data[3])
		cards.append(card)

	#find a set and keep topping up the cards
	while True:
		find_set(cards, [])
		print('Choose cards to remove by index:')
		for x in range(len(cards)):
			print(f'{x}: {cards[x]}')
		usr_in = input()
		cards.remove(usr_in.split()[0])
		cards.remove(usr_in.split()[1])
		cards.remove(usr_in.split()[2])

		print('Enter details of new cards. Enter 0 to stop adding new cards.')
		print('Format: Card <num>: <colour> <shape> <shading> <amount>')
		print('Colour format:\n1 - Orange\n2 - Green\n3 - Pink')
		print('Shape format:\n1 - Round\n2 - Diamond\n3 - Squiggle')
		print('Shading format:\n1 - Clear\n2 - Partial\n3 - Filled')
		print('Amount format: 1 or 2 or 3')
		while True:
			card = {}
			data = input(f'Card: ')
			data = data.split()
			if '0' in data:
				break
			card['colour'] = colours[int(data[0]) - 1]
			card['shape'] = shapes[int(data[1]) - 1]
			card['shade'] = shades[int(data[2]) - 1]
			card['amount'] = int(data[3])
			cards.append(card)

if __name__ == '__main__':
	main()
import random

naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Rainha', 'Rei']
deck = []
hand = []
for naipe in naipes:

    for valor in valores:

        deck.append(valor + " de " + naipe)

print(f'existem {len(deck)} cartas neste deck')

print('sacando...')

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'existem {len(deck)} cartas neste deck')

print(f'Sua mao tem: {hand}')
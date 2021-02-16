import random
on = True
goal = 0
tries = 0
while on:
    if guess.isnumeric():
        tries = 3
        guess = 0
        goal = random.randint(1,10)
        print('Adivinhe um numero de 1 a 10!')
        print(f'debug goal = {goal}')
        while tries > 0:
            print('De o seu chute! para encerrar digite uma letra')
            guess = input()
            if guess.isnumeric():
                guess = int(guess)
                if guess == goal:
                    print('vencedor! Parabens!')
                    break
                tries -= 1
                print(f'tentativas: {tries}')
            else:
                on = False
                break
print('Fim de Jogo')
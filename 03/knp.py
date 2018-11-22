from random import randrange

hod = randrange(3)

if hod == 0:
	tah_pocitace = 'kámen'
elif hod == 1:
	tah_pocitace = "nůžky"
elif hod == 2:
	tah_pocitace = "papír"
	
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen':
    if tah_pocitace == 'kámen':
        print('Remíza.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'papír':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'nůžky':
        print('Remíza.')
    elif tah_pocitace == 'papír':
        print('Vyhrál jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrál jsi!')
    elif tah_pocitace == 'nůžky':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'papír':
        print('Remíza.')
else:
    print('Nerozumím.')  
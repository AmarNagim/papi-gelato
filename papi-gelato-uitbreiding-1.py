# papi gelato
# Amar Nagim

import time

def icecreamShop():
    print('Welkom bij Papi Gelato je mag alle smaken kiezen.')
    print('')
    time.sleep(1)

    amountIcecream = int(input('Hoeveel bolletjes wilt u?: '))

    if amountIcecream >= 4 and amountIcecream <= 8:
        print(f'Dan krijgt u van mij een bakje met {amountIcecream} bolletjes')
    while amountIcecream >8:
        print('Zulke grote bakken hebben we niet')
        print('')
        amountIcecream = int(input('Hoeveel bolletjes wilt u?: ')) 

    if amountIcecream >= 1 and amountIcecream <= 8:
        hornOrBox = input(f"""
Wilt u deze {amountIcecream} bolletje(s) in een 
A) hoorntje
B) bakje? """).lower()
        while hornOrBox not in ['a', 'b']:
            print('')
            print('Sorry, dat begreep ik niet..')
            hornOrBox = input(f"""
Wilt u deze {amountIcecream} bolletje(s) in een
A) hoorntje
B) bakje? """).lower()        
        if hornOrBox == 'a':
            hornOrBox = 'hoorntje'
        elif hornOrBox == 'b':
            hornOrBox = 'bakje'

    times = 1
    for flavour in range(amountIcecream):
        print('')
        flavourChoice = input(f'Welke smaak wilt u voor bolletje nummer {times}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ').lower()
        while flavourChoice not in ['a', 'c', 'm', 'v']:
            print('Sorry dat snap ik niet...')
            flavourChoice = input(f'Welke smaak wilt u voor bolletje nummer {times}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ').lower()           
        times += 1



                
    global orderAgain
    print('')
    orderAgain = input(f'Hier is uw {hornOrBox} met {amountIcecream} bolletje(s). Wilt u nog meer bestellen? (Y/N): ').lower()     

    while orderAgain not in ['y', 'n']:
        print('Sorry dat snap ik niet..')    
        orderAgain = input(f'Hier is uw {hornOrBox} met {amountIcecream} bolletje(s). Wilt u nog meer bestellen? (Y/N): ').lower()            

    if orderAgain == 'n':
        print('Bedankt voor uw bestelling, tot ziens!')    
        time.sleep(2)
        exit
icecreamShop()

if orderAgain == 'y':
    print('')
    icecreamShop()


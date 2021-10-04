# papi gelato
# Amar Nagim

import time

hornCount = 0
boxCount = 0
bolletjesCount = 0
#topping
slagroom = 0
sprinkels = 0
caramel = 0
#zakelijk
flavour = 0



def icecreamShop():
    global slagroom
    global sprinkels
    global caramel
    global boxCount
    global hornCount
    global amountIcecream
    global bolletjesCount
    global amountLiter
    times = 1
    

    print('Welkom bij Papi Gelato')
    print('')
    time.sleep(1)

    zakelijkOfParticulier = input('Bent u 1) particulier of 2) zakelijk: ')
    while zakelijkOfParticulier not in ['1', '2']:
        print('Sorry dat snap ik niet...')
        zakelijkOfParticulier = input('Bent u 1) particulier of 2) zakelijk: ')

    print('')


    # amount iceacream
    amountIcecream = False

    if zakelijkOfParticulier == '1':
        amountIcecream = int(input('Hoeveel bolletjes wilt u?: '))
        amountIcecream == True
    if zakelijkOfParticulier == '2':
        amountLiter = int(input('Hoeveel liter ijs wilt u?: '))      


    if amountIcecream:
        if  amountIcecream >= 4 and amountIcecream <= 8:
            print(f'Dan krijgt u van mij een bakje met {amountIcecream} bolletjes')
            bolletjesCount += amountIcecream
        while amountIcecream >8:
            print('Zulke grote bakken hebben we niet')
            print('')
            amountIcecream = int(input('Hoeveel bolletjes wilt u?: ')) 

        if amountIcecream >= 1 and amountIcecream <= 8:
            bolletjesCount += amountIcecream
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
                hornCount += 1
                hornOrBox = 'hoorntje'
            elif hornOrBox == 'b':
                boxCount += 1
                hornOrBox = 'bakje'
    

    # topping     
    if amountIcecream:       
        topping = input('\nWat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ').lower()
        while topping not in ['a', 'b', 'c', 'd']:
            print('\nSorry dat snap ik niet...\n')
            topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ').lower()
        if topping == 'a':
            print('U heeft geen topping gekozen')
        elif topping == 'b':
            print('U heeft voor de topping slagroom gekozen')
            slagroom +=1
        elif topping == 'c':
            print('U heeft voor de topping sprinkels gekozen')
            sprinkels +=1
        elif topping == 'd':
            print('U heeft voor de topping caramel saus gekozen')
            caramel +=1



    # flavour
    times = 1
    if amountIcecream:
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
    else:
        for flavour in range (amountLiter):
            flavourChoice = input(f'\nWelke smaak wilt u voor voor liter {times} A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ')
            times+=1
            while flavourChoice not in ['a', 'c', 'm', 'v']:
                print('Sorry dat snap ik niet...')
                flavourChoice = input(f'Welke smaak wilt u voor voor liter {times} A) Aardbei, C) Chocolade, M) Munt of V) Vanille?: ').lower()

icecreamShop()
if amountIcecream:
    if orderAgain == 'y':
        print('')
        icecreamShop()

    priceAmountIceCream = format(bolletjesCount*1.10, ".2f")
    priceHornCount = format(hornCount*1.25, ".2f")
    priceBoxCount = format(boxCount*0.75, ".2f")
    #topping
    priceSlagroom = format(slagroom*0.50, ".2f")
    priceSprinkels = format(sprinkels*0.30, ".2f")
    priceCaramel = format(caramel*0.90, ".2f")




    

    print('     ---------------------------["Papi Gelato"]---------------------------')
    print('')
    if amountIcecream == 0:
        print(f'      Horrentje(s)          {hornCount} x €1.25   = €{priceHornCount}')
        print(f'      Bakje(s)              {boxCount} x €0.75   = €{priceBoxCount}')
    elif hornCount == 0:    
        print(f'      Bolletje(s)           {bolletjesCount} x €1.10    = €{priceAmountIceCream}                                           ')
        print(f'      Bakje(s)              {boxCount} x €0.75   = €{priceBoxCount}')
        
    elif boxCount == 0:    
        print(f'      Bolletje(s)           {bolletjesCount} x €1.10   = €{priceAmountIceCream}                                           ')
        print(f'      Horrentje(s)          {hornCount} x €1.25   = €{priceHornCount}')
    else:
        print(f'      Bolletje(s)           {bolletjesCount} x €1.10    = €{priceAmountIceCream}                                           ')
        print(f'      Horrentje(s)          {hornCount} x €1.25   = €{priceHornCount}')
        print(f'      Bakje(s)              {boxCount} x €0.75   = €{priceBoxCount}')
    if slagroom >0 and sprinkels >0 and caramel >0:
        print(f'      Topping slagroom      {slagroom} x €0.50    = €{priceSlagroom}                                           ')
        print(f'      Topping sprinkels     {sprinkels} x €0.30    = €{priceSprinkels}                                           ')
        print(f'      Topping caramel       {caramel} x €0.90    = €{priceCaramel}                                           ')
    elif slagroom == 0 and sprinkels >0 and caramel >0:
        print(f'      Topping sprinkels     {sprinkels} x €0.30    = €{priceSprinkels}                                           ')
        print(f'      Topping caramel       {caramel} x €0.90    = €{priceCaramel}                                           ')
    elif slagroom >0 and sprinkels == 0 and caramel >0:
        print(f'      Topping slagroom      {slagroom} x €0.50    = €{priceSlagroom}                                           ')
        print(f'      Topping caramel       {caramel} x €0.90    = €{priceCaramel}                                           ')    
    elif slagroom >0 and sprinkels >0 and caramel == 0:
        print(f'      Topping slagroom      {slagroom} x €0.50    = €{priceSlagroom}                                           ')
        print(f'      Topping sprinkels     {sprinkels} x €0.30    = €{priceSprinkels}                                           ')
    elif slagroom >0 and sprinkels == 0 and caramel == 0:
        print(f'      Topping slagroom      {slagroom} x €0.50    = €{priceSlagroom}                                           ')
    elif slagroom == 0 and sprinkels >0 and caramel == 0:
        print(f'      Topping sprinkels     {sprinkels} x €0.30    = €{priceSprinkels}                                           ')
    elif slagroom == 0 and sprinkels == 0 and caramel >0:
        print(f'      Topping caramel       {caramel} x €0.90    = €{priceCaramel}                                           ')


    priceAmountIceCreamFloat = float(priceAmountIceCream)
    priceHornCountFloat = float(priceHornCount)
    priceBoxCountFloat = float(priceBoxCount)
    #topping
    priceSlagroomFloat = float(slagroom)
    priceSprinkelsFloat = float(sprinkels)
    priceCaramelFloat = float(caramel)


    total = format(priceAmountIceCreamFloat+priceHornCountFloat+priceBoxCountFloat+slagroom+sprinkels+caramel, ".2f")
    print('                                        -------- +                                           ')
    print(f'      Totaal                            = €{total}                                  ')

else:
    priceWithoutTax = float(format(amountLiter*9.80, ".2f"))
    priceWithTax = float(format(priceWithoutTax/100*109, ".2f"))
    
    print('\n\n    ---------------------------["Papi Gelato"]---------------------------')
    print(f'    Liter                             {amountLiter} x €9.80 = €{format(priceWithoutTax, ".2f")}     ')
    print('                                                 --------------------')

    print(f'    Totaal inc. BTW                             = €{format(priceWithTax, ".2f")}                                 ')
    print(f'    BTW (9%)                                    = €{format(priceWithTax-priceWithoutTax, ".2f")}                                 ')

import random

mains = ['cauliflower', 'tilapia fillet', 'pork loin', 'salmon', 'potatos', 'three color squash', 'eggplant', 'steak', 'baguette']
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20] 
flairs = ['with balsamico', 'with garlic and oil', 'with minted yogurt', 'with chutney', 'with salad', 'with salsa', 'over sticky rice', 'au jus', 'with basmati rice']
flairprices = [2, 1, 3, 1, 3, 1, 2, 2, 2,] 
alreadyadded = []

menuitems = int(input ("How many menu items would you like to see? (max 9): "))

total = 0

for i in range(menuitems):
    main = random.choice(mains)
    flair = random.choice(flairs)

    if main + flair in alreadyadded:
        continue

    alreadyadded.append(main + flair)

    price = prices[mains.index(main)]
    flairprice = flairprices[flairs.index(flair)]
    print(f'{main} {flair}, ${price} + ${flairprice} = ${price + flairprice}')
    total += price + flairprice
print (f"total price: ${total}")

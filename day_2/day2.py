print('Welcome to the Tip Calculator!')
total = int(input('Please write a total bill: '))
perc_tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))
tip_per_person = total*perc_tip/100/people
print(f'Earch person should pay: {tip_per_person}')

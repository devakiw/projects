import random
import string
adjectives = ['sleepy', 'hyperactive', 'restricted','manic','lethargic', 'blunted','courageous','tired','inattentive', 'psychotic','driven','fixated']
nouns = ['pizza','rosti', 'gorgonzola','mushroom','truffle','bread', 'egg', 'carrot','rice','chicken','potato', 'sushi','lobster','lettuce','celery','parsnip']

print('Welcome to password picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('Your password of the day is: %s' %password)
    response = input('Would you like another password? Type y or n:')
    if response == 'n' :
        break 

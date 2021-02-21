import random

massages = ['It is certain', 'It is decidedly so', 'Yes definitely',
            'Reply hazy try again', 'Ask again later', 'Concentrate and ask again',
            'My reply is on', 'Outlook not so good', 'Very doubtful']

print(massages[random.randint(0, len(massages) -1)])
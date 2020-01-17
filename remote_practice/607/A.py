T = int(input())

for i in range(T):
    string = input()
    lang = string[-5:]
    if lang == 'mnida':
        print('KOREAN')
    elif lang[-2:] == 'po':
        print('FILIPINO')
    elif lang[-4:] == 'desu' or lang[-4:] == 'masu':
        print('JAPANESE')
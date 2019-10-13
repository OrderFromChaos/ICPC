# Given a bag of scrabble tiles, what's the maximum score that can be achieved
# by placing those 100 tiles end to end? For each word you find, you earn points
# relative to its letters. Finding multiple accrues no new points.
# There are two wildcards that give no value, but can be any letter.

# Going to start by ignoring wildcards, then work my way up.

from copy import deepcopy
import random

# the Xth key is a set of all words of X length
with open('538scrabble.txt', 'r') as f:
    data = f.readlines()

wordlookup = dict()
for word in data:
    word = word.strip()
    length = len(word)
    if length in wordlookup.keys():
        wordlookup[length].append(word)
    else:
        wordlookup[length] = [word]
# Faster lookup:
wordlookup = {key: set(wordlookup[key]) for key in wordlookup if wordlookup[key]}

lettervalue = {
    'e': 1,
    'a': 1,
    'i': 1,
    'o': 1,
    'n': 1,
    'r': 1,
    't': 1,
    'l': 1,
    's': 1,
    'u': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10
}

inventory = (
    ['e']*12 +
    ['a','i']*9  +
    ['o']*8  +
    ['n','r','t']*6  +
    ['l','s','u','d']*4  +
    ['g']*3  +
    ['b','c','m','p','f','h','v','w','y']*2 +
    ['k','j','x','q','z']
)

for i in wordlookup:
    print(i, len(wordlookup[i]))

def ngram(word, index, n):
    return word[index-(n-1):index+1]

def countPointsWord(word):
    global lettervalue
    summa = 0
    for letter in word:
        summa += lettervalue[letter]
    return summa

def getPointsPhrase(phrase):
    global wordlookup
    seen = []
    points = 0
    for index, letter in enumerate(phrase):
        if index >= 24:
            top_n = 25
        else:
            top_n = index + 2
        for n in range(2, top_n):
            subword = ngram(phrase, index, n)
            # Note: n == len(subword)
            if subword not in seen and subword in wordlookup[n]:
                seen.append(subword)
                points += countPointsWord(subword) # Could memoize or precompute?
    return seen, points

test_str = 'wordstotestmmegamm'

seen, points = getPointsPhrase(test_str)
print(seen)
print(points)

# print('Trying greedy append solution...')
# inventorybackup = deepcopy(inventory)
# inventorybackup2 = deepcopy(inventory)
# history = []
# # Have to "randomly" select first character; no one length strings
# inventorybackup = list(set(inventorybackup)) # Remove repeats
# while len(inventorybackup):
#     seed = random.choice(inventorybackup)
#     finstring = seed
#     inventorybackup.remove(seed)
#     inventory = deepcopy(inventorybackup2)
#     while len(inventory):
#         scores = []
#         for letter in inventory:
#             scores.append((getPointsPhrase(finstring + letter)[1], letter))
#         winner = max(scores)[1]
#         finstring += winner
#         inventory.remove(winner)
#     print('Greedy winner with seed of {0}:'.format(seed), finstring)
#     metrics = getPointsPhrase(finstring)
#     print('With a score of:', metrics[1])
#     # print('And matches of:', sorted(metrics[0], key = lambda x: len(x), reverse=True))
#     history.append((metrics[1], finstring))

# inventory = inventorybackup2

# print(sorted(history, reverse=True)[0])



# inventorybackup = deepcopy(inventory)

# print('Trying greedy insert solution...')
# random.seed(13)
# finlist = ['a','u']
# inventory.remove('a')
# inventory.remove('u')
# while len(inventory):
#     insertion = random.choice(inventory)
#     scores = []
#     for position in range(len(finlist)):
#         testlist = deepcopy(finlist)
#         testlist.insert(position, insertion)
#         newstr = ''.join(testlist)
#         metrics = getPointsPhrase(newstr)
#         scores.append((metrics[1], newstr))
#     best = max(scores)
#     finlist = list(best[1])
#     inventory.remove(insertion)

# ans = ''.join(finlist)
# print((getPointsPhrase(ans)[1], ans))


# print('Trying pareto optimal approach...')
# final = deepcopy(inventory)
# random.shuffle(final)
# netgain = getPointsPhrase(''.join(final))[1]
# while netgain > 0:
#     strversion = ''.join(final)
#     prescore = getPointsPhrase(strversion)[1]
#     print(prescore, strversion)
#     netgain = 0
#     secondarybreak = False
#     for ind, char in enumerate(final):
#         temp = deepcopy(final)
#         del temp[ind]
#         tempbackup = deepcopy(temp)
#         for newpos in range(len(temp)):
#             temp.insert(newpos, char)
#             newscore = getPointsPhrase(''.join(temp))
#             newgain = newscore[1] - prescore
#             if newgain > netgain:
#                 netgain = newgain
#                 final = temp
#                 secondarybreak = True
#                 break
#             else:
#                 temp = deepcopy(tempbackup)
#         if secondarybreak:
#             break


# print('Trying random search replacements...')

# final = 'carboxymethylcellulosesiforeshadowersipreformattingoreawakeneditnonunionizedibijugatetagapedquaivv'
# # final = deepcopy(inventory)
# # random.shuffle(final)
# # final = ''.join(final)
# numchars = len(final)
# while True:
#     prescore = getPointsPhrase(final)[1]

#     movelength = random.randint(1,5)
#     startpos = random.randint(0,numchars - movelength)
#     selection = list(final[startpos : startpos+movelength])
#     random.shuffle(selection)
#     selection = ''.join(selection)
#     newstr = final[:startpos] + selection + final[startpos+movelength:]

#     postscore = getPointsPhrase(newstr)[1]
#     if postscore > prescore:
#         final = newstr
#         # print(movelength)
#         print(postscore, final)


print('Reasoning based on dataset...')
wordscores = []
for word in data:
    word = word.strip()
    wordscores.append((getPointsPhrase(word)[1],word))

bestwords = sorted(wordscores, reverse=True)
print(bestwords[:10])

def wordPossible(word, charset):
    chars = deepcopy(charset)
    possible = True
    for letter in word:
        if letter in chars:
            chars.remove(letter)
        else:
            possible = False#
            break
    if possible:
        return True, chars
    else:
        return False, []

inventorybackup = deepcopy(inventory)
finstr = ''
i = 0
while inventory:
    currword = bestwords[i][1]
    satisf, chars = wordPossible(currword, inventory)
    if satisf:
        finstr += currword
        print(finstr)
        inventory = chars
    i += 1
    if i > len(bestwords) - 1:
        finstr += ''.join(inventory)
        break

print(getPointsPhrase(finstr)[1], finstr)


inventory = inventorybackup

print('Trying pareto optimal approach...')
final = list(finstr)
netgain = getPointsPhrase(''.join(final))[1]
while netgain > 0:
    strversion = ''.join(final)
    prescore = getPointsPhrase(strversion)[1]
    print(prescore, strversion)
    netgain = 0
    secondarybreak = False
    for ind, char in enumerate(final):
        temp = deepcopy(final)
        del temp[ind]
        tempbackup = deepcopy(temp)
        for newpos in range(len(temp)):
            temp.insert(newpos, char)
            newscore = getPointsPhrase(''.join(temp))
            newgain = newscore[1] - prescore
            if newgain > netgain:
                netgain = newgain
                final = temp
                secondarybreak = True
                break
            else:
                temp = deepcopy(tempbackup)
        if secondarybreak:
            break
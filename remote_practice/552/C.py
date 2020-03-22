from itertools import starmap, combinations_with_replacement

F, R, C = [int(x) for x in input().split()]

# TODO
# Rewrite in order of:
# 1. Generate 0,7 two-pairings
# 2. For each pair, run week 1 as the first pair, week 2 as the second, and see which produces the
#    highest non-negative result

# Figure out how many full weeks there are
weekf = lambda x, m: (x - x % m)//m
weeks = min(starmap(weekf, [(F,3),(R,2),(C,2)]))

# Generate first-last week pairings
pairings = combinations_with_replacement(range(7), 2)

maxdays = 0
for p in pairings:
    # Do first week
    for c in ranges:
        inv = [F,R,C]
        w = eats[c[0]:c[1]]
        for m in w:
            inv[m] -= 1
        if all([x > 0 for x in inv]):
            days = c[1] - c[0]
            if days > maxdays:
                maxdays = days
                print(w)
    
    # Do week block
    
    # Do second week



# F = F - 3 * weeks
# R = R - 2 * weeks
# C = C - 2 * weeks

# # Now just solve the first and final weeks brute force
# eats = [0,0,1,2,0,2,1]
# if weeks > 0:
#     firstweek = combinations(range(7), 2)
#     secondweek = combinations(range(7), 2)
#     # both = combinations
#     # maxdays = 0
#     # for c in ranges:
#     #     inv = [F,R,C]
#     #     w = eats[c[0]:c[1]]
#     #     for m in w:
#     #         inv[m] -= 1
#     #     if all([x > 0 for x in inv]):
#     #         days = c[1] - c[0]
#     #         if days > maxdays:
#     #             maxdays = days
#     #             print(w)
# else:
#     ranges = combinations(range(7), 2)
#     maxdays = 0
#     for c in ranges:
#         inv = [F,R,C]
#         w = eats[c[0]:c[1]]
#         for m in w:
#             inv[m] -= 1
#         if all([x > 0 for x in inv]):
#             days = c[1] - c[0]
#             if days > maxdays:
#                 maxdays = days
#                 print(w)

# print(F, R, C, weeks)

# print(maxdays)
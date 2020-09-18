
nums = [4,8,15,16,23,42]
prods = dict()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        x, y = nums[i], nums[j]
        prods[x*y] = (x, y)

# Queries:
# 1 2
# 2 3
# 3 4
# 4 5
# (6 can be figured out by elimination)

p = lambda x, y: print(f'? {x} {y}', flush=True)

query = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5)
]

ans = []

for q in query:
    p(*q)
    ans.append(int(input()))

b = list(set(prods[ans[0]]) & set(prods[ans[1]]))[0]
a = list(set(prods[ans[0]]) - {b})[0]
c = list(set(prods[ans[1]]) - {b})[0]
d = list(set(prods[ans[2]]) - {c})[0]
e = list(set(prods[ans[3]]) - {d})[0]
f = list(set(nums) - {a,b,c,d,e})[0]
print(f'! {a} {b} {c} {d} {e} {f}')
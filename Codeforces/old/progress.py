import matplotlib.pyplot as plt
import seaborn as sns

with open('solvedata.txt','r') as f:
    data = f.readlines()
data = [list(map(int,x.split())) for x in data]
days = [x[0] for x in data]
elo = [x[1] for x in data]

plt.scatter(days,elo)
plt.xlim(left=280)
plt.ylabel('Solved problem @ Codeforces ELO')
plt.xlabel('Days from Jan 1st, 2019')
plt.show()
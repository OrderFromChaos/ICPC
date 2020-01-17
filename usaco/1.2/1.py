"""
ID: sourcef3
LANG: PYTHON3
TASK: test
"""
# must use sys.stderr.write('message') for logging messages
with open('test.in','r') as f:
    data = f.readlines()
with open('test.out','w') as f:
    f.write(str(sum([int(x) for x in data[0].split(' ')])))
    f.write('\n')
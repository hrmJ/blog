import sys

def getLineLevel(linein):
    strstart = linein.lstrip()      # find the start of text in line
    x = linein.find(strstart)       # find the text index in the line
    n = linein.count("\t", 0, x)    # count the tabs
    return(n + 1)                   # return the count + 1 (for level)

with open(sys.argv[1],'r') as f:
    text = f.read()

output = ''
for line in text.splitlines():
    level = getLineLevel(line)
    line = line.lstrip()
    if level == 1:
        output += '{}\n{}'.format(line,len(line)*'=')
    elif level == 2:
        output += '{}\n{}'.format(line,len(line)*'-')
    elif level > 4: 
        output += '- {}'.format(line)
    else: 
        output += '{} {}'.format(level*'#',line)
    output += '\n'*2

print(output)

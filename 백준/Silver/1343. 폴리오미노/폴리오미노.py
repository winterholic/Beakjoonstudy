word = list(input())
#print(word)

polyomino = ""
present_num_X = 0
flag = 1

for w in word:
    polyomino += w
    
    if polyomino[-4:] == 'XXXX':
        polyomino = polyomino[:-4] + 'AAAA'
        
polyomino = polyomino.replace('XX', 'BB')

if 'X' in polyomino :
    print(-1)
else :
    print(polyomino)
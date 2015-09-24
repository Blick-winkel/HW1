import time

st = open('long_poem.txt', 'r', encoding = 'utf-8')
words = open('new.txt', 'r', encoding = 'utf-8')
wordsmass = []
stmass = []
stmass2 = []
t1 = 0
t2 = 0

for i in words:
    i = i.strip('\n')
    wordsmass.append(i.lower())

for string in st:
    stmass.append(string.lower())
    
    string = string.strip('\n')
    string = string.strip('!')
    string = string.strip('?')
    string = string.strip('.')
    string = string.strip(':')
    string = string.strip('…')
    string = string.strip(',')
    
    stmass2.append(string.lower())



def snip_search(st,words):
    f = open('snippets.txt','w', encoding = 'utf-8')
    global wordsmass, t1
    t0 = time.clock()
    for w in wordsmass:
        for n in range(len(stmass)):
            if w in stmass[n]:
                 f.write(stmass[n-1] + stmass[n] + stmass[n+1] + '\r\n')
                 

    f.close()
    t1 = time.clock() - t0
    print (t1)

def rhymes(st, words):
    f = open('rhymes.txt','w', encoding = 'utf-8')
    global wordmass, t2
    s = []
    t0 = time.clock()
    for w in wordsmass:
        for n in range(len(stmass2)):
            if w in stmass2[n]:
                if w[-2:] == stmass2[n-2][-2:] and stmass2[n-2].split(' ')[-1] not in s:
                    f.write(w + '-' + stmass2[n-2].split(' ')[-1] + '\r\n')
                    s.append(stmass2[n-2].split(' ')[-1])
                    
                if w[-2:] == stmass2[n-1][-2:] and stmass2[n-1].split(' ')[-1] not in s:
                    f.write(w + '-' + stmass2[n-1].split(' ')[-1] + '\r\n')
                    s.append(stmass2[n-1].split(' ')[-1])
                    
                if w[-2:] == stmass2[n+1][-2:] and stmass2[n+1].split(' ')[-1] not in s:
                    f.write(w + '-' + stmass2[n+1].split(' ')[-1] + '\r\n')
                    s.append(stmass2[n+1].split(' ')[-1])
                    
                if w[-2:] == stmass2[n+2][-2:] and stmass2[n+2].split(' ')[-1] not in s:
                    f.write(w + '-' + stmass2[n-2].split(' ')[-1] + '\r\n')
                    s.append(stmass2[n+2].split(' ')[-1])

    t2 = time.clock() - t0

    print (t2)

                
print (t1 + t2)
                
    
    
    
snip_search(st,words)
rhymes(st,words)

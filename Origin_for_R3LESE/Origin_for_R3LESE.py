f = open('accs.txt','r')
r = open('result.txt','w')
gh = open('good.txt', 'w')
ll = open('bad.txt','w')
code = f.read()
f.close()
accounts = []
goods = []
bads = []
z = None
count = 0
word = 'Данные для входа:'
word1 = 'Origin ID'
word2 = 'Уровень проверки: Не точный'
word3 = 'Статус почты: Подтверждён'
word4 = 'Статус почты: Не подтверждён'
word5 = 'Уровень проверки: Точный'

while True: 
    c = code.find(word)
    d = code.find(word1)

    if z == c or c == -1:
        break

    else:
        z=c
    q = code[c:d+19]
    w = code[c+18:d-1] + " | "
    code = code.replace(q,"")        
    a = code.find(word5)
    b = code.find(word2)

    if a < b:
        y = code.find(word3) #Подтверждён
        i = code.find(word4) #Не подтверждён

        if y < i :
             e = code[y:y+25]
             h = code[y+14:y+25] + "\n"
             bads.append(w + "\n")
             
        else:
            e = code[i:i+28]
            h = code[i+14:i+28] + "\n"
            goods.append(w + "\n")
        code = code.replace(word5,"",1)
        code = code.replace(e,"",1)

    else:
        code = code.replace(word2,"",1)
        bads.append(w + "\n")
        h = "?" + "\n"          
    accounts.append(w+h)
     
for i in range (len(accounts)):
    print(accounts[i])
    r.write(accounts[i]) 
 
for k in range (len(goods)):
    gh.write(goods[k])
 
for j in range (len(bads)):
    ll.write(bads[j])
    
   








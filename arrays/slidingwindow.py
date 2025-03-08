def maximumLengthSubstring(s: str)-> int:
    l, r = 0, 0 #ponteiros left e right
    _max = 1  #o maximo de tamanho de uma sequencia de strings diferentes em um array só pode ser um
    counter = {} # hashmap guardará quanto de cada string tem nele ao atender os requisitos do exercício
    counter[s[0]]=1 #na posição inicial ja conta como um

    while r < len(s)-1: #enquanto o  ponteiro r for  menor que o tamanho máximo do array - 1
        r+=1 #ele avança uma casa
        if counter.get(s[r]): #se a string ja existir no hashmap
            counter[s[r]] +=1 #adiciona um no seu valor
        else: #caso não exista
            counter[s[r]] = 1 #seu valor agora é um (foi criado)

        while counter[s[r]] == 3: #se o valor for igual a 3
            counter[s[l]] -= 1 #é tirado o valor
            l+=1 #e o ponteiro esquerdo avança
        _max = max(_max, r-l+1) #o valor de max é igual o que ta entre right e left (ponteiros) + 1 pra escapar do length
    return _max, counter #retorno de max

print(maximumLengthSubstring(['b','c','b','b','b','c','b','a'])) #output: 4 que no caso seria ['b', 'c', 'b', 'a']

#preciso comentar esse código
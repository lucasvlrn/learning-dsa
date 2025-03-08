def firstUniqChar(s: str)-> int:
    d = {}  #abri um hashmap
    for idx, ch in enumerate(s): #percorre a string s usando o enumerate que da o caractere e um id
        if not d.get(ch): #se o caractere nao tiver no hashmap
            d[ch] = [idx, 1] #cria uma tupla (matriz, mas que nesse caso foi necessario passar pra uma lista) adicionando o item
        else: #caso ele ja tenha
            d[ch][1] +=  1 #incrementa o valor a partir da chave 
            
    for ch, val in d.items(): #for para verificar items de um dicionario, passando eles para tuplas chave valor, por isso o ch e val 
        if val[1] == 1: #se o valor na posição um for igual a um
            return val[0]  #retorna o index (posição)

    return -1 #retorno padrao se não der certo
    
    
print(firstUniqChar("LLucas"))
        
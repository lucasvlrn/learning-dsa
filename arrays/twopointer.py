# two pointer 
def reverseWords_manual(s):
        res='' #variavel vazia
        l, r = 0,0 #dois ponteiros (left e right)

        while r < len(s): #enquanto o ponteiro right não for até o fim da string
            if s[r] != ' ': #se o ponteiro r foi diferente de uma string vazia
                r += 1 #ele avança uma casa
            else: #se nao
                res += s[l:r+1][::-1] #pegar o que ta entre os ponteiros e inverter
                r += 1 #avança uma casa do ponteiro
                l = r #ponteiro left está no mesmo lugar que o right
        res += ' ' #concatenar a string vazia
        res += s[l:r+2][::-1] #pegar o que ta entre os ponteiros novamente e inverter (não sei o pq do r+2)
        return res[1:] #retorna a string ao contrário
    


print(reverseWords_manual("Luc aas")) #teste, output: cuL saa
print(reverseWords_manual("gdf97")) #teste, output: 79fdg

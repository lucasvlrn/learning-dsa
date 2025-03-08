

def binary_search(nums, n):
    lo = 0 #ponteiro para o início
    hi = len(nums) #ponteiro para o fim

    while lo<hi: #enquanto o primeiro ponteiro for menor que o do fim
        mid = int((lo+hi)/2) #definição de ponteiro no meio da estrutura de dados 
        if nums[mid] == n: #se o numero que procuramos for igual ao ponteiro do meio
            return mid #ele será retornado
        elif nums[mid] < n: #se o numero do meio for menor que o que procuramos
            lo = mid + 1 #o ponteiro inicial aponta para o meio mais 1 da estrutura, desconsiderando todos os outros atras
        else: #se o numero do meio for maior que o que procuramos
            hi = mid #todos os numeros a frente do ponteiro do meio são desconsiderados e o ponteiro que aponta para o último, retorna para o meio
    return "Não encontrado em", nums


arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 6))




def binary_search(nums, n, lo, hi):

    while lo<hi: #enquanto o primeiro ponteiro for menor que o do fim
        mid = int((lo+hi)/2) #definição de ponteiro no meio da estrutura de dados 
        if nums[mid] == n: #se o numero que procuramos for igual ao ponteiro do meio
            return mid #ele será retornado
        elif nums[mid] < n: #se o numero do meio for menor que o que procuramos
            lo = mid + 1 #o ponteiro inicial aponta para o meio mais 1 da estrutura, desconsiderando todos os outros atras
        else: #se o numero do meio for maior que o que procuramos
            hi = mid #todos os numeros a frente do ponteiro do meio são desconsiderados e o ponteiro que aponta para o último, retorna para o meio
    return "Não encontrado em", nums


def exponential_search(arr, target):
    if(arr[0] == target): ##se o primeiro indice for o target
        return 0 #retorna ele
    n = len(arr) #caso não, cria um ponteiro que aponta para o final do array
    i = 1 #e um  que aponta para o segundo indice

    while i < n and arr[i] < target: #enquanto i for menor que o tamanho do array e o numero buscado menor que o target
        i*=2 #o ponteiro de i avança em ele mesmo x2 (1, 2, 4, 8, 16...)
    if arr[i] == target:  #se achar o target
        return #retorna seu indice

    return binary_search(arr, target, i//2, min(i, n-1)) #se não achar, fazer uma binary search no subarray formado, passando os ponteiros com estes dois parametros finais
    
arr = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
  11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
  31, 32, 33, 34, 35, 36, 37, 38, 39, 40
]

target = 32

result = exponential_search(arr, target)
print(f"Element found at index {result}")


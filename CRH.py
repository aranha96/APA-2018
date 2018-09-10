file = open("couting.txt", "r")
n = int(file.readline())
a = []
for line in file:
    a.append(int(line))

def CountingSort(arr,n,pos):
    intervalo = 10
    aux =  [0] * (intervalo + 1)
    saida = [0] * n



    for j in range(0,n):
        aux[int((arr[j]/pos)%intervalo)] += 1

    for i in range(0,intervalo):
        aux[i] += aux[i - 1]

    i = n - 1
    while(i >= 0):
        
        saida[aux[int((arr[i]/pos)%intervalo)]- 1] = arr[i]
        aux[int((arr[i]/pos)%intervalo)] -= 1
        i -= 1
        
    for k in range(0,n):
        arr[k] = saida[k]
       
def RadixSort(arr):
    n = len(arr)
    maior = max(arr)
    mul = 1

    while(maior):
        CountingSort(arr,n,mul)
        mul *= 10
        maior -= 1
        
    return arr 

def Heapify(a, n, i):
    
  while True:
    maior = n
    esq = 2*n + 1
    drt = esq + 1
    
    for j in [esq, drt]:
      if (j < i and a[int(j)] > a[int(maior)]):
        maior = j
        
    if (maior == n):
      return

    a[int(n)], a[int(maior)] = a[int(maior)], a[int(n)]
    n = maior

def Max_Heap(a, n):
    
  i = n / 2 - 1
  
  while (i >= 0):
      
    Heapify(a, i, n)
    i -= 1

def HeapSort(a, n):
    
  Max_Heap(a, n)
  j = n - 1
  
  while (j > 0):
    
    a[int(0)], a[int(j)] = a[int(j)], a[int(0)]
    Heapify(a, 0, j)
    j -= 1

b = [11,17,22,39,55,58,19,100,191,101,203] #teste inicial
c = a #array de entrada




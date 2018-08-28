import numpy as np
import math

file = open("couting.txt", "r")
n = int(file.readline())
a = []
for line in file:
    a.append(int(line))
k = 9989

def Counting(a,n,k):
    aux =  np.zeros(k+1)
    saida = np.zeros(n)

    for j in range(0,n):
        aux[a[j]] = aux[a[j]] + 1

    for i in range(1,k + 1):
        aux[i] = aux[i] + aux[i - 1]

    for l in range(0,n):
        ind1 = a[l]
        ind2 = aux[ind1] - 1
        saida[int(ind2)] = a[l]
        aux[ind1] = aux[ind1] - 1
        
    return saida

def InsertionSort(a):
    for i in range(1,len(a)):
        k = a[i]
        j = i-1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = k
        
def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
 
def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        InsertionSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1

c = a
bucketSort(c)
y = Counting(a,n,k)
print(y)
print(c)


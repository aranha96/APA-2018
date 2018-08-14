import numpy as np

file = open("couting.txt", "r")
n = int(file.readline())
a = []
for line in file:
    a.append(int(line))

def InsertionSort(a,n):
    for i in range(1,n):
        k = a[i]
        j = i-1
        while j >= 0 and k < a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = k

def SelectionSort(a,n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    
def MergeSort(a,p,r):
    if p < r:
        q = (p+r)/2
        MergeSort(a,p,q)
        MergeSort(a,q+1,r)
        Merge(a,p,q,r)

def Merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    l =  np.zeros(n1 + 1)
    r = np.zeros(n2 + 1)
    
    for i in range(0, n1):
        l[i] = a[p + i -1]
    for j in range(0,n2):
        r[j] = a[q + j]

    i = 1
    j = 1

    for k in range(p, r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i = i +1
        else:
            a[k] = r[j]
            j = j + 1

def QuickSort(a,l,h):
    if l < h:
        p = Particiona(a,l,h)
        QuickSort(a,l,p - 1)
        QuickSort(a,p + 1,h)

def Particiona(a,l,h):
    pivot = a[h]
    i = l - 1
    for j in range(l, h - 1):
        if a[j] < pivot:
            i = i + 1
            a[i],a[j] = a[j],a[i]
    if a[h] < a[i + 1]:
        a[i + 1],a[h] = a[h],a[i + 1]
    return i + 1
        
 
c1 = a
c2 = a
c3 = a
c4 = a
InsertionSort(c1,n)
SelectionSort(c2,n)
MergeSort(c3,50,50)
QuickSort(c4,0,n-1)



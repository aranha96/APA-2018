'\Abre arquivo de texto'\
       
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
    
    
c1 = a
c2 = a
InsertionSort(c1,n)
SelectionSort(c2,n)
print(c2)

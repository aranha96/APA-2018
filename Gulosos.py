a = [[0,23,17,19],[23,0,22,20],[17,22,0,25],[19,20,25,0]]
pai = []
rank = []

def getArestas(a,n):

    linha = []
    coluna = []
    
    for i in range(0,n):
        for j in range(0,n):

            if(a[i][j] > 0):
                linha.append(i)
                coluna.append(j)
                         
    return linha, coluna
        

def getVertices(a,n):
    
    vertices = [0]*n
    
    for i in range(0,n):
        vertices[i] = i

    return vertices

def makeSet(vertice):
    
    pai.append(vertice)
    rank.append(0)
    
def find(vertice):
    
    if (pai[vertice] != vertice):
        pai[vertice] = find(pai[vertice])
        
    return pai[vertice]

def union(vertice1, vertice2):
    r1 = find(vertice1)
    r2 = find(vertice2)

    if (r1 != r2):
        if(rank[r1] > rank[r2]):
            pai[r2] = r1
        else:
            pai[r1] = r2
        if (rank[r1] == rank[r2]):
            rank[r2] += 1
    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

def matrix(a,rows,g):
    #Dataframe for aesthetic output: (can reuse from this point on)
    df = pd.DataFrame(a, index=rows, columns=rows) #both rows and columns are same
    print(df.to_string())
    
    #finds minimum (non zero) and the index
    minval = np.amin(a[np.nonzero(a)])
    print(minval)
    
    itemindex = np.where(df.values==minval)
    index_list = sorted([itemindex[0][0],itemindex[0][1]], reverse=True)
    print(index_list)

    #Species detection, deletion and updating
    first = rows[index_list[0]]
    second = rows[index_list[1]]

    del rows[index_list[0]]
    del rows[index_list[0]]
    add = [first,'/', second]
    add = ''.join(add)
    rows.append(add)

    #i think larger one MAY have to come first, look into this later
    a = np.delete(a, index_list[0], 1) #delete second column
    a = np.delete(a, index_list[1], 1) #delete first column
    a = np.delete(a, index_list[0], 0) #delete second row
    a = np.delete(a, index_list[1], 0) #delete first row

    #updates tree
    newnode = len(g.nodes)+1
    g.add_node(newnode)
    g.node[newnode]['label'] = add
    g.add_edge(

    for j in g.nodes:
        print(g.node[j]['label'])
    
    return {'rows':rows, 'a':a}

def WPMGA(file):
    #initial file reading
    fmatrix = open(file+'.txt').read()
    fmatrix = [item.split() for item in fmatrix.split('\n')]
    
    a = np.array(fmatrix)
    
    a = np.delete(a, 0, 1) #delete first column
    a = np.delete(a, 0, 0) #delete first row

    rows = fmatrix[0]
    rows.remove('-')
    a = a.astype(int)

    #phylo tree initialization
    g = nx.Graph()
    g.add_nodes_from(g.nodes(), label = -1)
    for node in range(1,len(rows)+1):
        g.add_node(node)
        g.node[node]['label'] = rows[node-1]
    
    hi = matrix(a,rows,g)
    print(hi)
    return g

item = WPMGA('matrix3')
    

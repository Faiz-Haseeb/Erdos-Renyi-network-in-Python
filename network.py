import random
import matplotlib as plt

def create_network(n:int, p:float):
    """ Creates an adjacency list representation of an Erdos-Renyi network

        Parameters: 
        -self: mandatory reference to this object.
        -n: number of nodes of the network.
        -p: probability that each pair of nodes will be connected.

        Returns:
        An adjacency matrix representation of the Erdos-Renyi network, in the form of a nested list.
    """
    adj_mat = []

    for i in range(n):
        #populating the list with 0s first.
        adj_mat.append([0]*n)

    for r in range(n):
        for c in range(n):
            if (r < c):
                #generating a random number to create links based on probability
                temp_p = random.random()
                if temp_p < p:
                    adj_mat[r][c] = 1

    return adj_mat

def avg_degree(G):
    pass

def avg_cluster(G):
    pass

def avg_pathlen(G):
    pass

def plot(G):
    pass



# a = create_network(5,0.5)
# for n in a:
#     print(n,'\n')


      
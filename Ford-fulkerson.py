import random
#Representing the flow network


#Node class
class Node:

    def __init__(self, ID):
        self.ID = ID
        self.connections = {}
        self.visited = False
        self.parent = None
    
    def add_connection(self, toAdd, weight):
        self.connections[toAdd] = weight

#Function to generate network dictionary of size n.
def generate_network(n):
    nodes = {}

    #Create new nodes and add to dictionary.
    for i in range(1, n, 1):
        nodes[i] = Node(i)
    
    #Generate connections


#Dictionary of Nodes, ID = keys, node object = values.
Nodes = {

}







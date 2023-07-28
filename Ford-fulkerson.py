import random
#Representing the flow network

#Node class
class Node:

    def __init__(self, ID):
        self.ID = ID
        self.connections = {}
        self.visited = False
        self.parents = []
    
    #Function to add a connection (edge) between 2 nodes that contains a capacity and flow.
    def add_connection(self, toAdd, capacity):
        self.connections[toAdd] = {
            'capacity': capacity,
            'flow': 0
        }

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_visited(self, boolean):
        self.visited = boolean


#Function to generate network dictionary of size n.
def generate_network(n):

    nodes = {}

    #Create new nodes and add to dictionary.
    for i in range(1, n + 1):
        nodes[i] = Node(i)
    
    
    
    for node in nodes:
        #(n//2) ensuring integer division
        num_connections = random.randint(1, (n//2) + 1) 
        
        available_nodes = dict(nodes)

        #Ensures we dont create a self loop during initialization
        del available_nodes[node]

        for _ in range(num_connections): 

            to_add = random.choice(list(available_nodes.keys()))

            #Generating random capcity thats no more than 5
            capacity = random.randint(1, 6)

            nodes[node].add_connection(to_add, capacity)
            
            #Now we set the parent of toAdd to indicate the direction of flow.
            nodes[to_add].add_parent(node)

            del available_nodes[to_add]
        
    return nodes


nodes = generate_network(6)

for node_id, node in nodes.items():
        print(f"Node {node_id}:")
        
        for edges, edge_data in node.connections.items():

            capacity = edge_data['capacity']
            flow = edge_data['flow']
            print(f"\tConnected to Node {edges}, Capacity: {capacity}, Flow: {flow}")



print("Breakpoint ting")




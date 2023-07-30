import random
#Representing the flow network
#Node class

#GLOBAL VARIABLES 
#Algorithm iterations
iterations = 0

#Program running flag
running = False

class Node:

    def __init__(self, ID):
        self.ID = ID
        self.connections = {}
        self.connections_total = 0
        self.visited = False
        self.children = []
        self.sink = False
        self.source = False

    #Adding a connection models adding an edge between 2 nodes that contains a capacity and flow.
    def add_connection(self, toAdd, capacity):

        if toAdd.ID in self.connections or self.ID in toAdd.connections:
         print(f"The connection between {self.ID} and {toAdd.ID} already exists." )

        else:
            self.connections[toAdd] = {
                'node': toAdd,
                'capacity': capacity,
                'flow': 0
            }

        self.connections_total += 1
        self.add_child(toAdd)

    def add_child(self, child):
        self.children.append(child)

    def set_visited(self, boolean):
        self.visited = boolean


#Function to generate network dictionary of size n.
def generate_network(n):

    nodes = {}

    #Create new nodes and add to dictionary.
    for i in range(1, n + 1):
        nodes[i] = Node(i)

    #Set the source and sink node.
    nodes[1].source = True
    nodes[len(nodes)].sink = True

    #Function END

    return generate_connections2(nodes, n)

def generate_connections2(nodes, n):
            #for each node we need to do a couple things.
            #generate 1 - 3 connections
            #Check if the node is a sink or source node
            #get the available nodes that can the node can be connected to
            #randomly pick a node.
            #create the connection

    for node in nodes.values():

        if node.source == True:
            num_connections = random.randint(1 ,(n//2))
            available_nodes = dict(nodes)
            
            #Delete current node to avoid self loop
            #Delete sink node (i dont want a direct connection)
            del available_nodes[1]
            del available_nodes[n]

            for _ in range(num_connections):
                to_Add = random.choice(list(available_nodes.keys()))
                capacity = random.randint(1,5)

                node.add_connection(nodes[to_Add], capacity)


                #Source node will have children
                #node.add_child(nodes[to_Add])

        elif node.sink == True:
            #Generate no connections. Connections model the direction. So if sink node has 
            #0 connections, it means it has 0 outwards directions, only receiving input.
            pass
            
        else:
            #Current node is neither sink nor source.
            #A non-sink/source node can have a no. of connections equal to half of the total nodes
            #excluding source and sink nodes

            num_connections = random.randint(1, ((n-1) // 2))
            available_nodes = dict(nodes)
            
            del available_nodes[1]
            del available_nodes[node.ID]

            for _ in range(num_connections):
                to_Add = random.choice(list(available_nodes.keys()))

                
                capacity = random.randint(1,5)

                node.add_connection(nodes[to_Add], capacity)

                
                #node.add_child(nodes[to_Add])

    return nodes
        





def generate_connections(nodes, n):
        
        for node in nodes:
            #for each node we need to do a couple things.
            #generate 1 - 3 connections
            #Check if the node is a sink or source node
            #get the available nodes that can the node can be connected to
            #randomly pick a node.
            #create the connection

            #(n//2) ensuring integer division
            num_connections = random.randint(1,4)
            sourceFlag = True if nodes[node].source  == True else False
            sinkFlag = True if nodes[node].sink == True else False
            available_nodes = dict(nodes)

            #Ensures we dont create a self loop during initialization
            del available_nodes[node]

            #Check if current node is a source or sink node
            if nodes[node].source == True:

                for _ in range(num_connections):

                    key_picked = random.choice(list(available_nodes.keys()))
                    to_Add = nodes[key_picked]
                    capacity = random.randint(1, 6)

                    nodes[node].add_connection(to_Add, capacity)
                    
                    #Source nodes will have children, but can not be a child. Until algorithm starts.
                    nodes[node].add_child(to_Add)

            elif nodes[node].sink == True:
                
                #if the num_connections to 
                if num_connections > 1:
                
                    pass



            else:
                for _ in range(num_connections): 

                    #I should include a generate connections function.
                    #Generate network function is growing  too large.

                    key_picked = random.choice(list(available_nodes.keys()))
                    to_Add= nodes[key_picked]

                    #Generating random capcity thats no more than 5
                    capacity = random.randint(1, 6)
                    nodes[node].add_connection(to_Add, capacity)
                    
                    #Add children nodes
                    nodes[node].add_child(to_Add)

                del available_nodes[key_picked]

        return nodes

#Function sets random connections for sink node.
def set_connection_sink(nodes, node, random):
    
    rand = random

    if node.sink == True:
        pass
    else:
        print("No sink node detected")





#Function to print nodes info, takes a dictionary of nodes as the argument.
def print_Node_info(x):

    for node_id, node in x.items():
       
        print(f"Node {node.ID}", (" (source node)") if node.source else " (sink node)" if node.sink else "")
            
        for node_id, node_data in node.connections.items():
            capacity = node_data['capacity']
            flow = node_data['flow']
            print(f"\tConnected to Node {node_id.ID}, Capacity: {capacity}, Flow: {flow}")

        message = ""

        if len(node.children) == 0:
            print(" No children")
        else:
            for i in range(1, len(node.children)):
                message += str(node.children[i].ID)

            print(" Children: ", len(node.children))
    

#Main code

random.seed(67)
nodes = generate_network(5)
print_Node_info(nodes)



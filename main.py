import queue
import time
import networkx as nx
import matplotlib.pyplot as plt


def bfs(graph, start):
    """Retrieve the Breadth First Search order for a graph.
    
    Parameters
    ----------
    graph : A networkx graph
    
    start : Node
    
    """
    visited = set()
    que = queue.Queue() #intialize 'FIFO' queue
    que.put(start)
    order = []
    
    while not que.empty():
        vertex = que.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    que.put(node)
    return order

def dfs(graph, start, visited = None):
    """Retrieve the Depth First Search order for a graph.
    
    Parameters
    ----------
    graph : A networkX graph
    
    start : Node
    
    visited: set or None (default)
    """
    if visited is None:
        visited = set()
    order = []
    
    if start not in visited:
        order.append(start)
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                order.extend(dfs(graph, node, visited))
    return order
                       
def visualize_search(goal, order, title, graph, positions):
    """Create the visualization for the graph.
    
    Parameters
    ----------
    goal : integer
        The value that the user is searching for
    order : list
        Retrieved from running dfs or bfs
    
    title: string
        the title label for the graph
    
    graph: A networkX graph
    
    positions: A dictionary with nodes as keys and positions as values.
        the positions on the plot for each node
    """
    plt.figure() # initialize plot
    plt.title(title) # title of the graph
    for i, node in enumerate(order, start = 1):
        plt.clf() # clear and begin to update graph
        plt.title(title) # title of the graph
        nx.draw(graph, positions, with_labels=True, node_color=['g' if (n == node and n == goal) else 'r' if  n == node else 'y' for n in graph.nodes])
        plt.draw()
        plt.pause(2.0) # amount of time between each step
        if node == goal: # search is complete 
            break
    plt.show()


def generateGraph(nodes, edges):
    """Generate the graph. Returns a networkX graph.
    
    Parameters
    ----------
    nodes : integer
        The number of nodes in the graph
    edges : integer
        The number of edges in the graph
    
    Notes
    -----
    gnm_random_graph : 
        returns an arbitrary graph based on # nodes and edges determined by the user.
    is_connected: returns boolean
        returns True if the graph is well-connected
    """
    # brute force the intial graph generation
    while True:
        graph = nx.gnm_random_graph(nodes, edges) #
        if nx.is_connected(graph): #verify that the generated graph is well-connected
            return graph

def main(): 
    nodes = int(input("Enter the number of nodes: "))
    while True:
        try:
            edges = int(input(f"Enter the number of edges: "))
            if edges >= (nodes-1): # verify # of edges is appropiate with # of nodes
                break  # Exit the loop if the input is valid
            else:
                print("Please enter a valid number of edges.") #edge entry was not valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    graph = generateGraph(nodes, edges) # brute force until graph connects
    positions = nx.spring_layout(graph) # automatically determine position of node on the plot

    search = input(f"Enter the search algorithm (BFS or DFS): ").upper()
    print(f"* * Reminder: Your nodes are in range({nodes}) * *")
    goal = int(input(f"What Node would you like to search for? : "))
    
    if search == "BFS":
        visualize_search(goal, bfs(graph, 0), 'BFS Visualization', graph, positions)
        time.sleep(1.0)
    elif search == "DFS":
        visualize_search(goal, dfs(graph, 0), 'DFS Visualization', graph, positions)
        time.sleep(1.0)


if __name__ == "__main__":
    while True:
            main()
            user_input = input("Do you want to restart? (YES/NO): ")
            if user_input.upper() != "YES":
                break
from collections import defaultdict
from collections import deque
from queue import Queue, PriorityQueue
import sys

graph = defaultdict(list)
argv= sys.argv
def addEdge(graph, u, v):
    graph[u].append(v)

if(len(sys.argv)!= 2):
    print("You must enter a .txt file ..!")
    sys.exit(1)

if(str(sys.argv[1]).endswith(".txt") != True):
    print("Your input file must be .txt format !!!")
    sys.exit(1)

file = open(argv[1],'r')
nodes = []
nodes_neighbours = []
for line in file :
    nodes.append(line[0])
    for i in range(3,len(line),5):
            if line[i+2] != '0':
                nodes_neighbours.append(line[i])

    for x in nodes_neighbours:
        addEdge(graph,nodes[0],x)
    nodes = []
    nodes_neighbours = []
file.close()

def BFS(graph, start, goal):
    if start == goal:
        return start

    queue = deque([start])
    parent = {}
    parent[start] = start

    while queue:
        currentNode = queue.popleft()
        for neighbor in graph[currentNode]:
            if neighbor == goal:
                parent[neighbor] = currentNode
                return print_path(parent, neighbor, start)

            if neighbor not in parent:
                parent[neighbor] = currentNode
                queue.append(neighbor)
    return None


def print_path(parent, goal, start):
    path = [goal]
    while goal != start:
        goal = parent[goal]
        path.insert(0, goal)
    return path


def DFS(graph, start, goal):

    path_list = [[start]]
    while path_list:

        path = path_list.pop()

        last_node = path[-1]
        if last_node == goal:
            return path

        else:
            for node in graph[last_node]:
                if node not in path:

                    new_path = path + [node]

                    path_list.append(new_path)

    print('No path exists between %s and %s' % (start, goal))

def addEdgewithCost(graph, node , values):
    graph[node] = values

file = open(argv[1],'r')
graphForUCS = {}
for line in file.readlines() :
    nodes = []
    nodes.append(line[0])
    line = line.rstrip('\n')
    line = line[3:-1]
    nodes_neighbours = []
    for element in line.split(",") :
        element = element.strip()
        if element[2] != "0" :
            nodes_neighbours.append(element)


    addEdgewithCost(graphForUCS , nodes[0] , nodes_neighbours)
file.close()



def UCS(graph, start,goal):
	queue = [(0,[start])]
	visited = set()
	while queue:
		path = queue.pop(0)
		vertex = path[1][-1]
		if vertex == goal:
			return path[1]
		elif vertex not in visited:
			for current_neighbour in graph.get(vertex, []):
				new_path = list(path[1])
				new_path.append(current_neighbour[0])
				new_path = (path[0] + int(current_neighbour[2]), new_path)
				queue.append(new_path)
			queue.sort(key= lambda x:x[0])
			visited.add(vertex)
	return 0

start_node = str(input("Please enter the start state : "))
goal_node = str(input("Please enter the goal state : "))


bfs_result = BFS(graph,start_node.upper(),goal_node.upper())
dfs_result = DFS(graph, start_node.upper(), goal_node.upper())
ucs_result = UCS(graphForUCS,start_node.upper(),goal_node.upper())
if(bfs_result is None ):
    print("There is no path between",start_node.upper(),"and",goal_node.upper())
else :
    if bfs_result is not None :
        print("BFS :",' - '.join(map(str,bfs_result)))


    if dfs_result is not None :
        print("DFS :",' - '.join(map(str, dfs_result)))


    if ucs_result is not None :
        print("UCS :",' - '.join(map(str,ucs_result)))


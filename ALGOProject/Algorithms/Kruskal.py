from collections import defaultdict
import copy

# A utility function to find set of an element i 
# (uses path compression technique) 
def find(parent, i): 
	if parent[i] == i: 
		return i 
	return find(parent, parent[i]) 

# A function that does union of two sets of x and y 
# (uses union by rank) 
def union(parent, rank, x, y): 
	xroot = find(parent, x) 
	yroot = find(parent, y) 

	# Attach smaller rank tree under root of 
	# high rank tree (Union by Rank) 
	if rank[xroot] < rank[yroot]: 
		parent[xroot] = yroot 
	elif rank[xroot] > rank[yroot]: 
		parent[yroot] = xroot 

	# If ranks are same, then make one as root 
	# and increment its rank by one 
	else : 
		parent[yroot] = xroot 
		rank[xroot] += 1

def kruskal(V, G, initial_node):
	graph = copy.deepcopy(G)
	result =[] #This will store the resultant MST
	i = 0 # An index variable, used for sorted edges 
	e = 0 # An index variable, used for result[] 
	graph = sorted(graph,key=lambda item: item[2])
	parent = [] ; rank = [] 
	# Create V subsets with single elements 
	for node in range(V): 
		parent.append(node) 
		rank.append(0) 
	# Number of edges to be taken is equal to V-1 
	while e < V - 1 : 
		# Step 2: Pick the smallest edge and increment 
				# the index for next iteration 
		u,v,w = graph[i]
		i = i + 1
		x = find(parent, u) 
		y = find(parent ,v) 
		# If including this edge does't cause cycle, 
			# include it in result and increment the index 
			# of result for next edge 
		if x != y: 
			e = e + 1	
			result.append([u,v,w]) 
			union(parent, rank, x, y)

	total_cost = 0			
	for i in range(len(result)):
		total_cost += result[i][-1]

	result.append(round(total_cost,2))
	
	return result
import numpy as np


# Function to check if goal state solvable or not
def solvable(node):
	node = list(np.reshape(node,9))
	node = [x1 for x1 in node if x1!=0]
	count2 = 0
	for i in range(0, len(node)):
		node2 = node[i]
		count1 = 0
		for j in range(i, len(node)):
			if node[j]< node2:
				count1= count1+1
			count2 = count2 + count1
	if count2%2 == 0:
		return True
	else:
		return False
	
# Function to find the index of the blank tile for a given state
def blank_tile_location(node):
	node_state = node
	for i in range(len(node_state)):
		for j in range(len(node_state[i])):
			if node_state[i][j] == 0:
				print('The Start Point for Blank tile is: ', (i,j))
				return (i,j)
			else:
				continue

# Functions to move in up,down,left & right directions
def action_move_left(k1, i, j):
	node_state = k1
	action = 'Move left'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j-1] = current_node[i][j-1], current_node[i][j]
	print('Moved Left')
	return action, parent_node, current_node
	

def action_move_right(k2, i, j):
	node_state = k2
	action = 'Move right'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j+1] = current_node[i][j+1], current_node[i][j]
	print('Moved Right')
	return action, parent_node, current_node
	

def action_move_up(k3, i, j):
	node_state = k3
	action = 'Move up'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i-1][j] = current_node[i-1][j], current_node[i][j]
	print('Moved Up')
	return action, parent_node, current_node
	

def action_move_down(k4, i, j):
	node_state = k4
	action = 'Move down'
	parent_node = node_state.copy() 
	current_node = node_state.copy()
	current_node[i][j], current_node[i+1][j] = current_node[i+1][j], current_node[i][j]
	print('Moved Down')
	return action, parent_node, current_node



# Function that checks if node is new and adds it to the explored nodes

def add_node(node_state, parent_node, action):
	global k 
	print('k is:', k)
	# Checks if node is new or not
	for i in range(len(explored_nodes.values())):
		if (node_state == explored_nodes[i][0]).all():
			print('Not a new node')
			return
		else:
			continue
	k = k+1
	explored_nodes[k] = [node_state, parent_node, action]
		

# Function to generate the childs of a given node
def child_generator(node):
	
	child_nodes = []
	i,j = blank_tile_location(node)
	if j>0 and j<=2:
		a1, p1, c1= action_move_left(node, i, j)
		add_node(c1, p1, a1)
		child_nodes.append(c1)
	if j>=0 and j<2:
		a2, p2, c2= action_move_right(node, i, j)
		add_node(c2, p2, a2)
		child_nodes.append(c2)
	if i>0 and i<=2:
		a3, p3, c3= action_move_up(node, i, j)
		add_node(c3, p3, a3)
		child_nodes.append(c3)
	if i>=0 and i<2:
		a4, p4, c4= action_move_down(node, i, j)
		add_node(c4, p4, a4)
		child_nodes.append(c4)

	return child_nodes

# Function to backtrack from a given node
def backtrack(node_ind):
	path = [explored_nodes[node_ind][0]]
	while node_ind > 0:
		parent = explored_nodes[node_ind][1]
		path.insert(0, parent)
		for i in range(len(explored_nodes.values())):
			if (parent == explored_nodes[i][0]).all():
				parent_key = i
			else:
				continue
		node_ind = parent_key
		print('Node_ind is:', node_ind)
	return path


# Asking the user to enter the start node
node_state_1 = []
bfs = []
k= 0
glob = False
explored_nodes = {}
print('Enter the start node elementwise in row order: ')
for i in range(0, 3):
	ele = [int(input()), int(input()), int(input())]
	node_state_1.append(ele)

node_state_1 = np.array(node_state_1)

print('The start node you entered is: ', node_state_1)
print(' ')

# Specify the goal node here
goal_node = np.array([[1,2,3], [4,5,6], [7,8,0]])
print('The goal node to reach is: ', goal_node)
print('')

status = solvable(node_state_1)

if status == True:
	print('The node state can be solved')
	# Displaying the start node info
	explored_nodes = {k: [node_state_1,np.zeros((3,3)), 'None']}
	print('The start node info is: ', explored_nodes)
	print('')


	# Brute Force Search
	bfs.append(node_state_1)

	while len(bfs) > 0:
		c1 = bfs[0]
		print('c1 is:', c1)
		print('')
		bfs.pop(0)
		childs = child_generator(c1)
		for i in childs:
			bfs.append(i)
		if (c1 == goal_node).all():
			print('Goal node found!!')		
			break
	print('The explored nodes were:' , explored_nodes)
	print('')


	for i in range(len(explored_nodes.values())):
		if (goal_node == explored_nodes[i][0]).all():
			goal_key = i
		else:
			continue

	final_path= backtrack(goal_key)

	print('The Final Path is:', final_path)

	# Bag generated path to the nodePath.txt file

	file1 = open("nodePath.txt", "w")
	for node in final_path:
		node = np.array2string(np.reshape(node,9))
		file1.write(node[1:-1])
		file1.write("\n")

	file1.close()

	# Bag all explored states to the Nodes.txt file

	file2 = open("Nodes.txt", "w")
	 
	for node1 in explored_nodes.keys():
		node = np.array2string(np.reshape(explored_nodes[node1][0],9))
		file2.write(node[1:-1])
		file2.write("\n")

	file2.close()



	# Bag all node and parent node indexes to the Nodes.txt file

	file3 = open("NodesInfo.txt", "w") 

	for ni in explored_nodes.keys():
		ni = str(ni)
		indices = ni + ' 0'
		file3.write(indices)
		file3.write("\n")

	file3.close()

else:
	print('Sorry the goal state you entered is unsolvable')	
	
	
	
	




import numpy as np

# Function to find the index of the blank tile for a given state
def blank_tile_location(k):
	node_state = explored_nodes[k][0]
	for i in range(len(node_state)):
		for j in range(len(node_state[i])):
			if node_state[i][j] == 0:
				print('The Start Point for Blank tile is: ', (i,j))
				return (i,j)
			else:
				continue

# Functions to move in up,down,left & right directions
def action_move_left(k, i, j):
	node_state = explored_nodes[k][0]
	action = 'Move left'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j-1] = current_node[i][j-1], current_node[i][j]
	print('Moved Left')
	return action, parent_node, current_node
	

def action_move_right(k, i, j):
	node_state = explored_nodes[k][0]
	action = 'Move right'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j+1] = current_node[i][j+1], current_node[i][j]
	print('Moved Right')
	return action, parent_node, current_node
	

def action_move_up(k, i, j):
	node_state = explored_nodes[k][0]
	action = 'Move up'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i-1][j] = current_node[i-1][j], current_node[i][j]
	print('Moved Up')
	return action, parent_node, current_node
	

def action_move_down(k, i, j):
	node_state = explored_nodes[k][0]
	action = 'Move down'
	parent_node = node_state.copy() 
	current_node = node_state.copy()
	current_node[i][j], current_node[i+1][j] = current_node[i+1][j], current_node[i][j]
	print('Moved Down')
	return action, parent_node, current_node



# Function that checks if node is new and adds it to the explored nodes
def add_node(k5, node_state, parent_node, action):
	# Checks if node is new or not
	if (k5 in explored_nodes.keys()) == True:
		 print('Not a new node')
	else:
		explored_nodes[k5] = [node_state, parent_node, action]

# Brute Force Search Recursive Function
def child_generator(node_ind, k):
	global glob 
	glob = False
	child_nodes = []
	i,j = blank_tile_location(node_ind)
	if j>0 and j<=2:
		a1, p1, c1= action_move_left(node_ind, i, j)
		if np.array_equal(c1, goal_node) == True:
			glob == True
		k = k+1
		i1 = k
		add_node(i1, c1, p1, a1)
		child_nodes.append(i1)
	if j>=0 and j<2:
		a2, p2, c2= action_move_right(node_ind, i, j)
		if np.array_equal(c2, goal_node) == True:
			glob == True
		k = k+1
		i2 = k
		add_node(i2, c2, p2, a2)
		child_nodes.append(i2)
	if i>0 and i<=2:
		a3, p3, c3= action_move_up(node_ind, i, j)
		if np.array_equal(c3, goal_node) == True:
			glob == True
		k = k+1
		i3 = k
		add_node(i3, c3, p3, a3)
		child_nodes.append(i3)
	if i>=0 and i<2:
		a4, p4, c4= action_move_down(node_ind, i, j)
		if np.array_equal(c4, goal_node) == True:
			glob == True
		k = k+1
		i4 = k
		add_node(i4, c4, p4, a4)
		child_nodes.append(i4)

	parent_child[node_ind] = child_nodes
	return parent_child, k, glob

# Asking the user to enter the start node
node_state_1 = []
global k 
i2_count = 1
k=0
parent_child = {}
print('Enter the start node elementwise in row order: ')
for i in range(0, 3):
	ele = [int(input()), int(input()), int(input())]
	node_state_1.append(ele)

node_state_1 = np.array(node_state_1)

print('The start node you entered is: ', node_state_1)
print(' ')

goal_node = np.array([[1,2,3], [4,5,6], [7,8,0]])
print('The goal node to reach is: ', goal_node)
print('')

# Displaying the start node infooal
explored_nodes = {k: [node_state_1, 'None', 'None']}
print('The start node info is: ', explored_nodes)
print('')

PC, kx, glob = child_generator(k, k)

print('The explored indices are:', PC)
# Brute Force Search

PC_len = len(PC.keys())

while glob == False:
	start = list(PC.keys())[0]		
	#print('Start is:', start)
	for i in range(start,PC_len):
		if i2_count == int(2):
			break		
		print('I is:', i == 2)
		for j in parent_child[i]:
			print('J is:', j)
			PC, kx, glob = child_generator(j,kx)
		print('Depth till now:', parent_child)
		print('')
		if i == 2:
			i2_count = int(i2_count+1)

	key = list(PC.keys())
	del PC[key[0]]
	#print (PC)
	PC_len = len(PC.keys())
	#print(PC_len)

		
print('Goal node found!!')
 	
	
	
	
	




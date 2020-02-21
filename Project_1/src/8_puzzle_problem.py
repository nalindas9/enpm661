import numpy as np

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
def action_move_left(k, i, j):
	node_state = k
	action = 'Move left'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j-1] = current_node[i][j-1], current_node[i][j]
	print('Moved Left')
	return action, parent_node, current_node
	

def action_move_right(k, i, j):
	node_state = k
	action = 'Move right'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j+1] = current_node[i][j+1], current_node[i][j]
	print('Moved Right')
	return action, parent_node, current_node
	

def action_move_up(k, i, j):
	node_state = k
	action = 'Move up'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i-1][j] = current_node[i-1][j], current_node[i][j]
	print('Moved Up')
	return action, parent_node, current_node
	

def action_move_down(k, i, j):
	node_state = k
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
def child_generator(node):	
	child_nodes = []
	i,j = blank_tile_location(node)
	if j>0 and j<=2:
		a1, p1, c1= action_move_left(node, i, j)
		#add_node(i1, c1, p1, a1)
		child_nodes.append(c1)
	if j>=0 and j<2:
		a2, p2, c2= action_move_right(node, i, j)
		#add_node(i2, c2, p2, a2)
		child_nodes.append(c2)
	if i>0 and i<=2:
		a3, p3, c3= action_move_up(node, i, j)
		#add_node(i3, c3, p3, a3)
		child_nodes.append(c3)
	if i>=0 and i<2:
		a4, p4, c4= action_move_down(node, i, j)
		#add_node(i4, c4, p4, a4)
		child_nodes.append(c4)

	return child_nodes

# Asking the user to enter the start node
node_state_1 = []
bfs = []
global k 
glob = False
i2_count = []
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

# Displaying the start node info
explored_nodes = {k: [node_state_1, 'None', 'None']}
print('The start node info is: ', explored_nodes)
print('')

# Brute Force Search
bfs.append(node_state_1)

while len(bfs) > 0:
	c1 = bfs[0]
	print('c1 is:', c1)
	print('')
	if (c1 == goal_node).all():
		break
	else:
		bfs.pop(0)
		childs = child_generator(c1)
		for i in childs:
			bfs.append(i)
	
	




"""
while glob == False:
	#print('PC keys:',list(PC.keys()))
	#print('Hello!!!!!!!!!!!')
	#print('Explored Nodes:', explored_nodes.keys())
	start = list(PC.keys())[0]		
	#print('Start is:', start)
	for i in range(start,PC_len):		
		if (explored_nodes[i][0] == goal_node).all():
			glob == True
		print('I is:', i)
		if (i in parent_child.keys()) == True:		
			for j in parent_child[i]:
				PC, kx= child_generator(j,kx)
			print('Depth till now:', parent_child)
			print('')
		else:
			print('Sorry key does not exist')
			continue
	key = list(PC.keys())
	del PC[key[0]]
	#print (PC)
	PC_len = len(PC.keys())
	#print(PC_len)
"""
		
print('Goal node found!!')
 	
	
	
	
	




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
def action_move_left(k):
	i,j = blank_tile_location(k)
	node_state = explored_nodes[k][0]
	action = 'Move left'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j-1] = current_node[i][j-1], current_node[i][j]
	print('Moved Left')
	k=k+1
	return action, parent_node, current_node, k
	

def action_move_right(k):
	i,j = blank_tile_location(k)
	node_state = explored_nodes[k][0]
	action = 'Move right'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i][j+1] = current_node[i][j+1], current_node[i][j]
	print('Moved Right')
	k=k+1	
	return action, parent_node, current_node, k
	

def action_move_up(k):
	i,j = blank_tile_location(k)
	node_state = explored_nodes[k][0]
	action = 'Move up'
	parent_node = node_state.copy()
	current_node = node_state.copy()
	current_node[i][j], current_node[i-1][j] = current_node[i-1][j], current_node[i][j]
	print('Moved Up')
	k=k+1
	return action, parent_node, current_node, k
	

def action_move_down(k):
	i,j = blank_tile_location(k)
	node_state = explored_nodes[k][0]
	action = 'Move down'
	parent_node = node_state.copy() 
	current_node = node_state.copy()
	current_node[i][j], current_node[i+1][j] = current_node[i+1][j], current_node[i][j]
	print('Moved Down')
	k=k+1	
	return action, parent_node, current_node, k



# Function that checks if node is new and adds it to the explored nodes
def add_node(k, node_state, parent_node, action):
	# Checks if node is new or not
	if (k in explored_nodes.keys()) == True:
		 print('Not a new node')
	else:
		explored_nodes[k] = [node_state, parent_node, action]

# Brute Force Search Recursive Function
def BFS(k):
	final_node = explored_nodes[k][0]
	

	if np.array_equal(final_node, goal_node) == True:
		print('Goal Node found!!')
		return 1

	if j >= 0 and j <= 2 and i >= 1 and i<=2:
			a1, p1, c1, k1 = action_move_up(k)
			explored_nodes[k1] = [c1, p1, a1]
			BFS(k1)
	else:
			print('Sorry! Out of bounds')

	if j >= 0 and j <= 2 and i >= 0 and i<=1:
			a2, p2, c2, k2 = action_move_down(k)
			explored_nodes[k2] = [c2, p2, a2]
			BFS(k2)
	else:
			print('Sorry! Out of bounds')

	if j >= 0 and j <= 1 and i >= 0 and i<=2:
			a3, p3, c3, k3 = action_move_right(k)
			explored_nodes[k3] = [c3, p3, a3]
			BFS(k3)
	else:
			print('Sorry! Out of bounds')

	if j >= 1 and j <= 2 and i >= 0 and i<=2:
			a4, p4, c4, k4 = action_move_left(k)
			explored_nodes[k4] = [c4, p4, a4]
			BFS(k4)
	else:
			print('Sorry! Out of bounds')
	
	
	

# Asking the user to enter the start node
node_state_1 = []
k = 0
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

i,j = blank_tile_location(k)

# Brute Force Search
BFS(k)
	
	
	




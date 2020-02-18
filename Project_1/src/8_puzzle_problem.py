# Function to find the index of the blank tile for a given state
def blank_tile_location(node_state):
	for i in range(len(node_state)):
		for j in range(len(node_state[i])):
			if node_state[i][j] == 0:
				return (i,j)
			else:
				continue

# Functions to move in up,down,left & right directions
def action_move_left(node_state):
	i,j = blank_tile_location(node_state)
	if j >= 1 and j <= 2 and i >= 0 and i<=2:
		node_state[i][j], node_state[i][j-1] = node_state[i][j-1], node_state[i][j]
		print('Moved Left')	
	else:
		print('Sorry! Out of bounds')
	return node_state

def action_move_right(node_state):
	i,j = blank_tile_location(node_state)
	if j >= 0 and j <= 1 and i >= 0 and i<=2:
		node_state[i][j], node_state[i][j+1] = node_state[i][j+1], node_state[i][j]
		print('Moved Right')	
	else:
		print('Sorry! Out of bounds')
	return node_state

def action_move_up(node_state):
	i,j = blank_tile_location(node_state)
	if j >= 0 and j <= 2 and i >= 1 and i<=2:
		node_state[i][j], node_state[i-1][j] = node_state[i-1][j], node_state[i][j]
		print('Moved Up')	
	else:
		print('Sorry! Out of bounds')
	return node_state

def action_move_down(node_state): 
	i,j = blank_tile_location(node_state)
	if j >= 0 and j <= 2 and i >= 0 and i<=1:
		node_state[i][j], node_state[i+1][j] = node_state[i+1][j], node_state[i][j]
		print('Moved Down')	
	else:
		print('Sorry! Out of bounds')		
	return node_state

def add_node(parent_node, node_state, k):
	# Checks if node is new or not
	if ([node_state, parent_node] in explored_nodes.values()) == True:
		 print('Not a new node')
	else:
		k=k+1
		explored_nodes[k] = [node_state, parent_node]

	
# Asking the user to enter the start node
node_state_1 = []
k = 0
parent_nodes = []
print('Enter the start node elementwise in row order: ')
for i in range(0, 3):
	ele = [int(input()), int(input()), int(input())]
	node_state_1.append(ele)

print('The start node you entered is: ', node_state_1)
print(' ')

# Displaying the start node info
explored_nodes = {k: [node_state_1, 'None']}
print('The start node info is: ', explored_nodes)
print('')

i,j = blank_tile_location(node_state_1)

print('The blank tile in the start node is at:', (i, j))

p1 = node_state_1[:]   # Change to np.array ,, list not working for shallow copy. Also return parent nodes in action functions itself
parent_nodes.append(p1)

c1 = action_move_down(node_state_1)
print('')
add_node(parent_nodes[k], c1, k)

print('Explored nodes after action are: ', explored_nodes)


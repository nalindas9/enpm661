def blank_tile_location(node_state):
	for i in range(len(node_state)):
		for j in range(len(node_state[i])):
			if node_state[i][j] == 0:
				return (i,j)
			else:
				continue



# Asking the user to enter the start node
node_state_1 = []
n = int(input('Enter the start node elementwise in row order: '))
for i in range(0, 3):
	ele = [int(input()), int(input()), int(input())]
	node_state_1.append(ele)

print('The start node you entered is: ', node_state_1)
print(' ')

# Displaying the start node info
explored_nodes = {1: [node_state_1, 'None']}
print('The start node info is: ', explored_nodes)
print('')

i,j = blank_tile_location(node_state_1)

print('The blank tile in the start node is at:', (i, j))


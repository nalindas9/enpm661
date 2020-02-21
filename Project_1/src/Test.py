import numpy as np

current_node = np.array([[1,2,3], [4,5,6], [7,8,0]])
goal_node = np.array([[1,2,3], [4,5,6], [7,8,0]])

if (current_node == goal_node).all():
	print('Goal Found')
else:
	print ('Not found')




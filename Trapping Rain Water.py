# Trapping Rain Water
# from https://www.geeksforgeeks.org/trapping-rain-water/

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

w = len(arr)
h = max(arr)
container = [ [ '0' for i in range(w) ] for j in range(h) ]
container.append(['#']*w)

print (str(arr) + '\n')

def displayContainer():
	for i in container:
		print (i)
	print ()

for i in range(0, w):
	if(arr[i] != 0):
		for n in range(h, h-arr[i]-1, -1):
			container[n][i] = '#'

displayContainer()

def fillContainer(row):
	left, right = -1, -1
	for i in range(0, len(row)):
		if(row[i]=='#'):
			left = i
			break
	for i in range(len(row)-1, 0-1, -1):
		if(row[i]=='#'):
			right = i
			break
	if(left==-1 or right==-1 or left==right):
		return row
	else:
		for i in range(left, right):
			if(row[i]=='0'):
				row[i] = 'w'
		return row


for i in range(0, len(container)-1):
	container[i] = fillContainer(container[i])

displayContainer()

print (sum(row.count('w') for row in container))

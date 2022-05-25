from collections import defaultdict

boards = [["5","3",".",".","7","7",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".","2","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]





def testB(boards):
	row = defaultdict(set)
	col = set()
	boxes = set()
	for x in range(9):
		for y in range(9):
			print(boards[x][y])
			if boards[x][y] == '.':
				continue
			if boards[x][y] in row[x]:
				print("dublicat found")
				# return False
			row[x].add(boards[x][y])
			print(row)
	return True

print(testB(boards))
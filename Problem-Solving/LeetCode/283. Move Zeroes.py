def rzero(a):
	temp = a
	for x in a:
		if x==0:
			temp.remove(x)
			temp.append(x)
	return temp



print(rzero([0,1,0,3,12]))

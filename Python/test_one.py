import pysnooper

@pysnooper.snoop()
def sam(x,y):
	return x+y

sam(2,4)
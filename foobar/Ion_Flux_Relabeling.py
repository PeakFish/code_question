
#def answer(h, q):
    # your code here

i = 0
#topVal = -1
output = []
j = 0

class Node:
	"""docstring for Node"""
	def __init__(self, val, lc, rc):
		#super(Node, self).__init__()
		self.lc = lc
		self.rc = rc
		self.val = val

def answer(h, q):
	global i
	global output
	global j
	# your code here
	output = []
	i = 0
	j = 0
	h -= 1
	treeroot = Node(0, None, None)

	def add(n):
		if(n.lc):
			add(n.lc)
		else:
			n.lc = Node(0, None, None)

		if(n.rc):
			add(n.rc)
		else:
			n.rc = Node(0, None, None)

	def postOrderWrite(n):
		global i
		if(n):
			postOrderWrite(n.lc)
			postOrderWrite(n.rc)
			i = i + 1
			n.val = i

	def getOne(n):
		global output
		global j
		if(n.lc and n.rc):
			lc = n.lc
			rc = n.rc
			getOne(n.lc)
			getOne(n.rc)
			if(lc.val == o[j] or rc.val == o[j]):
				output.append(n.val)
				j += 1


	b = sorted(enumerate(q), key=lambda x:x[1])

	o = sorted(q)

	print(q)
	print(o)
	print(b)

	#构建二叉树
	while(h > 0):
		h -= 1
		add(treeroot)
	#后续添加数字
	postOrderWrite(treeroot)
	#计算结果
	getOne(treeroot)
	print(output)
	#重新排序
	#ii = 0
	#while(ii < len(q)):
	#	q[b[ii][0]] = output[ii]
	#	ii += 1

	return q

#1 2 3 4 7
print(answer(3, [3,4,1,7,2]))

raw_input()

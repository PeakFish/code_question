i = 0
output = []
j = 0

class Node:
	def __init__(self, val, lc, rc, p):
		#super(Node, self).__init__()
		self.lc = lc
		self.rc = rc
		self.val = val
		self.p = p

def answer(h, q):
	global i
	global output
	global j
	output = []
	i = 0
	j = 0
	h -= 1
	treeroot = Node(0, None, None, None)

	def add(n):
		if(n.lc):
			add(n.lc)
		else:
			n.lc = Node(0, None, None, n)

		if(n.rc):
			add(n.rc)
		else:
			n.rc = Node(0, None, None, n)

	def postOrderWrite(n):
		global i
		if(n):
			postOrderWrite(n.lc)
			postOrderWrite(n.rc)
			i = i + 1
			n.val = i

	def postOrderRead(n):
		global output
		global j
		if(n):
			postOrderRead(n.lc)
			postOrderRead(n.rc)
			if(n.val == o[j]):
				parent = n.p
				if(parent):
					output.append(parent.val)
				else:
					output.append(-1)
				j += 1
				if(j >= len(o)):
					j = len(o) - 1

	b = sorted(enumerate(q), key=lambda x:x[1])
	o = sorted(q)
	#构建二叉树
	while(h > 0):
		h -= 1
		add(treeroot)
	#后续添加数字
	postOrderWrite(treeroot)
	#计算结果
	postOrderRead(treeroot)
	#重新排序
	ii = 0
	while(ii < len(q)):
		q[b[ii][0]] = output[ii]
		ii += 1

	return q


print(answer(5, [19, 14, 28]))

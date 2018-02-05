import pycparser as pyc

class visitor(pyc.c_ast.NodeVisitor):

	def __init__(self, funcname):
		self.funcname = funcname

	
	def visit_ID(self, node):
		print node.name
	
	def visit_If(self,node):
		if node.cond.op == "=":
			print "WARNING"


	def visit_Assignment(self, node):
		print node.lvalue, node.rvalue, node.op
		v.visit(node.lvalue)
		v.visit(node.rvalue)


	def visit_FuncDef(self, node):
		print "hello"
		# print node.body
		for i in node.body:
			print "i=",i
			v.visit(i)


ast = pyc.parse_file("test1.c", use_cpp=True)
ast.show()
v = visitor("main")
v.visit(ast)


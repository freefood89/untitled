class BaseCommand():
	def __init__(self): pass
	def execute(self): pass

class NewCommand(BaseCommand):
	def __init__(self, fn, args=None):
		self.execute = fn
		self.args = args
		
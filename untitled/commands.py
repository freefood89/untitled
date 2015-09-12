class BaseCommand():
	def __init__(self): pass
	def execute(self): pass

class NewCommand(BaseCommand):
	def __init__(self, fn):
		self.execute = fn
		
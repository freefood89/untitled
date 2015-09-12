class CommandError(Exception):
	def __init__(self, value="Command Not Found"):
		self.value = value
	def __str__(self):
		return repr(self.value)

class CommandError(Exception):
	def __init__(self, keyword):
		self.value = "Command '%s' Not Found" % keyword
	def __str__(self):
		return repr(self.value)

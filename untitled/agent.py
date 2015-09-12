class Agent():
	def __init__(self):
		self.commands = dict()
		pass

	def register_command(self, keyword, cmd):
		self.commands[keyword] = cmd

	def call_command(self, cmd):
		cmd.execute()

	def call_by_keyword(self, keyword):
		self.commands[keyword].execute()

	def run(self):
		# begin IO loop
		pass





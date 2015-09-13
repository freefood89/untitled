from functools import wraps

from .commands import NewCommand
from .exceptions import CommandError

class Agent():
	def __init__(self):
		self.commands = dict()
		pass

	def register_command(self, keyword, cmd):
		self.commands[keyword] = cmd

	def register(self, keyword):
		def decorator(fn):
			cmd = NewCommand(fn)
			self.register_command(keyword, cmd)
			return fn
		return decorator

	def run_command(self, cmd, args=None):
		if args:
			cmd.execute(args)
		else:
			cmd.execute()

	def call_by_keyword(self, keyword, args=None):
		if keyword not in self.commands:
			raise CommandError(keyword)
		command = self.commands[keyword]
		self.run_command(command,args)

	def run(self):
		# TODO make IO loop nicer
		while True:
			command = input('>').split(' ')
			keyword = command[0]
			try:
				self.call_by_keyword(keyword, command)
			except CommandError as e:
				print(e)






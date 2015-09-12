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

	def run_command(self, cmd):
		cmd.execute()

	def call_by_keyword(self, keyword):
		if keyword not in self.commands:
			raise CommandError()
		self.commands[keyword].execute()

	def run(self):
		# TODO make IO loop nicer
		while True:
			keyword = input('>')
			self.commands[keyword].execute()






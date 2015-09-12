from untitled import Agent, NewCommand

agent = Agent()

def foo():
	print('foooooooo')

agent.call_command(NewCommand(foo))
agent.register_command('foo', NewCommand(foo))
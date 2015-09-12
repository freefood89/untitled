from untitled import Agent, NewCommand

agent = Agent()

def foo():
	print('foooooooo')

agent.run_command(NewCommand(foo))

agent.register_command('foo', NewCommand(foo))
agent.call_by_keyword('foo')

@agent.register('bar')
def bar():
	print('Que?')

agent.run()
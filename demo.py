import requests
import re

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

urlRegex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

@agent.register('google')
def google(args):
	if len(args) < 2:
		print('you forgot your search query')
		return
	r = requests.get('http://www.google.com/search?q=%s' % args[1])
	for link in re.findall(urlRegex, r.text):
		print(link)

@agent.register('echo')
def echo(args):
	if len(args) > 1:
		print(' '.join(args[1:]))


# @agent.register('echo')
# def echo():
# 	print()

agent.run()
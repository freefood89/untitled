# Untitled Module

This is my crappy attempt at creating a REPL loop framework... I'm trying to learn from [mitsuhiko/flask](https://github.com/mitsuhiko/flask). Also, this is a work in progress; if you somehow find this project and want to request a feature, please post an issue and apply the "enhancement" label.

## How To Use

```python
from untitled import Agent

agent = Agent()
@agent.register('knock-knock')
def respond():
	print("who's there?")

agent.run()

```

Look at demo.py for an example...
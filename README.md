# Untitled Module

This is my crappy attempt at creating a REPL loop framework... I'm learning from [mitsuhiko/flask](https://github.com/mitsuhiko/flask)

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
# WorkoutFromHomeBot

A Discord bot designed to help automate home workouts within a Discord server. 

## Development
 
To test this bot locally, you'll need to add the bot token as a local environment variable. To do this, create a file called `init.sh` similar to the following: 

```
#!/bin/bash

export DISCORD_TOKEN={discord token string}
```

replacing {discord token string} for the token value. Then, you can run `source ./init.sh` to populate your environment variables with the token value, after which the bot can run locally. 

To test the bot, simply run `python bot/main.py`, and issue commands in the Discord server. It may be useful to temporarily modify command names in your test code to prevent duplicate responses from the Heroku bot and your local instance.


## Deployment
This bot is deployed to Heroku, and will automatically update whenever changes are pushed to the mainline branch. 

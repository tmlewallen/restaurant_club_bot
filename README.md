# Restaurant Club Bot

This is a discord bot that runs on AWS Lambda with Url Invocations. It can also be run locally as a flask server to test locally. 

## Bot Dev Setup

In the `bot` directory, 
1. Make a virtual env (package targets >= python3.11)
1. Activate your virtual env
1. run `make`
1. If you want to run locally, rename `.env.sample` to `.env` and supply values to the keys in the file - see [Discord docs for how to fetch these](https://discord.com/developers/docs/quick-start/getting-started#fetching-your-credentials)

And start developing

```
cd bot
python3 -m venv .venv
source .venv/bin/activate
make
```

See `makefile` for other options. 

Note: In order to connect your local flask server to a public endpoint you'll need a tool like [ngrok](https://download.ngrok.com/downloads/mac-os)
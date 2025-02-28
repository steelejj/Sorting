# Instructions
This app uses docker to make it easier to run and interact with the app.

## Local
### Build
Build the docker image by running `./build.sh`

#### Run
There are two options for running.
Tests: `./run.sh --test`

Interactive (this can be used if you want to change things or investigate on the fly): `./run.sh --interactive`

## Repl
1. Install dependencies with `pip install -r requirements.txt` (assuming using pytest)
2. Set PYTHONPATH to the root of the repo
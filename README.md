# Concordance
Given an arbitrary text document written in English, the application will generate a concordance, i.e. an alphabetical list of all word occurrences, labeled with word frequencies and the _sentence_ numbers in which each occurrence appeared.

# Setup & Usage

1. `git clone https://github.com/dansheikh/concordance.git`

2. `git clone https://github.com/dansheikh/docks.git`

3. Within the "Sandbox" directory of the "docks" clone execute: `docker build -t concordance -f ubuntu/Dockerfile .`

4. Start container (in daemon mode) with: `docker run --rm -t -d -P -p 5432:5432 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/Downloads/concordance:/home/dev/Projects/concordance concordance`

5. Connect to running container with: `docker exec -u dev -it [container id] env TERM=xterm /bin/bash -l`

6. Launch application with: `/home/dev/Projects/concordance/app.py [corpus file path] [concordance (CSV) file path]`

__Notes__:

1. Above setup assumes `concordance.git` is cloned within `~/Downloads`
2. Concordance occurrence locations are zero-indexed

# Minimum Requirements

1. Python 3.6.0
2. NLTK 3.2.2

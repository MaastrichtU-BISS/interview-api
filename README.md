# BISS Interview API
## Running the server
First of all, `git pull` this repository, or download (and unzip) the code from the green 'Code' button. Then open a shell or CMD session and navigate to the folder containing these files.

### Running the server using Docker
Install Docker for your system from `https://www.docker.com/products/docker-desktop`, then `cd` a command line to the directory with this repository and run `docker build -t api-server .`. When this is done, the server can be run by running `docker run --rm -d -p 5001:5001 api-server`. Again, the server will now run on `http://localhost:5001/`.

### Running the server using Python
As a more unreliable alternative, the server can be run locally using Python. On a system with Python 3.5+ installed with Flask (in a virtual environment), the server can simply be run using `python api-server.py`. The server will then accept connections at `http://localhost:5001/`.

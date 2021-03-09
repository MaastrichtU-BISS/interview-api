# BISS Interview API

## Running the server

First of all, `git clone` this repository, or download (and unzip) the code from the green 'Code' button. Then open a shell or CMD session and navigate to the folder containing these files.

### Running the server using Docker

Install Docker for your system from `https://www.docker.com/products/docker-desktop`, then `cd` a command line to the directory with this repository and run `docker build -t api-server .`. When this is done, the server can be run by running `docker run --rm -d -p 5001:5001 api-server`. Again, the server will now run on `http://localhost:5001/`.

### Running the server using Python

As a more unreliable alternative, the server can be run locally using Python. On a system with Python 3.5+ installed with Flask (in a virtual environment), the server can simply be run using `python api-server.py`. The server will then accept connections at `http://localhost:5001/`.

## Using the API

The API is a very simple API just to handle some messaging and provide sample data. The following endpoints are available:

```GET http://localhost:5001/get_id/```
Generates and returns a unique ID to use for a visitor that fills out the questions/personal data. Used to uniquely link data retrieved at different steps in the process, and retrieve DIRECTOR results.

Example return data:

```JSON
{"id": "26aa5cd2-8750-4b22-ab86-1bbaad1aa14a"}
```

```POST http://localhost:5001/submit/<ID>```
Can be used to store any kind of JSON data related to an ID. Data should be provided in valid JSON format in the request's data. E.g. `http://localhost:5001/submit/26aa5cd2-8750-4b22-ab86-1bbaad1aa14a`
Will throw a 404 on a non-existent ID.

Example return data:

```JSON
{"status": "success", "id": "26aa5cd2-8750-4b22-ab86-1bbaad1aa14a"}
```

```GET http://localhost:5001/score/<ID>```
Generates (randomly generated) scores for a user's DIRECTOR scan. Every major category has an 'overall' score (slide 1) and 5 indicators for that category (slide 2). E.g. `http://localhost:5001/score/26aa5cd2-8750-4b22-ab86-1bbaad1aa14a`
Throws a 404 on a non-existent ID.

Example return data:

```JSON
{
  "id":"26aa5cd2-8750-4b22-ab86-1bbaad1aa14a",
  "scores":{
    "innovation":{
      "overall":2.5108952761799563,
      "indicators":{
        "indicator0":2.5108952761799563,
        "indicator1":1.964049985518833,
        "indicator2":1.5445006450465484,
        "indicator3":3.8587729237276607,
        "indicator4":3.213929566389628
      }
    },
    "capabilities":{
      "overall":1.5445006450465484,
      "indicators":{
        "indicator0":3.213929566389628,
        "indicator1":3.8587729237276607,
        "indicator2":1.5445006450465484,
        "indicator3":2.5108952761799563,
        "indicator4":1.964049985518833
      }
    },
    "strategy":{
      "overall":3.8587729237276607,
      "indicators":{
        "indicator0":1.964049985518833,
        "indicator1":2.5108952761799563,
        "indicator2":3.8587729237276607,
        "indicator3":1.5445006450465484,
        "indicator4":3.213929566389628
      }
    },
    "hrm":{
      "overall":3.213929566389628,
      "indicators":{
        "indicator0":1.964049985518833,
        "indicator1":1.5445006450465484,
        "indicator2":2.5108952761799563,
        "indicator3":3.213929566389628,
        "indicator4":3.8587729237276607
      }
    },
    "organization":{
      "overall":1.964049985518833,
      "indicators":{
        "indicator0":2.5108952761799563,
        "indicator1":1.964049985518833,
        "indicator2":3.213929566389628,
        "indicator3":3.8587729237276607,
        "indicator4":1.5445006450465484
      }
    }
  }
}
```

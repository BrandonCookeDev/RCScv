# RCScv 
A python, ReactJS based solution to implement OpenCV in order to automate Melee streaming

## Authors
* Brandon (cookiE) Cookie ~ *RecursionGG*
* Jarrod (@JarrodBlantonFitness) Blanton

## Requirements
* [OpenCV](https://opencv.org/releases.html)
* [Python 3.6](https://www.python.org/downloads/)
* [NodeJS + NPM](https://nodejs.org/en/)
* PIP
    * Download the [pip installation file](https://bootstrap.pypa.io/get-pip.py) to any location
    * Run `python get-pip.py` in that location

## Setup
After the above requirements are installed, we need to setup the project.
* First setup the python project
    * Run the following in the `python/` directory:
        * `pip install -r requirements.txt`
* Next we need to setup the React server
    * Run the following in the `react-server/` directory:
        * `npm install`
        * This should install all dependencies in the main react-server folder, and the webapp folder

## Running
To run the app: 
* go to `python/` directory
* run `py app.py`
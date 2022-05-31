# README

## Installation Procedures:
1. Install Python 3.8
2. Browse to this repo and run this command:
> pip -r install requirements.txt
3. Setup the env files
> cp .env.example .env
4. BASE_URL will be filled with the base website url we want to test for. e.g. `https://www.juicychain.org`
5. Run this command to run single test. e.g. `python tests/home/test_home_up.py`
> python <DIRECTORY_PATH> 
6. Run this command to run multiple tests at once
> python tests/home.py

## Setup in Containerized Environment
1. Build the docker images
> docker build -t gcr.io/chefchain-staging-341708/selenium:TAG_NAME_HERE .
2. Run the docker images
3. Inside the container directory run the same command as in Step 5 or 6 above.

## External Useful Links
Loading Test Suites Unittest Python Selenium 
https://chercher.tech/python/loading-test-suites-unittest-python-selenium
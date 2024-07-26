### Next: How to run app for kafka  

Create new python  environment 

python -m venv venv

Activate new python virtual environment: 

venv\Scripts\activate.bat 

When you run :
pip list , you should have pin and setuptolls only

Make local install:
pip install poetry

Update packages from poetry.lock file
poetry update

You should have clean environment to start.
After running docker file kafka-with-zookeeper on Docker Desktop .
You can run this app for testing how coins are transfered/published into subsriber

Run :

faststream run app_pub_order:app --workers 1



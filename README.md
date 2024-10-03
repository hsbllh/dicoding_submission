# Bike Sharing Dashboard 🚲🚲

## Setup Environment - Anaconda

conda create --name main.py python=3.12
conda activate dashboard
pip install -r requirements.txt

## Setup Environment - Shell/Terminal

mkdir dashboard
cd dashboard
pipenv install
pipenv shell
pip install -r requirements.txt

## Run steamlit app

streamlit run main.py

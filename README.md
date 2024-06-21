To run the scripts in a self-contained environment, follow the steps below.

1. Change your current working directory to the project root
2. Create a virtual environment
```
python -m venv venv
```
3. Activate your virtual environment and set PYTHONPATH
```
source venv/bin/activate
export PYTHONPATH=$(pwd)
```
4. Install required packages
```
pip install requirements.txt
```
5. Run the python scripts from the project root

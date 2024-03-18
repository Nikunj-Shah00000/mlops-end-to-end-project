echo [$(date)]: "START"

echo [$(date)]: "Creating env with python 3.9 ..."

conda create --prefix ./env python=3.9 -y

echo [$(date)]: "Activating the conda..."

source activate ./env

echo [$(date)]: "Installing the dev requirements..."

pip install -r requirements.txt

echo [$(date)]: "END"
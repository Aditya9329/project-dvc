create env
```bash
conda create -n winequaltiy
```


activate
```bash
conda activate winequaltiy
```

create a req file,install the req
```bash
pip install -r req
```


after gathering data
```bash
git init
```

initialize git
```bash
 dvc init
 ```
add data so dvc can track it 
```bash
dvc add data_given/winequality-red.csv
```

some commits
```bash
 git add . 
git commit -m "first commit"
```

    


tox command 
```bash
tox
```
for rebuilding-
```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands
```bash
pip install -e .
```
    
build your own package commands-
```bash
python setup.py sdist bdist_wheel
```

create an artifacts folder

    mlflow server \
        --backend-store-uri sqlite:///mlflow.db \
        --default-artifact-root ./artifacts \
        --host 0.0.0.0 -p 1234
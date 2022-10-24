create env
    ```bash
    conda create -n winequaltiy
    ```


    activate
    ```bash
    conda activate winequaltiy
    ```

    create a req file
    install the req
    ```bash
    pip install -r req
    ```


    after gathering data

    git init

    dvc init

    dvc add data_given/winequality-red.csv

    git add . 
    git commit -m "first commit"

    


    tox command -
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
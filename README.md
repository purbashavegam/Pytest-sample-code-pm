# pytest-example
Python Testing Example -- pytest

This is a simple example of how to use pytest to integreate testing in Python application.


## Usage
This example comes with several test files (e.g. test_app.py, test_funcs.py, etc.).


## To Make Dev Env and get pytest
`python -m venv .venv`
`pip install pytest` or 
`pip install -r requirements.txt` [ if correctly available]


## Code Structure

```
myapp/
    app.py
    mymodule/
        __init__.py
        funcs.py
tests/
    __init__.py
    test_app.py
        mymodule/
            __init__.py
            test_additions.py
            test_funcs.py
```


## which test file for which py scripts?
```
test_app.py -> app.py
test_funcs.py -> funcs.py
test_additions.py is for additional test cases

```


## Other things to check

```text
test file always should be named with initializing the word "test"
```

```
to run the tests marked as others, run the following command −
pytest -m others -v

```

# How to distribute your package

## Create a setup file

`setup.py`

## How to install it locally

 ```
 python setup.py install
 ```

## How to create a source distribution

```
python setup.py sdist --format zip
```

To see all the options use

```
python setup.py sdist --help-formats
```


## How to get help on distutils

```
python setup.py --help
```

## How to install 3rd party packages

### Where I can find 3rd party packages

[http://pypi.python.org/pypi] a.k.a. "Cheese shop" 

### Using **distutils**

 ```
 python setup.py install
 ```
 
 ### Using **easy_install**
 
  ```
 easy_install pip
 ```
 
 
 ### Using **pip**
 
  ```
 pip install nose
 ```
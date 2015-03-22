# Shipping working and maintainable code

## Testing

* `unittest` is a framework for developing reliable automated tests
* You define _test cases_ by subclassing from `unittest.TestCase`
* `unittest.main()` is useful for running all of the tests in a module
* `setUp()` and `tearDown` fixtures run code _before_ and _after_ _each test method_
* Test methods are defined by creating method names that start with `test_`
* `TestCase.assert...` methods make a test method fail when the right conditions aren't met
* Use `TestCase.assertRaises()` in a **with-statement** to check that the right exceptions are thrown in a test
* `nose` is a useful tool for working with `unittest`-based tests

## Debugging

* Python's standard debugger is called `PDB`
* `PDB` is a standard command-line debugger
* `pdb.start_trace()` can be used to stop program execution and enter the debugger
* Your REPL's prompt will change to **(PDB)** when you're in the debugger
* You can access PDB's built-in help system by typing `help`
* Use `python -m pdb <script name>` to run a program under PDB from the start
* **PDB Commands**
    * `where` : shows the current call stack
    * `next`  : lets execution continue to the next line of code
    * `continue` : lets program execution continue indefinitely, or 
        until you stop it with `Ctrl-C`
    * `list` : shows you the source code at your current location
    * `return` : resumes execution until the end of the current function
    * `print()` : lets you see the values of objects in the debugger
* Use `quit` to exit PDB

## Virtual environments

* Virtual environments are light-weight, self-contained Python installations 
  that any user can create
* `pyvenv` is the standard tool for creating virtual environments
* `pyvenv` accepts both
    * a source-installation argument as well as
    * a directory name into which to create the new environment
* To use a virtual environment, you need to run its `activate` script
* When you activate a virtual environment, your prompt is modified to remind you

## Distribution

* The `distutils` package is used to help you distribute your Python code
* `distutils` is generally used in a `setup.py` script which users run to 
  install your software
* The main function in `distutils` is `setup()`
* `setup()` takes a number of arguments describing both the source files 
  as well as metadata for the code
* The most common way to use `setup.py` is to install code using
    ```
    python setup.py install
    ```
* `setup.py` can also be used to generate **distributions** of your code
* Distributions can be zip files, tarballs, or several other formats
* To see all of the options use
    ```
    python setup.py --help
    ```

## Installing 3rd-party packages

* Three common tools for installing 3rd-party software are
    * `distutils`
    * `easy_install`
    * `pip`
* The central repository for Python packages is the **Python Package Index**,
  also called **PyPI** or **"cheeseshop"**
* You can install `easy_install` by downloading and running `distribute_setup.py`
* You use `easy_install` to install modules by running from the command line
    ```
    easy_install <package name>
    ```
* You can install `pip` via `easy_install`
* To install modules with `pip` use the subcommand `install` 
    ```
    pip install <package name>
    ```
* You can use `__file__` attribute on a **module** to find out where 
  its source file is located
* 3rd-party python packages are generally installed int your installation's
  (or your virtual environment's) `site-packages` directory

## General

* You can pass `-m` to your Python command to have it run a module as a script
    ```
    python -m pdb myscript.py
    ```
* Debugging makes it clear that Python is evaluating everything at run time


"""Classes in Python

* All types in Python have a 'class'
* Classes define the structure and behavior of an object
* Class is determined when object is created
    * normally fixed for the lifetime
* Classes are the key support for Object-Oriented Programming in Python
* Classes are defined using the 'class' keyword followed by CamelCase name
* Class instances are created by calling the class as if it were a function
* Instance methods are functions defined inside the class
    * Should accept an object instance called self as the first parameter
* Methods are called using instance.method()
    * Syntactic sugar for passing self instance to method
    * i.e.
        * a = Person("John")
        * a.name() == Person.name(a)
* The optional __init__() method initializes new instances
    * if present, the constructor calls __init__()
    * __init__() is not the constructor
* Arguments passed to the constructor are forwarded to the initializer


* Instance attributes are created simply by assigning to them
* Implementation details are denoted by a leading underscore
    * There are no public, protected or private access modifiers in Python
* Accessing implementation details can be very useful
    * Especially during development and debugging
* Class invariants should be established in the initializer
    * If the invariants can't be established raise exceptions to signal failure
* Methods can have docstrings
* Classes can have docstrings
* Even within an object method calls to other methods must be preceded with self
* You can have as many classes and functions in a module as you wish
    * Related classes and global functions are usually grouped together this way
* Polymorphism in Python is achieved through duck typing
    * This is also known as 'late binding'
* Polymorphism in Python does not use shared base classes or interfaces
* Class inheritance is primarily useful for sharing implementation
* All methods are inherited, including special methods like the initializer

* Following the Law of Demeter can reduce coupling
* Don't feel compelled to use classes when a simple function will suffice
    * Functions are also objects so they can be passed as arguments in other functions or methods
* Use "Ask! Don't tell." to avoid coupling between objects

"""

from utils import *


def main():
    pass

if __name__ == '__main__':
    print(__doc__)
    main()
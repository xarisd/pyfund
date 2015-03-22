"""Files and Resource Management

* Files are opened using the built-in open() function
  which accepts a file mode to control
    * read/write/append (r/w/a) behavior and
    * whether the file is to be treated as raw binary (b) or or encoded text data (t)
* For text data you should specify a text encoding
* Text files deal with string objects and perform universal newline translation and string encoding
* Binary files deal with bytes objects with no newline translation or encoding.
* When writing files, it's our responsibility to provide newline characters for line breaks
* Files should always be closed after use
* Files provide various line-oriented methods for reading,
  and are also iterators which yield line by line
* Files are context managers and the with-statement can be used with context managers
  to ensure that clean up operations, such as closing files, are performed
* The notion of file-like-objects is loosely defined, but very useful in practice
    * Exercise EAFP to make the most of them
* Context managers aren't restricted to file-like-objects.
  We can also use tools in the contextlib standard library module,
  such as closing() wrapper to create our own context managers

"""

import sys
from utils import *

if __name__ == '__main__':
    print(__doc__)

    hrule("Open file for write()")
    fname = 'wasteland.txt'
    f = open(fname, mode='wt', encoding='utf-8')
    f.write('What are you saying dude?\n')
    f.write('Test TEST tst')
    f.close()

    hrule("Open file for read()")
    g = open(fname, mode='rt', encoding='utf-8')
    s1 = g.read()
    print(s1)

    hrule("Read a file with readline()")
    g.seek(0)
    s = g.readline()
    while s != '':
        if s[-1:] == '\n':
            s = s[:-1]
        print(s)
        s = g.readline()

    hrule("Read a file with readlines()")
    g.seek(0)
    lines = g.readlines()
    for line in lines:
        if line[-1:] == '\n':
            line = line[:-1]
        print(line)

    g.close()

    hrule("Write/Append to a file using writelines()")
    h = open(fname, mode='at', encoding='utf-8')
    h.writelines([
        'Son of the man, \n',
        'You cannot say, or guess, ',
        'for you know only, \n',
        'A heap of broken images, ',
        'where the sun beats\n',
    ])
    h.close()
    g = open(fname, mode='rt', encoding='utf-8')
    print(''.join(g.readlines()))
    g.close()
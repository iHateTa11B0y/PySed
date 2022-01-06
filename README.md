# PySed: A pythonic text tools for Unix command line

## Intro

Unix-like os has lots of tools to manipulate text in shell. For instance, `sed`, `awk`.
These tools are convenient to use, but not that friendly to beginners. **Python** is 
a popular script language for rookie coders, so wee wanna build a pythonic tools to offer
a substitution of Unix command `sed`, `awk` and so on.

## Usage
We reserve three sign to determine the text level we wanna manipulate with.

1. _t:  text-level, `_t` refering the whole input text in your commands
2. _l:  line-level, `_l` refering the input lines<List> in your commands
3. _c: column-level `_c` refering the colums for each line <List<List>> in your commands

text-level is exclusive, which mean you can only determine one text-level to perform 
pythonic commands at a time. Or you can seperate your commands by `;`

Examples:
```shell
# performing equal function
$  ps aux | grep agent | awk '{print $2}' | sed ":a;N;s/\n/,/g;ta"
$  ps aux | grep agent | pt '_c[1];_t.replace("\n", " ")' 
```

## Install

```shell
$ git clone $(repo)
$ cd $(repo)
$ python setup.py install
```
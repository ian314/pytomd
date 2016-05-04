###Package Create/Install###
    python setup.py sdist
    cd ../dist
    pip install pytomd-1.0.1.tar.gz
 
****************************
###CLI Info ###
```
    optional arguments:
      -h, --help  show this help message and exit
      -o OUTPUT   location to put README.md
      -p PATH     base path to scan files
      -e          execute the values
      --version   show program's version number and exit
    
    example:
        pytomd -o ./README.md -p ./src -e
```

### How to document code ###
* the first line is an explanation
* all tags within :<anything>: will in become a parameter
* example tags must go at the end and the code most me contained in 3 back-ticks.

```
def Waldo(var):
''' Here is an example of a class <<< explanation
:param var: This is a parameter <<< tag
:example:
```
Some example goes here
```
```







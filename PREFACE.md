###Package Create/Install###
    python setup.py sdist
    cd ../dist
    pip install pytomd-1.0.1.tar.gz
 
****************************
###CLI Info ###
    optional arguments:
      -h, --help  show this help message and exit
      -o OUTPUT   location to put README.md
      -p PATH     base path to scan files
      -e          execute the values
      --version   show program's version number and exit

* example usage:
    pytomd -o ./README.md -p ./src -e
set -e

cd $(dirname $0) && cd ..

flake8 . --max-line-length=119

coverage erase
nosetests --with-coverage


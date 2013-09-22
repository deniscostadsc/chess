set -e

cd $(dirname $0) && cd ..

flake8 . --max-line-length=119

nosetests --with-coverage --cover-erase --ignore-files="^unittest2"
#!/bin/bash

set -e

cd $(dirname $0) && cd ..

flake8 . --max-line-length=119

py.test --cov chess tests/ --cov-report term-missing

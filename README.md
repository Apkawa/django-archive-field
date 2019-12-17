[![PyPi](https://img.shields.io/pypi/v/django-archive-field.svg)](https://pypi.python.org/pypi/django-archive-field)
[![Build Status](https://travis-ci.org/Apkawa/django-archive-field.svg?branch=master)](https://travis-ci.org/Apkawa/django-archive-field)
[![Codecov](https://codecov.io/gh/Apkawa/django-archive-field/branch/master/graph/badge.svg)](https://codecov.io/gh/Apkawa/django-archive-field)
[![Requirements Status](https://requires.io/github/Apkawa/django-archive-field/requirements.svg?branch=master)](https://requires.io/github/Apkawa/django-archive-field/requirements/?branch=master)
[![PyUP](https://pyup.io/repos/github/Apkawa/django-archive-field/shield.svg)](https://pyup.io/repos/github/Apkawa/django-archive-field)
[![PyPI](https://img.shields.io/pypi/pyversions/django-archive-field.svg)]()
[![PyPi](https://img.shields.io/pypi/v/django-archive-field.svg)](https://pypi.python.org/pypi/django-archive-field)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


# Installation

```bash
pip install django-archive-field

```

or from git

```bash
pip install -e git+https://githib.com/Apkawa/django-archive-field.git#egg=django-archive-field
```

## Django and python version

| Python<br/>Django |      2.7           |        3.5         |      3.6           |      3.7           |       3.8          |
|:-----------------:|--------------------|--------------------|--------------------|--------------------|--------------------|
| 1.8               | :heavy_check_mark: |       :x:          |      :x:           |       :x:          |      :x:           |
| 1.11              | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |      :x:           |
| 2.2               |       :x:          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| 3.0               |       :x:          |       :x:          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

:bangbang: Support Python 2.7 will be removed after 2020-01-01

# Usage


# Contributing

## run example app

```bash
pip install -r requirements.txt
./test/manage.py migrate
./test/manage.py runserver
```

## run tests

```bash
pip install -r requirements.txt
pytest
tox
```

## Update version

```bash
python setup.py bumpversion
```

## publish pypi

```bash
python setup.py publish
```







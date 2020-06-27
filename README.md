[![Build Status](https://travis-ci.org/ladybug-tools/honeybee-standards.svg?branch=master)](https://travis-ci.org/ladybug-tools/honeybee-standards)

[![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)](https://www.python.org/downloads/release/python-270/) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![IronPython](https://img.shields.io/badge/ironpython-2.7-red.svg)](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/)

# honeybee-standards

Default standards and templates used throughout honeybee extensions and plugins.

In addition to housing defaults, this package also includes a folder structure
that can be used to add assets into the installed standards libraries of the
extensions. Assets can be added by placing honeybee .json, .idf, or .rad files
in the respective folder within the folder structure (or by adding them to the
respective user_library.json, user_library.idf, or user_library.rad).

## Energy assets

The following energy asset can be added with this package:

* Schedules (and schedule type limits)
* Program Types
* Constructions (and material layers)
* Construction Sets

## Radiance assets

The following radiance asset can be added with this package:

* Modifiers
* Modifier Sets

## Installation

```console
pip install honeybee-standards
```

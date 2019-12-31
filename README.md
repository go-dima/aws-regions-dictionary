# aws-regions-dictionary

[![Build Status](https://travis-ci.org/go-dima/aws-regions-dictionary.svg?branch=master)](https://travis-ci.org/go-dima/aws-regions-dictionary)

Installation:

```
pip install git+https://github.com/go-dima/aws-regions-dictionary.git --user
```

Usage Example:

```
#!/bin/python

from AwsRegionsDictionary.RegionsMapping import mapToRegionKey

print(mapToRegionKey('Frankfurt'))
print(mapToRegionKey('eu-central-1'))
```
Output:
```
eu-central-1
eu-central-1
```

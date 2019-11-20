# aws-regions-dictionary

Installation:

```
pip install git+https://github.com/go-dima/aws-regions-dictionary.git --user
```

Usage Example:

```
#!/bin/python

from AwsRegionsDictionary import RegionsMapping

print(RegionsMapping.findRegion('Frankfurt'))
print(RegionsMapping.findRegion('eu-central-1'))
```
Output:
```
eu-central-1
eu-central-1
```

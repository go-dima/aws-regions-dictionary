regions = {
    "n. virginia" : "us-east-1",
    "ohio" : "us-east-2",
    "n. california" : "us-west-1",
    "oregon" : "us-west-2",
    "hong kong" : "ap-east-1",
    "mumbai": "ap-south-1",
    "seoul" : "ap-northeast-2",
    "singapore" : "ap-southeast-1",
    "sydney" : "ap-southeast-2",
    "tokyo" : "ap-northeast-1",
    "central" : "ca-central-1",
    "frankfurt" : "eu-central-1",
    "ireland" : "eu-west-1",
    "london" : "eu-west-2",
    "paris" : "eu-west-3",
    "stockholm" : "eu-north-1",
    "bahrain" : "me-south-1",
    "sao paulo" : "sa-east-1"
}

def findRegion(regionStr):
    regionStr_lower = regionStr.lower()
    if regionStr_lower in regions.values():
        return regionStr_lower
    if regionStr_lower in regions.keys():
        return regions[regionStr_lower]
    raise KeyError(f"{regionStr} is not recognized.")

regions = {
    "N. Virginia" : "us-east-1",
    "Ohio" : "us-east-2",
    "N. California" : "us-west-1",
    "Oregon" : "us-west-2",
    "Hong Kong" : "ap-east-1",
    "Mumbai": "ap-south-1",
    "Seoul" : "ap-northeast-2",
    "Singapore" : "ap-southeast-1",
    "Sydney" : "ap-southeast-2",
    "Tokyo" : "ap-northeast-1",
    "Central" : "ca-central-1",
    "Frankfurt" : "eu-central-1",
    "Ireland" : "eu-west-1",
    "London" : "eu-west-2",
    "Paris" : "eu-west-3",
    "Stockholm" : "eu-north-1",
    "Bahrain" : "me-south-1",
    "Sao Paulo" : "sa-east-1"
}

def findRegion(regionStr):
    if regionStr in regions.values():
        return regionStr
    if regionStr in regions.keys():
        return regions[regionStr]
    raise KeyError(f"{regionStr} is not recognized.")

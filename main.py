import json
import re
import argparse
import os.path

parser = argparse.ArgumentParser(description="Build SVG roadmap image from JSON")
parser.add_argument("-f","--file",required=True,help="Path to file to parse")
parser.add_argument("-d","--debug",help="Debug mode",action="store_true")
args = parser.parse_args()

#Check file path
if os.path.exists(args.file):
    if args.debug:
        print("DEBUG: File " + args.file + " exists")
    fileToOpen=args.file

#Open the file
try:
    with open(fileToOpen) as roadmapJSONFile:
        roadmapJSONData = json.load(roadmapJSONFile)
except:
    print("Error parsing " + args.file + " as a JSON file")
    exit()

#Parse out the required fields
roadmapTitle = roadmapJSONData["Title"]
roadmapYears = roadmapJSONData["Years"]
roadmapMeasure = roadmapJSONData["Measure"]

#Validate options
if int(roadmapYears) > 3 and roadmapMeasure == "Q" :
    print("ERROR: Can't have quarter resolution beyond 3 years")
    exit(1)

if int(roadmapYears) > 5:
    print("ERROR: Can't have more then 5 years in a drawing")
    exit(1)

#Track Count
trackPattern = re.compile('[Tt][Rr][Aa][Cc][Kk][0-9][0-9]?')
tracksFound = []
for key in roadmapJSONData:
    isKeyTrack = trackPattern.match(key)
    if isKeyTrack:
        if args.debug:
            print("DEBUG: " + key + " is found")
        tracksFound.append(key)

totalTrackCount = len(tracksFound)
tracksFound.sort()

if args.debug:
    print("DEBUG: Number of tracks found - " + str(totalTrackCount))

#Calculate the canvas size needed

#Start building the SVG

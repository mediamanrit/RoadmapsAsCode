import json
import argparse
import os.path
from datetime import datetime
from roadmap import JSON2roadmap

parser = argparse.ArgumentParser(description="Build SVG roadmap image from JSON")
parser.add_argument("-f","--file",required=True,help="Path to file to parse")
parser.add_argument("-d","--debug",help="Debug mode",action="store_true")
args = parser.parse_args()

#Check file path
if os.path.exists(args.file):
    if args.debug:
        print("DEBUG: File " + args.file + " exists")
else:
    print("ERROR: File " + args.file + " does not exist")
    exit()
    
file_to_open=args.file

#Open the file
try:
    file_obj = open(file_to_open)
    roadmapJSONData = json.load(file_obj)
except:
    raise
    exit()

j2r = JSON2roadmap(1,roadmapJSONData)
svg_out = j2r.get_roadmap()

destname = "jsontest-gradient-3YQ.svg"
if os.path.exists(destname):
    os.remove(destname)

file_out_obj = open(destname,"x")
file_out_obj.write(svg_out)
file_out_obj.close()
import json
import argparse
import os.path
from datetime import datetime
from roadmap import JSON2roadmap

parser = argparse.ArgumentParser(description="Build SVG roadmap image from JSON")
parser.add_argument("-i","--infile",required=True,help="Path to the JSON file to parse")
parser.add_argument("-o","--outfile",required=True,help="Name and path of the SVG file to create")
parser.add_argument("-f","--forceoverwrite",help="Overwrite the output file if it exists already",action="store_true")
parser.add_argument("-d","--debug",help="Debug mode",action="store_true")
args = parser.parse_args()

#Check file path
file_to_open=args.infile

try:
    if os.path.exists(file_to_open):
        if args.debug:
            print("DEBUG: File " + file_to_open + " exists")
    else:
        raise("File " + file_to_open + " does not exist")
except:
    raise
    exit(1)

#Open the file
try:
    file_obj = open(file_to_open)
    roadmapJSONData = json.load(file_obj)
except:
    raise
    exit()

#Create the roadmap and get the SVG
try:
    j2r = JSON2roadmap(1,roadmapJSONData)
    svg_out = j2r.get_roadmap()
except:
    raise

try:
    destname = args.outfile
    if os.path.exists(destname):
        if args.forceoverwrite:
            os.remove(destname)
        else:
            raise("Destination file already exists")
except:
    raise("Error creating the file " + destname)

try:
    file_out_obj = open(destname,"x")
    file_out_obj.write(svg_out)
    file_out_obj.close()
except:
    raise ("Error creating the new file" + destname)
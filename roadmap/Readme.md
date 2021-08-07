# Inner workings of the Roadmap module
---
## Description
The Roadmap module provides the core functionality of the Roadmaps As Code toolset.  In it lives classes that produce the different types of roadmap visuals.

---
## Taxonomy
Some of the words used in the documentation and code and what they mean:
* **Strategy**: A high level direction or wish list that states where something is headed to.  Sometimes with an undefined timeline.
* **Roadmap**: A representation of the state of things over a time span.
* **Track**: A line on a roadmap, defined by starting and ending points.
* **Milestone**: A point on a track that indicates a state change.  Typically milestone meanings on all tracks share a common set of state defintions.
* **Technology Architect**: The person who made this tool due to a large lack of capability and understanding in my industry.
---
## Usage
Here are the methods to use the class

**__init__**(*self*, *name: str*, *num_years: int*, *roadmap_start_year:int*, *measure: str*)
Class instance definition. Requires:
 * name (str): Name of the roadmap graphic.  Will go in the title field in the output.
 * num_years (int): How many years to include on the graphic.
 * roadmap_start_year (int): What year to start the graphic at.
 * measure (str):  What is the measure inside the year.  Either Halves (measure="H") or Quarters (measure="Q").

**build_image**(*self*):
Creates and returns the svg image.

**set_title_options**(*self*, *bg_color: str*, *text_color: str*)
Sets the options for the title bar. Requires:
 * bg_color (str): The background color for the title box in hex format.
 * text_color (str): The text color for the title box in hex format.

**set_footer_text**(*self*,*footer_text:str*)
Sets the text for the footer.  Requires:
 * footer_text (str): The text that will appear in the footer of the image.

**add_milestone_definition**(*self*, *milestone_name:str*, *milestone_bgcolor:str*, *milestone_letter:str*)
Adds a milestone definition for the roadmap.  Milestones on each track will use these parameters when they get placed on each track as needed.
* milestone_name (str): Name of the milestone
* milestone_bgcolor (str): Color of the milestone diamond that will go on the tracks
* milestone_letter (str): The letter that will go in the diamond on the tracks

**add_track**(*self*, *track_name:str*, *start_year:int*, *start_division:str*, *end_year:int*, *end_division:str*, *track_fontcolor*:str="#000000", *track_bgcolor*:str="#FFFFFF")
Adds a track to an instance of a roadmap.  Requires:
 * track_name (str): The name of the track.  Will go on the track itself as well.
 * start_year (int): The year the track starts.
 * start_division (str): The division the track starts (ie, Q3, H1, etc).
 * end_year (int): The year the track ends.
 * end_division (str): The division the track ends (ie, Q3, H1, etc).
 Optional:
 * track_fontcolor (str): The hex color the font on the track will be.  Defaults to "#000000".
 * track_bgcolor (str): The hex color the track will be.  Defaults to "#FFFFFF".

**add_track_milestone**(*self*, *track_name:str*, *milestone_name:str*, *milestone_year:int*, *milestone_division:str*)
Adds milestones to tracks on a roadmap.  Requires:
* track_name (str): The name of the track (created with add_track) to put the milestone on.
* milestone_name (str): The name of the milestone (defined by add_milestone_definition) to put on the track.
* milestone_year (int): The year the milestone is in.
* milestone_division (str): The division the milestone is in (ie, Q3, H1, etc).


---
## Example
The following example creates a roadmap that starts in 2020 and shows 3 years, with Quarter resolution
```python
from roadmap import Roadmap

#Create the roadmap
r = Roadmap("Sample Roadmap",3,2020,"Q")

#Add the milestone definitions
r.add_milestone_definition("Emerging", "#0000FF", "E")
r.add_milestone_definition("Standard", "#00FF00", "S")
r.add_milestone_definition("Containment", "#FFFF00", "C")
r.add_milestone_definition("Retirement", "#FF3399", "R")
r.add_milestone_definition("Retired", "#FF0000", "X")

#Line that ends in the middle
r.add_track("Test Track 1",2010,"Q2",2021,"Q2")
r.add_track_milestone("Test Track 1","Standard",2011,"Q1")
r.add_track_milestone("Test Track 1","Containment",2018,"Q1")
r.add_track_milestone("Test Track 1","Retirement",2020,"Q1")
r.add_track_milestone("Test Track 1","Retired",2021,"Q2")

#Line that starts and goes out with no milestones
r.add_track("Test Track 2",2021,"Q1",2029,"Q4")

#Line that starts and ends
r.add_track("Test Track 3",2020,"Q1",2022,"Q2")
r.add_track_milestone("Test Track 3","Standard",2020,"Q1")
r.add_track_milestone("Test Track 3","Containment",2021,"Q3")
r.add_track_milestone("Test Track 3","Retirement",2022,"Q2")
r.add_track_milestone("Test Track 3","Retired",2022,"Q2")

#Line that goes through
r.add_track("Test Track 4",2010,"Q2",2029,"Q3")

#Add a footer
r.add_footer_text("Some footer text would go here")

#Generate and store the svg code
out = r.build_image()
```

---
## Roadmap class inner workings
* self variables
    * endpoints (dict) = Dictionary to have pre-defined pixel points on the drawing for each stopping point.  Static, built when an instance is created.
        * endpoints["*a*Y"] (dict) = Dictionary for the points on a roadmap that contains *a* Years (ex: 1Y, 2Y, etc)
        * endpoints["*a*Y"]["Y*b*"] (dict) = Dictionary for the points on a road map in Year *a* for the *b*'th year on the map (ex: Y2 is the 2nd year in the roadmap)
        * endpoints["*a*Y"]["Y*b*"]["*cd*"] (dict) = The points on the roadmap for the *c*'th division of *d* scale.  Scale is either Q for quarters or H for halves.  (ex: 2H is the 2nd half of the year)
    * first_track_y (int) = Y position for the first track.  Static in the code, to aid in track placement.
    * footer_text (str) = Text that goes in the footer.  Accessed & changed via methods.
    * footer_text_color = Hex formatted color for the color of the text in the footer.  Access & chaged via methods.
    * measure (str) = Defines the measure for the year divisions.   H=Year Halves.  Q=Year Quarters.
    * milestones (dict) = Dictionary that stores the configurations of the milestone definitions for the roadmap (not specific milestones on the track)
        * milestones[*milestone_name*] (dict) = Stores the options for the milestone named *milestone_name*
        * milestones[*milestone_name*]["bgcolor"] = Hex formatted color for the background of the milestone diamond.
        * milestones[*milestone_name*]["letter"] = One letter to represent the milestone on the graphic.
    * name (str) = Title of the roadmap.
    * num_years (int) = Number of years on the roadmap.
    * roadmap_end_year (int) = The year the roadmap ends.  This is derrived from roadmap_start_year and num_years at creation time of the instance.
    * roadmap_start_year (int) = The year the roadmap starts.
    * spacing_track_y (int) = Y spacing between tracks.  Static in the code, to aid in track placement.
    * title_bg_color (str) = Hex formatted color for the background of the title box.
    * title_text_color (str)= Hex formatted color for the color of the text in the title box.
    * tracks (dict) = Dictionary that stores the configurations of each track on the roadmap.
        * tracks[*track_name*] (dict) = Dictionary to store information about a single track named *track_name*.  Created by add_track method.
        * tracks[*track_name*]["start_year"] (int) = The year *track_name* starts. Created by add_track method.
        * tracks[*track_name*]["start_division"] (str) = The division *track_name* starts. Created by add_track method.
        * tracks[*track_name*]["end_year"] (int) = The year *track_name* ends. Created by add_track method.
        * tracks[*track_name*]["end_division"] (str) = The division *track_name* ends. Created by add_track method.
        * tracks[*track_name*]["milestones"] (dict) = Dictionary to track the milestones for *track_name* .
        * tracks[*track_name*]["milestones"][*milestone_name*] (dict) = Dictionary to track the settings for the *milestone_name* milestone on the *track_name* track.
        * tracks[*track_name*]["milestones"][*milestone_name*]["milestone_year"] (int) = The year the *milestone_name* is in for the *track_name* track.
        * tracks[*track_name*]["milestones"][*milestone_name*]["milestone_division"] (str) = The division the *milestone_name* is in for the *track_name* track.
    
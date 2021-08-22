# JSON File Information
This describes the properties and structure of the JSON file that is read / expected for the json2roadmap class to process it.

[This](https://github.com/mediamanrit/RoadmapsAsCode/blob/main/tests/testRoadmap.json) is a full sample file, which is used for testing functionality of the code.

The following is a simple example of a roadmap with one track.
```
    {
        "schemaVersion" : "1",
        "title" : "Sample JSON Roadmap",
        "titleBGColor" : "#0000FF",
        "titleTextColor" : "#000000",
        "gradientFill" : "true",
        "footerText" : "Some footer text would go here",
        "years" : "3",
        "startYear" : "2020",
        "measure" : "Q",
        "bgcolor" : "#111111",
        "milestones" : {
            "Standard" : {
                "color" : "#00FF00",
                "letter" : "S"
            },
            "Retired" : {
                "color" : "#FF0000",
                "letter": "X"
            }
        },
        "tracks" : {
            "JSON Test Track 1" : {
                "beginYear" : "2010",
                "beginDivision" : "Q2",
                "endYear" : "2021",
                "endDivision" : "Q2",
                "bgcolor" : "#000084",
                "milestones" : {
                    "Standard" : {
                        "year": "2011",
                        "division": "Q1"
                    },
                    "Retired" : {
                        "year" : "2021",
                        "division": "Q2"
                    }
                }
            }
        }
    }
```

* **schemaVersion** - Version of the schema that is used for the file
* **title** - Title of the roadmap
* **titleBGColor** - Background color of the title box, in hex format
* **titleTextColor** - Text color of the title, in hex format
* **gradientFill** - Set to "true" if the tracks should be filled with gradients between milestones
* **footerText** - Text to put in the footer
* **years** - How many years to put on the roadmap
* **startYear** - What year to start the roadmap on
* **measure** - "Q" for quarters, "H" for halves
* **bgcolor** - Background color for the image in hex format.  Defaults to transparent.
* **milestones** - Contains a sub list of the milestone definitions
  * ***"[Milestone Name 1]"*** - Name of the milestone, w/ list of sub properties
    * **color** - What color, in hex, the milestone should be
    * **letter** - What letter to put in the milestone
  * ***"[Milestone Name 2...]"***
    * **color**
    * **letter**
* **tracks** - Contains a sub list of the tracks on the drawing
  * ***"[JSON Test Track 1]"*** - Name of the track, w/ list of sub properties
    * **beginYear** - Year the track starts
    * **beginDivision** - The division the track starts (ie, H2)
    * **endYear** - The year the track ends
    * **endDivision** - The division the track ends (ie, H1)
    * **bgcolor** - Background color of the track in hex if gradient is not used.  Default to white.
    * **milestones** - Contains a sub list of the milestones on this track
      * ***"[Milestone Name 1]"***
        * **year**
        * **division**
      * ***"[Milestone Name 2...]"***
        * **year**
        * **division**
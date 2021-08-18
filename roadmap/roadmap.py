import re
"""Module for making Roadmap graphics"""

class Roadmap:
    """Time-based roadmap class"""
    def __init__(self, name: str, num_years: int, roadmap_start_year:int, measure: str):
        """Spawn the Roadmap"""
        #Check the options
        try:
            testing_years = int(num_years)
            if not (testing_years >= 1 and testing_years <= 5):
                raise ValueError(
                    "num_years must be between 1 and 5")
        except:
            print("Must provide a valid value for num_years (1-5)")
            raise
        try:
            testing_startyear = int(roadmap_start_year)
            if not (testing_startyear > 1960 and testing_startyear < 3000):
                raise ValueError(
                    "Must provide a startyear between 1960 and 3000")
        except:
            print("Mut provide a valid start year")
            raise
        try:
            measurematch = re.compile("^[QqHh]$")
            if not measurematch.match(measure):
                raise ValueError ("Invalid measure provided")
        except:
            print("Must provide a valid value for measure (H or Q)")
            raise

        #Load the options
        self.name = name
        self.num_years = int(num_years)
        self.roadmap_start_year = int(roadmap_start_year)
        self.measure = measure.upper()
        self.roadmap_end_year = int(roadmap_start_year) + (int(num_years) - 1)
        
        #Set the defaults
        self.title_bg_color = "#FFFFFF"
        self.title_text_color = "#000000"
        self.tracks = {}
        self.milestones = {}
        self.first_track_y = 210
        self.spacing_track_y = 85
        self.footer_text = ""
        self.footer_text_color = "#000000"

        #Define the arror end positions
        self.endpoints = {}
        self.endpoints["1Y"] = {}
        self.endpoints["1Y"]["Y1"] = {}
        self.endpoints["1Y"]["Y1"]["H1"] = 300
        self.endpoints["1Y"]["Y1"]["H2"] = 900
        self.endpoints["1Y"]["Y1"]["Q1"] = 150
        self.endpoints["1Y"]["Y1"]["Q2"] = 450
        self.endpoints["1Y"]["Y1"]["Q3"] = 760
        self.endpoints["1Y"]["Y1"]["Q4"] = 1060
        self.endpoints["2Y"] = {}
        self.endpoints["2Y"]["Y1"] = {}
        self.endpoints["2Y"]["Y1"]["H1"] = 148
        self.endpoints["2Y"]["Y1"]["H2"] = 448
        self.endpoints["2Y"]["Y1"]["Q1"] = 73
        self.endpoints["2Y"]["Y1"]["Q2"] = 223
        self.endpoints["2Y"]["Y1"]["Q3"] = 373
        self.endpoints["2Y"]["Y1"]["Q4"] = 523
        self.endpoints["2Y"]["Y2"] = {}
        self.endpoints["2Y"]["Y2"]["H1"] = 753
        self.endpoints["2Y"]["Y2"]["H2"] = 1053
        self.endpoints["2Y"]["Y2"]["Q1"] = 678
        self.endpoints["2Y"]["Y2"]["Q2"] = 828
        self.endpoints["2Y"]["Y2"]["Q3"] = 978
        self.endpoints["2Y"]["Y2"]["Q4"] = 1128
        self.endpoints["3Y"] = {}
        self.endpoints["3Y"]["Y1"] = {}
        self.endpoints["3Y"]["Y1"]["H1"] = 95
        self.endpoints["3Y"]["Y1"]["H2"] = 295
        self.endpoints["3Y"]["Y1"]["Q1"] = 48
        self.endpoints["3Y"]["Y1"]["Q2"] = 146
        self.endpoints["3Y"]["Y1"]["Q3"] = 245
        self.endpoints["3Y"]["Y1"]["Q4"] = 343
        self.endpoints["3Y"]["Y2"] = {}
        self.endpoints["3Y"]["Y2"]["H1"] = 500
        self.endpoints["3Y"]["Y2"]["H2"] = 700
        self.endpoints["3Y"]["Y2"]["Q1"] = 453
        self.endpoints["3Y"]["Y2"]["Q2"] = 551
        self.endpoints["3Y"]["Y2"]["Q3"] = 650
        self.endpoints["3Y"]["Y2"]["Q4"] = 748
        self.endpoints["3Y"]["Y3"] = {}
        self.endpoints["3Y"]["Y3"]["H1"] = 905
        self.endpoints["3Y"]["Y3"]["H2"] = 1105
        self.endpoints["3Y"]["Y3"]["Q1"] = 858
        self.endpoints["3Y"]["Y3"]["Q2"] = 956
        self.endpoints["3Y"]["Y3"]["Q3"] = 1055
        self.endpoints["3Y"]["Y3"]["Q4"] = 1153
        self.endpoints["4Y"] = {}
        self.endpoints["4Y"]["Y1"] = {}
        self.endpoints["4Y"]["Y1"]["H1"] = 0
        self.endpoints["4Y"]["Y1"]["H2"] = 0
        self.endpoints["4Y"]["Y2"] = {}
        self.endpoints["4Y"]["Y2"]["H1"] = 0
        self.endpoints["4Y"]["Y2"]["H2"] = 0
        self.endpoints["4Y"]["Y3"] = {}
        self.endpoints["4Y"]["Y3"]["H1"] = 0
        self.endpoints["4Y"]["Y3"]["H2"] = 0
        self.endpoints["4Y"]["Y4"] = {}
        self.endpoints["4Y"]["Y4"]["H1"] = 0
        self.endpoints["4Y"]["Y4"]["H2"] = 0
        self.endpoints["5Y"] = {}
        self.endpoints["5Y"]["Y1"] = {}
        self.endpoints["5Y"]["Y1"]["H1"] = 0
        self.endpoints["5Y"]["Y1"]["H2"] = 0
        self.endpoints["5Y"]["Y2"] = {}
        self.endpoints["5Y"]["Y2"]["H1"] = 0
        self.endpoints["5Y"]["Y2"]["H2"] = 0
        self.endpoints["5Y"]["Y3"] = {}
        self.endpoints["5Y"]["Y3"]["H1"] = 0
        self.endpoints["5Y"]["Y3"]["H2"] = 0
        self.endpoints["5Y"]["Y4"] = {}
        self.endpoints["5Y"]["Y4"]["H1"] = 0
        self.endpoints["5Y"]["Y4"]["H2"] = 0
        self.endpoints["5Y"]["Y5"] = {}
        self.endpoints["5Y"]["Y5"]["H1"] = 0
        self.endpoints["5Y"]["Y5"]["H2"] = 0
        
    def set_title_options(self, bg_color: str, text_color: str):
        """Sets the formatting options for the title of the roadmap"""
        #Check the options
        try:
            colormatch = re.compile("^#(?:[0-9a-fA-F]{3}){1,2}$")
            if not colormatch.match(bg_color):
                raise ValueError ("Invalid bg_color provided")
            if not colormatch.match(text_color):
                raise ValueError ("Invalid text_color provided")
        except:
            print("Please set valid colors!")
            raise

        #Set the variables
        self.title_bg_color = bg_color
        self.title_text_color = text_color

        #Rebuild the title box
        self.__build_title_box()

    def set_footer_text(self,footer_text:str):
        """Define what should be in the footer"""
        self.footer_text = footer_text

    def add_milestone_definition(self, milestone_name:str, milestone_bgcolor:str, milestone_letter:str):
        """Add the milestone definition to the object"""
        #validate the color
        try:
            colormatch = re.compile("^#(?:[0-9a-fA-F]{3}){1,2}$")
            if not colormatch.match(milestone_bgcolor):
                raise ValueError ("Invalid milestone_bgcolor provided")
        except:
            print("Please set valid colors!")
            raise

        #Validate it's not a duplicate
        try:
            if milestone_name in self.milestones:
                raise ValueError ("Cannot add a duplicate milestone definition")
        except:
            raise

        self.milestones[milestone_name] = {}
        self.milestones[milestone_name]["bgcolor"] = milestone_bgcolor
        self.milestones[milestone_name]["letter"] = milestone_letter[0]

    def add_track(self, track_name:str, start_year:int, start_division:str, end_year:int, end_division:str, track_fontcolor:str="#000000", track_bgcolor:str="#FFFFFF"):
        """Add a track to the roadmap"""
        # Check the options
        try:
            testing_startyear = int(start_year)
            if not (testing_startyear > 1960 and testing_startyear < 3000):
                raise ValueError(
                    "Must provide a startyear between 1960 and 3000")

            testing_endyear = int(end_year)
            if not (testing_endyear > 1960 and testing_endyear < 3000):
                raise ValueError(
                    "Must provide an endyear between 1960 and 3000")

            measure_test = re.compile('[QH][1234]')

            if not measure_test.match(start_division):
                raise ValueError(
                    "Must provide a start_division in matching [QH][1234]")

            if not measure_test.match(end_division):
                raise ValueError(
                    "Must provide a end_division in matching [QH][1234]")
        except:
            print("Error parsing arguments sent to add_track")
            raise

        try:
            colormatch = re.compile("^#(?:[0-9a-fA-F]{3}){1,2}$")
            if not colormatch.match(track_bgcolor):
                raise ValueError ("Invalid track_bgcolor provided")
        except:
            print("Please set track_bgcolor colors!")
            raise

        try:
            colormatch = re.compile("^#(?:[0-9a-fA-F]{3}){1,2}$")
            if not colormatch.match(track_fontcolor):
                raise ValueError ("Invalid track_fontcolor provided")
        except:
            print("Please set track_fontcolor colors!")
            raise

        #Check if the measure of the roadmap = the measure of the track requested
        #If not, adjust accordingly.  Round up when quarters to halves
        adjusted_start_division = self.__round_division(start_division)
        adjusted_end_division = self.__round_division(end_division)

        #Load the track into the dict
        self.tracks[track_name] = {}
        self.tracks[track_name]["start_year"] = start_year
        self.tracks[track_name]["start_division"] = adjusted_start_division
        self.tracks[track_name]["end_year"] = end_year
        self.tracks[track_name]["end_division"] = adjusted_end_division
        self.tracks[track_name]["track_bgcolor"] = track_bgcolor
        self.tracks[track_name]["track_fontcolor"] = track_fontcolor

    def add_track_milestone(self, track_name:str, milestone_name:str, milestone_year:int, milestone_division:str):
        """Add a milestone to a track by the track's name"""
        #If no milestones have been made yet, create the dict to store them
        if "milestones" not in self.tracks[track_name]:
            self.tracks[track_name]["milestones"] = {}

        try:
            #Validate the provided milestone
            if not (milestone_year > 1960 and milestone_year < 3000):
                raise ValueError(
                    "Must provide a startyear between 1960 and 3000")
            if not (milestone_year >= self.tracks[track_name]["start_year"] and milestone_year <= self.tracks[track_name]["end_year"]):
                raise ValueError(
                    "Milestone year must be in the year range of the track")
            
            division_test = re.compile('[QH][1234]')
            if not division_test.match(milestone_division):
                raise ValueError(
                    "Must provide a start_division in matching [QH][1234]")

        except:
            print("Error validating milestone options")
            raise()

        adjusted_milestone = self.__round_division(milestone_division)

        #Store the milestone
        self.tracks[track_name]["milestones"][milestone_name] = {}
        self.tracks[track_name]["milestones"][milestone_name]["milestone_year"] = milestone_year
        self.tracks[track_name]["milestones"][milestone_name]["milestone_division"] = adjusted_milestone

    def get_footer_text(self):
        """Return whatever is currently defined to be in the footer"""
        return self.footer_text

    def get_track(self, name):
        """Get the details of a track by its name"""
        try:
            #Return the dict for the requested track
            return self.tracks[name]
        except:
            raise

    def del_track(self, name):
        """Remove a track from the roadmap"""
        try:
            #Delete the requested track from the dict
            del self.tracks[name]
            return True
        except:
            raise
    
    def __build_footer(self):
        """Private function: generates the svg code for the footer"""
        #Loop through the tracks to find the highest Y value
        last_y = 500
        for onetrack in self.tracks:
            if self.tracks[onetrack]["y"] > last_y:
                last_y = self.tracks[onetrack]["y"]
        
        #Add a buffer, that's where our footer goes
        footer_y = str(last_y + 80)
        
        svg_footer = "<text x=\"600\" y=\"" + footer_y + "\" fill=\"" + self.footer_text_color + "\" font-family=\"Helvetica\" font-size=\"14px\" text-anchor=\"middle\">" + self.footer_text + "</text>"
        return svg_footer

    def __build_title_box(self):
        """Private function: generates the svg code for the title box"""
        self.svg_title = "<g id=\"titleBox\">"
        self.svg_title = self.svg_title + "<rect x=\"0\" y=\"0\" width=\"1200\" height=\"60\" rx=\"9\" ry=\"9\" fill=\"" + self.title_bg_color + "\" stroke=\"#000000\" pointer-events=\"all\" />"
        self.svg_title = self.svg_title + "<text x=\"600\" y=\"39\" fill=\"" + self.title_text_color + "\" font-family=\"Helvetica\" font-size=\"30px\" text-anchor=\"middle\" font-weight=\"bold\" text-decoration=\"underline\">" + self.name + "</text>"
        self.svg_title = self.svg_title + "</g>"

    def __build_tracks(self):
        svg_tracks = "<g id=\"Tracks\">"
        track_number = 0 # Using counter starting at 0 to track which roadmap track this is.
        for onetrack in self.tracks:
            #Figure out starting X position
            if self.tracks[onetrack]["start_year"] < self.roadmap_start_year:
                self.tracks[onetrack]["start_x"] = 0
            else:
                starting_year_column = (self.tracks[onetrack]["start_year"] - self.roadmap_start_year) + 1
                start_yeartext = "Y" + str(starting_year_column) #ex: Y2
                
                start_division_number = self.tracks[onetrack]["start_division"][1]
                start_divisiontext = self.measure + str(start_division_number) # ex: Q3, or H1

                year_count_text = str(self.num_years) + "Y"
                self.tracks[onetrack]["start_x"] = self.endpoints[year_count_text][start_yeartext][start_divisiontext]

            #Figure out ending x position
            #If the ending year for the track is past the ending year of the requested plan...
            if self.tracks[onetrack]["end_year"] > self.roadmap_end_year:
                self.tracks[onetrack]["end_x"] = 1200
            else:
                ending_year_column = (self.tracks[onetrack]["end_year"] - self.roadmap_start_year ) + 1
                end_yeartext = "Y" + str(ending_year_column) #ex: Y2

                end_division_number = self.tracks[onetrack]["end_division"][1]
                end_divisiontext = self.measure + str(end_division_number) # ex: Q3, or H1
                
                year_count_text = str(self.num_years) + "Y"
                self.tracks[onetrack]["end_x"] = self.endpoints[year_count_text][end_yeartext][end_divisiontext]

            #Figure out the starting y position
            my_y = self.first_track_y + (track_number * self.spacing_track_y)
            self.tracks[onetrack]["y"] = my_y

            track_bgcolor = self.tracks[onetrack]["track_bgcolor"]
            track_fontcolor = self.tracks[onetrack]["track_fontcolor"]

            #Create the lines
            #If the end is on the page, make it a rectangle
            if self.tracks[onetrack]["end_x"] < 1200:
                height = 40
                tail_bottom_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"]) #Start, bottom left of box
                tail_top_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"] - height) #Point 1
                tail_top_right = str(self.tracks[onetrack]["end_x"]) + " " + str(self.tracks[onetrack]["y"] - height) # Point 2
                tail_bottom_right = str(self.tracks[onetrack]["end_x"]) + " " + str(self.tracks[onetrack]["y"])
                #Add the rectangle
                svg_tracks = svg_tracks + "<path d=\"M " + tail_bottom_left + " L " + tail_top_left + " L " + tail_top_right + " L " + tail_bottom_right + " Z\" fill=\"" + track_bgcolor + "\" stroke=\"" + track_fontcolor + "\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" pointer-events=\"all\" />"

                #Add the label
                label_y = str(self.tracks[onetrack]["y"] - 13)
                label_x = str((self.tracks[onetrack]["start_x"] + self.tracks[onetrack]["end_x"]) / 2) #Center of the width of the tail/box
                svg_tracks = svg_tracks + "<text x=\"" + label_x + "\" y=\"" + label_y + "\" fill=\"" + track_fontcolor + "\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(onetrack) + "</text>"

            #If the end is off page, make it an arrow.
            else:
                height = 40
                #define points for the arrow (7 total)
                tail_bottom_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"]) #Start, bottom left of arrow path
                tail_top_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"] - height) #Point 1
                tail_top_right = "1158 " + str(self.tracks[onetrack]["y"] - height) # Point 2
                arrow_left_up = "1158 "+ str(self.tracks[onetrack]["y"] - height - 20) # point 3
                arrow_right_out = "1199.5 " + str(self.tracks[onetrack]["y"] - (height / 2))
                arrow_right_in = "1158 " + str(self.tracks[onetrack]["y"] + 20)
                arrow_left_down = "1158 " + str(self.tracks[onetrack]["y"])
                
                #Add the arrow
                svg_tracks = svg_tracks + "<path d=\"M " + tail_bottom_left + " L " + tail_top_left + " L " + tail_top_right + " L " + arrow_left_up + " L " + arrow_right_out + " L " + arrow_right_in + " L " + arrow_left_down + " Z\" fill=\""+ track_bgcolor + "\" stroke=\"" + track_fontcolor + "\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" pointer-events=\"all\" />"

                #Add the text
                label_y = str(self.tracks[onetrack]["y"] - 13)
                label_x = str((self.tracks[onetrack]["start_x"] + 1158) / 2) #Center of the width of the tail/box
                svg_tracks = svg_tracks + "<text x=\"" + label_x + "\" y=\"" + label_y + "\" fill=\"" + track_fontcolor + "\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(onetrack) + "</text>"

            #Add the milestones
            if "milestones" in self.tracks[onetrack]:
                for onemilestone in self.tracks[onetrack]["milestones"]:
                    milestone_year = self.tracks[onetrack]["milestones"][onemilestone]["milestone_year"]
                    milestone_division = self.tracks[onetrack]["milestones"][onemilestone]["milestone_division"]
                    #If the milestone is supposed to be on the roadmap timeframe
                    if (milestone_year >= self.roadmap_start_year and milestone_year <= self.roadmap_end_year):
                        #Build the year column by text
                        milestone_year_column = (milestone_year - self.roadmap_start_year ) + 1
                        milestone_yeartext = "Y" + str(milestone_year_column) #ex: Y2

                        #Build the division column by text
                        milestone_division_number = milestone_division[1]
                        milestone_divisiontext = self.measure + str(milestone_division_number) # ex: Q3, or H1
                        
                        year_count_text = str(self.num_years) + "Y"
                        self.tracks[onetrack]["milestones"][onemilestone]["center_x"] = self.endpoints[year_count_text][milestone_yeartext][milestone_divisiontext]

                        #Calculate & add the diamond
                        milestone_x_start = self.tracks[onetrack]["milestones"][onemilestone]["center_x"]
                        milestone_y_start = self.tracks[onetrack]["y"]
                        diamond_top = str(milestone_x_start) + " " + str(milestone_y_start - 50)
                        diamond_right = str(milestone_x_start + 20) + " " + str(milestone_y_start - 20)
                        diamond_bottom = str(milestone_x_start) + " " + str(milestone_y_start + 10)
                        diamond_left = str(milestone_x_start - 20) + " " + str(milestone_y_start - 20)
                        svg_tracks = svg_tracks + "<path d=\"M " + diamond_top + " L " + diamond_right + " L " + diamond_bottom + "L " + diamond_left + " Z\" fill=\"" +self.milestones[onemilestone]["bgcolor"] + "\" stroke=\"#000000\" stroke-miterlimit=\"10\" pointer-events=\"all\" />"

                        #Put the label on the diamond
                        label_y = str(milestone_y_start - 15)
                        label_x = str(milestone_x_start)
                        svg_tracks = svg_tracks + "<text x=\"" + label_x + "\" y=\"" + label_y + "\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"14px\" text-anchor=\"middle\">" + self.milestones[onemilestone]["letter"] + "</text>"
            
            track_number = track_number + 1
        
        svg_tracks = svg_tracks + "</g>"
        return svg_tracks

    def __build_opening(self):
        #Loop through the tracks to find the highest Y value
        last_y = 500
        for onetrack in self.tracks:
            if self.tracks[onetrack]["y"] > last_y:
                last_y = self.tracks[onetrack]["y"]
        last_y = last_y + 150

        svg_opening = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        svg_opening = svg_opening + "<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">"
        svg_opening = svg_opening + "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" width=\"1200px\" height=\"" + str(last_y) + "px\">"
        return svg_opening

    def __build_year_boxes(self,num_years):
        #Build the year boxes
        self.svg_year_boxes = "<g id=\"yearBoxes\">"
        if num_years == 1:
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"0\" y=\"70\" width=\"1200\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"600\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year) + "</text>"
        elif num_years == 2:
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"0\" y=\"70\" width=\"595\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"298\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year) + "</text>"
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"605\" y=\"70\" width=\"595\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"903\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year + 1) + "</text>"
        elif num_years == 3:
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"0\" y=\"70\" width=\"390\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"195\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year) + "</text>"
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"405\" y=\"70\" width=\"390\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"600\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year + 1) + "</text>"
            self.svg_year_boxes = self.svg_year_boxes + "<rect x=\"810\" y=\"70\" width=\"390\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
            self.svg_year_boxes = self.svg_year_boxes + "<text x=\"1005\" y=\"90\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(self.roadmap_start_year + 2) + "</text>"
        self.svg_year_boxes = self.svg_year_boxes + "</g>"

    def __build_division_boxes(self):
        #Build the division boxes
        svg_division_boxes = "<g id=\"yearDivisionBoxes\">"
        if self.num_years == 1:
            if self.measure == "H":
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"595\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"298\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"    
                svg_division_boxes = svg_division_boxes + "<rect x=\"605\" y=\"104\" width=\"595\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"903\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
            else:
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"148\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"301\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"449\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"603\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"751\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"905\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1053\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
        elif self.num_years == 2:
            if self.measure == "H":
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"148\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"300\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"448\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"605\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"753\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"905\" y=\"104\" width=\"295\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1053\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
            else:
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"73\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"150\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"223\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"300\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"373\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"450\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"523\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"605\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"678\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"755\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"828\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"905\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"978\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"1055\" y=\"104\" width=\"145\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1128\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
        elif self.num_years == 3:
            if self.measure == "H":
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"95\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"200\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"295\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"405\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"500\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"605\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"700\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"810\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"905\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"1010\" y=\"104\" width=\"190\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1105\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">H2</text>"
            else:
                svg_division_boxes = svg_division_boxes + "<rect x=\"0\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"48\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"98\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"146\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"197\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"245\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"295\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"343\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"405\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"453\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"503\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"551\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"602\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"650\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"700\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"748\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"810\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"858\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q1</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"908\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"956\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q2</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"1007\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1055\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q3</text>"
                svg_division_boxes = svg_division_boxes + "<rect x=\"1105\" y=\"104\" width=\"95\" height=\"30\" rx=\"4.5\" ry=\"4.5\" fill=\"#ffffff\" stroke=\"#000000\" pointer-events=\"all\" />"
                svg_division_boxes = svg_division_boxes + "<text x=\"1153\" y=\"124\" fill=\"#000000\" font-family=\"Helvetica\" font-size=\"16px\" text-anchor=\"middle\">Q4</text>"
        svg_division_boxes = svg_division_boxes + "</g>"
        return svg_division_boxes

    def __round_division(self,division):
        """Round the requested division as needed.  Pass directly through if it's fine"""
        if self.measure != division[0].upper():
            if self.measure == "H" and division[0].upper() == "Q":
                #If first half of year, set to H1.  Otherwise H2
                if int(division[1]) < 3:
                    division_out = "H1"
                else:
                    division_out = "H2"
            elif self.measure == "Q" and division[0].upper() == "H":
                #if first half of the year, set to Q2.  Otherwise Q4
                if int(division[1]) == 1:
                    division_out = "Q2"
                else:
                    division_out = "Q4"
        else:
            division_out = division.upper()
        return division_out

    def build_image(self):
        """Compile all of the pieces into one svg string"""

        #Build the title box
        self.__build_title_box()
        
        #Build the year boxes
        self.__build_year_boxes(self.num_years)
        
        #Build the division boxes
        svg_division_boxes = self.__build_division_boxes()
        
        #Build the tracks
        svg_tracks = self.__build_tracks()
        
        #Build the footer
        svg_footer = self.__build_footer()

        #Build the opening SVG block.  This has to be last in order to set the height properly
        svg_opening = self.__build_opening()

        #Build the SVG closing block
        svg_closing = "</svg>"

        svg = svg_opening
        svg = svg + self.svg_title
        svg = svg + self.svg_year_boxes
        svg = svg + svg_division_boxes
        svg = svg + svg_tracks
        svg = svg + svg_footer
        svg = svg + svg_closing

        return svg
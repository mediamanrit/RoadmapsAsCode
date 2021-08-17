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
        if self.measure == "H":
            self.columns = 2 * self.num_years
        else:
            self.columns = 4 * self.num_years

        #Set the defaults
        self.title_bg_color = "#FFFFFF"
        self.title_text_color = "#000000"
        self.tracks = {}
        self.milestones = {}
        self.first_track_y = 210
        self.spacing_track_y = 85
        self.footer_text = ""
        self.footer_text_color = "#000000"

        self.trackopt_gradient = False
        self.trackopt_height = 40

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

        #create the dict for the column-based endpoints
        self.column_endpoints = {}
        self.column_endpoints["1YQ"] = {}
        self.column_endpoints["1YQ"][1] = 150
        self.column_endpoints["1YQ"][2] = 450
        self.column_endpoints["1YQ"][3] = 760
        self.column_endpoints["1YQ"][4] = 1060
        self.column_endpoints["1YH"] = {}
        self.column_endpoints["1YH"][1] = 300
        self.column_endpoints["1YH"][2] = 900
        
        self.column_endpoints["2YQ"] = {}
        self.column_endpoints["2YQ"][1] = 73
        self.column_endpoints["2YQ"][2] = 223
        self.column_endpoints["2YQ"][3] = 373
        self.column_endpoints["2YQ"][4] = 523
        self.column_endpoints["2YQ"][5] = 678
        self.column_endpoints["2YQ"][6] = 828
        self.column_endpoints["2YQ"][7] = 978
        self.column_endpoints["2YQ"][8] = 1128
        self.column_endpoints["2YH"] = {}
        self.column_endpoints["2YH"][1] = 148
        self.column_endpoints["2YH"][2] = 448
        self.column_endpoints["2YH"][3] = 753
        self.column_endpoints["2YH"][4] = 1053

        self.column_endpoints["3YQ"] = {}
        self.column_endpoints["3YQ"][1] = 48
        self.column_endpoints["3YQ"][2] = 146
        self.column_endpoints["3YQ"][3] = 245
        self.column_endpoints["3YQ"][4] = 343
        self.column_endpoints["3YQ"][5] = 453
        self.column_endpoints["3YQ"][6] = 551
        self.column_endpoints["3YQ"][7] = 650
        self.column_endpoints["3YQ"][8] = 748
        self.column_endpoints["3YQ"][9] = 858
        self.column_endpoints["3YQ"][10] = 956
        self.column_endpoints["3YQ"][11] = 1055
        self.column_endpoints["3YQ"][12] = 1153
        self.column_endpoints["3YH"] = {}
        self.column_endpoints["3YH"][1] = 95
        self.column_endpoints["3YH"][2] = 295
        self.column_endpoints["3YH"][3] = 500
        self.column_endpoints["3YH"][4] = 700
        self.column_endpoints["3YH"][5] = 905
        self.column_endpoints["3YH"][6] = 1105

        self.column_endpoints["4YH"] = {}
        self.column_endpoints["4YH"][1] = 0
        self.column_endpoints["4YH"][2] = 0
        self.column_endpoints["4YH"][3] = 0
        self.column_endpoints["4YH"][4] = 0
        self.column_endpoints["4YH"][5] = 0
        self.column_endpoints["4YH"][6] = 0
        self.column_endpoints["4YH"][7] = 0
        self.column_endpoints["4YH"][8] = 0

        self.column_endpoints["5YH"] = {}
        self.column_endpoints["5YH"][1] = 0
        self.column_endpoints["5YH"][2] = 0
        self.column_endpoints["5YH"][3] = 0
        self.column_endpoints["5YH"][4] = 0
        self.column_endpoints["5YH"][5] = 0
        self.column_endpoints["5YH"][6] = 0
        self.column_endpoints["5YH"][7] = 0
        self.column_endpoints["5YH"][8] = 0
        self.column_endpoints["5YH"][9] = 0
        self.column_endpoints["5YH"][10] = 0

        my_marker = str(self.num_years) + "Y" + self.measure
        self.my_column_endpoints = self.column_endpoints[my_marker]
        
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
    
    def set_track_options(self, gradient_fill:bool=None):
        """Set options for all tracks"""
        try:
            if gradient_fill is not None:
                self.trackopt_gradient = gradient_fill
        except:
            raise

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

        #Calculate what columns the milestones should go in for this roadmap...
        #If the milestone is supposed to be on the roadmap timeframe
        if (milestone_year >= self.roadmap_start_year and milestone_year <= self.roadmap_end_year):
            if self.measure == "H":
                bigstep = 2 * (milestone_year - self.roadmap_start_year )
            else:
                bigstep = 4 * (milestone_year - self.roadmap_start_year )
            
            littlestep = int(adjusted_milestone[1])
            self.tracks[track_name]["milestones"][milestone_name]["milestone_column"] = bigstep + littlestep
            print("added milestone for column " + str(bigstep + littlestep))

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
        svg_gradients = "<defs>"
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

            #First check to see if we are supposed to do gradients, AND if we have milestones
            if self.trackopt_gradient and "milestones" in self.tracks[onetrack]:
                #go through the milestones and build the color maps for the gradients.
                    milestone_order={}
                    for onemilestone in self.tracks[onetrack]["milestones"]:
                        if not "milestone_column" in self.tracks[onetrack]["milestones"][onemilestone]:
                            continue
                        mcolumn = self.tracks[onetrack]["milestones"][onemilestone]["milestone_column"]
                        #mbg = self.milestones[onemilestone]["bgcolor"]
                        milestone_order[mcolumn] = onemilestone

                        currentkey = 0
                        prevkey = None
                        #Loop through the milestones, sorted by column number.
                        for ordered_mkey in sorted(milestone_order.keys()):
                            currentkey = ordered_mkey
                            if prevkey == None:
                                prevkey = currentkey
                                continue

                            #Build the graident definition for the previous color to the current color
                            sanitized_track_name = onetrack.replace(" ","_")
                            svg_gradient_name = "gradient_" + sanitized_track_name + "_" + milestone_order[prevkey] + "_to_" + milestone_order[currentkey]
                            svg_gradient_start = self.milestones[milestone_order[prevkey]]["bgcolor"]
                            svg_gradient_end = self.milestones[milestone_order[currentkey]]["bgcolor"]
                            svg_gradients = svg_gradients + "<linearGradient x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"0%\" id=\"" + svg_gradient_name + "\">"
                            svg_gradients = svg_gradients + "<stop offset=\"0%\" stop-color=\"" + svg_gradient_start + "\" />"
                            svg_gradients = svg_gradients + "<stop offset=\"100%\" stop-color=\"" + svg_gradient_end + "\" />"
                            svg_gradients = svg_gradients + "</linearGradient>"

            #Create the lines
            #First check to see if we are supposed to do gradients, AND if we have milestones.  If so,
            #draw boxes for the gradients.  If not, draw the big boxes
            if self.trackopt_gradient and "milestones" in self.tracks[onetrack]:
                #If the end is on the page, make it a rectangle w/ a milestone at the end as defined
                if self.tracks[onetrack]["end_x"] < 1200:
                    #If the track starts at the left edge,
                    if self.tracks[onetrack]["start_x"] == 0:
                        #Loop through the milestones in ordered manor
                        currentkey = 0
                        prevkey = None
                        first_box = True
                        #Loop through the milestones, sorted by column number.
                        for ordered_mkey in sorted(milestone_order.keys()):
                            currentkey = ordered_mkey
                            #If this is the first one, start X at 0
                            if prevkey == None:
                                prevkey = currentkey
                                continue
                            #Otherwise, start at the column position
                            else:
                                if first_box:
                                    this_start_x = 0
                                    first_box = False
                                else:
                                    this_start_column = self.tracks[onetrack]["milestones"][milestone_order[prevkey]]["milestone_column"]
                                    this_start_x = self.my_column_endpoints[this_start_column]
                                
                                this_end_column = self.tracks[onetrack]["milestones"][milestone_order[currentkey]]["milestone_column"]
                                this_end_x = self.my_column_endpoints[this_end_column]

                                sanitized_track_name = onetrack.replace(" ","_")
                                target_gradient_url = "url(#gradient_" + sanitized_track_name + "_" + milestone_order[prevkey] + "_to_" + milestone_order[currentkey] + ")"
                                box = self.__create_one_box(int(this_start_x),int(this_end_x),int(self.tracks[onetrack]["y"]),target_gradient_url,track_fontcolor)
                                svg_tracks = svg_tracks + box
                    #The track starts in the middle of the page
                    else:
                        #Loop through the milestones in ordered manor
                        currentkey = 0
                        prevkey = None
                        #Loop through the milestones, sorted by column number.
                        for ordered_mkey in sorted(milestone_order.keys()):
                            currentkey = ordered_mkey
                            #If this is the first one, start X at 0
                            if prevkey == None:
                                prevkey = currentkey
                                continue
                            #Otherwise, start at the column position
                            else:
                                this_start_column = self.tracks[onetrack]["milestones"][milestone_order[prevkey]]["milestone_column"]
                                this_start_x = self.my_column_endpoints[this_start_column]
                                
                                this_end_column = self.tracks[onetrack]["milestones"][milestone_order[currentkey]]["milestone_column"]
                                this_end_x = self.my_column_endpoints[this_end_column]

                                sanitized_track_name = onetrack.replace(" ","_")
                                target_gradient_url = "url(#gradient_" + sanitized_track_name + "_" + milestone_order[prevkey] + "_to_" + milestone_order[currentkey] + ")"
                                box = self.__create_one_box(int(this_start_x),int(this_end_x),int(self.tracks[onetrack]["y"]),target_gradient_url,track_fontcolor)
                                svg_tracks = svg_tracks + box
                        pass
                #If the end is off page, make it an arrow
                else:
                    pass
            else:
                #If the end is on the page, make it a rectangle
                if self.tracks[onetrack]["end_x"] < 1200:
                    box = self.__create_one_box(int(self.tracks[onetrack]["start_x"]),int(self.tracks[onetrack]["end_x"]),int(self.tracks[onetrack]["y"]),track_bgcolor,track_fontcolor)
                    svg_tracks = svg_tracks + box

                    #Add the text
                    label_y = str(self.tracks[onetrack]["y"] - 13)
                    label_x = str((self.tracks[onetrack]["start_x"] + self.tracks[onetrack]["end_x"]) / 2) #Center of the width of the tail/box
                    svg_tracks = svg_tracks + "<text x=\"" + label_x + "\" y=\"" + label_y + "\" fill=\"" + track_fontcolor + "\" font-family=\"Helvetica\" font-size=\"18px\" text-anchor=\"middle\">" + str(onetrack) + "</text>"

                #If the end is off page, make it an arrow.
                else:
                    #define points for the arrow (7 total)
                    tail_bottom_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"]) #Start, bottom left of arrow path
                    tail_top_left = str(self.tracks[onetrack]["start_x"]) + " " + str(self.tracks[onetrack]["y"] - self.trackopt_height) #Point 1
                    tail_top_right = "1158 " + str(self.tracks[onetrack]["y"] - self.trackopt_height) # Point 2
                    arrow_left_up = "1158 "+ str(self.tracks[onetrack]["y"] - self.trackopt_height - 20) # point 3
                    arrow_right_out = "1199.5 " + str(self.tracks[onetrack]["y"] - (self.trackopt_height / 2))
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
        svg_gradients = svg_gradients + "</defs>"

        retval = svg_gradients + svg_tracks
        return retval

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

    def __convert_division_to_column(self,year_in:str,step_in:int):
        """Take in a division format like Y1 2H and convert it to a column position"""
        try:
            if (year_in >= self.roadmap_start_year and year_in <= self.roadmap_end_year):
                if self.measure == "H":
                    bigstep = 2 * (year_in - self.roadmap_start_year )
                else:
                    bigstep = 4 * (year_in - self.roadmap_start_year )
                
                column = bigstep + step_in
                return column
            else:
                raise("Year not on the roadmap")
        except:
            raise

    def __create_one_box(self,start_x:int,end_x:int,start_y:int,bg_color:str,line_color:str):
        """Creates an SVG box"""
        bottom_left = str(start_x) + " " + str(start_y) #Start, bottom left of box
        top_left = str(start_x) + " " + str(start_y - self.trackopt_height) #Point 1
        top_right = str(end_x) + " " + str(start_y - self.trackopt_height) # Point 2
        bottom_right = str(end_x) + " " + str(start_y)
        
        box_svg = "<path d=\"M " + bottom_left + " L " + top_left + " L " + top_right + " L " + bottom_right + " Z\" fill=\"" + bg_color + "\" stroke=\"" + line_color + "\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" pointer-events=\"all\" />"

        return box_svg

    def __create_one_arrow_box(self,start_x:int,start_y:int,bg_color:str,line_color:str):
        """Creates an SVG arrow box"""
        #define points for the arrow (7 total)
        tail_bottom_left = str(start_x) + " " + str(start_y) #Start, bottom left of arrow path
        tail_top_left = str(start_x) + " " + str(start_y - self.trackopt_height) #Point 1
        tail_top_right = "1158 " + str(start_y - self.trackopt_height) # Point 2
        arrow_left_up = "1158 "+ str(start_y - self.trackopt_height - 20) # point 3
        arrow_right_out = "1199.5 " + str(start_y - (self.trackopt_height / 2))
        arrow_right_in = "1158 " + str(start_y + 20)
        arrow_left_down = "1158 " + str(start_y)
        
        #Add the arrow
        box_svg = "<path d=\"M " + tail_bottom_left + " L " + tail_top_left + " L " + tail_top_right + " L " + arrow_left_up + " L " + arrow_right_out + " L " + arrow_right_in + " L " + arrow_left_down + " Z\" fill=\""+ bg_color + "\" stroke=\"" + line_color + "\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" pointer-events=\"all\" />"
        
        return box_svg

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
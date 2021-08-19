from datetime import datetime
from roadmap import Roadmap

class JSON2roadmap:
    """Class to convert a json formatted dictionary to a roadmap object"""
    def __init__(self,schema_version: int,json_dictionary: dict):
        """Initalize the object"""
        self.json_dictionary = json_dictionary
        self.__load_json_dict()

    def get_roadmap(self):
        """Create and Return a roadmap object"""
        #Create the roadmap
        r = Roadmap(self.roadmap_title,self.roadmap_years,self.start_year,self.roadmap_measure)
        if self.gradient_fill == True:
            r.set_track_options(gradient_fill=True)

        #Add the milestone definitions
        for one_milestone_def in self.json_dictionary["milestones"]:
            milestone_color = self.json_dictionary["milestones"][one_milestone_def]["color"]
            milestone_letter = self.json_dictionary["milestones"][one_milestone_def]["letter"]
            r.add_milestone_definition(one_milestone_def, milestone_color,milestone_letter)

        #Add the tracks & their specific milestone points
        for one_track in self.json_dictionary["tracks"]:
            beginYear = int(self.json_dictionary["tracks"][one_track]["beginYear"])
            beginDivision = self.json_dictionary["tracks"][one_track]["beginDivision"]
            endYear = int(self.json_dictionary["tracks"][one_track]["endYear"])
            endDivision = self.json_dictionary["tracks"][one_track]["endDivision"]
            r.add_track(one_track,beginYear,beginDivision,endYear,endDivision)

            if "milestones" in self.json_dictionary["tracks"][one_track]:
                for one_track_milestone in self.json_dictionary["tracks"][one_track]["milestones"]:
                    milestone_year = int(self.json_dictionary["tracks"][one_track]["milestones"][one_track_milestone]["year"])
                    milestone_division = self.json_dictionary["tracks"][one_track]["milestones"][one_track_milestone]["division"]
                    r.add_track_milestone(one_track,one_track_milestone,milestone_year,milestone_division)

        if not self.footer_text == None:
            r.set_footer_text(footer_text)

        svg_out = r.build_image()

        return svg_out

    def __load_json_dict(self):
        """Validate the data that in the json dict and load the basic options"""

        #Parse out the required fields
        try:
            if "schemaVersion" in self.json_dictionary:
                self.schema_version = int(self.json_dictionary["schemaVersion"])
            else:
                self.schema_version = 1
            
            if "title" in self.json_dictionary:
                self.roadmap_title = self.json_dictionary["title"]
            else:
                raise ValueError ("Missing required parameter: title")
            
            if "years" in self.json_dictionary:
                self.roadmap_years = int(self.json_dictionary["years"])
            else:
                raise ValueError ("Missing required parameter: years")
            
            if "measure" in self.json_dictionary:
                self.roadmap_measure = self.json_dictionary["measure"]
            else:
                raise ValueError ("Missing required parameter: measure")
        except:
            raise

        #Set the optional fields
        if "titleBGColor" in self.json_dictionary:
            self.title_bg_color = self.json_dictionary["titleBGColor"]
        else:
            self.title_bg_color = "#FFFFFF"

        if "titleTextColor" in self.json_dictionary:
            self.title_text_color = self.json_dictionary["titleTextColor"]
        else:
            self.title_text_color = "#000000"

        if "gradientFill" in self.json_dictionary:
            if self.json_dictionary["gradientFill"].lower() == "true":
                self.gradient_fill = True
        else:
            self.gradient_fill = False

        if "footer_text" in self.json_dictionary:
            self.footer_text = self.json_dictionary["footerText"]
        else:
            self.footer_text = None

        if "startYear" in self.json_dictionary:
            self.start_year = self.json_dictionary["startYear"]
        else:
            today = datetime.today()
            self.start_year = today.year

        try:
            #Validate options
            if int(self.roadmap_years) > 3 and roadmap_measure == "Q" :
                raise ValueError ("ERROR: Can't have quarter resolution beyond 3 years")

            if int(self.roadmap_years) > 5:
                raise ValueError ("ERROR: Can't have more then 5 years in a drawing")

        except:
            raise
#Static test, 3 years w/ quarter resolution
import os
from roadmap import Roadmap
r = Roadmap("Static RM Test",3,2020,"Q")
r.set_track_options(gradient_fill=True)

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

#Line that starts and goes out
r.add_track("Test Track 2",2021,"Q1",2029,"Q4")
r.add_track_milestone("Test Track 2","Emerging",2021,"Q1")

#Line that starts and ends
r.add_track("Test Track 3",2020,"Q1",2022,"Q2")
r.add_track_milestone("Test Track 3","Standard",2020,"Q1")
r.add_track_milestone("Test Track 3","Containment",2021,"Q3")
r.add_track_milestone("Test Track 3","Retirement",2022,"Q2")
r.add_track_milestone("Test Track 3","Retired",2022,"Q2")

#Line that goes through w/o milestones on the screen
r.add_track("Test Track 4",2010,"Q2",2029,"Q3")
r.add_track_milestone("Test Track 4","Standard",2010,"Q2")
r.add_track_milestone("Test Track 4","Containment",2029,"Q3")

#Line that goes through w milestones
r.add_track("Test Track 5",2011,"Q2",2029,"Q3")
r.add_track_milestone("Test Track 5","Emerging",2012,"Q4")
r.add_track_milestone("Test Track 5","Standard",2019,"Q1")
r.add_track_milestone("Test Track 5","Containment",2020,"Q4")
r.add_track_milestone("Test Track 5","Retirement",2022,"Q4")
r.add_track_milestone("Test Track 5","Retired",2029,"Q2")

#Line that starts and ends, with only one milestone
r.add_track("Test Track 6",2020,"Q1",2022,"Q2")
r.add_track_milestone("Test Track 6","Emerging",2020,"Q2")

#Line that starts and stops w/ no milestones on the screen
r.add_track("Test Track 7",2020,"Q3",2022,"Q1")




#Add a footer
r.set_footer_text("Some footer text would go here")

out = r.build_image()

destname = "test-gradient-3YQ.svg"
if os.path.exists(destname):
    os.remove(destname)

f = open(destname,"x")
f.write(out)
f.close()
exit()
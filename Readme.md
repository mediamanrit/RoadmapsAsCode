# Roadmaps As Code
---
## Overview
Technology owners and planners spend a lot of time each year in drawing tools keeping visuals of tech roadmaps up to date. They also need to track deltas over the years to ensure proper history is kept. Wouldn't it be nice if that was easier?

That's the intent behind Roadmaps As Code.  A technologist uses JSON formatted data to produce roadmaps.  Think of how much better this is:
1. Create the base file when Windows NT 3.5 is adopted by your group/company.
2. As new versions of Windows are released, adopeted, and retired you continually add the time definitions to the file.
3. At any point you ask the program to give you a multi-year graphical view over any year span.
4. You get time back producing time consuming visuals every year.

Key features of the tool:
* Common JSON format used for everything
* Flexible milestone definitions that can utilize your existing taxonomy
* Modular code, so you can use it how you see fit (embedded in a website, command line based, etc)
* SVG output of all graphics, consumable virtually anywhere

My end goal is to create a tool that can be consumed in real time displaying current state or past states of architecture roadmaps and plans.

---
## Usage
To use the class, see the [Readme file](https://github.com/mediamanrit/RoadmapsAsCode/blob/main/roadmap/Readme.md) in the roadmap folder.

---
## Sample
This sample was generated using the JSON2roadmap class:

![Sample roadmap](https://raw.githubusercontent.com/mediamanrit/RoadmapsAsCode/main/docs/sample.svg)


# Help for the inner workings of the Roadmap module
---
## Description
The Roadmap module provides the core functionality of the Roadmaps As Code toolset.  In it lives classes that produce the different types of roadmap visuals.

---
## Usage

---
## Example

---
## Roadmap class inner workings
* self variables
    * name (str) = Title of the roadmap 
    * num_years (int) = Number of years on the roadmap
    * roadmap_start_year (int) = The year the roadmap starts
    * measure (str) = measure
    * roadmap_end_year (int) = The year the roadmap ends.  This is derrived from roadmap_start_year and num_years
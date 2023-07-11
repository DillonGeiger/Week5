# Week5-PythonToolbox_TornadoTools
author: Dillon Geiger

Hello, 
This repository is for the Python toolbox tornadotools. In this toolbox there are currently (4) tools that pertain to tornado data.

TornadoSelection() makes a user Input selection based off the following criteria: Within a date range, within a state, and of a specific magnitude.

TornadoBuffer() makes a user input buffer based off the following criteria: desired distance and desired output name.

CountyTornado() makes a user input new feature class based off the following criteria: state, county, year. The new feature class is out named with the format countystateyear. New fields are added to the new feature class labeled: inj_t, fat_t, cost_t, and year. the fields are then populated with the total number of injuries, fatalities, and costs for the given year.

PathSelection() Makes a user input selection based off the following criteria: Within a state, magnitude, distance, with optional year and date range.

The attached files include an initial python script and a python tool script For all tools except tornado buffer due to the simplicity of script. Additionally there are python toolbox files for every tool and for the python toolbox.


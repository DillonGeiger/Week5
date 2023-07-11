#Create a new Python Toolxbox that will allow the user to select tornado paths based on state, magnitude, path length > a 
#specific distance, and optionally a year or date range (provide both options)

import arcpy
in_tornado = parameters[0].valueAsText
state = parameters[1].valueAsText
magnitude = parameters[2].valueAsText
path_len_sql = parameters[3].valueAsText

#OPTIONAL
year = parameters[4].valueAsText
start_date = parameters[5].valueAsText
end_date = parameters[6].valueAsText

# make state selections
state_sql = "st = '{}'".format(state)
state_sel = arcpy.management.SelectLayerByAttribute(in_tornado, 'NEW_SELECTION', state_sql)
statelyr = arcpy.management.CopyFeatures (state_sel, 'state_sel')

# make mag selections
mag_sql = "mag = {}".format(magnitude)
mag_sel = arcpy.management.SelectLayerByAttribute('state_sel', 'SUBSET_SELECTION', mag_sql)
maglyr = arcpy.management.CopyFeatures (mag_sel, 'mag_sel')

# make mag selections
path_len_sel = arcpy.management.SelectLayerByAttribute('mag_sel', 'SUBSET_SELECTION', path_len_sql)
path_len_lyr = arcpy.management.CopyFeatures (path_len_sel, 'path_len_sel')

#make year selection
year_sql = "yr = {}".format(year)
year_sel = arcpy.management.SelectLayerByAttribute('path_len_sel', 'SUBSET_SELECTION', year_sql)
yearlyr= arcpy.management.CopyFeatures (year_sel, 'year_sel')

#date range selection 
date_sql = "date >='" + start_date + "'AND date <='" + end_date + "'"
date_sel = arcpy.management.SelectLayerByAttribute('path_len_sel', 'SUBSET_SELECTION', date_sql)
yearlyr= arcpy.management.CopyFeatures (date_sel, 'date_sel')
#source code for the development of a python toolbox in arcgis Pro.
#Author: Dillon Geiger
#import arcpy 
#define source data

import arcpy
in_fc = "tornado_initpoint"

#made date selection *within range*
date_SQL = """date BETWEEN '1960-01-01' AND '2020-01-01'"""
date_sel = arcpy.management.SelectLayerByAttribute(in_fc, "NEW_SELECTION", date_SQL)
datelyr = arcpy.management.GetCount(date_sel)
arcpy.AddMessage(datelyr)

#of the selection make an aditional selection WITHIN a state.
state_SQL = """st = 'CO'"""
state_sel = arcpy.management.SelectLayerByAttribute(date_sel, "SUBSET_SELECTION", state_SQL)
statelyr = arcpy.management.GetCount(state_sel)
arcpy.AddMessage(statelyr)

##with the results make a final selection 
mag_SQL = """mag = 2"""
mag_sel = arcpy.management.SelectLayerByAttribute(state_sel, "SUBSET_SELECTION", mag_SQL)
maglyr = arcpy.management.GetCount(mag_sel)
arcpy.AddMessage(maglyr)

#export the results as a new fc.
out_fc = "TornadoSelection"
arcpy.management.CopyFeatures(in_fc, out_fc)

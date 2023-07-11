# Create a new Python Toolbox that will allow the user to select a US state/county and year, returns injuries, fatalities, and
# damage costs for that county and year as a new feature class named in the format CountyStateYear, e.g. AdamsWI1994.
# The feature geography will be the county
# Feature attributes will include new columns for injuries, fatalities, cost and year; these will be populated with the
# sum of injuries, fatalities, and cost. You will want to use cursors to populate the attributes.


import arcpy

in_boundary = parameters[0].valueAsText
in_tornado = parameters[1].valueAsText
state = parameters[2].valueAsText
county = parameters[3].valueAsText
year = parameters[4].valueAsText
# make State selection boundary selection
state_SQL = "STUSPS ='" + state + "'"
state_sel = arcpy.management.SelectLayerByAttribute(
    in_boundary, 'NEW_SELECTION', state_SQL)

# make county selection based off state selection and
county_SQL = "NAME ='" + county + "'"
county_sel = arcpy.management.SelectLayerByAttribute(
    state_sel, 'SUBSET_SELECTION', county_SQL)

# export as new fc
out_fc = str("{}{}{}".format(county, state, year))
new_fc = arcpy.management.CopyFeatures(county_sel, out_fc)

# make tornado selection based off year
year_SQL = "yr = {}".format(year)
tornado_sel = arcpy.management.SelectLayerByAttribute(
    in_tornado, 'NEW_SELECTION', year_SQL)

# make selection of tornado_sel within new fc
tornado_clip = arcpy.analysis.Clip(tornado_sel, new_fc, "Tornado_Clip")

# create new fields in new_fc and populate with clip values
year_field = ["year", 'LONG', "year", "year"]
inj_field = ["total_injuries", 'LONG', "inj_t"]
fatal_field = ["total_fatalities", 'LONG', "fatal_t"]
cost_field = ["total_cost", 'LONG', "cost_t"]
new_fields = arcpy.management.AddFields(
    new_fc, [year_field, inj_field, fatal_field, cost_field])


# populate new fields with attribute data from tornado_clip
fields_S = ['yr', 'inj', 'fat', 'loss', 'closs']
inj_list = []
fat_list = []
cost_list = []
with arcpy.da.SearchCursor('Tornado_Clip', fields_S) as cursor:
    for row in cursor:
        year = row[0]
        inj = row[1]
        fat = row[2]
        cost = row[3] + row[4]
        inj_list.append(inj)
        fat_list.append(fat)
        cost_list.append(cost)

year_cal = arcpy.management.CalculateField(new_fc, 'year', year)
inj_cal = arcpy.management.CalculateField(new_fc, 'inj_t', sum(inj_list))
inj_cal = arcpy.management.CalculateField(new_fc, 'fat_t', sum(fat_list))
inj_cal = arcpy.management.CalculateField(new_fc, 'cost_t', sum(cost_list))
arcpy.management.SelectLayerByAttribute(in_boundary, 'CLEAR_SELECTION')
arcpy.management.SelectLayerByAttribute(in_tornado, 'CLEAR_SELECTION')
print("done")
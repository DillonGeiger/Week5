 wksp = arcpy.evn.workspace = "C:\\Dillon Geiger\\GIS_4085_Python_II\\week5\\week5.gdb"
        in_feature = parameters[0].valueAsText
        start_date = parameters[1].valueAsText
        end_date = parameters[2].valueAsText
        state = parameters[3].valueAsText
        magnitude = parameters[4].valueAsText

        #made date selection *within range*
        date_SQL = """date BETWEEN '{}' AND '{}'""".format(start_date, end_date)
        datelyr = arcpy.management.SelectLayerByAttribute(in_feature, "NEW_SELECTION", date_SQL)
        datecnt = arcpy.management.GetCount(datelyr)
        arcpy.AddMessage(datecnt)
        arcpy.management.CopyFeatures(datelyr, 'date_test')

        #of the selection make an aditional selection WITHIN a state.
        stlyr = arcpy.management.SelectLayerByAttribute(datelyr, "SUBSET_SELECTION", state)
        stcnt = arcpy.management.GetCount(stlyr)
        arcpy.AddMessage(stcnt)
        arcpy.management.CopyFeatures(stlyr, 'state_test')

        #with the results make a final selection 
        mag_SQL = """mag = {}""".format(magnitude)
        maglyr = arcpy.management.SelectLayerByAttribute(stlyr, "SUBSET_SELECTION", mag_SQL)
        magcnt = arcpy.management.GetCount(maglyr)
        arcpy.AddMessage(magcnt)
        arcpy.management.CopyFeatures(maglyr, 'mag_test')


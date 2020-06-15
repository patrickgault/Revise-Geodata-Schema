## PROJECT:  Geodata Processing
## AUTHOR:   Patrick Gault
## LICENSE:  MIT
## DATE:     2020-06-01
## UPDATED:  


# Import Site Packages
import arcpy
​
# Environment Settings
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = "4326"
​
# Set workspace
ProjectFolder = 
​
​
# 1. Import Data to Processing GDB ------------------------------------------------------------------

DataIn1 = ProjectFolder + "\\" + "Input_Data\\lby_adm_unosat_lbsc_20180507.gdb" # Update the Data In folders to reflect source data
DataIn2 = ProjectFolder + "\\" + "Input_Data\\zwe_adm_zimstat_ocha_itos_20180911.gdb"
DataIn3 = ProjectFolder + "\\" + "Input_Data\\dji_adm_fews_shp"
ProcessingGDB = ProjectFolder + "\\" + "Processing\\Processing.gdb"
OutputGDB = ProjectFolder + "\\" + "DIS_Data_Standards.gdb"
ShapefileOutput = ProjectFolder + "\\" + "Output_SHP"
​
arcpy.env.workspace = DataIn1
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    arcpy.FeatureClassToGeodatabase_conversion(fc, ProcessingGDB)
    
arcpy.env.workspace = DataIn2
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    arcpy.FeatureClassToGeodatabase_conversion(fc, ProcessingGDB)
    
arcpy.env.workspace = DataIn3
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    arcpy.FeatureClassToGeodatabase_conversion(fc, ProcessingGDB)


# 2. Create Field Dictionary and Rename Existing Fields ------------------------------------------------------------------

# CREATE DICTIONARY TO RENAME EXISTING FIELDS WITH CORRECT OUTPUT VALUES 
## Review input datasets to see if there are any fields not listed belo that should be renamed, particularly 'NL_NAME' fields
​
# Create Dictionary
d = { #Admin 0 Names and Codes
    "admin0Name_en":"NAME_0",
    "ADM0_EN":"NAME_0",
    "admin0Pcode":"ISO",
    "ADM0_PCODE":"ISO",
    
    #Admin 1 Names and Codes
    "admin1Name_en":"NAME_1",
    "admin1Name_ar":"NL_NAME_1",
    "ADM1_EN":"NAME_1",
    "ADM1_PCODE":"CCN_1",
    "admin1Pcode":"CCN_1",
     
     #Admin 2 Names and Codes
    "admin2Name_en":"NAME_2",
    "admin2Name_ar":"NL_NAME_2",
    "ADM2_EN":"NAME_2",
    "ADM2_PCODE":"CCN_2",
    "admin2Pcode":"CCN_2",
    
    #Admin 3 Names and Codes
    "admin3Name_en":"NAME_3", 
    "adminName3_ar":"NL_NAME_3",
    "ADM3_EN":"NAME_3",
    "ADM3_PCODE":"CCN_2",
    "admin3Pcode":"CCN_3",
    
    #Admin 3 Names and Codes
    "admin4Name_en":"NAME_4", 
    "adminName4_ar":"NL_NAME_4",
    "ADM4_EN":"NAME_4",
    "ADM4_PCODE":"CCN_4",
    "admin4Pcode":"CCN_4"}
​
# Rename Fields
arcpy.env.workspace = ProcessingGDB
fcList = arcpy.ListFeatureClasses() #get a list of feature classes
for fc in fcList:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name in d:
            arcpy.AlterField_management(fc, field.name, d[field.name], d[field.name])


# 3. Create Missing Fields ------------------------------------------------------------------

# CREATE FIELDS THAT ARE MISSING
## See the wildcards "*adm1*", etc. that are used to select the datasets. These won't work if the filename is "Admin1"
​
# Add Data Source and Date Fields to All Feature Classes
for fc in fcList:  #loop through feature classes
    arcpy.management.AddField(fc,'DATA_SOURCE', 'TEXT',"","","",'DATA_SOURCE')
    arcpy.management.AddField(fc,'DATE_ACCESSED', 'TEXT',"","","",'DATE_ACCESSED')
​
# Add ID and Type Fields to Each Admin Level
fcList_adm1 = arcpy.ListFeatureClasses("*adm1*") #get a list of feature classes
for fc in fcList_adm1:  #loop through feature classes
    arcpy.management.AddField(fc,'ID_0','LONG',"","","",'ID_0')
    arcpy.management.AddField(fc,'ID_1','LONG',"","","",'ID_1')
    arcpy.management.AddField(fc,'TYPE_1', 'TEXT',"","","",'TYPE_1')
    arcpy.management.AddField(fc,'ENGTYPE_1', 'TEXT',"","","",'ENGTYPE_1')
​
fcList_adm2 = arcpy.ListFeatureClasses("*adm2*") #get a list of feature classes
for fc in fcList_adm2:  #loop through feature classes
    arcpy.management.AddField(fc,'ID_0','LONG',"","","",'ID_0')
    arcpy.management.AddField(fc,'ID_1','LONG',"","","",'ID_1')
    arcpy.management.AddField(fc,'ID_2','LONG',"","","",'ID_2')
    arcpy.management.AddField(fc,'TYPE_2', 'TEXT',"","","",'TYPE_2')
    arcpy.management.AddField(fc,'ENGTYPE_2', 'TEXT',"","","",'ENGTYPE_2')
    
fcList_adm3 = arcpy.ListFeatureClasses("*adm3*") #get a list of feature classes
for fc in fcList_adm3:  #loop through feature classes
    arcpy.management.AddField(fc,'ID_0','LONG',"","","",'ID_0')
    arcpy.management.AddField(fc,'ID_1','LONG',"","","",'ID_1')
    arcpy.management.AddField(fc,'ID_2','LONG',"","","",'ID_2')
    arcpy.management.AddField(fc,'ID_3','LONG',"","","",'ID_3')
    arcpy.management.AddField(fc,'TYPE_3', 'TEXT',"","","",'TYPE_3')
    arcpy.management.AddField(fc,'ENGTYPE_3', 'TEXT',"","","",'ENGTYPE_3')
    
fcList_adm4 = arcpy.ListFeatureClasses("*adm4*") #get a list of feature classes
for fc in fcList_adm4:  #loop through feature classes
    arcpy.management.AddField(fc,'ID_0','LONG',"","","",'ID_0')
    arcpy.management.AddField(fc,'ID_1','LONG',"","","",'ID_1')
    arcpy.management.AddField(fc,'ID_2','LONG',"","","",'ID_2')
    arcpy.management.AddField(fc,'ID_3','LONG',"","","",'ID_3')
    arcpy.management.AddField(fc,'ID_4','LONG',"","","",'ID_4')
    arcpy.management.AddField(fc,'TYPE_4', 'TEXT',"","","",'TYPE_4')
    arcpy.management.AddField(fc,'ENGTYPE_4', 'TEXT',"","","",'ENGTYPE_4')

# 4. Calculate Fields ------------------------------------------------------------------

# CALCULATE ID_1-x FIELDS USING NUMBERS IN CCN FIELDS
## CCN fields are an output of renaming the PCODE fields above and the first two alpha characters are removed
​
fcList = arcpy.ListFeatureClasses() #get a list of feature classes
for fc in fcList:  #loop through feature classes
    fieldList = arcpy.ListFields(fc,"ID_*")  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        arcpy.management.CalculateField(fc, field.name, '"0"') #calculate each field to 0
        if field.name.lower() == "id_1": 
             arcpy.management.CalculateField(fc, field.name,"!CCN_1![2:]")
        elif field.name.lower() == "id_2": 
             arcpy.management.CalculateField(fc, field.name,"!CCN_2![2:]")
        elif field.name.lower() == "id_3": 
             arcpy.management.CalculateField(fc, field.name,"!CCN_3![2:]")
        elif field.name.lower() == "id_4": 
             arcpy.management.CalculateField(fc, field.name,"!CCN_4![2:]")
​
​
# DEFINE ISO, ID_O, and ADMIN UNIT TYPE VARIABLES and CALCULATE FIELDS
## Set ISO and ID_0 Variables -- See for codes: https://www.iban.com/country-codes
### 
​
Country1_ISO = '"ZWE"'
Country1_ISOWC = "zwe*"
Country1_ID_0 = "716"
Country1_Type1 = '"Province"'
Country1_EngType1 = '"Province"'
Country1_Type2 = '"District"'
Country1_EngType2 = '"District"'
Country1_Type3 = '"Ward"'
Country1_EngType3 = '"Ward"'
Country1_Type4 = '" "'
Country1_EngType4 = '" "'
Country1_DataSource = '"https://data.humdata.org/dataset/zimbabwe-administrative-levels-0-3-boundaries"'
Country1_DateAccessed = '"5/29/20"'
​
Country2_ISO = '"LBY"'
Country2_ISOWC = "lby*"
Country2_ID_0 = "434"
Country2_Type1 = '"Province"'
Country2_EngType1 = '"Province"'
Country2_Type2 = '"Muhafazat"'
Country2_EngType2 = '"Governorate"'
Country2_Type3 = '""'
Country2_EngType3 = '""'
Country2_Type4 = '" "'
Country2_EngType4 = '" "'
Country2_DataSource = '"https://data.humdata.org/dataset/admin-boundaries-villages-libya-cods"'
Country2_DateAccessed = '"5/29/20"'
​
​
Country3_ISO = '"DJI"'
Country3_ISOWC = "dji*"
Country3_ID_0 = "262"
Country3_Type1 = '"Region"'
Country3_EngType1 = '"Region"'
Country3_Type2 = '"District"'
Country3_EngType2 = '"District"'
Country3_Type3 = '""'
Country3_EngType3 = '""'
Country3_Type4 = '" "'
Country3_EngType4 = '" "'
Country3_DataSource = '"https://data.humdata.org/dataset/djibouti-administrative-levels-0-2-boundaries"'
Country3_DateAccessed = '"5/29/20"'
​
# Calculate Fields
## This only goes up to Admin 3 -- Add Admin 4 and beyond as needed.
​
fcList_Country1 = arcpy.ListFeatureClasses(Country1_ISOWC) #get a list of feature classes
for fc in fcList_Country1:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name.lower() == "id_0":
            arcpy.management.CalculateField(fc, field.name, Country1_ID_0)   
        elif field.name.lower() == "iso":
            arcpy.management.CalculateField(fc, field.name, Country1_ISO)
        elif field.name.lower() == "type_1":
            arcpy.management.CalculateField(fc, field.name,Country1_Type1)
        elif field.name.lower() == "engtype_1":
            arcpy.management.CalculateField(fc, field.name,Country1_EngType1)
        elif field.name.lower() == "type_2":
            arcpy.management.CalculateField(fc, field.name,Country1_Type2)
        elif field.name.lower() == "engtype_2":
            arcpy.management.CalculateField(fc, field.name,Country1_EngType2)
        elif field.name.lower() == "type_3":
            arcpy.management.CalculateField(fc, field.name,Country1_Type3)
        elif field.name.lower() == "engtype_3":
            arcpy.management.CalculateField(fc, field.name,Country1_EngType3)
        elif field.name.lower() == "type_4":
            arcpy.management.CalculateField(fc, field.name,Country1_Type4)
        elif field.name.lower() == "engtype_4":
            arcpy.management.CalculateField(fc, field.name,Country1_EngType4)
        elif field.name.lower() == "data_source":
            arcpy.management.CalculateField(fc, field.name,Country1_DataSource)
        elif field.name.lower() == "date_accessed":
            arcpy.management.CalculateField(fc, field.name,Country1_DateAccessed)
            
fcList_Country2 = arcpy.ListFeatureClasses(Country2_ISOWC) #get a list of feature classes
for fc in fcList_Country2:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name.lower() == "id_0":
            arcpy.management.CalculateField(fc, field.name, Country2_ID_0)   
        elif field.name.lower() == "iso":
            arcpy.management.CalculateField(fc, field.name, Country2_ISO)
        elif field.name.lower() == "type_1":
            arcpy.management.CalculateField(fc, field.name,Country2_Type1)
        elif field.name.lower() == "engtype_1":
            arcpy.management.CalculateField(fc, field.name,Country2_EngType1)
        elif field.name.lower() == "type_2":
            arcpy.management.CalculateField(fc, field.name,Country2_Type2)
        elif field.name.lower() == "engtype_2":
            arcpy.management.CalculateField(fc, field.name,Country2_EngType2)
        elif field.name.lower() == "type_3":
            arcpy.management.CalculateField(fc, field.name,Country2_Type3)
        elif field.name.lower() == "engtype_3":
            arcpy.management.CalculateField(fc, field.name,Country2_EngType3)
        elif field.name.lower() == "type_4":
            arcpy.management.CalculateField(fc, field.name,Country2_Type4)
        elif field.name.lower() == "engtype_4":
            arcpy.management.CalculateField(fc, field.name,Country2_EngType4)
        elif field.name.lower() == "data_source":
            arcpy.management.CalculateField(fc, field.name,Country2_DataSource)
        elif field.name.lower() == "date_accessed":
            arcpy.management.CalculateField(fc, field.name,Country2_DateAccessed)
            
fcList_Country3 = arcpy.ListFeatureClasses(Country3_ISOWC) #get a list of feature classes
for fc in fcList_Country3:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name.lower() == "id_0":
            arcpy.management.CalculateField(fc, field.name, Country3_ID_0)   
        elif field.name.lower() == "iso":
            arcpy.management.CalculateField(fc, field.name, Country3_ISO)
        elif field.name.lower() == "type_1":
            arcpy.management.CalculateField(fc, field.name,Country3_Type1)
        elif field.name.lower() == "engtype_1":
            arcpy.management.CalculateField(fc, field.name,Country3_EngType1)
        elif field.name.lower() == "type_2":
            arcpy.management.CalculateField(fc, field.name,Country3_Type2)
        elif field.name.lower() == "engtype_2":
            arcpy.management.CalculateField(fc, field.name,Country3_EngType2)
        elif field.name.lower() == "type_3":
            arcpy.management.CalculateField(fc, field.name,Country3_Type3)
        elif field.name.lower() == "engtype_3":
            arcpy.management.CalculateField(fc, field.name,Country3_EngType3)
        elif field.name.lower() == "type_4":
            arcpy.management.CalculateField(fc, field.name,Country3_Type4)
        elif field.name.lower() == "engtype_4":
            arcpy.management.CalculateField(fc, field.name,Country3_EngType4)
        elif field.name.lower() == "data_source":
            arcpy.management.CalculateField(fc, field.name,Country3_DataSource)
        elif field.name.lower() == "date_accessed":
            arcpy.management.CalculateField(fc, field.name,Country3_DateAccessed)
​
# 5. Delete Extra Fields ------------------------------------------------------------------

# DELETE EXTRANEOUS FIELDS 
DontDeleteFields = ['NAME_0', 'NAME_1', 'NAME_2', 'NAME_3', 'NAME_4','NL_NAME_1', 'NL_NAME_2', 'NL_NAME_3', 'NL_NAME_4',
                    'ID_0', 'ID_1', 'ID_2', 'ID_3', 'ID_4', 'ISO','TYPE_1', 'TYPE_2', 'TYPE_3', 'TYPE_4','ENGTYPE_1',
                    'ENGTYPE_2', 'ENGTYPE_3', 'ENGTYPE_4', 'VARNAME_1','VARNAME_2','VARNAME_3','VARNAME_4','CCN_1',
                    'CCN_2', 'CCN_3', 'CCN_4', 'OBJECTID', 'Shape', 'Shape_Length', 'Shape_Area', 'DATA_SOURCE', 'DATE_ACCESSED']
​
fcList = arcpy.ListFeatureClasses() #get a list of feature classes
for fc in fcList:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList:
        if field.name not in set(DontDeleteFields):
            try:
                arcpy.DeleteField_management(fc,field.name)    
            except:
                print (arcpy.GetMessages())
# 6. Rename Feature Classes and Export ------------------------------------------------------------------

# RENAME FEATURE CLASSES
#for fc in fcList_Country3:
#    if "adm1" in fc:
#        arcpy.Rename_management(fc, (Country3_ISO + "_adm1"))
​
# Export to Output GDB
OutputGDB = ProjectFolder + "\\" + "DIS_Data_Standards.gdb\\Output"
for fc in fcList:  #loop through feature classes
    arcpy.FeatureClassToGeodatabase_conversion([fc], OutputGDB)
​
​
# Export to Output Shapefile

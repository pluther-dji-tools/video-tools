#-------------------------------------------------------------------------------
# Name:        Converts DBF to SHP
# Purpose:
#-------------------------------------------------------------------------------

# Import system modules
import sys
import string
import os
import arcgisscripting

def makeShape(XY_Table, Y_Field, X_Field, Output_Feature_Class):
    # Create the Geoprocessor object
    gp = arcgisscripting.create()

    # Load required toolboxes...
    gp.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.5/ArcToolbox/Toolboxes/Data Management Tools.tbx")

    # Local variables...
    Layer_Name_or_Table_View = ""

    # Process: Make XY Event Layer...
    gp.MakeXYEventLayer_management(XY_Table, X_Field, Y_Field, Layer_Name_or_Table_View, "")

    # Process: Copy Features...
    gp.CopyFeatures_management(Layer_Name_or_Table_View, Output_Feature_Class, "", "0", "0", "0")
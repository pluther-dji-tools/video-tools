import shapefile
import csv

def convertToShape(csvFileName,xField,yField,shapeFileName):
    csvFile = open(csvFileName)

    coordinates = list(csv.DictReader(csvFile))
    shpWriter = shapefile.Writer(shapefile.LINE)
    shpWriter.autoBalance = 1
    shpWriter.field(xField,"F")
    shpWriter.field(yField,"F")

    polyLineParts = []

    for coordinate in coordinates:
        partTuple = [coordinate[xField],coordinate[yField]]
        polyLineParts.append(partTuple)

    shpWriter.line(parts=polyLineParts)
    shpWriter.save('shapefile/' + shapeFileName)

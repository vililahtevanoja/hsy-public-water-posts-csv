import shapefile
import simplekml
from pyproj import Transformer

csv_data = ["Id,Address,Longitude,Latitude\n"]

# from ETRS-GK25 (EPSG:3879) offered by HSY data, to EPSG:4326 also known as WGS84 which is accepted by Google Maps
coord_transformer = Transformer.from_crs("epsg:3879", "epsg:4326", always_xy=True)
kml = simplekml.Kml()

with shapefile.Reader("data/HSY_Vesipostit", encoding="latin") as sf:
    assert sf.shapeType == shapefile.POINT
    shapeRecs = sf.shapeRecords()
    # print(shapeRecs[0].shape.points)
    for shapeRec in shapeRecs:
        id = shapeRec.record[0]
        address = shapeRec.record[1]
        lon_utm = shapeRec.record[2]
        lat_utm = shapeRec.record[3]
        lat, lon = coord_transformer.transform(lat_utm, lon_utm)
        # print(shapeRec.record)
        line = f"{id},{address},{lat},{lon}\n"
        csv_data.append(line)
        kml.newpoint(name=address, address=address, coords=[(lat, lon)])

# print(csv_data)

with open("output.csv", "w") as f:
    f.writelines(csv_data)

kml.save("output.kml")

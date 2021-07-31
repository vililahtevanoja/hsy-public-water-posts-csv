# hsy-public-water-posts-csv

This project takes [public water post data](https://hri.fi/data/dataset/paakaupunkiseudun-vesipostit) from HSY Open data in ESRI Shape format, and outputs a CSV-file with `Id,Address,Latitude,Longitude` data, which can be e.g. imported into a Google Maps My Map.

## Installation and use

Install requirements

```
pip install -r requirements.txt
```

Get data from HSY
```
mkdir data
curl https://avoidatastr.blob.core.windows.net/avoindata/AvoinData/1_Vesi_ja_viemarit/Vesipostit/Shp/HSY_Vesipostit_shp.zip --output data.zip
unzip data.zip -d data
```

Run parser
```
python3 parser.py
```

The output is written to file named `output.csv`.

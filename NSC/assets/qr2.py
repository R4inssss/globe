# borderless_qrcode.py

import segno

qrcode = segno.make_qr("""
https://api.globe.gov/search/v1/measurement/?protocols=air_temp_monthlies&datefield=measuredDate&startdate=2010-01-01&enddate=2018-01-01&geojson=TRUE&sample=TRUE
""")
qrcode.save(
    "borderless_qrcode.png",
    scale=1,
    border=0,
)

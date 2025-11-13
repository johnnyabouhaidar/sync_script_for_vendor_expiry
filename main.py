import json
from DB_layer import *

with open('sample_payload.json', "r", encoding="utf-8") as f:
    vendorsObj = json.load(f)


#print(vendorsObj["value"])

select_from_table("SELECT * FROM [OBB_K2_ETendering].[Vendors].[RegisteredVendors]")

for vendor in vendorsObj["value"]:
    print(vendor["VendorAccountNumber"])



import json
from DB_layer import *

with open('sample_payload.json', "r", encoding="utf-8") as f:
    vendorsObj = json.load(f)


#print(vendorsObj["value"])

#select_from_table("SELECT * FROM [OBB_K2_ETendering].[Vendors].[RegisteredVendors]")




curre_vendors_from_sql = select_from_table("SELECT * FROM [OBB_K2_ETendering].[Vendors].[RegisteredVendors]")
for idx,sql_vendor in curre_vendors_from_sql.iterrows():
    for json_vendor in vendorsObj["value"]:
        if str(sql_vendor["AccountNumber"]) == json_vendor["VendorAccountNumber"]:
            print(sql_vendor["AccountNumber"])
            print(update_into_table("UPDATE [OBB_K2_ETendering].[Vendors].[RegisteredVendors] SET RenewalDate='{0}', ExpiryDate='{1}' where AccountNumber='{2}'".format(json_vendor["Expirationdate"],json_vendor["Expirationdate"],sql_vendor["AccountNumber"])))



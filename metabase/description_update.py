import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)
metabase_host = "http://localhost:3456/api"
csv_file_path = (
    "/Users/anhlai/Downloads/Survey data needs in Redshift - Tables in Redshift.csv"
)

# You must be a superuser to do this.
# get a session token to authenticate all future requests
response = requests.post(
    f"{metabase_host}/session",
    json={"username": "anhlai@remitano.com", "password": "Remi123"},
)
session_id = response.json()["id"]
# session_id, for example" '761802a2-2c04-4912-8e22-6edbb6bc32ec
headers = {"X-Metabase-Session": session_id}
# By default, sessions are good for 14 days.
print(session_id)

# === 1.Update table description
# Get all Redshift tables.
response = requests.get(f"{metabase_host}/table", headers=headers)
tables = response.json()

pp.pprint(f">>> Total Redshift tables: {len(tables)}")
redshift_table_map = {}
for table in tables:
    # print(f"=== table display name: {table['display_name']}")
    # print(f"    name: {table['name']}")
    # print(f"    before description: {table['description']}")
    # print(f"    table_id: {table['id']}")
    # print(f"    db_id: {table['db_id']}")
    lower_name = table["name"].lower()
    lower_name = lower_name.replace(" ", "")
    if lower_name not in redshift_table_map:
        redshift_table_map[lower_name] = {}
        redshift_table_map[lower_name]["table_id"] = table["id"]
        redshift_table_map[lower_name]["db_id"] = table["db_id"]
    else:
        print(f"    >>> Duplicate table name: {table['display_name']}")

    # Update table description
    # response = requests.put(f'{metabase_host}/table/{table["id"]}', headers=headers,
    #                         json={'description': f"Table {table['display_name']} description"})
    # print(f"    Update description ({response.status_code}): {response.json()['description']}")

# All tables in Redshift
print(f"=== All tables in Redshift")
pp.pprint(redshift_table_map)

# Read TABLE NAME, DESCRIPTION from CSV file
# Data sample:
# ('lucky_trade_tokens,remi_prod,lucky_trade_tokens,00:00 every '
#  'day,,remipool,raw table,"Table type: raw table\n')
# 'Source: remi_prod/ lucky_trade_tokens\n'
# 'Frequency: 00:00 every day\n'
# ('Information: ",MKT-CAMPAIGN,LUCKY,Anh '
#  'Do,USED,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,\n')

# first item before comma is table name, description will be the text between 2 double quotes (""), may be spread in
# multiple lines
table_to_be_update = {}
with open(csv_file_path, "r") as f:
    lines = f.readlines()
    table_name = ""
    description = ""
    open_quote = False
    close_quote = False
    maps = {
        "Table type": False,
        "Source": False,
        "Frequency": False,
        "Information": False,
    }
    for line in lines:
        if table_name == "" and '"Table type:' in line:
            table_name = line.split(",")[0]
        # if table_name is not empty, then description is the text between 2 double quotes
        if table_name != "" and (not open_quote or not close_quote):
            if (
                '"Table type:' in line
                or "Source:" in line
                or "Frequency:" in line
                or "Information:" in line
            ):
                if not open_quote:
                    open_quote = True
                    description += line[line.find('"Table type') + 1 :]
                    maps["Table type"] = True
                # if not close and maps of table type, source, frequency, information is True, then close quote
                # then we collect all information of this table
                elif not close_quote and all(maps.values()):
                    # breakpoint()
                    close_quote = True
                else:
                    if "Source:" in line:
                        description += line
                        maps["Source"] = True
                    elif "Frequency:" in line:
                        description += line
                        maps["Frequency"] = True
                    elif "Information:" in line:
                        description += line[: line.find('"')]
                        maps["Information"] = True
        if table_name != "" and open_quote and close_quote:
            # print(f"\n=== table_name: {table_name}")
            # print(f">>> description: {description}")
            table_name = table_name.lower().replace(" ", "")
            table_to_be_update[table_name] = description
            # reset table_name, description, open_quote, close_quote
            table_name = ""
            description = ""
            open_quote = False
            close_quote = False
            # reset maps
            maps = {
                "Table type": False,
                "Source": False,
                "Frequency": False,
                "Information": False,
            }


# Update table description
for table_name, description in table_to_be_update.items():
    if table_name in redshift_table_map:
        table_id = redshift_table_map[table_name]["table_id"]
        db_id = redshift_table_map[table_name]["db_id"]
        response = requests.put(
            f"{metabase_host}/table/{table_id}",
            headers=headers,
            json={"description": description},
        )
        print(
            f"Updated description ({response.status_code}): {response.json()['description']}"
        )
    else:
        print(f"Table {table_name} not found in Redshift")

# === 2. Hide table
# Update Table with ID 1 (Products table).
# When Browse data, you can not see this table.
# But you can see this table when you run query.
# response = requests.put(f'{metabase_host}/table/1', headers=headers,
#                         json={
#                             'visibility_type': 'hidden',
#                             'description': 'Update visibility_type',
#                         })
# data = response.json()
# print(f"Hide table {data['name']} result: {response.status_code}")

from db.mysql_connect import connect_database, disconnect_database
import pandas as pd
import os

conn = connect_database()

current_path = os.getcwd()
file = "city_housing.csv"
destination_path = os.path.join(current_path, "data_files", file)

query = """
SELECT *
FROM `u479841347_sql_course`.`city_house_prices`
"""

# read_sql is a convenience wrapper around read_sql_query and read_sql_table, and it can
# be used to route to either of those. Because we know we are reading a query here,
# we will use the base read_sql_query method to make our intentions clear.
df = pd.read_sql_query(query, conn)

# Data transformation steps
df.set_index('Date', inplace=True)
# The stack() function in Pandas acts much like a pivot. Use reset_index()
# to reset the date index created above as a column
df = df.stack().reset_index()
df.columns = ["date", "city", "price"]
# Add a state column
state = df["city"].str.split("-", expand=True)
df["state"] = state[0]

df.to_csv(destination_path, index=False)

disconnect_database(conn)

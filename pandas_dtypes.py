from db.mysql_connect import connect_database
import pandas as pd

conn = connect_database()

query = "SELECT year " \
    ", title " \
    ", genre " \
    ", avg_vote " \
    "FROM `u479841347_sql_course`.`imdb_movies`" \
    "LIMIT 10"

# read_sql is a convenience wrapper around read_sql_query and read_sql_table, and it can
# be used to route to either of those. Because we know we are reading a query here,
# we will use the base read_sql_query method to make our intentions clear.
df = pd.read_sql_query(query, conn)

print(df.head())
print(df.dtypes)

conn.close()
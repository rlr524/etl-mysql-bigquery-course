from db.mysql_connect import connect_database
import pandas as pd

conn = connect_database()

query: str = "SELECT year " \
    ", title " \
    ", genre " \
    ", avg_vote " \
    "FROM `u479841347_sql_course`.`imdb_movies`" \
    "WHERE year BETWEEN '2005' and '2006'" \
    "ORDER BY avg_vote desc"

# read_sql is a convenience wrapper around read_sql_query and read_sql_table, and it can
# be used to route to either of those. Because we know we are reading a query here,
# we will use the base read_sql_query method to make our intentions clear.
df = pd.read_sql_query(query, conn)

print(df['year'].unique())

year_2005: bool = df['year'] == 2005
print(year_2005)

# The ~ acts as a NOT operator on the dataframe
print(df[~year_2005].head())

conn.close()

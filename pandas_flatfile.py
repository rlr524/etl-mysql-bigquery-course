from db.mysql_connect import connect_database, disconnect_database
import pandas as pd
import os

conn = connect_database()

current_path = os.getcwd()
file = "movies.csv"
file_filtered = "movies_filtered.csv"
destination_path = os.path.join(current_path, "data_files", file)
destination_path_filtered = os.path.join(current_path, "data_files", file_filtered)

query: str = "SELECT year " \
    ", title " \
    ", genre " \
    ", avg_vote " \
    "FROM `u479841347_sql_course`.`imdb_movies`" \
    "WHERE year BETWEEN '2005' and '2010'" \
    "ORDER BY avg_vote desc"

# read_sql is a convenience wrapper around read_sql_query and read_sql_table, and it can
# be used to route to either of those. Because we know we are reading a query here,
# we will use the base read_sql_query method to make our intentions clear.
df = pd.read_sql_query(query, conn)

print(df['year'].unique())

year_2005: bool = df['year'] == 2005

df.to_csv(destination_path, index=False)
df[year_2005].to_csv(destination_path_filtered, index=False)

disconnect_database(conn)

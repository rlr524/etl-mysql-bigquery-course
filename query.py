from db.mysql_connect import connect_database

conn = connect_database()
cursor = conn.cursor()

query = "SELECT year " \
    ", title " \
    "FROM `u479841347_sql_course`.`imdb_movies`" \
    "LIMIT 10"

query_kids = "SELECT name " \
    ", children " \
    "FROM `u479841347_sql_course`.`name_children`" \

cursor.execute(query_kids)

for (name, children) in cursor:
    print(f"{name}: {children}")

conn.close()

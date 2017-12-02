import sqlite3

with sqlite3.connect("blog.db") as connection:
	cursor = connection.cursor()
	cutsor.execute("DROP TABLE if exists  posts")
	cursor.execute("CREATE TABLE posts(title TEXT NOT NULL, post TEXT NOT NULL) ")
	cursor.execute("INSERT INTO posts VALUES('good', 'I am good')")
	cursor.execute("INSERT INTO posts VALUES('well', 'I am well')")
	cursor.execute("INSERT INTO posts VALUES('super', 'I am super')")

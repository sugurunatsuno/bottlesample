import sqlite3

connection = sqlite3.connect('./test.db')

#cursor = connection.execute("create table phrase(id int, ja text, other text)")

cursor = connection.execute("insert into phrase values (0, '何が？', 'what?')")


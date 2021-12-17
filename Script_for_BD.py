import random
from pprint import pprint

import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://vkotlyar:0276@localhost:5432/new_music_website')
connection = engine.connect()

# test = connection.execute(""" SELECT * FROM genre;
# """)
# pprint(test)
#
# with open ('result', 'w', encoding = 'utf-8') as f:
#     f.write(test)

# connection.execute("""INSERT INTO
#
# """)

# Добавила жанры
# with open('C:\HomeworkNetology\Module_2\Genre.json', encoding='utf-8') as file:
#     for genre in file:
#         genre_name = genre.strip()
#         connection.execute(f"INSERT INTO genre(genre)  VALUES ('{genre_name}');")

# Добавила исполнителей
# with open('C:\HomeworkNetology\Module_2\Autors.json', encoding='utf-8') as file:
#     for line in file:
#         autors = line.split(' — ')
#         autor_nickname = autors[0].strip()
#         autor_name = autors[1].strip()
#         connection.execute(f"INSERT INTO autors (name, nickname)  VALUES ('{autor_name}', '{autor_nickname}');")

# Связать исполнителей и жанры
# connection.execute("""
# INSERT INTO autor_genre VALUES (23,7), (24,8);
#
# """)

# Заполнение таблицы Альбомы
# with open('C:\HomeworkNetology\Module_2\Alboms.txt', encoding='utf-8') as file:
#     for line in file:
#         alboms = line.split('	')
#         year = alboms[0].strip()
#         alboms_name = alboms[1].strip()
#         connection.execute(f"INSERT INTO alboms (albom_name, year_)  VALUES ('{alboms_name}', '{year}');")

# Заполнение таблицы Песни
# with open('C:\HomeworkNetology\Module_2\Songs', encoding='utf-8') as file:
#     for line in file:
#         songs = line.split(' - ')
#         song_name = songs[0].strip()
#         duration = songs[1].strip().split(':')
#         duration_in_sec = int(duration[0].replace('(','')) * 60 + int(duration[1].replace(')', ''))
#         print(duration_in_sec)
#         albom_id = songs[-1].strip()
#         connection.execute(f"INSERT INTO songs (song_name, duration_min_sec, album_id) "
#                            f"VALUES ('{song_name}', '{duration_in_sec}', '{albom_id}');")

# Заполнение таблицы Autor_Albom
def Insert_connection_tables(first_table_name, second_table_name, table_for_insert,first_column, second_column):
    min_first_table_ID = connection.execute (f"SELECT MIN(id) FROM {first_table_name};").fetchone()
    max_first_table_ID = connection.execute (f"SELECT MAX(id) FROM {first_table_name};").fetchone()
    min_second_table_ID = connection.execute (f"SELECT MIN(id) FROM {second_table_name};").fetchone()
    max_second_table_ID = connection.execute (f"SELECT MAX(id) FROM {second_table_name};").fetchone()
    for_insert = min(max_first_table_ID[0], max_second_table_ID[0])
    for i in range( 1, for_insert):
        connection.execute(f"INSERT INTO {table_for_insert} ({first_column}, {second_column}) "
                   f"VALUES ('{random.randint(int(min_first_table_ID[0]), int(max_first_table_ID[0]))}',"
                   f"'{random.randint(int(min_second_table_ID[0]), int(max_second_table_ID[0]))}');")
#
# Insert_connection_tables('autors','alboms','autor_albom', 'autor_id', 'albom_id')

# Заполнение таблицы Коллекции
# with open('C:\HomeworkNetology\Module_2\Collection', encoding='utf-8') as file:
#     for line in file:
#         collection = line.split(' (')
#         year = int(collection[1].strip().replace(')', ''))
#         collection_name = collection[0].strip()
#         connection.execute(f"INSERT INTO collections (collection_name, year_)  VALUES ('{collection_name}', '{year}');")

Insert_connection_tables('songs', 'collections', 'songs_collection', 'songs_id', 'collection_id')


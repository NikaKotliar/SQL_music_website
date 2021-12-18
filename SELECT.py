import random
from pprint import pprint

import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://vkotlyar:0276@localhost:5432/new_music_website')
connection = engine.connect()
# название и год выхода альбомов, вышедших в 2018 году;
print(connection.execute (f"SELECT albom_name, year_ FROM alboms WHERE  year_ = 2018;").fetchall())
# название и продолжительность самого длительного трека;
print(connection.execute (f"SELECT song_name, duration_min_sec FROM songs ORDER BY duration_min_sec DESC ; ").fetchone())
# название треков, продолжительность которых не менее 3,5 минуты;;
print(connection.execute (f"SELECT song_name FROM songs WHERE duration_min_sec >= 210;").fetchall())
# названия сборников, вышедших в период с 2018 по 2020 год включительно;
print(connection.execute (f"SELECT collection_name FROM collections WHERE year_ BETWEEN 2018 AND 2021;").fetchall())
# исполнители, чье имя состоит из 1 слова;
print(connection.execute (f"SELECT name FROM autors WHERE name NOT LIKE '%% %%';").fetchall())
# название треков, которые содержат слово "мой"/"my".
print(connection.execute (f"SELECT song_name FROM songs WHERE song_name LIKE '%%mir%%';").fetchall())
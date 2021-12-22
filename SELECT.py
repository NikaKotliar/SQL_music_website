import random
from pprint import pprint
import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://vkotlyar:0276@localhost:5432/new_music_website')
connection = engine.connect()

# # название и год выхода альбомов, вышедших в 2018 году;
# print(connection.execute (f"SELECT albom_name, year_ FROM alboms WHERE  year_ = 2018;").fetchall())
# # название и продолжительность самого длительного трека;
# print(connection.execute (f"SELECT song_name, duration_min_sec FROM songs ORDER BY duration_min_sec DESC ; ").fetchone())
# # название треков, продолжительность которых не менее 3,5 минуты;;
# print(connection.execute (f"SELECT song_name FROM songs WHERE duration_min_sec >= 210;").fetchall())
# # названия сборников, вышедших в период с 2018 по 2020 год включительно;
# print(connection.execute (f"SELECT collection_name FROM collections WHERE year_ BETWEEN 2018 AND 2021;").fetchall())
# # исполнители, чье имя состоит из 1 слова;
# print(connection.execute (f"SELECT name FROM autors WHERE name NOT LIKE '%% %%';").fetchall())
# # название треков, которые содержат слово "мой"/"my".
# print(connection.execute (f"SELECT song_name FROM songs WHERE song_name LIKE '%%mir%%';").fetchall())

# количество исполнителей в каждом жанре;
# print(connection.execute ("""
# SELECT COUNT(a.id), genre f FROM autors a
# JOIN autor_genre ag ON a.id = ag.autor_id
# JOIN  genre g ON ag.genre_id = g.id
# GROUP BY genre ;
# """).fetchall())

# количество треков, вошедших в альбомы 2019-2020 годов;
# pprint(connection.execute ("""
# SELECT COUNT(s.id), year_ FROM songs s
# JOIN alboms a ON s.album_id = a.id
# WHERE year_ BETWEEN 2015 AND 2020
# GROUP BY year_ ;
# """).fetchall())

# средняя продолжительность треков по каждому альбому;
# result = connection.execute ("""
# SELECT AVG(s.duration_min_sec), a.albom_name FROM songs s
# JOIN alboms a ON s.album_id = a.id
# GROUP BY a.albom_name;""").fetchall()
# for i in result:
#     print (f" {round(float(i[0]/60),2)} минут - средняя продолжительность альбома '{i[1]}' ")

# все исполнители, которые не выпустили альбомы в 2020 году;
# pprint(connection.execute ("""
# SELECT DISTINCT a.nickname FROM autors a
# JOIN autor_albom aa ON a.id = aa.autor_id
# JOIN alboms a_ ON aa.albom_id = a_.id
# WHERE NOT year_ = 2020;
# """).fetchall())

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
# pprint(connection.execute ("""
# SELECT collection_name FROM collections c
# JOIN songs_collection sc ON c.id = sc.collection_id
# JOIN songs s ON sc.songs_id = s.id
# JOIN alboms a ON s.album_id = a.id
# JOIN autor_albom aa ON a.id = aa.albom_id
# JOIN autors a_ ON aa.autor_id = a_.id
# WHERE nickname = 'Егор Крид';
# """).fetchall())

# название альбомов, в которых присутствуют исполнители более 1 жанра;
# pprint(connection.execute ("""
# SELECT DISTINCT albom_name FROM alboms a
# JOIN autor_albom aa ON a.id = aa.albom_id
# JOIN
# (SELECT COUNT(genre_id), autor_id from autor_genre
# GROUP BY autor_id
# HAVING COUNT(genre_id) > 1
# ) ag ON aa.autor_id = ag.autor_id
#  ;
# """).fetchall())

# наименование треков, которые не входят в сборники;
# pprint(connection.execute ("""
# SELECT song_name FROM songs s
# LEFT JOIN songs_collection sc ON s.id = sc.songs_id
# JOIN collections c ON sc.collection_id = c.id
# WHERE sc.collection_id = NULL
#   ;
#  """).fetchall())

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
# pprint(connection.execute ("""
# SELECT DISTINCT name FROM autors a
# JOIN autor_albom aa ON a.id = aa.autor_id
# JOIN alboms al ON aa.albom_id = al.id
# JOIN
# (SELECT s.id, album_id FROM songs s
# ORDER BY duration_min_sec DESC
# LIMIT 1) min ON al.id = min.album_id
#   ;
#  """).fetchall())

# название альбомов, содержащих наименьшее количество треков.
min_songs = connection.execute ("""
SELECT COUNT(s.id) co, s.album_id FROM songs s
GROUP BY album_id
LIMIT 1
;
 """).fetchall()
min_songs_1 = int(min_songs[0][0])

pprint(connection.execute ("""
SELECT al.albom_name, COUNT(album_id) co from alboms al
JOIN songs s ON al.id = s.album_id
group by al.id, al.albom_name
HAVING COUNT(album_id) = """ + min_songs_1.__str__() + """
;
 """).fetchall())

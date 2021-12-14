create table if not exists Genre(
ID serial primary key,
Genre varchar(40) not null
);

create table if not exists Autors(
ID serial primary key,
Name varchar(40) not null, 
Nickname varchar(40)
);

create table if not exists Autor_Genre(
Autor_ID integer references Autors(ID),
Genre_ID integer references Genre(ID),
constraint pk primary key (Autor_ID, Genre_ID)
);

create table if not exists Alboms(
ID serial primary key, 
Albom_name varchar(40) not null,
year_ integer check(year_ < 2030)
);

create table Autor_Albom(
ID serial primary key,
Autor_ID integer references Autors(ID), 
Albom_ID integer references Alboms(ID)
);

create table if not exists Songs(
ID serial primary key,
Song_name varchar(40) not null,
Duration_min_sec integer,
Album_ID integer references Alboms(ID)
);


create table if not exists Collections(
ID serial primary key, 
COllection_name varchar(40) not null,
Year_ integer check(year_ < 2030)
);

create table if not exists Songs_Collection(
Songs_ID integer references Songs(ID),
Collection_ID integer references Collections(ID),
constraint SC primary key(Songs_ID, Collection_ID)
);

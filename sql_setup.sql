CREATE DATABASE library_data
USE library_data

CREATE table users (
    id int auto_increment primary key,
    name varchar(255) not null,
);

CREATE TABLE authors (
    id int auto_increment primary key,
    name varchar(255) not null,
    biography varchar(255) null
);

create table books (
    id int auto_increment primary key,
    name varchar(255) not null,
    author_id int,
    borrowed tinyint(1), NOT NULL,
    foreign key (author_id) references authors(id)
);

create TABLE current_transactions (
    id int auto_increment primary key,
    user_id,
    book_id,
    foreign key(user_id) references users(id),
    foreign key (book_id) references books(id)
);
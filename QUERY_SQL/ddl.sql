create database if not exists users;

use Login_cadastro;

create table users(
id_user int not null auto_increment,
nome varchar(30),
sobrenome varchar(50),
email varchar(50),
telefone varchar(50),
senha varchar(200),
primary key(id_user)
); 
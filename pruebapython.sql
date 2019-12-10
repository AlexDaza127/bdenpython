create database pruebapython;
use pruebapython;
create table usuarios(id int primary key, nombre varchar(45), email varchar(45), pass int);

/*insercion de los registros en la tabla usuarios*/

insert into usuarios (id, nombre, email, pass) values (1, 'Skyler Drews', 'sdrews0@buzzfeed.com', 480);
insert into usuarios (id, nombre, email, pass) values (2, 'Eloisa Hazell', 'ehazell1@oaic.gov.au', 778);
insert into usuarios (id, nombre, email, pass) values (3, 'Antone Swanne', 'aswanne2@vistaprint.com', 682);
insert into usuarios (id, nombre, email, pass) values (4, 'Neddy Dabling', 'ndabling3@google.es', 159);
insert into usuarios (id, nombre, email, pass) values (5, 'Fleurette Larver', 'flarver4@utexas.edu', 198);
insert into usuarios (id, nombre, email, pass) values (6, 'Kylie Jarmain', 'kjarmain5@edublogs.org', 466);
insert into usuarios (id, nombre, email, pass) values (7, 'Hilary Praten', 'hpraten6@irs.gov', 764);
insert into usuarios (id, nombre, email, pass) values (8, 'Neel Ewols', 'newols7@dailymail.co.uk', 823);
insert into usuarios (id, nombre, email, pass) values (9, 'Marnie Dybell', 'mdybell8@acquirethisname.com', 604);
insert into usuarios (id, nombre, email, pass) values (10, 'Jennifer Poff', 'jpoff9@taobao.com', 908);

select * from usuarios;




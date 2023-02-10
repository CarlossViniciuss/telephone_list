# from connection import *

# cur.execute(

# )

# create table cadastro(
# 	id SERIAL PRIMARY KEY,
# 	name VARCHAR(255) not null,
# 	phone_number int not null
# )

# insert into cadastro(name, phone_number) values ('Goku', 42423255)

# select * from cadastro

# create table inserir_contato (
# 	id SERIAL PRIMARY KEY,
# 	contatos_inserir_lista int not null,
# 	cadastro_id integer not null,
# 	foreign key (cadastro_id) references cadastro (id)
# )

# insert into inserir_contato (contatos_inserir_lista, cadastro_id) values (22222, 1)

# select * from inserir_contato


# select * from inserir_contato inner join cadastro on inserir_contato.cadastro_id = cadastro.id
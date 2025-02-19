create table usuarios (
  id bigint primary key generated always as identity,
  nombre text not null,
  email text not null unique,
  password text not null
);

create table productos (
  id bigint primary key generated always as identity,
  tipo text not null,
  size text not null,
  color text not null
);

create table pedido (
  id bigint primary key generated always as identity,
  date timestamp with time zone not null,
  id_usuario bigint not null,
  status text not null,
  foreign key (id_usuario) references usuarios (id)
);

create table item_orden (
  id bigint primary key generated always as identity,
  id_pedido bigint not null,
  imagen text not null,
  description text not null,
  foreign key (id_pedido) references pedido (id)
);

alter table item_orden

alter table item_orden
add column id_producto bigint not null references productos (id);
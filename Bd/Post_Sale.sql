create database Post_Sale;
Use Post_Sale;

create table Rol(
	idRol int primary key auto_increment,
    tipoRol varchar(45) not null,
    nombreRol varchar(45) not null
);

create table Usuario(
	idUsuario int primary key auto_increment,
    nombreUsu varchar(45) not null,
    apellidoUsu varchar(45) not null,
    telefonoUsu varchar(45) not null,
    emailUsu varchar(45) not null,
    direccioUsu varchar(45) not null,
    contraUsu varchar(45) not null,
    idRolFK int not null,
    foreign key (idRolFK) references rol(idRol)
);

create table Garantias(
	idGarantia int primary key auto_increment,
    fechaGar date not null,
    descripcionGar text not null,
    tipoGar varchar(255) not null,
    idUsuFK int not null,
    foreign key(idUsuFK) references usuario(idUsuario)
);

create table Contrato(
	idContrato int primary key auto_increment,
    tipoCont varchar(255) not null,
    descripcionCon text not null,
    idGarFK int not null,
    foreign key (idGarFK) references garantias(idGarantia),
    idUsuFK int not null,
    foreign key(idUsuFK) references usuario(idUsuario)
);

create table Pqrs(
	idPqrs int primary key auto_increment,
    tipoPq varchar(255) not null,
    descripPqrs text not null,
    idGarFK int not null,
    foreign key (idGarFK) references garantias(idGarantia),
    idConFK int not null,
    foreign key(idConFK) references contrato(idContrato)
);
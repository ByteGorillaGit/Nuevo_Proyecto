create database Post_Sale;
Use Post_Sale;

create table Rol(
	idRol varchar(45) primary key,
    tipoRol varchar(45) not null,
    nombreRol varchar(45) not null
);

create table Usuario(
	idUsuario varchar(45) primary key,
    nombreUsu varchar(45) not null,
    apellidoUsu varchar(45) not null,
    telefonoUsu varchar(45) not null,
    emailUsu varchar(45) not null,
    direccioUsu varchar(45) not null,
    descripUsu varchar(45) not null,
    idRolFk varchar(45) not null,
    foreign key (idRolFK) references rol(idRol)
);

create table Garantias(
	idGarantia varchar(45) primary key,
    fechaGar date not null,
    descripcionGar text not null,
    tipoGar varchar(255) not null,
    idUsuFK varchar(45) not null,
    foreign key(idUsuFK) references usuario(idUsuario)
);

create table Contrato(
	idContrato varchar(45) primary key,
    tipoCont varchar(255) not null,
    descripcionCon text not null,
    idGarFK varchar(45) not null,
    foreign key (idGarFK) references garantias(idGarantia),
    idUsuFK varchar(45) not null,
    foreign key(idUsuFK) references usuario(idUsuario)
);

create table Pqrs(
	idPqrs varchar(20) primary key,
    tipoPq varchar(255) not null,
    descripPqrs text not null,
    idGarFK varchar(45) not null,
    foreign key (idGarFK) references garantias(idGarantia),
    idConFK varchar(45) not null,
    foreign key(idConFK) references contrato(idContrato)

);
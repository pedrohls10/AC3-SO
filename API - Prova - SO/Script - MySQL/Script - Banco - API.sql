create database dadosTorcida;	

use dadosTorcida;

create table tb_torcida(
	idTorcida int auto_increment primary key,
    nome varchar(45),
    timeCoracao varchar(45),
    jogadorPreferido varchar(45),
    data_hora datetime
);	

select * from tb_torcida;
drop database dadosTorcida;	
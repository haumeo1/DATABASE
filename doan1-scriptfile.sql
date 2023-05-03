
drop database if exists `TRUONGHOC`;


create database `TRUONGHOC`;


use TRUONGHOC;
drop table if exists sogddt;
create table sogddt (
    stt CHAR(3) NOT NULL,
    sogd VARCHAR(100) NOT NULL
);


 drop table if exists phonggd;
 create table phonggddt(
     maphonggd CHAR(3) not null primary key,
     tenphonggd VARCHAR(50) default null
     
     );

 drop table if exists loaihinh;
 create table loaihinh(
     maloaihinh char(5) not null primary key,
     tenloaihinh varchar(50) default null
     
     );


drop table if exists loaitruong;
create table loaitruong(
     maloaitruong char(10) not null primary key,
     tenloaitruong varchar(50) default null
     
     );


drop table if exists bachoc;
 create table bachoc(
     ma char(20) not null primary key,
     tenbachoc varchar(50) default null
     
     );


drop table if exists thongtintruong;
 create table thongtintruong(
    matruong varchar(20) not null primary key,
    tentruong varchar(100) not null,
    diachi varchar(256) default null,
    phonggd char(20) not null,
    loaihinh char(5) not null,
    loaitruong char(10) not null,
    bachoc char(20) not null,
    
    CONSTRAINT fk_capbac FOREIGN KEY(bachoc) REFERENCES bachoc(ma),
    CONSTRAINT fk_phonggd FOREIGN KEY(phonggd) REFERENCES phonggddt(maphonggd),
    CONSTRAINT fk_loaihinh FOREIGN KEY(loaihinh) REFERENCES loaihinh(maloaihinh),
    CONSTRAINT fk_loaitruong FOREIGN KEY(loaitruong) REFERENCES loaitruong(maloaitruong)
    ) ; 

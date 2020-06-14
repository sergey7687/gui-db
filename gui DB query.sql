create table employee
 (emp_id smallint unsigned not null auto_increment,
  first_name varchar(20) not null,
  last_name varchar(20) not null,
  address varchar(20) not null,
  phone_number varchar(20) not null,
  company_email varchar(20) not null,
  start_date date not null,
  end_date date,
  superior_emp_id smallint unsigned,
  dept_id smallint unsigned,
  job_title varchar(20),
  salary decimal(16,4),
  constraint fk_e_emp_id
    foreign key (superior_emp_id) references employee (emp_id) on update cascade
on delete cascade,
  constraint fk_dept_id
    foreign key (dept_id) references department (dept_id),
  constraint pk_employee primary key (emp_id)
 );
 

 create table department
 (dept_id smallint unsigned not null auto_increment,
  dep_name varchar(20) not null,
  constraint pk_department primary key (dept_id)
 );
 
 
 insert into department (dep_name) 
 values ('Administration'),
  ('Product Development'),
  ( 'Marketing'),
  ('Sales'),
  ('Accounting');
  
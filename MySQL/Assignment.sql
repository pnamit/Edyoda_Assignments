CREATe database salescompany1;
use salescompany1;

/*Table 1: SalesPeople
Snum is Primary key
Sname is Unique constraint

Snum Sname City Comm
1001 Peel. London .12
1002  Serres Sanjose .13
1004 Motika London .11
1007 Rifkin Barcelona .15
1003 Axelrod Newyork .10

*/


CREATE TABLE Salespeople(
snum INT not null,
sname varchar(50) not null,
city varchar(50),
comm varchar(25),
primary key (snum),
unique(sname)
);

insert into salespeople(snum,sname,city,comm)
values (1001,"Peel.","London",".12");
insert into salespeople(snum,sname,city,comm)
values (1002,"Serres","Sanjose",".13");
insert into salespeople(snum,sname,city,comm)
values (1004,"Motika","London",".11");
insert into salespeople(snum,sname,city,comm)
values (1007,"Rifkin","Barcelona",".15");
insert into salespeople(snum,sname,city,comm)
values (1003,"Axelrod","Newyork",".10");

select * from salespeople;

/*Table 2: Customers

Cnum is Primary Key
City has not null constraint .
Snum is foreign key constraint refers Snum column of SalesPeople table.

Cnum Cname City Snum
2001  Hoffman London 1001
2002  Giovanni Rome 1003
2003  Liu Sanjose 1002
2004  Grass Berlin 1002
2006 Clemens London 1001
2008 Cisneros Sanjose 1007
2007 Pereira Rome 1004
*/

CREATE TABLE Customers(
Cnum INT not null,
Cname varchar(50) not null,
city varchar(50) not null,
Snum INT,
primary key (cnum),
foreign key (snum) references salespeople(snum)
);

insert into customers(cnum,cname,city,snum)
values 
		(2001,"Hoffman","London",1001),
        (2002,"Giovanni","Rome",1003),
		(2003,"Liu","Sanjose",1002),
		(2004,"Grass","Berlin",1002),
		(2006,"Clemens","London",1001),
		(2008,"Cisneros","Sanjose",1007),
		(2007,"Pereira","Rome",1004);

select * from customers;

/*Table 3: Orders

Onum is Primary key
Cnum is foreign key refers to Cnum column of Customers table. Snum is foreign key refers Snum column of SalesPeople table.

Onum Amt Odate Cnum Snum
3001 18.69 3-10-1990 2008 1007
3003 767.19 3-10-1990 2001 1001
3002 1900.10 3-10-1990 2007 1004
3005  5160.45 3-10-1990 2003 1002
3006  1098.16 3-10-1990 2008 1007
3009 1713.23 4-10-1990 2002 1003
3007  75.75 4-10-1990 2004 1002
3008  4273.00 5-10-1990 2006 1001
3010  1309.95 6-10-1990 2004 1002
3011  9891.88 6-10-1990 2006 1001
*/

CREATE TABLE Orders(
Onum INT not null,
Amt decimal(10,2),
Odate date not null,
Cnum INT,
Snum INt,
primary key (Onum),
foreign key (cnum) references customers(cnum),
foreign key (snum) references salespeople(snum)
);

insert into orders(onum,amt,odate,cnum,snum)
values 
	(3001, 18.69,str_to_date("3-10-1990","%d-%m-%Y"), 2008, 1007),
	(3003,767.19,str_to_date("3-10-1990","%d-%m-%Y"),2001,1001),
	(3002,1900.10,str_to_date("3-10-1990","%d-%m-%Y"),2007,1004),
	(3005,5160.45,str_to_date("3-10-1990","%d-%m-%Y"),2003,1002),
	(3006,1098.16,str_to_date("3-10-1990","%d-%m-%Y"),2008,1007),
	(3009,1713.23,str_to_date("4-10-1990","%d-%m-%Y"),2002,1003),
	(3007,75.75,str_to_date("4-10-1990","%d-%m-%Y"),2004,1002),
	(3008,4273.00,str_to_date("5-10-1990","%d-%m-%Y"),2006,1001),
	(3010,1309.95,str_to_date("6-10-1990","%d-%m-%Y"),2004,1002),
	(3011,9891.88,str_to_date("6-10-1990","%d-%m-%Y"),2006,1001);

select * from orders;
    
/*On the basis of above tables perform given below questions

Count the number of Salesperson whose name begin with ‘a’/’A’.
Display all the Salesperson whose all orders worth is more than Rs. 2000.
Count the number of Salesperson belonging to Newyork.
Display the number of Salespeople belonging to London and belonging to Paris.
Display the number of orders taken by each Salesperson and their date of orders.
*/

-- Count the number of Salesperson whose name begin with ‘a’/’A’.

use salescompany1;
select * from salespeople;

Select count(sname) as number_of_salespeople from salespeople where (sname like 'a%' or sname like 'A%');

-- Display all the Salesperson whose all orders worth is more than Rs. 2000.

select salespeople.snum,sname,amt from salespeople,orders where salespeople.snum=orders.snum and amt > 2000;

-- Count the number of Salesperson belonging to Newyork.

select count(snum) as number_of_salespeople from salespeople where city='Newyork';    

-- Display the number of Salespeople belonging to London and belonging to Paris.

select city,count(*) as number_of_salespeople from salespeople where (city='London' or city ='Paris') group by city;

-- Display the number of orders taken by each Salesperson and their date of orders.

select orders.snum,sname,odate,count(*) as number_of_orders from salespeople,orders where salespeople.snum=orders.snum group by snum,odate order by salespeople.snum,odate;

-- End of Assignment    

CREATE TABLE users (
	id integer NOT NULL,
	createdat timestamp NULL,
	updatedat timestamp NULL,
	city varchar(100) NULL,
	country varchar(100) NULL,
	email varchar(150) NOT NULL,
	birthDate  timestamp NULL,
	gender varchar(20) NULL,
	issmoking bool NULL,
	profession varchar(250) NULL,
	income real null,
	PRIMARY KEY (id)
);

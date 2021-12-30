
CREATE TABLE subscriptions (
	id SERIAL NOT NULL,
	userid integer  NOT NULL,
	createdat timestamp NULL,
	startdate timestamp NULL,
	enddate timestamp NULL,
	status varchar(20) NULL,
	amount real null,
	PRIMARY KEY (id),
	FOREIGN KEY (userid) REFERENCES users (id)
);
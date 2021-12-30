
CREATE TABLE messages (
	id bigint NOT NULL,
	senderid integer NOT NULL,
	receiverid integer NOT NULL,
	createdat timestamp null,
	PRIMARY KEY (id)
	--FOREIGN KEY (senderid) REFERENCES users (id),
	--FOREIGN KEY (receiverid) REFERENCES users (id)
);

DROP TABLE IF EXISTS URLs;

CREATE TABLE URLs(
       id INT NOT NULL AUTO_INCREMENT,
       url_str VARCHAR(512) NOT NULL,
       ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       PRIMARY KEY (id)
);

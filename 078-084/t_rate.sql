CREATE TABLE IF NOT EXISTS t_rate (
   ID        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   TYPE      CHAR(1), -- U - USD, E - EURO
   DATE      INTEGER,
   RATE      REAL
);
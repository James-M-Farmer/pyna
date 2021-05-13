#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('switches.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS switches
 (ID INT PRIMARY KEY     ,
 hostname           CHAR(50),
 ip            CHAR(20),
 startup_config        CHAR,
 running_config         CHAR,
 valid_config         BOOL);''')
print("Table created successfully")
conn.close()

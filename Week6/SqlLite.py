import sqlite3

def GO():
    conn = sqlite3.connect('northwind.db')
    ##copy fuckin paste
    c = conn.cursor()

    # Get all tables
    c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")



    print c.fetchall()

    # Insert a row of data
    #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    #conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def db_shell():
    con = sqlite3.connect('northwind.db')
    con.text_factory = str ## this is done to decode the shit strings in the database
    con.isolation_level = None
    cur = con.cursor()

    buffer = ""

    print "Enter your SQL commands to execute in sqlite3."
    print "Enter a blank line to exit."

    while True:
        line = raw_input()
        if line == "":
            break
        buffer += line
        ##print buffer
        if sqlite3.complete_statement(buffer):
            print buffer
            try:
                buffer = buffer.strip()
                cur.execute(buffer)

                if buffer.lstrip().upper().startswith("SELECT"):
                    values = cur.fetchall()
                    names = list(map(lambda x: x[0], cur.description))
                    print names
                    for val in values:
                        print val
            except sqlite3.Error as e:
                print "An error occurred:", e.args[0]
            buffer = ""

    con.close()

    #SELECT * FROM Products WHERE ProductID in (SELECT ProductID FROM Orders Where CustomerID = 'ALFKI'); this gets all the products in the orders of ALFKI
#SELECT * FROM Orders WHERE CustomerID in (SELECT CustomerID FROM Customers WHERE CompanyName = 'ALFKI');
GO()

db_shell()
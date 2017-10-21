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
##first
# Select * from (Select OrderID, CustomerID From Orders) OO INNER JOIN (Select * from (select * from 'Order Details' where OrderID IN(Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI'))))) OD INNER JOIN (select ProductName, ProductID from Products) P on OD.ProductID = P.ProductID) ODD on OO.OrderID = ODD.OrderID;


    #SELECT ProductID, ProductName FROM Products WHERE ProductID in (SELECT ProductID FROM Orders Where CustomerID = 'ALFKI'); this gets all the products in the orders of ALFKI;
#SELECT * FROM Orders WHERE CustomerID in (SELECT CustomerID FROM Customers WHERE CompanyName = 'ALFKI');
# Select * from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI');

## SELECT OrderID, Count(OrderID) from (Select OrderID, ProductID from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID);
## Select OrderID, Count(OrderID) from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID;
#Select OrderID, OrderDate from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1);
##Select * from (select * from 'Order Details' where OrderID = 10408) OD INNER JOIN (select * from Products) P on OD.ProductID = P.ProductID;
#Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1);

##Select * from (Select * from Orders INNER JOIN (select * from 'Order Details' where OrderID in (Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1))) OD INNER JOIN (select * from Products) P on OD.ProductID = P.ProductID)) OJ on Orders.OrderID = OJ.OrderID);

###CUrrent state
##Select * from (select * from 'Order Details' where OrderID IN(Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1))) OD INNER JOIN (select * from Products) P on OD.ProductID = P.ProductID;
##the last one
##Select * from (Select * From Orders) OO INNER JOIN (Select * from (select * from 'Order Details' where OrderID IN(Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1))) OD INNER JOIN (select * from Products) P on OD.ProductID = P.ProductID) ODD on OO.OrderID = ODD.OrderID;
## trimmed a bit
## ##Select * from (Select OrderID, CustomerID From Orders) OO INNER JOIN (Select * from (select OrderID, ProductID, Quantity from 'Order Details' where OrderID IN(Select OrderID from Orders where OrderID in (Select OrderId from (Select OrderID, Count(OrderID) as oc from 'Order Details' where OrderID in (Select OrderID from Orders where CustomerID = 'ALFKI') group by OrderID) where oc > 1))) OD INNER JOIN (select ProductID, ProductName from Products) P on OD.ProductID = P.ProductID) ODD on OO.OrderID = ODD.OrderID;
GO()

db_shell()
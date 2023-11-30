import pyodbc

from Model.Customer import Customer
from Model.Order import Order
from Model.Product import Product


class PharmacyModel:
    def __init__(self, server, database, username, password):
        try:
            self.conn = pyodbc.connect(
                f'DRIVER={{SQL Server}};SERVER={server},1433;DATABASE={database};UID={username};PWD={password}')
            self.cursor = self.conn.cursor()
            self.create_tables()
            print("Kết nối thành công!")
        except pyodbc.Error as e:
            print(f"Lỗi kết nối: {str(e)}")


    def create_tables(self):
        self.cursor.execute('''
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Products' AND xtype='U')
            CREATE TABLE Products (
                ID INT PRIMARY KEY IDENTITY(1,1),
                Name NVARCHAR(255) NOT NULL,
                Barcode NVARCHAR(255) NOT NULL,
                Price FLOAT NOT NULL,
                Quantity INT NOT NULL
            )
        ''')
        self.cursor.execute('''
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Orders' AND xtype='U')
            CREATE TABLE Orders (
                OrderID INT PRIMARY KEY IDENTITY(1,1),
                CustomerID INT NOT NULL,
                TotalAmount FLOAT NOT NULL,
                PaymentMethod NVARCHAR(100) NOT NULL
            )
        ''')
        self.cursor.execute('''
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Customers' AND xtype='U')
            CREATE TABLE Customers (
                CustomerID INT PRIMARY KEY IDENTITY(1,1),
                Name NVARCHAR(255) NOT NULL,
                Email NVARCHAR(255) NOT NULL,
                Phone NVARCHAR(20) NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self, product):
        query = 'INSERT INTO Products (Name, Barcode, Price, Quantity) VALUES (?, ?, ?, ?)'
        self.cursor.execute(query, (product.name, product.barcode, product.price, product.quantity))
        self.conn.commit()

    def remove_product(self, barcode):
        query = 'DELETE FROM Products WHERE Barcode = ?'
        self.cursor.execute(query, (barcode,))
        self.conn.commit()

    def update_product(self, barcode, updated_product):
        query = 'UPDATE Products SET Name=?, Price=?, Quantity=? WHERE Barcode=?'
        self.cursor.execute(query, (updated_product.name, updated_product.price, updated_product.quantity, barcode))
        self.conn.commit()

    def get_product_by_barcode(self, barcode):
        query = 'SELECT * FROM Products WHERE Barcode = ?'
        result = self.cursor.execute(query, (barcode,)).fetchone()
        if result:
            return Product(result[1], result[2], result[3], result[4])
        else:
            return None

    def create_order(self, order):
        query = 'INSERT INTO Orders (CustomerID, TotalAmount, PaymentMethod) VALUES (?, ?, ?)'
        self.cursor.execute(query, (order.customer_id, order.total_amount, order.payment_method))
        self.conn.commit()

    def get_order_by_id(self, order_id):
        query = 'SELECT * FROM Orders WHERE OrderID = ?'
        result = self.cursor.execute(query, (order_id,)).fetchone()
        if result:
            return Order(result[0], [], result[2], result[1], result[3])
        else:
            return None

    def add_customer(self, customer):
        query = 'INSERT INTO Customers (Name, Email, Phone) VALUES (?, ?, ?)'
        self.cursor.execute(query, (customer.name, customer.email, customer.phone))
        self.conn.commit()

    def get_customer_by_id(self, customer_id):
        query = 'SELECT * FROM Customers WHERE CustomerID = ?'
        result = self.cursor.execute(query, (customer_id,)).fetchone()
        if result:
            return Customer(result[0], result[1], result[2], result[3])
        else:
            return None

    def __del__(self):
        self.conn.close()
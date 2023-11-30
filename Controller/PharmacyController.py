from Model.Customer import Customer
from Model.Order import Order
from Model.Product import Product
import pandas as pd


class PharmacyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Nhập lựa chọn của bạn: ")

            if choice == "1":
                self.create_product()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.update_product()
            elif choice == "5":
                self.display_product()
            elif choice == "6":
                self.create_order()
            elif choice == "7":
                self.display_order()
            elif choice == "8":
                self.create_customer()
            elif choice == "9":
                self.display_customer()
            elif choice == "0":
                print("Cảm ơn bạn đã sử dụng ứng dụng quản lý!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

    def create_product(self):
        name = self.view.get_input("Nhập tên sản phẩm: ")
        barcode = self.view.get_input("Nhập mã vạch: ")
        price = float(self.view.get_input("Nhập giá: "))
        quantity = int(self.view.get_input("Nhập số lượng: "))
        new_product = Product(name, barcode, price, quantity)
        self.model.add_product(new_product)

    def remove_product(self):
        barcode = self.view.get_input("Nhập mã vạch sản phẩm cần xóa: ")
        self.model.remove_product(barcode)

    def update_product(self):
        barcode = self.view.get_input("Nhập mã vạch sản phẩm cần cập nhật: ")
        product = self.model.get_product_by_barcode(barcode)
        if product:
            name = self.view.get_input("Nhập tên sản phẩm mới: ")
            price = float(self.view.get_input("Nhập giá mới: "))
            quantity = int(self.view.get_input("Nhập số lượng mới: "))
            updated_product = Product(name, barcode, price, quantity)
            self.model.update_product(barcode, updated_product)
        else:
            print("Sản phẩm không tồn tại!")

    def display_product(self):
        product_id = int(self.view.get_input("Nhập Barcode sản phẩm: "))
        product = self.model.get_product_by_barcode(product_id)
        self.view.display_product_info(product)

    def create_order(self):
        customer_id = int(self.view.get_input("Nhập ID khách hàng: "))
        total_amount = float(self.view.get_input("Nhập tổng số tiền: "))
        payment_method = self.view.get_input("Nhập phương thức thanh toán: ")
        order = Order(None, [], total_amount, customer_id, payment_method)
        self.model.create_order(order)

    def display_order(self):
        order_id = int(self.view.get_input("Nhập ID đơn hàng: "))
        order = self.model.get_order_by_id(order_id)
        self.view.display_order_info(order)

    def create_customer(self):
        name = self.view.get_input("Nhập tên khách hàng: ")
        email = self.view.get_input("Nhập email: ")
        phone = self.view.get_input("Nhập số điện thoại: ")
        new_customer = Customer(None, name, email, phone)
        self.model.add_customer(new_customer)

    def display_customer(self):
        customer_id = int(self.view.get_input("Nhập ID khách hàng: "))
        customer = self.model.get_customer_by_id(customer_id)
        self.view.display_customer_info(customer)

    def load_data_from_csv(self, filename):
        try:
            data = pd.read_csv(filename)
            return data
        except FileNotFoundError:
            print("File không tồn tại.")
            return None

    def export_data_to_csv(self, data, filename):
        data.to_csv(filename, index=False)
        print(f"Dữ liệu đã được lưu vào file {filename}.csv")

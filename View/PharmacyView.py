class PharmacyView:
    def display_menu(self):
        print("1. Thêm sản phẩm")
        print("2. Thêm sản phẩm từ file csv")
        print("3. Xóa sản phẩm")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Tìm kiếm sản phẩm sản phẩm")
        print("6. Tạo đơn hàng")
        print("7. Hiển thị thông tin đơn hàng")
        print("8. Thêm thông tin khách hàng")
        print("9. Hiển thị thông tin khách hàng")
        print("0. Thoát")

    def get_input(self, prompt):
        return input(prompt)

    def display_product_info(self, product):
        if product:
            print(f"Tên: {product.name}")
            print(f"Mã vạch: {product.barcode}")
            print(f"Giá: {product.price}")
            print(f"Số lượng: {product.quantity}")
        else:
            print("Không tìm thấy sản phẩm!")

    def display_order_info(self, order):
        if order:
            print(f"ID Đơn hàng: {order.order_id}")
            print(f"Tổng số tiền: {order.total_amount}")
            print(f"ID Khách hàng: {order.customer_id}")
            print(f"Phương thức thanh toán: {order.payment_method}")
        else:
            print("Không tìm thấy đơn hàng!")

    def display_customer_info(self, customer):
        if customer:
            print(f"ID Khách hàng: {customer.customer_id}")
            print(f"Tên: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Số điện thoại: {customer.phone}")
        else:
            print("Không tìm thấy khách hàng!")

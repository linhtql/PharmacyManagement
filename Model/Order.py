class Order:
    def __init__(self, order_id, products, total_amount, customer_id, payment_method):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount
        self.customer_id = customer_id
        self.payment_method = payment_method

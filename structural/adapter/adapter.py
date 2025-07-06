# Old Method
class PaypalGateway:
    def make_payment(self, amount: float):
        print(f"Processing payment of: {amount:.2f} via Paypal!")

# New Method
class RayzorPayGateway:
    def make_payment(self, amount: float):
        print(f"Processing payment of: {amount:.2f} via Rayzorpay!")

# Adapter

class PaymentAdapter:
    def __init__(self, getway: RayzorPayGateway):
        self.gateway = getway

    def process_payment(self, amount: float):
        self.gateway.make_payment(amount)


def process_user_payment(payment_processor, amount: float):
    payment_processor.process_payment(amount)



if __name__ == "__main__":
    print("Old Method - Paypal")
    old_getway = PaypalGateway()
    old_getway.make_payment(499.99)

    print("New Method - Rayzorpay")
    new_getway = RayzorPayGateway()
    adapter = PaymentAdapter(new_getway)
    process_user_payment(adapter, 799.99)
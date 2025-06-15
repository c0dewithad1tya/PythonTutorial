#This code is for creating a payment orchestration system using Python. It includes classes for handling different payment methods, such as credit cards and PayPal, and a main function to demonstrate their usage. The code is structured to allow for easy extension and modification in the future.

#
# Payment Orchestration System 

class CreditCardPayment:
    """Class to handle credit card payments."""
    def process(self, amount):
        return f"Credit card payment of ${amount} processed successfully."

class PayPalPayment:
    """Class to handle PayPal payments."""
    def process(self, amount):
        return f"PayPal payment of ${amount} processed successfully."

def process_payment(payment_method, amount):
    """Process a payment using the specified payment method."""
    if payment_method == "credit_card":
        return CreditCardPayment().process(amount)
    elif payment_method == "paypal":
        return PayPalPayment().process(amount)
    else:
        raise ValueError("Unsupported payment method")
    
def main():
    """Main function to demonstrate payment processing."""
    try:
        amount = 100.0  # Example amount to be processed
        payment_method = "credit_card"  # Change to "paypal" to test PayPal payment

        result = process_payment(payment_method, amount)
        print(f"Payment processed successfully: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


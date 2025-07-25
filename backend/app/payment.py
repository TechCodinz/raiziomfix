import os
from paystackapi.paystack import Paystack
import stripe as stripe_lib

PAYSTACK_KEY = os.getenv('PAYSTACK_KEY')
STRIPE_KEY = os.getenv('STRIPE_KEY')


def pay_with_paystack(amount: int, email: str):
    """Mocked Paystack payment."""
    if not PAYSTACK_KEY:
        # No key, return mock response
        return {"status": "mock", "reference": "mock-paystack"}
    paystack = Paystack(secret_key=PAYSTACK_KEY)
    # Real integration would go here
    return {"status": "success", "reference": "paystack-ref"}


def pay_with_stripe(amount: int, email: str):
    """Mocked Stripe charge."""
    if not STRIPE_KEY:
        return {"status": "mock", "reference": "mock-stripe"}
    stripe_lib.api_key = STRIPE_KEY
    # Real charge logic would go here
    return {"status": "success", "reference": "stripe-ref"}

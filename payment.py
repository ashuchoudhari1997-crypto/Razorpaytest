import razorpay
from config import *

client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

def create_order(amount):

    data = {
        "amount": amount,
        "currency": "INR",
        "receipt": "receipt_001"
    }

    return client.order.create(data=data)
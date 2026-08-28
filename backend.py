from fastapi import FastAPI
from payment import create_order

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Backend Running"}


@app.get("/create-order")
def create_payment():

    order = create_order(1000)

    return order
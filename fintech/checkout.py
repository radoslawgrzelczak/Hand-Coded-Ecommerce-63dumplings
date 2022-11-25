import stripe
import os
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv()

DOMAIN_URL = os.getenv("DOMAIN_URL")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
stripe.api_version = os.getenv("STRIPE_API_VERSION")

def create_checkout_session(type:int, order_quantity: int):
    try: 
        DUMPLINGS_PRICE_ID = select_dumplings(type)      

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': DUMPLINGS_PRICE_ID,
                    'quantity': order_quantity
                }
            ],
            mode='payment',
            success_url=DOMAIN_URL + '/success',
            cancel_url=DOMAIN_URL + '/cancel',
            payment_method_types=['card']
        )
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
    return checkout_session

def select_dumplings(type: int):
    if type == 1:
        return os.getenv("POLISH_WARRIORS_PRICE_ID")
    elif type == 2:
        return os.getenv("SPINACH_BOMBS_PRICE_ID")
    elif type == 3:
        return os.getenv("SOUP_DUMPLINGS_PRICE_ID")
    elif type == 4:
        return os.getenv("FOREST_DUEL_PRICE_ID")
    else:
        return os.getenv("POLISH_WARRIORS_PRICE_ID")
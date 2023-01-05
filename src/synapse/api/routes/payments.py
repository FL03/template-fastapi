#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""

import stripe
import json
import os

# from flask import Flask, render_template, jsonify, request, send_from_directory, redirect
from dotenv import load_dotenv, find_dotenv

from fastapi import APIRouter, Cookie, Form, Request
from fastapi.responses import RedirectResponse
from typing import Union

from synapse.core import session
router = APIRouter(tags=["payments"])
sesh = session()

# For sample support and debugging, not required for production:
stripe.set_app_info(
    'FL03/synapse',
    version='0.1.0',
    url='https://github.com/FL03/synapse')

stripe.api_key = sesh.settings.stripe_secret_key

# static_dir = str(os.path.abspath(os.path.join(
#     __file__, "..", os.getenv("STATIC_DIR"))))



@router.get('/')
def get_example():
    return dict(message="Welcome")


@router.get('/config')
def get_publishable_key():
    return {
        'publishableKey': sesh.settings.stripe_public_key,
        'basicPrice': os.getenv('BASIC_PRICE_ID'),
        'proPrice': os.getenv('PRO_PRICE_ID')
    }


# Fetch the Checkout Session to display the JSON result on the success page
@router.get('/checkout-session')
def get_checkout_session(sesh: str):
    checkout_session = stripe.checkout.Session.retrieve(sesh)
    return checkout_session


@router.post('/create-checkout-session')
def create_checkout_session(price: str = Form()):
    # price = request.form.get('priceId')
    domain_url = sesh.settings.domain

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [customer_email] - lets you prefill the email input in the form
        # [automatic_tax] - to automatically calculate sales tax, VAT and GST in the checkout page
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + '/success.html?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/canceled.html',
            mode='subscription',
            # automatic_tax={'enabled': True},
            line_items=[{
                'price': price,
                'quantity': 1
            }],
        )
        return RedirectResponse(checkout_session.url)
    except Exception as e:
        return {'error': {'message': str(e)}}


@router.post('/customer-portal')
def customer_portal(sid: Union[str, None] = Cookie(default=None)):
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session = stripe.checkout.Session.retrieve(sid)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url = sesh.settings.domain

    session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )
    return RedirectResponse(session.url)


@router.post('/webhook')
def webhook_received():
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    print('event ' + event_type)

    if event_type == 'checkout.session.completed':
        print('🔔 Payment succeeded!')

    return {'status': 'success'}


if __name__ == '__main__':
    app.run(port=4242)

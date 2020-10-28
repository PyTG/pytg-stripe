import logging

from modules.pytg.load import manager

from .StripeManager import StripeManager

def initialize():
    StripeManager.initialize()

def connect():
    load_manager().load_api_keys()
    load_manager().allocate_payment_link_retriever()
    pass

def load_manager():
    return StripeManager.load()

def main():
    payment_link = manager("stripe").retrieve_checkout_link("cs_test_LwkHgZtUwoY1JgzwXsw1LH8hsg7Y11chaZAd9wrqQHJKMcG6MOWCviTy")

    print(payment_link)

def depends_on():
    return []
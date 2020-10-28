import yaml, stripe

from modules.pytg.Manager import Manager
from modules.pytg.load import manager

from .payment.OnlineStaticPagePaymentLinkRetriever import OnlineStaticPagePaymentLinkRetriever

class StripeManager(Manager):
    @staticmethod
    def initialize():
        StripeManager.__instance = StripeManager()

        return

    @staticmethod
    def load():
        return StripeManager.__instance

    def __init__(self):
        self.__interface = stripe

    def load_api_keys(self):
        settings = manager("config").load_settings("stripe")

        self.__secret_key = settings["secret_key"]
        self.__publishable_key = settings["public_key"]

        self.__interface.api_key = self.__secret_key

    def allocate_payment_link_retriever(self):
        settings = manager("config").load_settings("stripe")

        self.__payment_link_retriever = OnlineStaticPagePaymentLinkRetriever(settings["payment_base_url"])

    def get_interface(self):
        return self.__interface

    def retrieve_checkout_link(self, session_id):
        return self.__payment_link_retriever.retrieve_url(self.__publishable_key, session_id)
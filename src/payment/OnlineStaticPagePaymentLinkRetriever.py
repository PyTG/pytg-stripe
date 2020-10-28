import os 

class OnlineStaticPagePaymentLinkRetriever:
    def __init__(self, payment_link):
        self.__url_format = payment_link + "?publishableKey={}&sessionId={}"

    def retrieve_url(self, publishable_key, session_id):
        return self.__url_format.format(publishable_key, session_id)
import requests
import hmac
import hashlib
import time
from typing import Optional

BASE_URL = 'https://api.txbit.io/api/'

class TxbitAPI:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    def _get_nonce(self):
        return int(time.time() * 1000)

    def _get_signature(self, url: str):
        return hmac.new(bytes(self.api_secret, 'utf-8'),
                        bytes(url, 'utf-8'),
                        hashlib.sha512).hexdigest().upper()

    def _public_request(self, path: str, params={}):
        url = BASE_URL + path
        response = requests.get(url, params=params)
        return response.json()

    def _private_request(self, path: str, params={}):
        url = BASE_URL + path
        nonce = self._get_nonce()
        url += f'?apikey={self.api_key}&nonce={nonce}'
        signature = self._get_signature(url)
        headers = {'apisign': signature}
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    # Public methods
    def get_markets(self):
        return self._public_request('public/getmarkets')

    def get_currencies(self):
        return self._public_request('public/getcurrencies')

    def get_ticker(self, market: str):
        params = {'market': market}
        return self._public_request('public/getticker', params)

    def get_market_summaries(self):
        return self._public_request('public/getmarketsummaries')

    def get_market_summary(self, market: str):
        params = {'market': market}
        return self._public_request('public/getmarketsummary', params)

    def get_orderbook(self, market: str, type_: str='both'):
        params = {'market': market, 'type': type_}
        return self._public_request('public/getorderbook', params)

    def get_market_history(self, market: str):
        params = {'market': market}
        return self._public_request('public/getmarkethistory', params)

    # Private methods
    def buy_limit(self, market: str, quantity: float, rate: float):
        params = {'market': market, 'quantity': quantity, 'rate': rate}
        return self._private_request('market/buylimit', params)

    def sell_limit(self, market: str, quantity: float, rate: float):
        params = {'market': market, 'quantity': quantity, 'rate': rate}
        return self._private_request('market/selllimit', params)

    def cancel_order(self, uuid: str):
        params = {'uuid': uuid}
        return self._private_request('market/cancel', params)

    def get_open_orders(self, market: Optional[str]=None):
        params = {'market': market} if market else {}
        return self._private_request('market/getopenorders', params)

    def get_balances(self):
        return self._private_request('account/getbalances')

    def get_balance(self, currency: str):
        params = {'currency': currency}
        return self._private_request('account/getbalance', params)

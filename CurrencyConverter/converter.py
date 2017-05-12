import requests

class Converter():
    base_url = None  # url of site
    base_currency = None
    full_url = None  # url for request
    rates = None

    def __init__(self):
        self.base_url = r'http://api.fixer.io/'
        self.base_currency = 'USD'
        self.update_rates()

    # Updating list of rates
    def update_rates(self):
        self.full_url = self.base_url + r'latest?base=' + self.base_currency
        request = requests.get(self.full_url)
        if request.ok:
            self.rates = request.json().get('rates')
        else:
            err_msg = '{0} currency was not found.'.format(self.base_currency)
            raise requests.exceptions.HTTPError(err_msg)

    def change_base_currency(self, new_base_currency):
        if new_base_currency != self.base_currency:
            self.base_currency = new_base_currency.upper()
            self.update_rates()

    # Get rate for specified target_currency
    def __get_rate(self, target_currency):
        if target_currency == self.base_currency:
            return 1
        if target_currency in self.rates:
            return self.rates.get(target_currency)
        else:
            raise KeyError('Currency {0} is not found'.format(target_currency))

    def convert(self, value, target_currency):
            return float(value) * self.__get_rate(target_currency.upper())
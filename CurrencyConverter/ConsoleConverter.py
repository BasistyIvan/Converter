import re
import requests
from converter import Converter

def isFloat(value):
    if re.match(r'[0-9]+\.?[0-9]{,2}', value):  # Regular expression excludes not float values
        return True
    else:
        raise TypeError('Sum should be a number in format: 5.40 or 76')

def main():
    converter = Converter()

    print('To exit the program type "exit" in "Sum>" field')
	
	# To catch errors from change_base_currency method
    try:
        print('List of available currencies:')
        for curr in converter.get_currencies():
            print(curr)  
        #converter.change_base_currency('gbp')
        while True:
            try:
                value = input('Sum> ')
                if value.lower() == 'exit':
                    break
                elif isFloat(value):
                    value = float(value)
                    exchange_currency = input('To currency> ').upper()
                    result = converter.convert(value, exchange_currency)
                    print('{0:.2f} {1} is {2:.2f} {3}'.format(value, converter.base_currency, result, exchange_currency))
            except (ValueError, TypeError, KeyError) as err:
                print(err)
    except requests.exceptions.HTTPError as err:
        print(err)
main()
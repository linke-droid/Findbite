import requests
import json
import glom

# YelpAPI
# businessId

# key should be hidden
api_key = 'zJAj4o-JYOnTfrbVIrTeO9HM4S9KaEt71QTyt5Ud-EShBRcH_twkMEjSGTVfJXgHOCVxYEEP92xqS0pQOhhOSIzh2IXZ8bs4Q-bJzp76yMam2xXR4A1FhdOlDJCJYHYx'
headers = {'Authorization': 'bearer %s' % api_key}
global protein_food, type_food, price_food


def get_restaurants(protein_food, type_food, price_food):
    search_api_url = 'https://api.yelp.com/v3/businesses/search'

    # define parameters
    params = {
        'term': protein_food,
        'categories': type_food,
        'price': price_food,
        'limit': 50,
        'location': 'Sweden, Malmö', }

    # request yelp API https://www.yelp.com/developers/documentation/v3/business_search
    response = requests.get(url=search_api_url, headers=headers, params=params)

    businesses = response.json()
    # loop through businesses list

    # convert the data into a json object
    data = json.loads(response.text)

    # prints out the json object
    print(json.dumps(data, indent=4, separators=(". ", " = ")))

    # extracts businesses into a python list
    businesses = data['businesses']

    # loops through the list and checks the price range 1-4 and prints it out.
    for x in range(1, 4):
        for business in businesses:
            print('restauarnt', business['name'])
            print('number of reviews',
                  business['review_count'])
            if "price category" in business:
                if len('price') == x:
                    print('price', business['price'])
                    print('\n')
        return businesses

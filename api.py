import requests
import json
# YelpAPI
# businessId

# key should be hidden
api_key = 'zJAj4o-JYOnTfrbVIrTeO9HM4S9KaEt71QTyt5Ud-EShBRcH_twkMEjSGTVfJXgHOCVxYEEP92xqS0pQOhhOSIzh2IXZ8bs4Q-bJzp76yMam2xXR4A1FhdOlDJCJYHYx'
headers = {'Authorization': 'bearer %s' % api_key}


def get_restaurants(protein_food, type_food, price_food):
    search_api_url = 'https://api.yelp.com/v3/businesses/search'

    # define parameters
    params = {
        'term': protein_food,
        'categories': type_food,
        'price': price_food,
        'limit': 1,
        'location': 'Sweden, Malmö',
        'sort_by': 'distance'}

    # request yelp API https://www.yelp.com/developers/documentation/v3/business_search
    response = requests.get(url=search_api_url, headers=headers, params=params)

    # convert the data into a json object
    data = json.loads(response.text)

    # prints out the json object
    print(json.dumps(data, indent=4))

    # extracts businesses into a python list
    businesses = data['businesses'] or []

    businesses.sort(key=lambda d: d["price"].count('$'))

    # loops over the bussinesses in the list
    for business in businesses:
        print('id', business['id'])
        print('name', business['name'])
        print('review_count', business['review_count'])
        print('image_url', business['image_url'])
        if "price" in business:
            print('price', business['price'])
            print('\n')
    return businesses








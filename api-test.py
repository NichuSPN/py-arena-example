from arena.api import initializeAPIsFromConfig


# For these examples, this may seem to be a useless way to do it
# But when you have complex headers that you need to add to every API call, this will come in handy
APIConfigs = {
    "game-of-thrones": {
        "baseUrl": "https://www.anapioficeandfire.com"
    },
    "restful-api-test": {
        "baseUrl": "https://api.restful-api.dev"
    },
    "corona": {
        "baseUrl": "https://api.covidtracking.com"
    }
}

apis = initializeAPIsFromConfig(APIConfigs)

def onSuccess(result):
    print("Here is the result --->>> ", result)
    
def onError(error):
    print("A unexpected error happened --->>> ", error)


# Get Endpoints that fetches all Game of Thrones Characters
apis["game-of-thrones"].runAPIWithCallbacks({
        "method": "get", 
        "endpoint": "/api/characters"
    },
    onSuccess,
    onError)

# Get Endpoint without query params to fetch all the data
apis["restful-api-test"].runAPIWithCallbacks({
        "method": "get", 
        "endpoint": "/objects"
    },
    onSuccess,
    onError)

# Get Endpoints with query params to fetch specific object
apis["restful-api-test"].runAPIWithCallbacks({
        "method": "get", 
        "endpoint": "/objects",
        "queryParams": {"id": 3}
    },
    onSuccess,
    onError)

# Create a object using the post method
apis["restful-api-test"].runAPIWithCallbacks({
        "method": "post", 
        "endpoint": "/objects",
        "data": {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.98,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    },
    onSuccess,
    onError)

apis["corona"].runAPIWithCallbacks({
        "method": "get", 
        "endpoint": "/v1/us/20200501.json"
    },
    onSuccess,
    onError)
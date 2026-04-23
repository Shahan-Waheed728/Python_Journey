def http_request(status):
    match status:
       case 200:
             return "OK!"
       case 404:
             return "Not Found!"
       case 500:
             return "Internal Server Error!"
       case _:
              return "Unknown Error!"
        
print(http_request(200))
print(http_request(404))
print(http_request(500))
print(http_request(203))
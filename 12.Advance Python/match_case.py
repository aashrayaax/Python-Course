def http_status(status):
    match status:
        case 200:
             return "OK"
        case 400:
             return " NOT FOUND OK"
        case 60:
             return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(60))




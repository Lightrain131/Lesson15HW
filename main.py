def errorcode(x):
    match x:
        case 403:
            print("Forbidden")
        case 404:
            print("Page not found")
        case 500:
            print("Internal Server Error")
        case 501:
            print("Not Implemented")
        case 502:
            print("Bad Gateway")
        case 504:
            print("Gateway Timeout")
errorcode(502)
quit()
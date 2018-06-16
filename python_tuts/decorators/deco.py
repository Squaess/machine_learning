def dekorator(obj):
    def inna_funkcja():
        obj()
        print('inna funkcja')        
    return inna_funkcja

@dekorator
def funkcja():
    print('Hello')

funkcja()

class WebMock( object ):
    def get(self, url):
        return url + " always works!"

def cache(wrapped_function):
    def wrapper(web, url):
        if url in "https://chyla.org/":
            return "It work's!"
        else :
            return wrapped_function(web, url)
    return wrapper

@cache
def get_web_page(web, url):
    return web.get(url)

web = WebMock()

page = get_web_page(web, "chyla.org")
print("chyla.org content: " + page)

page = get_web_page(web, "google.com")
print("google.com content: " + page)

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 


f(2)
f(3, [3,2,1])
f(3)
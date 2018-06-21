from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def init(self):
        self.buttonz = 0

    def handle_starttag(self, tag, attrs):        
        if tag == 'button' :            
            print("Click Click ...")
            self.buttonz = self.buttonz + 1
            
        elif tag == 'input':
            for i,j in attrs:
                if i =='type' and (j == 'submit' or j == 'reset' or j == 'button'):                    
                    print("Click click 2...")
                    self.buttonz = self.buttonz + 1
                    break
                elif i == 'class':
                    classes = i.split(" ")
                    for c in classes:
                        upper_c = c.upper()
                        if 'BUTON' in upper_c or 'BTN' in upper_c:
                            self.buttonz = self.buttonz + 1
                            break
                    
        else:
            for name, value in attrs:
                if name == 'class':
                    classes = value.split(" ")                    
                    for c in classes:
                        upper_c = c.upper()                        
                        if 'BUTTON' in upper_c or 'BTN' in upper_c:                            
                            print('Hello')
                            self.buttonz = self.buttonz + 1
                            break

parser = MyHTMLParser()
parser.init()
parser.feed('<!DOCTYPE html>  <html>  <head>  <title>Example test page</title>  </head>  <body>  <a href="#" name="NonButtonLink">boring link</a>  <a href="#" class="btn btn-small">interesting button-link</a>  <button class="funnyButton">Click me!</button>  <a href="#" class="funnyButton">I’m a special Button!</a>    <form>  <input type="submit" name="saveButton" value="Submit me!">  </form>​ <button  class="bartosz btn-small"> Click clickitty click </button>  </body>  </html>  ')
print(parser.buttonz)


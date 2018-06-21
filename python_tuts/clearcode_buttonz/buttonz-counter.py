import urllib.request
import pandas as pd
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    """Class for parsing html

    Attributes
    -----------
    buttonz : int - counted buttonz for feed method

    """

    def init(self):
        """
        This metod is init and also a reset method.
        Should be invoked before every feed method.
        """
        self.buttonz = 0

    def handle_starttag(self, tag, attrs):
        """
        Whenever Parser encounters start tag this method is called
        """

        if tag == 'button' :    #If the tag is button then we're happy 
                                #because we found the button
            self.buttonz = self.buttonz + 1
            
        elif tag == 'input':    # we have to check if it is a button by 
                                # type or by class
            for name, value in attrs:
                if name =='type' and (value == 'submit' or value == 'reset' or value == 'button'):
                    self.buttonz = self.buttonz + 1
                    break
                elif name == 'class':
                    classes = value.split(" ")                    
                    for c in classes:
                        upper_c = c.upper()
                        if 'BUTTON' in upper_c or 'BTN' in upper_c:
                            self.buttonz = self.buttonz + 1
                            break
                    
        else:                   # we just check if it has properly
                                # class value
            for name, value in attrs:
                if name == 'class':
                    classes = value.split(" ")                    
                    for c in classes:
                        upper_c = c.upper()                        
                        if 'BUTTON' in upper_c or 'BTN' in upper_c:                            
                            self.buttonz = self.buttonz + 1                            
                            break

def loadData(path):
    """
    Parameters
    -----------
    path : string

    Returns
    -------
    data: string
    """
    with open(path, 'r') as f:
        data = f.read()

    return data

def processData(data):
    """
    Parameters
    -----------
    data : string
    """

    data = data.split("\n")
    buttonz_count = {}          # Dictionary for storeing results

    parser = MyHTMLParser()

    for i in range(len(data)):
        site = data[i]
        if site != "":
            if 'http' not in site:
                site = 'http://'+ site
            try:
                content = urllib.request.urlopen(site).read()            
            except urllib.error.URLError:
                print('Nie można nawiązać połączenia, ponieważ komputer docelowy'
                    'aktywnie go odmawia {}'.format(site))
                buttonz_count[data[i]] = 'Error'
                continue
            parser.init()
            parser.feed(str(content))
            buttonz_count[data[i]] = parser.buttonz
    return buttonz_count

if __name__ == '__main__':

    '''
    Check if the arguments are properly passed to compute 
    '''
    if len(sys.argv) != 3:    
        sys.exit('Arguments are not sufficient')
    
    
    try:        
        data = loadData(sys.argv[1])
    except FileNotFoundError:
        exit('Wrong input file.')

    #Disctionary containing all results
    buttonz_count = processData(data)

    #Two lists for making clear csv file
    adress = [i for i in buttonz_count.keys()]
    number_of_buttons = [buttonz_count[i] for i in adress]
    d = {'adress' : pd.Series(adress),
         'number_of_buttons' : pd.Series(number_of_buttons)
        }
    out = pd.DataFrame(d)
    out.to_csv(sys.argv[2], index=False)
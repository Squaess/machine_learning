import unittest
Parser = __import__("buttonz-counter").MyHTMLParser

class TestParser(unittest.TestCase):
    
    def test_simple_button(self):
        # Test for the simplest button
        buttonz = "<button>Przycisk</button>"
        parser_1 = Parser()
        parser_1.init()
        parser_1.feed(buttonz)
        self.assertEqual(parser_1.buttonz, 1)

    def test_input_button(self):
        #Test for input buttons
        button1 = """
                    <input type="submit" value="Submit button">
                    <input type="reset" value="Reset button">
                    <input type="button" value="Button button">
                  """
        button2 = """
                    <input type="text" class="Button">
                    <input type="text" class="niestety-nie-przycisk">
                    <input type="submit" class="btn">
                  """
        parser = Parser()
        parser.init()
        parser.feed(button1)
        self.assertEqual(parser.buttonz, 3)

        parser.init()
        parser.feed(button2)
        self.assertEqual(parser.buttonz, 2)

    def test_class_button(self):
        #Test class buttons
        button1 = """
                    <a href="#" class="button">But</a>
                    <a href="#" class="buTtOn">But</a>
                    <a href="#" class="sssbuttonssss">But</a>
                    <a href="#" class="btn44431">But</a>
                    <a href="#" class="Ale-btN-kurde">But</a>
                """
        parser = Parser()
        parser.init()
        parser.feed(button1)
        self.assertEqual(parser.buttonz, 5)

    def test_multiple_in_one_button(self):
        #Test for counting only one button if spoted many 'keywords'
        button1 = """
                    <button href="#" class="button btn">Button</a>
                  """
        button2 = """
                    <input type="submit" class="Button" name="BTN">
                  """
        clearcode_example = """
                    <button  class="btn btn-small"> Click clickitty click </button>
                  """
                  
        parser = Parser()
        parser.init()
        parser.feed(button1)
        self.assertEqual(parser.buttonz, 1)

        parser.init()
        parser.feed(button2)
        self.assertEqual(parser.buttonz, 1)

        parser.init()
        parser.feed(clearcode_example)
        self.assertEqual(parser.buttonz, 1)

        all_buttons = button1 + button2 + clearcode_example
        parser.init()
        parser.feed(all_buttons)
        self.assertEqual(parser.buttonz, 3)


    def test_clearcode_example(self):
        # Testing clearcode example
        html = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Example test page</title>
                    </head>
                    <body>
                        <a href="#" name="NonButtonLink">boring link</a>
                        <a href="#" class="btn btn-small">interesting button-link</a>
                        <button class="funnyButton">Click me!</button>
                        <a href="#" class="funnyButton">I’m a special Button!</a>

                        <form>
                            <input type="submit" name="saveButton" value="Submit me!">
                        </form>
                    </body>
                </html>
                """
        parser = Parser()
        parser.init()
        parser.feed(html)
        self.assertEqual(parser.buttonz, 4)
        

if __name__ == '__main__':
    unittest.main()
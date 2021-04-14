"""
This package lets you very easily incorporate a login screen into your app.
--------- USAGE ---------
In your main.py file, include the following import statement:
import typetowritescreen
Then, in the kv file where you want to use the login screen, include this statement:
#:include typetowritescreen/typetowritescreen.kv
Now you can instantiate the typetowrite class, which inherits from the
Kivy Screen class. That means you need to add it to your ScreenManager.
Example:
    `main.kv`
    ScreenManager:
        typetowritescreen:
            id: type_to_write_screen

            name:'type_to_write_screen'

"""
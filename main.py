from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            
        </style>
    </head>
    <body>
        <form action="/" method='POST'>
            <label for="rot">Rotate by: <label/>
                <input id="rot" type="text" name="rot" value="0" />
                <textarea name="user_input" >{0}</textarea>
            <button type="submit">Submit Query</button>
        </form>
    </body>
</html>
"""




@app.route("/", methods=['POST'])
def encrypt(): 
    user_input = request.form['user_input']
    num_rot = int(request.form['rot'])
    encrypted = rotate_string(user_input, num_rot)
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format('')

app.run()
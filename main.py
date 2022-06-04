import json

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("F:\Python\Labs\inventory.json", "r") as json_in:
        inventory = json_in.read()
    return {"File inventory:" : json.loads(inventory)}

@app.route("/index.html")
def print_stuff():
    with open("something.csv", "w") as json_out:
       if json_out.write("Something"):
            return "<iframe frameborder=\"0\" height=\"200\" scrolling=\"no\" src=\"https://playlist.megaphone.fm?e=ADV5008883012\" width=\"100%\"></iframe>"

if __name__ =='__main__':
    app.run(debug=True)
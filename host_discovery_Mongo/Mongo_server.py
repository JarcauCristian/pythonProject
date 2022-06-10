from flask import Flask, request
from db_apis import get_all_hosts, set_host

app = Flask(__name__)


@app.route('/hosts', methods=["GET", "PUT"])
def hosts():

    if request.method == "GET":
        return get_all_hosts()

    elif request.method == "PUT":
        hostname = request.args.get("hostname")
        if not hostname:
            return "must provide hostname on PUT", 400

        host = request.get_json()
        set_host(host)
        return {}, 204


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request
from db_apis import get_all_hosts, set_host, get_host, get_host_status
from flask_restx import Api
from flask_cors import CORS
from apidoc_models import ApiModels

app = Flask(__name__)
CORS(app)

api = Api(app, version="1.0", title="My App", description="A simple app that make life easy", default="my-app",
          default_label="")
ApiModels.set_api_models(api)


@app.route('/hosts', methods=["GET", "PUT"])
def hosts():
    if request.method == "GET":
        return get_all_hosts(), 200

    elif request.method == "PUT":
        hostname = request.args.get("hostname")
        if not hostname:
            return "must provide hostname on PUT", 400

        host = request.get_json()
        set_host(host)
        return {}, 204


@app.route('/hosts/status', methods=["GET"])
def host_satus():

    if request.method == "GET":
        host = get_host("192.168.1.1")

        host_status = {
            "host": host["host"]["hostname"],
            "status": get_host_status(host["host"]["hostname"])
        }
        return host_status, 200


if __name__ == '__main__':
    app.run(debug=True)

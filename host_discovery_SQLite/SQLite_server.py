from flask import Flask, request
from extensions import db
from db_apis import get_all_hosts, set_host


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.app_context().push()

db.create_all()


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


def main():
    app.run(debug=True)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting SQLite_server!")
        exit()

import flask
import requests
from flask import request, Response
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/bit", methods= ["GET", "POST"])
def bit_data_read():

    if request.method == "GET":
            username = request.headers["username"]
            password = request.headers["password"]
            # branch = request.form["branch"]
            response = requests.get(f"https://api.bitbucket.org/2.0/repositories/sushil29/bitfilesrepo/src/master/README.md",
                                       auth=(username, password))

            if response.status_code == 401:
                return Response(json.dumps({"error": "Invalid Credentials"}), response.status_code)
            elif response.status_code == 404:
                return Response(json.dumps({"error": "Invalid API"}), response.status_code)
            else:
                return response.text
            # else:
            #     return Response(json.dumps({"error": "Invalid commit number"}), 404)


if __name__ == '__main__':
    app.run(debug=True)
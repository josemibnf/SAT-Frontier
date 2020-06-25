from flask import Flask, request
import frontier

app = Flask(__name__)

if __name__ == "__main__":

    @app.route('/', methods=['GET', 'POST'])
    def post():
        cnf = request.json.get('cnf')
        solution = frontier.ok(cnf=cnf)
        return {'interpretation':solution}

    app.run(host='0.0.0.0', port=8080)
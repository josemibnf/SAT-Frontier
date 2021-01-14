from flask import Flask, request, send_file
import io
import frontier
from api_pb2 import *

app = Flask(__name__)

if __name__ == "__main__":

    @app.route('/', methods=['GET', 'POST'])
    def post():
        cnf = Cnf.ParseFromString(request.json.get('cnf'))
        solution = frontier.ok(cnf=cnf)
        return send_file(
            io.BytesIO(Interpretation.SerializeToString(solution)),
            as_attachment=True,
            attachment_filename='abc.abc',
            mimetype='attachment/x-protobuf'
        )

    app.run(host='0.0.0.0', port=8080)
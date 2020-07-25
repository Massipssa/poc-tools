from flask import Flask, request, Response, jsonify, render_template
import json
from src.sql import Variable
from src.sql.settings import create_session
import logging

app = Flask(__name__)

log = logging.getLogger(__name__)

session = None


@app.route("/test")
def test():
    return jsonify(status='OK')


@app.route("/hello/<user>")
def index(user):
    return render_template('hello.html', name=user)


@app.route("/api/variables")
def get_all_variables():
    result = Variable.select_all(session=session)
    return jsonify([e.serialize() for e in result])


@app.route('/api/variables/<key>', methods=['GET'])
def get_by_id(key):
    log.debug("Key: {}".format(key))
    item = Variable.get_by_key(key=key)
    return Response(json.dumps(item.serialize()), mimetype='application/json')


@app.route("/api/create_variable", methods=['POST'])
def create_variable():
    content = request.get_json(silent=True)
    Variable.create(key=content['key'], value=content['value'], is_encrypted=content['is_encrypted'])
    return '', 200


@app.route("/api/variables/<key>", methods=['DELETE'])
def delete(key):
    Variable.delete(key=key)
    return '', 204


if __name__ == '__main__':
    session = create_session()
    app.run(debug=True)
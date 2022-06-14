from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from core.config import GlobalConfig
from core.error import *
from core.logger import Logger
from constant import API_PORT

from api.router import *


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# Router register
# app.register_blueprint(category_api)
# app.register_blueprint(product_api)

# Router register


# Load global configuration
GlobalConfig()


@app.route('/ping')
def ping():
    return 'Pong !!!'


@app.before_request
def before_request_func():
    if request.method != 'OPTIONS':
        Logger.instance() \
            .info(f'[{request.remote_addr}][CALL][{request.method}] {request.path}')


@app.after_request
def after_request_func(response):
    if request.method != 'OPTIONS':
        Logger.instance() \
            .info(f'[{request.remote_addr}][RES][{request.method}] {request.path}')
    return response


@app.errorhandler(InternalError)
def internalExceptionHander(error):
    Logger.instance() \
        .error(f'[INTERNAL_ERROR][{error.Code}] {error.Msg}')
    return make_response(
        jsonify({
            'Success': False,
            'Error': {
                'Code': error.Code,
                'Msg': error.Msg
            }
        })
    )


@app.errorhandler(Exception)
def exceptionHander(error):
    Logger.instance().error(str(error))
    return make_response(
        jsonify({
            'Success': False,
            'Error': {
                'Code': HTTP_ERROR_500,
                'Msg': str(error)
            }
        })
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=API_PORT,
            threaded=True,
            debug=True)

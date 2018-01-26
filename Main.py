"""
Module that is running json validation server
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 80


class MyError:
    """
    Class introducing a error validating given json file
    """
    def __init__(self, error_code, error_msg, error_place, filename, connection_id):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_place = error_place
        self.filename = filename
        self.connection_id = connection_id

    def default(self):
        """
        Function to return the class as a dictionary so it can easily be converted to json
        """
        return self.__dict__


class MyHandler(BaseHTTPRequestHandler):
    """
    Class for handling requests from the client. In out case - only PUT request
    """
    def do_PUT(self):
        """
        Overridden function to handle PUT request from the client
        """
        length = int(self.headers['Content-Length'])
        content = str(self.rfile.read(length), 'utf-8')
        try:
            loaded_content = json.loads(content)
            pretty = json.dumps(loaded_content, indent=4)
            self.send_response(200)
            self.wfile.write(bytes('\n', 'utf-8'))
            self.wfile.write(bytes(pretty, "utf-8"))
        except json.decoder.JSONDecodeError as exception:
            error_msg = exception.args[0]
            error_place = 'line {exception.lineno} column {exception.colno} (char {exception.pos})'.format(exception=exception)
            filename = str(self.path).split('/')[-1]
            connection_id = int(str(self.connection).split(', ')[-1][0:5])
            my_error = MyError(1, error_msg, error_place, filename, connection_id)
            my_error.error_code = id(my_error)
            pretty_error = json.dumps(my_error.default(), indent=4)
            self.send_response(400)
            self.wfile.write(bytes('\n', 'utf-8'))
            self.wfile.write(bytes(pretty_error, "utf-8"))


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        print('Server started working')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped working')
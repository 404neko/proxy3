from proxy2 import *

class ThreadingHTTPSServer(ThreadingHTTPServer):
    address_family = socket.AF_INET
    daemon_threads = True

    cakey = 'ca.key'
    cacert = 'ca.crt'

    def get_request(self):
        request, client_address = self.socket.accept()
        request = ssl.wrap_socket(request, keyfile=self.cakey, certfile=self.cacert, server_side=True)
        return request, client_address

    def handle_error(self, request, client_address):
        # surpress socket/ssl related errors
        cls, e = sys.exc_info()[:2]
        if cls is socket.error or cls is ssl.SSLError:
            pass
        else:
            return HTTPServer.handle_error(self, request, client_address)

if __name__ == '__main__':
    main(ServerClass=ThreadingHTTPSServer)

import sys, os
cwd = os.getcwd()
myapp_directory = cwd + '/diti'
sys.stdout = sys.stderr
sys.path.insert(0,myapp_directory)
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "diti.settings"
from paste.exceptions.errormiddleware import ErrorMiddleware
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
# To cut django out of the loop, comment the above application = ... line ,
# and remove "test" from the below function definition.
def testapplication(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Running Python version ' + sys.version + '\n\n'
    response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
    # to test paste's error catching prowess, uncomment the following line
    # while this function is the "application"
    #raise("error")
    start_response(status, response_headers)    
    return [output]
application = ErrorMiddleware(application, debug=True)

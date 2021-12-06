import json
import file
import database
import functions

#Change .. to Bullboard when finished

read_file_string = "../"

def login(request):
    body = file.read_file(read_file_string + "frontend/pages/index.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

# We want to serve the register page here.
def register(request):
    body = file.read_file(read_file_string + "frontend/pages/create_account.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

# We want to serve the register page here.
def edit(request):
    body = file.read_file(read_file_string + "frontend/pages/edit_profile.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

def newsfeed(request):
    body = file.read_file(read_file_string + "frontend/pages/newsfeed.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

def map(request):
    body = file.read_file(read_file_string + "frontend/pages/live_map.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

def messages(request):
    body = file.read_file(read_file_string + "frontend/pages/direct_messages.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

# Respond to HTML paths here.
def resp_to_html_paths(request):
    path = request.path
    body = file.read_file(read_file_string + "frontend/pages%s" % path)
    response_code = 200
    if path.endswith(".css"):
        return [body, response_code, "text/css"]
    elif path.endswith(".js"):
        return [body, response_code, "text/javascript"]
    elif path.endswith(".png"):
        return [body, response_code, "image/png"]
    else:
        return [body, response_code, "image/jpeg"]

def login_attempt(request, data):
    if database.verify_login(data):
        #Create login token on successful login
        token = functions.login_token()
        database.store_token(data['email'], token)
        header = {'Set-Cookie': 'token=' + token + '; Max-Age=3600; HttpOnly'}
        return [header, b"User Found", 200, "text/plain"]
    else:
        return ["", b"Content Not Found", 404, "text/plain"]

def create_account(request, data):
    if functions.verify_password(data['password'], data['rePassword']):
        database.add_user(data)
        return [b"", b"User Added", 201, "text/plain"]
    else:
        return [b"", b"Password does not meet all requirements or does not match", 404, "text/plain"]

#Loads newsfeed
def newsfeed(request):
    body = file.read_file(read_file_string + "frontend/pages/newsfeed.html")
    response_code = 200
    content_type = "text/html"
    return [body, response_code, content_type]

#Loads user profile
def profile(request):
    token = request.cookies.get('token')
    if token:
        body = functions.load_profile(token)
        if body:
            response_code = 200
            content_type = "text/html"
            return [body, response_code, content_type]
        else:
            return [b"", b"You must log in", 403, "text/plain"]
    else:
        return [b"", b"You must log in", 403, "text/plain"]


def add_post(request, data):
    return

def edit_profile(request, data):
    token = request.cookies.get('token')
    if token:
        body = functions.load_profile(token)
        if body:
            image_string = functions.add_image(data['picture'])
            database.update_profile(data, image_string, token)
            response_code = 200
            content_type = "text/plain"
            return [b"", b"Profile Updated", response_code, content_type]
        else:
            return [b"", b"You must log in", 403, "text/plain"]
    else:
        return [b"", b"You must log in", 403, "text/plain"]

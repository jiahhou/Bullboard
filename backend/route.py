import request, respond, actions
import re

class Router:
    # Initialize state variables
    def __init__(self, server):
        self.server = server
        self.routes = []
    
    # Add a list of possible request paths
    def add_route(self, route):
        self.routes.append(route)
    
    # We'll handle the request here. If a request is matched, we can respond to it appropiately.
    def handle_request(self, request):
        for route in self.routes:
            print(route.path)
            if route.match_req(route.path, request.path):
                route.action(self.server)
                return
        # If we've reached here, it means we never found a match. We can send a 404 Not Found.
        respond.send_failure(self.server)

class Route:
    # Initialize state variables
    def __init__(self, method, path, action):
        self.method = method
        self.path = path
        self.action = action

    # Use regex to match the current request against a list of all possible requests
    def match_req(self, route, request):
        search = re.search('^%s' % str(request), str(route))
        if search: 
            return True 
        else: 
            return False


def add_paths(router):
    # Each route is associated with a request type, path, and action.
    router.add_route(Route("GET", "/login", actions.login))
    router.add_route(Route("GET", "/", actions.login))
    router.add_route(Route("GET", "/register", actions.register))
    router.add_route(Route("GET", "/functions.js", actions.resp_to_html_paths))
    router.add_route(Route("GET", "/styles.css", actions.resp_to_html_paths))
    router.add_route(Route("GET", "/Bull_Board_Mat.png", actions.resp_to_html_paths))
    router.add_route(Route("GET", "/bull_knocker.jpeg", actions.resp_to_html_paths))
    router.add_route(Route("GET", "/welcome_mat.png", actions.resp_to_html_paths))
    # TODO - More routes will be added #


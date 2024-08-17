import requests

def check_csp(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if 'Content-Security-Policy' header is present
        csp_header = response.headers.get('Content-Security-Policy')

        if csp_header:
            print(f"Content-Security-Policy header found: {csp_header}")
        else:
            print("No Content-Security-Policy header found.")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    url = input("Enter the URL to check: ")
    if not url.startswith(('http://', 'https://')):
        print("Please include the protocol (http:// or https://) in the URL.")
    else:
        check_csp(url)

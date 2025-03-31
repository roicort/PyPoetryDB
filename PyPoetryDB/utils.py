def format_response(response):
    """Format the API response for easier consumption."""
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

def handle_errors(response):
    """Handle errors from the API response."""
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
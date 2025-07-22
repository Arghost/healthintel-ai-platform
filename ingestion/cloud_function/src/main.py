import requests
from datetime import datetime

def ingest_health_data(request):
    """
    Cloud Function to ingest data from a public API (placeholder).
    Logs timestamp and basic response info to Cloud Logging.
    """
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] Starting ingestion...")

    # Simulated public data source
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"✅ Fetched {len(response.json())} records from {url}")
    except requests.RequestException as e:
        print(f"❌ Error during ingestion: {e}")
        return f"Error: {e}", 500

    return "Ingestion completed successfully", 200
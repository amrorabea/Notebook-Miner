from waitress import serve
from app import app

if __name__ == "__main__":
    print("Starting server...")
    print("Server running on http://0.0.0.0:8000")
    print("Press Ctrl+C to quit")
    
    # Configure and run Waitress
    serve(
        app,
        host='0.0.0.0',
        port=8000,
        threads=4,               # Number of worker threads
        channel_timeout=300,     # Connection timeout in seconds
        cleanup_interval=30,     # How often to check for connection timeouts
        ident='CustomDashboard'  # Server identifier
    )
    
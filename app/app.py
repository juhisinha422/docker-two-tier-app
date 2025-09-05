import os
from flask import Flask
from flask_mysqldb import MySQL

# Initialize the Flask application
app = Flask(__name__)

# --- Database Configuration ---
# We get these values from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'mydatabase')

# Initialize MySQL
mysql = MySQL(app)

# --- Routes ---
@app.route('/')
def index():
    try:
        # Try to get a database connection
        cur = mysql.connection.cursor()
        
        # If we get here, the connection was successful
        cur.close()
        db_status = "Successfully connected to the database!"
        status_color = "green"
    except Exception as e:
        # If an exception occurs, the connection failed
        db_status = f"Database connection failed: {e}"
        status_color = "red"

    # Return a simple HTML page showing the connection status
    return f"""
    <html>
        <head><title>Two-Tier App Status</title></head>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <h1>Flask Application Tier</h1>
            <p>This is the web server front-end.</p>
            <h2 style="color: {status_color};">{db_status}</h2>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible outside the container
    app.run(host='0.0.0.0', port=5000)

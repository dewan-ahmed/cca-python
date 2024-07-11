from flask import Flask, send_from_directory, request, render_template_string
import os

app = Flask(__name__)

# Serve static files from the root directory
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('.', path)

@app.route('/')
def index():
    pod_name = os.getenv('HOSTNAME', 'Unknown')
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Captain Canary's Adventures</title>
            <style>
                body {{
                    text-align: center;
                    font-family: Arial, sans-serif;
                }}
                #canaryImg {{
                    width: 50%;
                    max-width: 500px; /* Adjust max-width as needed */
                    margin-top: 50px;
                }}
                #content {{
                    margin-top: 20px;
                }}
            </style>
            <script>
                function toggleImage() {{
                    var img = document.getElementById('canaryImg');
                    var btn = document.getElementById('toggleBtn');
                    var text = document.getElementById('displayText');
                    if (img.src.includes('canary-working.png')) {{
                        img.src = '/canary-vacation.png';
                        btn.textContent = 'Back to Work!';
                        text.innerHTML = "It's " + new Date().toLocaleTimeString('en-US', {{ timeZone: 'Pacific/Honolulu', hour: '2-digit', minute: '2-digit', hour12: true }}) + " in Hawaii.<br>While you're stuck debugging, Captain Canary is catching waves and enjoying the Aloha spirit! 🏄‍♂️🌺";
                    }} else {{
                        img.src = '/canary-working.png';
                        btn.textContent = 'Go on Vacation!';
                        text.innerHTML = 'Pod Name: {pod_name}';
                    }}
                }}
            </script>
        </head>
        <body>
            <img id="canaryImg" src="/canary-working.png" alt="Captain Canary Working">
            <div id="content">
                <button id="toggleBtn" onclick="toggleImage()">Go on Vacation!</button>
                <p id="displayText">Pod Name: {pod_name}</p>
            </div>
        </body>
        </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

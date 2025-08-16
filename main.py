import os
import datetime
import requests
from flask import Flask, session, redirect, request, url_for, jsonify, render_template
from websiteconfig import WebsiteConfig

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.urandom(24)  # Required for session

@app.route('/')
def index():
    theme = 'warm'  # Only warm theme available

    # Track online visitors (would normally be done with a database)
    visitor_id = request.remote_addr
    online_time = datetime.datetime.now()

    # For demo purposes, we'll just print this information
    print(f"Visitor {visitor_id} accessed the site at {online_time}")

    config = {
        'project_name': WebsiteConfig.PROJECT_NAME,
        'description': WebsiteConfig.DESCRIPTION,
        'bot_logo': WebsiteConfig.BOT_LOGO,
        'bot_invite_url': WebsiteConfig.BOT_INVITE_URL,
        'support_server_url': WebsiteConfig.SUPPORT_SERVER_URL,
        'topgg_vote_url': WebsiteConfig.TOPGG_VOTE_URL,
        'prefix_commands': WebsiteConfig.PREFIX_COMMANDS,
        'slash_commands': WebsiteConfig.SLASH_COMMANDS,
        'owner': WebsiteConfig.OWNER
    }

    return render_template(
        'index.html', 
        theme=theme, 
        config=config
    )

@app.route('/invite')
def invite():
    # Redirect to Discord bot invite link
    return redirect(WebsiteConfig.BOT_INVITE_URL)

@app.route('/support')
def support():
    # Redirect to support server
    return redirect(WebsiteConfig.SUPPORT_SERVER_URL)

@app.route('/bot-status')
def bot_status():
    """Return the current bot status"""
    import random

    return {
        'status': 'online',
        'uptime': 99.9,
        'ping': random.randint(8, 35),
        'last_updated': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Send to Discord webhook
        webhook_url = WebsiteConfig.CONTACT_WEBHOOK_URL

        # Format message for Discord
        embed = {
            "title": f"New Contact Form Submission: {subject}",
            "color": 3447003,  # Blue color
            "fields": [
                {"name": "Name", "value": name, "inline": True},
                {"name": "Email", "value": email, "inline": True},
                {"name": "Subject", "value": subject, "inline": True},
                {"name": "Message", "value": message, "inline": False}
            ],
            "footer": {
                "text": f"Sent from {WebsiteConfig.PROJECT_NAME} Contact Form"
            },
            "timestamp": datetime.datetime.utcnow().isoformat()
        }

        data = {
            "embeds": [embed],
            "username": "Contact Form Bot",
            "avatar_url": WebsiteConfig.BOT_LOGO
        }

        try:
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
            print(f"Contact form submission sent to Discord: {name} ({email}), Subject: {subject}")
        except Exception as e:
            print(f"Error sending to Discord webhook: {e}")

        # Return success response to the user
        return jsonify({'success': True, 'message': 'Your message has been sent!'})

if __name__ == '__main__':
    # Make sure templates directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Make sure static directory exists
    if not os.path.exists('static'):
        os.makedirs('static')

    # Use configured port and IP
    app.run(host=WebsiteConfig.IP_ADDRESS, port=WebsiteConfig.PORT, debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# Sample portfolio data
portfolio_data = {
    "name": "Alex Johnson",
    "title": "Full Stack Developer",
    "bio": "Passionate developer with 5+ years of experience building web applications.",
    "skills": ["Python", "Flask", "JavaScript", "React", "PostgreSQL", "Docker"],
    "projects": [
        {
            "title": "E-Commerce Platform",
            "description": "Built a full-featured online store with payment processing",
            "tech": ["Python", "Flask", "Stripe API", "PostgreSQL"],
            "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400"
        },
        {
            "title": "Task Management App",
            "description": "Collaborative project management tool with real-time updates",
            "tech": ["Python", "WebSockets", "React", "MongoDB"],
            "image": "https://images.unsplash.com/photo-1611224923853-80b023f02d71?w-400"
        },
        {
            "title": "Weather Dashboard",
            "description": "Real-time weather application with interactive maps",
            "tech": ["JavaScript", "API Integration", "Chart.js", "Bootstrap"],
            "image": "https://images.unsplash.com/photo-1592210454359-9043f067919b?w=400"
        }
    ],
    "contact": {
        "email": "hello@example.com",
        "github": "https://github.com/username",
        "linkedin": "https://linkedin.com/in/username"
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data, current_year=datetime.now().year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real app, you'd save this to a database or send an email
        print(f"New message from {name} ({email}): {message}")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

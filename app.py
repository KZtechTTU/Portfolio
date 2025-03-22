from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
        user_name="Your Name",
        user_title="Your Job Title",
        user_image=url_for('static', filename='image/your_image.jpg'),
        linkedin_url="https://linkedin.com/in/yourprofile",
        github_url="https://github.com/yourprofile",
        email="your.email@example.com",
        phone="+1234567890",
        about_me="A short bio about yourself.",
        experience=[
            {
                "company": "Company Name",
                "location": "Location",
                "position": "Job Title",
                "duration": "Start Date - End Date",
                "responsibilities": [
                    "Responsibility 1",
                    "Responsibility 2"
                ]
            }
        ],
        projects=[
            {
                "title": "Project Name",
                "description": "Brief description of your project."
            }
        ]
    )

if __name__ == '__main__':
    app.run(debug=True)

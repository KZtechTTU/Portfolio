# Portfolio Website Template  

This is a simple portfolio website template using Flask. Users can customize their personal details, profile picture, work experience, and projects dynamically.  

## Features  

- Responsive and customizable portfolio  
- Dynamic content rendering using Flask and Jinja2  
- Sections for About, Experience, Projects, and Contact  
- Image popup functionality  

## Installation  

### 1. Install Dependencies  

Ensure you have Python installed. Then, install Flask:  

```sh
pip install flask
```

### 2. Folder Structure

```
portfolio/
│-- static/
│   │-- style.css
│   │-- script.js
│   │-- image/
│       │-- your_image.jpg
│-- templates/
│   │-- index.html
│-- app.py
│-- requirements.txt
│-- README.md

```

### 3. Add Your Details

In `app.py`, define your personal details:

```python
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

```

### 4. Run the Application

```bash
python app.py
```

Then, open `http://127.0.0.1:5000/` in your browser.

## Customization

- **Profile Picture**: Place your image in `static/images/` and update `your_image` in `app.py`.
- **Work Experience & Projects**: Modify the `experience` and `projects` lists in `app.py`.
- **Styling**: Edit `static/style.css` for custom styles.

## License

This template is open-source and free to use for personal and professional projects.

---

Feel free to modify this template to match your personal or professional

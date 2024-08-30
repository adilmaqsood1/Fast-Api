
from fastapi import FastAPI, Form
from pydantic import EmailStr
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

# Endpoint to serve the HTML form
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admission Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 500px;
                margin: auto;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h2 {
                text-align: center;
                color: #333;
            }
            label {
                display: block;
                margin-bottom: 8px;
                color: #555;
            }
            input[type="text"], input[type="number"], input[type="email"] {
                width: 100%;
                padding: 8px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }
            input[type="submit"] {
                width: 100%;
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Admission Form</h2>
            <form action="/submit-form/" method="post">
                <label for="first_name">First Name:</label>
                <input type="text" id="first_name" name="first_name" required>
                
                <label for="last_name">Last Name:</label>
                <input type="text" id="last_name" name="last_name" required>
                
                <label for="age">Age:</label>
                <input type="number" id="age" name="age">
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    """

# Endpoint to handle the form submission
@app.post("/submit-form/")
def submit_form(
    first_name: str = Form(...),
    last_name: str = Form(...),
    age: Optional[int] = Form(None),
    email: EmailStr = Form(...)
):
    # Process the data (e.g., save to a database)
    # For now, we just return the data
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
    }


    
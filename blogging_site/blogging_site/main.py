from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
import uuid

app = FastAPI()

# Set up template and static file directories
app.mount("static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# In-memory "database" of posts (for simplicity)
posts = {}

# Home page showing all blog posts
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts})

# Page to create a new blog post
@app.get("/create-post", response_class=HTMLResponse)
def create_post_form(request: Request):
    return templates.TemplateResponse("create_post.html", {"request": request})

# Handling form submission to create a new post
@app.post("/create-post", response_class=HTMLResponse)
def create_post(request: Request, title: str = Form(...), content: str = Form(...)):
    post_id = str(uuid.uuid4())  # Generate a unique ID for the post
    posts[post_id] = {"title": title, "content": content}
    return RedirectResponse(url="/", status_code=303)

# Page to view a specific post by ID
@app.get("/post/{post_id}", response_class=HTMLResponse)
def post_detail(request: Request, post_id: str):
    post = posts.get(post_id)
    if not post:
        return templates.TemplateResponse("404.html", {"request": request})
    return templates.TemplateResponse("post_detail.html", {"request": request, "post": post})

# Page to edit an existing post
@app.get("/edit-post/{post_id}", response_class=HTMLResponse)
def edit_post_form(request: Request, post_id: str):
    post = posts.get(post_id)
    if not post:
        return templates.TemplateResponse("404.html", {"request": request})
    return templates.TemplateResponse("create_post.html", {"request": request, "post": post, "post_id": post_id})

# Handling form submission to edit an existing post
@app.post("/edit-post/{post_id}", response_class=HTMLResponse)
def edit_post(request: Request, post_id: str, title: str = Form(...), content: str = Form(...)):
    posts[post_id] = {"title": title, "content": content}
    return RedirectResponse(url=f"/post/{post_id}", status_code=303)

# Handling deleting a post
@app.get("/delete-post/{post_id}")
def delete_post(request: Request, post_id: str):
    if post_id in posts:
        del posts[post_id]
    return RedirectResponse(url="/", status_code=303)

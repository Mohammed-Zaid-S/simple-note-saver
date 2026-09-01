# Note Saver Web Application

A modern, full-stack note-taking web application built with FastAPI, MongoDB, and Jinja2 templates, featuring a clean card-based UI and persistent cloud storage.

## Features
- **Dynamic Note Viewing**: Browse all saved notes on a responsive grid layout with visual indicators for important entries.
- **Detailed View**: Click any note to navigate to its dedicated route (`/{title}`) and inspect its full content.
- **Note Creation**: Add new notes via an interactive form supporting titles, text bodies, and importance flags.
- **Note Deletion**: Remove obsolete notes seamlessly with direct backend integration.
- **Cloud Persistence**: Fully integrated with MongoDB Atlas for reliable data storage.

## Tech Stack
- **Backend**: Python, FastAPI, Uvicorn, PyMongo
- **Frontend**: Jinja2 Templates, HTML5, CSS3 (Inter font, CSS Grid, Flexbox)
- **Database**: MongoDB Atlas


## Getting Started

### Prerequisites

* Python 3.10+
* MongoDB Atlas account and connection string

### Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/notes-app.git](https://github.com/your-username/notes-app.git)
cd notes-app

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure the Database:**
Verify your MongoDB connection string in `main.py` points to your active database cluster.

### Running the Application

Launch the development server using FastAPI:

```bash
fastapi dev main.py

```

Open your browser and navigate to `http://127.0.0.1:8000` to interact with the live application.

```

```

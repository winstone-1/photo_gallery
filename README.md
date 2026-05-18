# 📸 Photo Gallery

A Django web app for browsing, filtering, and interacting with photos and artworks.

## Tech Stack
- Python 3.12 / Django 5.x
- PostgreSQL
- Tailwind CSS (CDN)
- Deployed on Render

## Setup
1. Clone the repo
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. Create `.env` (see `.env.example`)
5. Create PostgreSQL DB: `createdb photo_gallery_db`
6. `python manage.py migrate`
7. `python manage.py runserver`
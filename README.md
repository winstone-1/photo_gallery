# Photo Gallery

A Django web app for browsing, filtering, and interacting with a curated collection of photos and artworks.

## Tech Stack

- Python 3.14 / Django 6.x
- PostgreSQL
- Tailwind CSS (CDN)
- Cloudinary (image storage)
- Django Allauth (Google OAuth)
- Deployed on Render

## Local Setup

1. Clone the repo
   git clone https://github.com/winstone-1/photo-gallery.git
   cd photo-gallery

2. Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Create .env file in the project root
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=photo_gallery_db
   DB_USER=postgres
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=5432
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   GOOGLE_CLIENT_ID=your-client-id
   GOOGLE_CLIENT_SECRET=your-client-secret

5. Create PostgreSQL database
   createdb photo_gallery_db

6. Run migrations
   python manage.py migrate

7. Create superuser
   python manage.py createsuperuser

8. Start server
   python manage.py runserver

## Deployment on Render

1. Push code to GitHub
2. Go to render.com and create a new Web Service
3. Connect your GitHub repo
4. Set build command: ./build.sh
5. Set start command: gunicorn core.wsgi:application
6. Add all environment variables from .env (with production values)
7. Add a PostgreSQL database from Render dashboard
8. Update ALLOWED_HOSTS env var to your Render domain
9. Update Google OAuth redirect URI to your Render domain

## Live Site

https://your-app-name.onrender.com
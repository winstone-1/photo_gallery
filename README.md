# Photo Gallery

A  photo gallery web application built with Django, allowing users to register, browse a curated collection of photos, filter by tags, like or dislike photos, and manage their personal profiles. Supports Google OAuth sign-in via django-allauth and stores all media on Cloudinary.

---

## Live Link

[https://photo-gallery-9ij8.onrender.com](https://photo-gallery-9ij8.onrender.com)

---


## Features

### User Authentication
- Register with username, email, and password
- Login and logout with Django's built-in authentication system
- Google OAuth sign-in via django-allauth — users can sign in with their Google account in one click
- Custom user model extending Django's AbstractUser with bio and profile picture fields
- Password change functionality with session preservation using `update_session_auth_hash`

### User Profile Management
- Dedicated profile page showing username, email, bio, profile picture, and member since date
- Editable profile — users can update their username, email, bio, and profile picture
- Profile picture stored on Cloudinary with automatic URL resolution
- Password change form on the edit profile page with proper validation

### Photo Gallery
- Homepage gallery displaying all photos in a responsive 3-column grid
- Each photo card shows the image, title, tags, like/dislike counts, and upload date
- Clicking a photo card opens the full detail view with description, tags, uploader info, and vote buttons
- Photos are ordered by most recently uploaded
- Auth-gated — unauthenticated users are redirected to the login page

### Tag Filtering
- Photos can be tagged with multiple tags via a ManyToMany relationship
- Tag pills displayed above the gallery grid for one-click filtering
- Active tag is highlighted — clicking it again or clicking All resets the filter
- Tags on the photo detail page are clickable and redirect back to the filtered gallery

### Like and Dislike System
- Logged-in users can like or dislike any photo
- Voting is toggle-based — clicking the same vote removes it, clicking the opposite switches it
- Like and dislike counts update immediately on redirect
- Each user can only have one vote per photo enforced at the database level via `unique_together`

### Responsive Design
- Built with Tailwind CSS via CDN with a custom emerald green color palette
- Responsive grid layout — 1 column on mobile, 2 on tablet, 3 on desktop
- Mobile hamburger menu with JavaScript toggle
- Consistent dark theme across all pages using custom Tailwind color extensions

### Django Admin
- Custom `CustomUserAdmin` extending Django's `UserAdmin` with bio and profile picture fields
- `PhotoAdmin` with thumbnail preview, tag filter, and search by title and description
- `TagAdmin` and `LikeAdmin` registered with appropriate list displays and filters
- All models manageable from the admin panel at `/admin/`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| Framework | Django 6.0 |
| Database | PostgreSQL (local and Render) |
| Auth | Django built-in + django-allauth (Google OAuth2) |
| Media Storage | Cloudinary via django-cloudinary-storage |
| Styling | Tailwind CSS (CDN) |
| Static Files | WhiteNoise |
| Deployment | Render |
| Version Control | Git + GitHub |

---



## Local Setup

### Prerequisites
- Python 3.12 or higher
- PostgreSQL installed and running
- A Cloudinary account (free tier works)
- A Google Cloud project with OAuth2 credentials

### 1. Clone the repository

```bash
git clone https://github.com/winstone-1/photo_gallery.git
cd photo_gallery
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the `.env` file

Create a `.env` file in the project root with the following variables (see [Environment Variables](#environment-variables) for details):
- SECRET_KEY=your-secret-key
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- DB_NAME=photo_gallery_db
- DB_USER=postgres
- DB_PASSWORD=yourpassword
- DB_HOST=localhost
- DB_PORT=5432
- CLOUDINARY_CLOUD_NAME=your-cloud-name
- CLOUDINARY_API_KEY=your-api-key
- CLOUDINARY_API_SECRET=your-api-secret
- GOOGLE_CLIENT_ID=your-client-id
- GOOGLE_CLIENT_SECRET=your-client-secret
### 5. Create the PostgreSQL database

```bash
createdb photo_gallery_db
```

Or in psql:

```sql
CREATE DATABASE photo_gallery_db;
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---


## Database Setup

This project uses PostgreSQL. The Django models are:

### `accounts.CustomUser`
Extends Django's `AbstractUser` with:
- `email` — unique, required
- `bio` — optional text field
- `profile_picture` — optional image stored on Cloudinary

### `photo_gallery.Photo`
- `title` — CharField
- `description` — optional TextField
- `image` — ImageField stored on Cloudinary
- `tags` — ManyToManyField to Tag
- `uploaded_by` — ForeignKey to CustomUser
- `created_at` — auto timestamp

### `photo_gallery.Tag`
- `name` — unique CharField

### `photo_gallery.Like`
- `user` — ForeignKey to CustomUser
- `photo` — ForeignKey to Photo
- `value` — choice of `like` or `dislike`
- `unique_together` on user and photo — one vote per user per photo

---



## Deployment

This project is deployed on [Render](https://render.com).

### Steps

1. Push your code to GitHub

2. Create a PostgreSQL database on Render:
   - Render dashboard → **New** → **PostgreSQL**
   - Copy the connection details

3. Create a Web Service on Render:
   - Render dashboard → **New** → **Web Service**
   - Connect your GitHub repository
   - Build command: `./build.sh`
   - Start command: `gunicorn core.wsgi:application`

4. Set all environment variables on the web service using production values:
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-app.onrender.com`
   - All DB variables from the Render PostgreSQL dashboard
   - All Cloudinary and Google OAuth variables

5. Add your Render domain to Google Cloud Console OAuth redirect URIs

6. Deploy — Render runs `build.sh` which installs dependencies, collects static files, and runs migrations automatically

### `build.sh`

```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```



## Author

Winstone 
GitHub: [winstone-1](https://github.com/winstone-1)
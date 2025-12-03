# Deploy ShieldHer to Railway.app

Railway.app has a better free tier than Render with:
- ✅ Shell access for running migrations
- ✅ $5 free credit per month
- ✅ Better Docker support
- ✅ Automatic HTTPS

## Prerequisites

1. GitHub account (you already have this)
2. Railway account - Sign up at https://railway.app

## Step 1: Sign Up for Railway

1. Go to https://railway.app
2. Click **Login** or **Start a New Project**
3. Sign in with your GitHub account
4. Authorize Railway to access your repositories

## Step 2: Create a New Project

1. Click **New Project**
2. Select **Deploy from GitHub repo**
3. Choose your repository: **Cedar-Creatives/ShieldHer**
4. Railway will detect your project

## Step 3: Set Up Backend Service

1. Railway will detect the Dockerfile in `backend/`
2. Click on the backend service
3. Go to **Settings** tab
4. Set **Root Directory** to: `backend`
5. Set **Dockerfile Path** to: `Dockerfile`

## Step 4: Add PostgreSQL Database

1. In your project, click **New**
2. Select **Database** → **PostgreSQL**
3. Railway will create a database and set `DATABASE_URL` automatically

## Step 5: Set Environment Variables

Click on your backend service → **Variables** tab → Add these:

```bash
DJANGO_SETTINGS_MODULE=config.settings.production
SECRET_KEY=<generate-a-secret-key>
ENCRYPTION_KEY=CXFO5kh4zNCvoDRZyuRHQ1HlAlX_McKf0_yVQFQgTME=
ALLOWED_HOSTS=.railway.app
DEBUG=False
CORS_ALLOWED_ORIGINS=https://your-frontend-url.railway.app
PORT=8000
```

**To generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 6: Run Migrations

After the first deployment:

1. Click on your backend service
2. Go to **Settings** → **Service**
3. Scroll to **Deploy** section
4. Click **Open Shell** (this is available on Railway!)
5. Run:
   ```bash
   python manage.py migrate
   ```

## Step 7: Deploy Frontend

1. In your project, click **New** → **GitHub Repo**
2. Select the same repository
3. Click on the frontend service
4. Go to **Settings**
5. Set **Root Directory** to: `frontend`
6. Set **Build Command** to: `npm install && npm run build`
7. Set **Start Command** to: `npm run preview`

Or use a static host:
- Deploy `frontend/dist` to **Vercel** or **Netlify** (free)

## Step 8: Configure Frontend Environment

In frontend service → **Variables**:

```bash
VITE_API_URL=https://your-backend-url.railway.app
```

## Step 9: Get Your URLs

Railway will provide URLs like:
- Backend: `https://shieldher-backend-production.up.railway.app`
- Frontend: `https://shieldher-frontend-production.up.railway.app`

## Step 10: Update CORS

Update backend environment variable:
```bash
CORS_ALLOWED_ORIGINS=https://shieldher-frontend-production.up.railway.app
```

## Alternative: Use Railway CLI

Install Railway CLI:
```bash
npm install -g @railway/cli
```

Login and deploy:
```bash
railway login
railway init
railway up
```

## Troubleshooting

### Migrations Not Running?

Use the shell:
```bash
# In Railway dashboard → Backend service → Settings → Open Shell
python manage.py migrate
python manage.py createsuperuser  # Optional: create admin user
```

### Check Logs

Railway dashboard → Service → **Deployments** → Click on deployment → View logs

### Database Connection Issues

Railway automatically sets `DATABASE_URL`. Make sure your `production.py` uses:
```python
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}
```

## Cost Estimate

Railway free tier includes:
- $5 credit per month
- ~500 hours of usage
- Should be enough for a small project

## Advantages Over Render

✅ Shell access (can run migrations manually)
✅ Better Docker support
✅ Faster deployments
✅ Better free tier
✅ Easier to debug

## Files Already Configured

Your project is ready for Railway:
- ✅ `backend/Dockerfile` - Configured
- ✅ `backend/start.sh` - Runs migrations automatically
- ✅ Environment variables documented
- ✅ Database configuration ready

## Next Steps After Deployment

1. Test the reports feature
2. Create an admin user: `python manage.py createsuperuser`
3. Access admin at: `https://your-backend-url.railway.app/admin`
4. Verify all features work

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Your code is ready - just deploy!

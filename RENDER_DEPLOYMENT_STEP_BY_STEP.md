# 🚀 Complete Render Deployment Guide for ShieldHer

## 📋 Overview

This guide will walk you through deploying ShieldHer on Render.com from start to finish.

**What you'll deploy:**
- PostgreSQL Database (Free tier)
- Django Backend (Free tier)
- React Frontend (Free tier)

**Total cost:** $0/month (Free tier)

**Time required:** 30-45 minutes

---

## ✅ Prerequisites

Before starting, ensure you have:

- [ ] GitHub account
- [ ] Render.com account (sign up at https://render.com)
- [ ] Your ShieldHer code pushed to GitHub
- [ ] Production keys generated (we'll do this together)

---

## 📦 Part 1: Prepare Your Code

### Step 1.1: Generate Production Keys

Open terminal in your project:

```bash
cd backend
.\venv\Scripts\activate
python generate_production_keys.py
```

**Save the output!** You'll need these keys later. Copy them to a text file temporarily (we'll delete it after deployment).

**Example output:**
```
DJANGO_SECRET_KEY: qxbe74f9v=5qbnqer(if#qtlm08m^gs3...
JWT_SECRET_KEY: kLaxoqCjnprMXjmF9YjQM_mkLRGcd_bQrx3Y...
ENCRYPTION_KEY: vE3js7xbDZSWlZuEftfnHtsJRRrzx9d_wwUN...
```

### Step 1.2: Verify Your Code is on GitHub

```bash
# Check your remote
git remote -v

# If not set up, add your GitHub repo
git remote add origin https://github.com/YOUR_USERNAME/ShieldHer.git

# Push your code
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

**Important:** Make sure `.env` is in `.gitignore` (it already is - don't commit secrets!)

### Step 1.3: Verify Dockerfile Exists

Check that these files exist:
- ✅ `backend/Dockerfile`
- ✅ `frontend/Dockerfile`
- ✅ `backend/requirements/production.txt`

These are already in your project, so you're good to go!

---

## 🗄️ Part 2: Deploy PostgreSQL Database

### Step 2.1: Create Render Account

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended) or email
4. Verify your email

### Step 2.2: Create PostgreSQL Database

1. **Go to Render Dashboard**
   - URL: https://dashboard.render.com

2. **Click "New +" button** (top right)
   - Select "PostgreSQL"

3. **Configure Database:**

   ```
   ┌─────────────────────────────────────────────────┐
   │ Create PostgreSQL                               │
   ├─────────────────────────────────────────────────┤
   │ Name: shieldher-db                              │
   │ Database: shieldher                             │
   │ User: shieldher_user                            │
   │ Region: Oregon (US West) ← Choose closest      │
   │ PostgreSQL Version: 15                          │
   │ Datadog API Key: [leave empty]                  │
   │ Plan: Free                                      │
   └─────────────────────────────────────────────────┘
   ```

   **Settings:**
   - **Name:** `shieldher-db`
   - **Database:** `shieldher`
   - **User:** `shieldher_user`
   - **Region:** Oregon (US West) - or closest to your users
   - **PostgreSQL Version:** 15
   - **Plan:** Free

4. **Click "Create Database"**

5. **Wait for database to be created** (1-2 minutes)
   - Status will change from "Creating" to "Available"

### Step 2.3: Copy Database Connection String

1. **On the database page, find "Connections" section**

2. **Copy the "Internal Database URL"** (NOT External)
   - It looks like: `postgresql://shieldher_user:password@dpg-xxxxx/shieldher`
   - Click the copy icon next to it

3. **Save this URL** - you'll need it for the backend service

**⚠️ Important:** Use the **Internal** URL, not External!

```
✅ Internal Database URL: postgresql://shieldher_user:pass@dpg-xxxxx-a/shieldher
❌ External Database URL: postgresql://shieldher_user:pass@dpg-xxxxx-a.oregon-postgres.render.com/shieldher
```

---

## 🐍 Part 3: Deploy Django Backend

### Step 3.1: Create Web Service

1. **Click "New +" button** (top right)
   - Select "Web Service"

2. **Connect GitHub Repository**
   - Click "Connect account" if not connected
   - Authorize Render to access your repositories
   - Find and select your ShieldHer repository
   - Click "Connect"

### Step 3.2: Configure Backend Service

Fill in the form:

```
┌─────────────────────────────────────────────────┐
│ Create Web Service                              │
├─────────────────────────────────────────────────┤
│ Name: shieldher-backend                         │
│ Region: Oregon (US West) ← Same as database    │
│ Branch: main                                    │
│ Root Directory: [leave empty]                   │
│ Runtime: Docker                                 │
│ Dockerfile Path: backend/Dockerfile             │
│ Docker Context: backend                         │
│ Docker Command: [leave empty]                   │
│ Plan: Free                                      │
└─────────────────────────────────────────────────┘
```

**Settings:**
- **Name:** `shieldher-backend`
- **Region:** Oregon (US West) - **MUST match database region**
- **Branch:** `main` (or `master` if that's your default)
- **Root Directory:** Leave empty
- **Environment:** Docker
- **Dockerfile Path:** `backend/Dockerfile`
- **Docker Context:** `backend`
- **Docker Command:** Leave empty (uses CMD from Dockerfile)
- **Plan:** Free

### Step 3.3: Add Environment Variables

**Scroll down to "Environment Variables" section**

Click "Add Environment Variable" for each of these:

#### Required Variables:

| Key | Value | Notes |
|-----|-------|-------|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` | Fixed value |
| `SECRET_KEY` | `<your-generated-django-key>` | From Step 1.1 |
| `JWT_SECRET_KEY` | `<your-generated-jwt-key>` | From Step 1.1 |
| `ENCRYPTION_KEY` | `<your-generated-encryption-key>` | From Step 1.1 |
| `DATABASE_URL` | `<internal-database-url>` | From Step 2.3 |
| `ALLOWED_HOSTS` | `.onrender.com` | Fixed value |
| `DEBUG` | `False` | Fixed value |
| `CORS_ALLOWED_ORIGINS` | `https://shieldher-frontend.onrender.com` | Update after frontend deploy |
| `PORT` | `8000` | Fixed value |
| `RATE_LIMIT_ENABLED` | `True` | Fixed value |

**How to add each variable:**

1. Click "Add Environment Variable"
2. Enter Key (e.g., `SECRET_KEY`)
3. Enter Value (paste from your generated keys)
4. Click outside the field to save
5. Repeat for all variables

**Example:**
```
┌─────────────────────────────────────────────────┐
│ Key:   SECRET_KEY                               │
│ Value: qxbe74f9v=5qbnqer(if#qtlm08m^gs3...     │
└─────────────────────────────────────────────────┘
```

### Step 3.4: Create Web Service

1. **Scroll to bottom**
2. **Click "Create Web Service"**
3. **Wait for deployment** (5-10 minutes)

**You'll see:**
- "Build in progress..."
- "Deploying..."
- "Live" (when successful)

### Step 3.5: Run Database Migrations

Once the service is "Live":

1. **Click on your backend service** (shieldher-backend)
2. **Click "Shell" tab** (left sidebar)
3. **Wait for shell to connect** (may take 30 seconds)
4. **Run migrations:**

```bash
python manage.py migrate
```

**Expected output:**
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
  Applying sessions.0001_initial... OK
```

5. **Create superuser:**

```bash
python manage.py createsuperuser
```

**Enter:**
- Email: `admin@shieldher.com`
- Username: `admin`
- Password: `<choose-a-strong-password>`
- Password (again): `<same-password>`

**Save your admin credentials!**

6. **Load sample data (optional):**

```bash
python load_sample_data.py
```

### Step 3.6: Verify Backend is Working

1. **Copy your backend URL** (shown at top of service page)
   - Example: `https://shieldher-backend.onrender.com`

2. **Test health endpoint:**
   - Open browser: `https://shieldher-backend.onrender.com/api/health/`
   - Should see: `{"status":"healthy"}`

3. **Test admin panel:**
   - Open: `https://shieldher-backend.onrender.com/admin/`
   - Login with your superuser credentials
   - Should see Django admin dashboard

**✅ If both work, backend is deployed successfully!**

---

## ⚛️ Part 4: Deploy React Frontend

### Step 4.1: Create Static Site

1. **Click "New +" button** (top right)
   - Select "Static Site"

2. **Connect Repository**
   - Select your ShieldHer repository (already connected)
   - Click "Connect"

### Step 4.2: Configure Frontend Service

Fill in the form:

```
┌─────────────────────────────────────────────────┐
│ Create Static Site                              │
├─────────────────────────────────────────────────┤
│ Name: shieldher-frontend                        │
│ Branch: main                                    │
│ Root Directory: [leave empty]                   │
│ Build Command: cd frontend && npm install &&    │
│                npm run build                    │
│ Publish Directory: frontend/dist                │
└─────────────────────────────────────────────────┘
```

**Settings:**
- **Name:** `shieldher-frontend`
- **Branch:** `main`
- **Root Directory:** Leave empty
- **Build Command:** `cd frontend && npm install && npm run build`
- **Publish Directory:** `frontend/dist`

### Step 4.3: Add Environment Variable

**Scroll to "Environment Variables"**

Add one variable:

| Key | Value |
|-----|-------|
| `VITE_API_URL` | `https://shieldher-backend.onrender.com` |

**Replace with your actual backend URL from Step 3.6!**

### Step 4.4: Create Static Site

1. **Click "Create Static Site"**
2. **Wait for build** (3-5 minutes)

**You'll see:**
- "Build in progress..."
- "Publishing..."
- "Live" (when successful)

### Step 4.5: Verify Frontend is Working

1. **Copy your frontend URL**
   - Example: `https://shieldher-frontend.onrender.com`

2. **Open in browser**
   - Should see ShieldHer homepage
   - Navigation should work
   - Quick Exit button should be visible

**✅ If homepage loads, frontend is deployed!**

---

## 🔗 Part 5: Connect Frontend and Backend

### Step 5.1: Update CORS Settings

Now that you have the actual frontend URL, update backend CORS:

1. **Go to backend service** (shieldher-backend)
2. **Click "Environment" tab**
3. **Find `CORS_ALLOWED_ORIGINS`**
4. **Update value to your actual frontend URL:**
   ```
   https://shieldher-frontend.onrender.com
   ```
5. **Click "Save Changes"**
6. **Backend will automatically redeploy** (2-3 minutes)

### Step 5.2: Test Integration

1. **Open frontend:** `https://shieldher-frontend.onrender.com`

2. **Test Lessons Page:**
   - Click "Lessons" in navigation
   - Should see lessons loaded from backend
   - If you loaded sample data, you'll see 3 lessons

3. **Test Resources Page:**
   - Click "Resources" in navigation
   - Should see resources loaded from backend

4. **Test Report Form:**
   - Click "Report" in navigation
   - Form should load
   - Try submitting a test report

5. **Check Browser Console:**
   - Press F12 to open DevTools
   - Go to Console tab
   - Should see NO CORS errors
   - Should see NO 404 errors

**✅ If all pages work without errors, deployment is complete!**

---

## 🎉 Part 6: Final Verification

### Checklist

- [ ] Database is "Available" in Render dashboard
- [ ] Backend service is "Live"
- [ ] Frontend site is "Live"
- [ ] Backend health check responds: `/api/health/`
- [ ] Admin panel accessible: `/admin/`
- [ ] Frontend homepage loads
- [ ] Lessons page loads data from API
- [ ] Resources page loads data from API
- [ ] Report form is accessible
- [ ] No CORS errors in browser console
- [ ] Quick Exit button works
- [ ] Mobile responsive (test on phone or DevTools)

### Test All Features

1. **Homepage**
   - [ ] Loads without errors
   - [ ] Navigation works
   - [ ] Quick Exit button visible

2. **Lessons**
   - [ ] List loads from API
   - [ ] Lesson cards display correctly
   - [ ] Click on lesson works

3. **Resources**
   - [ ] List loads from API
   - [ ] Resource cards display correctly
   - [ ] External links work

4. **Report Form**
   - [ ] Form loads
   - [ ] Can fill out form
   - [ ] Submission works
   - [ ] Confirmation code received

5. **Admin Panel**
   - [ ] Login works
   - [ ] Can view lessons
   - [ ] Can view resources
   - [ ] Can view reports
   - [ ] Can create/edit content

---

## 📝 Part 7: Update Your README

Update your `README.md` with live URLs:

```markdown
## 🌐 Live Demo

**Frontend:** https://shieldher-frontend.onrender.com
**Backend API:** https://shieldher-backend.onrender.com
**Admin Panel:** https://shieldher-backend.onrender.com/admin/

> Note: Free tier may take 30-60 seconds for initial load (cold start)
```

Commit and push:

```bash
git add README.md
git commit -m "Add live deployment URLs"
git push origin main
```

---

## 🔒 Part 8: Security Checklist

After deployment, verify:

- [ ] `DEBUG=False` in production
- [ ] Unique production keys (not dev keys)
- [ ] `.env` not committed to Git
- [ ] Database uses internal URL
- [ ] CORS only allows your frontend
- [ ] Admin password is strong
- [ ] SSL/HTTPS active (automatic on Render)
- [ ] Rate limiting enabled

---

## 🐛 Troubleshooting

### Backend won't deploy

**Error: "Build failed"**

**Check:**
1. Dockerfile exists at `backend/Dockerfile`
2. Docker Context is set to `backend`
3. requirements/production.txt exists
4. Check build logs for specific error

**Fix:**
- Review logs in Render dashboard
- Ensure all dependencies in requirements.txt
- Check Python version compatibility

---

### Database connection error

**Error: "OperationalError: could not connect to server"**

**Check:**
1. Using **Internal** Database URL (not External)
2. Backend and database in same region
3. DATABASE_URL environment variable set correctly

**Fix:**
```
1. Go to database page
2. Copy Internal Database URL
3. Update DATABASE_URL in backend environment
4. Redeploy backend
```

---

### CORS errors in browser

**Error: "Access-Control-Allow-Origin" in console**

**Check:**
1. CORS_ALLOWED_ORIGINS includes your frontend URL
2. URL includes `https://` (not `http://`)
3. No trailing slash in URL
4. Backend has redeployed after CORS change

**Fix:**
```
1. Go to backend → Environment
2. Update CORS_ALLOWED_ORIGINS
3. Value: https://shieldher-frontend.onrender.com
4. Save (backend will redeploy)
5. Clear browser cache
6. Hard refresh (Ctrl+Shift+R)
```

---

### Frontend shows blank page

**Check:**
1. Build completed successfully
2. VITE_API_URL is set correctly
3. Publish directory is `frontend/dist`
4. Build command includes `cd frontend`

**Fix:**
```
1. Check build logs for errors
2. Verify VITE_API_URL in environment
3. Trigger manual deploy
4. Check browser console for errors
```

---

### Static files not loading (CSS/JS missing)

**Error: 404 on static files**

**Check:**
1. `collectstatic` ran in Dockerfile
2. WhiteNoise in MIDDLEWARE
3. STATIC_ROOT configured

**Fix:**
- Already configured in your Dockerfile
- If issue persists, check backend logs
- Verify `staticfiles` directory created

---

### Cold start delay (30-60 seconds)

**This is normal on free tier!**

**Why:**
- Free tier services spin down after 15 minutes of inactivity
- First request wakes up the service
- Subsequent requests are fast

**Solutions:**
1. **Accept it** - it's free!
2. **Upgrade to paid tier** ($7/month) - always on
3. **Use uptime monitor** - ping every 10 minutes to keep alive
   - UptimeRobot (free)
   - Better Uptime (free tier)

---

### Migrations not applied

**Error: "Table doesn't exist"**

**Fix:**
```bash
# In backend Shell tab
python manage.py migrate
python manage.py migrate --run-syncdb
```

---

### Can't access admin panel

**Error: 404 or login fails**

**Check:**
1. Superuser created
2. URL is correct: `/admin/` (with trailing slash)
3. Migrations applied

**Fix:**
```bash
# In backend Shell tab
python manage.py createsuperuser
```

---

## 📊 Monitoring Your Deployment

### Render Dashboard

**Check regularly:**
1. **Services status** - should be "Live"
2. **Build logs** - for errors
3. **Deploy logs** - for runtime errors
4. **Metrics** - CPU, memory usage

### Set Up Alerts

1. Go to service settings
2. Enable "Deploy Notifications"
3. Add your email
4. Get notified of deploy failures

### Health Checks

Render automatically monitors:
- HTTP health checks
- Service availability
- Auto-restart on failure

---

## 💰 Cost Breakdown

### Free Tier (Current)

| Service | Cost | Limits |
|---------|------|--------|
| PostgreSQL | $0 | 1GB storage, 90 days |
| Backend | $0 | 512MB RAM, spins down after 15min |
| Frontend | $0 | 100GB bandwidth/month |
| **Total** | **$0/month** | Good for demo/MVP |

### Paid Tier (When Ready)

| Service | Cost | Benefits |
|---------|------|----------|
| PostgreSQL Starter | $7/month | 10GB storage, daily backups |
| Backend Starter | $7/month | Always-on, 512MB RAM |
| Frontend | $0 | Same as free |
| **Total** | **$14/month** | Production-ready |

---

## 🚀 Next Steps

### After Successful Deployment:

1. **Test thoroughly** - use TESTING_GUIDE.md
2. **Share with team** - send live URLs
3. **Monitor for 24 hours** - check for errors
4. **Set up monitoring** - UptimeRobot or similar
5. **Document admin credentials** - store securely
6. **Plan for scaling** - when to upgrade

### Future Enhancements:

1. **Custom domain** - add your own domain
2. **Email service** - SendGrid or Mailgun
3. **File storage** - Cloudinary or AWS S3
4. **Monitoring** - Sentry for error tracking
5. **Analytics** - Privacy-friendly analytics
6. **Backups** - Regular database backups

---

## 📞 Getting Help

### Render Support

- **Documentation:** https://render.com/docs
- **Community:** https://community.render.com
- **Status:** https://status.render.com

### ShieldHer Resources

- **Deployment Plan:** `DEPLOYMENT_PLAN.md`
- **Testing Guide:** `TESTING_GUIDE.md`
- **Environment Config:** `ENV_CONFIGURATION_GUIDE.md`
- **Key Generation:** `GENERATE_PRODUCTION_KEYS.md`

---

## ✅ Deployment Complete!

**Congratulations! 🎉**

Your ShieldHer platform is now live and accessible to the world!

**Your URLs:**
- Frontend: `https://shieldher-frontend.onrender.com`
- Backend: `https://shieldher-backend.onrender.com`
- Admin: `https://shieldher-backend.onrender.com/admin/`

**Remember:**
- Monitor your services regularly
- Keep admin credentials secure
- Test all features after deployment
- Plan for scaling when needed

**You've successfully deployed a privacy-first platform to help survivors of digital violence. This is important work! 💜**

---

**Deployment Date:** ___________  
**Deployed By:** ___________  
**Frontend URL:** ___________  
**Backend URL:** ___________  
**Database:** ___________

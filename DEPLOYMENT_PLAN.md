# ShieldHer Deployment Plan

## Project Overview

**ShieldHer** is a privacy-first digital literacy and safety platform for survivors of digital violence. The platform is built with:

- **Frontend:** React 18 + Vite + TailwindCSS (Static Site)
- **Backend:** Django 4.2 + DRF + JWT Auth (Web Service)
- **Database:** PostgreSQL 15+
- **Key Features:** Anonymous reporting, digital literacy lessons, emergency resources, AI chatbot, anonymous donations

**Critical Requirements:**
- Privacy-first: No PII collection, anonymous by default
- Field-level encryption for sensitive data
- Rate limiting and security hardening
- Mobile-first responsive design
- WCAG 2.1 Level AA accessibility

---

## Recommended Deployment Strategy

### Option 1: Render.com (Recommended - Free Tier)

**Why Render:**
- ✅ Free tier available for all components
- ✅ Automatic SSL certificates
- ✅ GitHub integration with auto-deploy
- ✅ PostgreSQL database included
- ✅ Simple environment variable management
- ✅ Docker support for backend
- ✅ Static site hosting for frontend
- ⚠️ Cold starts on free tier (30-60s initial load)

**Cost:** $0/month (Free tier)

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│                    Render.com                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────────┐      ┌──────────────────┐   │
│  │  Static Site     │      │  Web Service     │   │
│  │  (Frontend)      │─────▶│  (Backend)       │   │
│  │  React + Vite    │      │  Django + DRF    │   │
│  └──────────────────┘      └────────┬─────────┘   │
│                                      │              │
│                             ┌────────▼─────────┐   │
│                             │  PostgreSQL DB   │   │
│                             │  (Internal)      │   │
│                             └──────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## Deployment Steps - Render.com

### Prerequisites
- [ ] GitHub repository with latest code
- [ ] Render.com account (free)
- [ ] Generate secure keys for production

### Step 1: Prepare Repository

1. **Generate Production Keys**
   ```bash
   # Generate Django SECRET_KEY
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   
   # Generate JWT SECRET_KEY
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   
   # Generate Fernet ENCRYPTION_KEY
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
   ```

2. **Verify Dockerfile Configurations**
   - Backend Dockerfile uses gunicorn ✓
   - Frontend builds to `dist` directory ✓
   - Static files collected in backend ✓

3. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

### Step 2: Deploy PostgreSQL Database

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New** → **PostgreSQL**
3. Configure:
   - **Name:** `shieldher-db`
   - **Database:** `shieldher`
   - **User:** `shieldher_user`
   - **Region:** Oregon (US West) or closest to target users
   - **PostgreSQL Version:** 15
   - **Plan:** Free
4. Click **Create Database**
5. **Save the Internal Database URL** (format: `postgresql://user:pass@host/db`)
   - Found in database dashboard under "Connections"
   - Use **Internal Database URL** (not External)

### Step 3: Deploy Backend (Django)

1. Click **New** → **Web Service**
2. Connect your GitHub repository
3. Configure:
   - **Name:** `shieldher-backend`
   - **Region:** Same as database (Oregon)
   - **Branch:** `main`
   - **Root Directory:** Leave empty
   - **Environment:** Docker
   - **Dockerfile Path:** `backend/Dockerfile`
   - **Docker Context:** `backend`
   - **Plan:** Free
4. **Add Environment Variables:**
   ```
   DJANGO_SETTINGS_MODULE=config.settings.production
   SECRET_KEY=<your-generated-django-secret-key>
   DATABASE_URL=<internal-database-url-from-step-2>
   ALLOWED_HOSTS=.onrender.com
   DEBUG=False
   CORS_ALLOWED_ORIGINS=https://shieldher-frontend.onrender.com
   JWT_SECRET_KEY=<your-generated-jwt-secret-key>
   ENCRYPTION_KEY=<your-generated-fernet-key>
   RATE_LIMIT_ENABLED=True
   PORT=8000
   ```
5. Click **Create Web Service**
6. Wait for initial deployment (5-10 minutes)

### Step 4: Run Database Migrations

1. Once backend is deployed, go to backend service dashboard
2. Click **Shell** tab
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
   - Enter email, username, and password
   - Save credentials securely

### Step 5: Deploy Frontend (React)

1. Click **New** → **Static Site**
2. Connect your GitHub repository
3. Configure:
   - **Name:** `shieldher-frontend`
   - **Branch:** `main`
   - **Root Directory:** Leave empty
   - **Build Command:** `cd frontend && npm install && npm run build`
   - **Publish Directory:** `frontend/dist`
4. **Add Environment Variable:**
   ```
   VITE_API_URL=https://shieldher-backend.onrender.com
   ```
   - Replace with your actual backend URL from Step 3
5. Click **Create Static Site**
6. Wait for build and deployment (3-5 minutes)

### Step 6: Update CORS Settings

1. Go back to backend service
2. Navigate to **Environment** tab
3. Update `CORS_ALLOWED_ORIGINS` with actual frontend URL:
   ```
   https://shieldher-frontend.onrender.com
   ```
4. Save changes (backend will auto-redeploy)

### Step 7: Verify Deployment

Test the following endpoints:

**Backend Health Check:**
```bash
curl https://shieldher-backend.onrender.com/api/health/
```

**Frontend Access:**
- Visit: `https://shieldher-frontend.onrender.com`
- Should load homepage without errors

**API Endpoints:**
- GET `/api/lessons/` - List lessons
- GET `/api/resources/` - List resources
- POST `/api/reports/` - Submit anonymous report (test with Postman)

**Admin Panel:**
- Visit: `https://shieldher-backend.onrender.com/admin/`
- Login with superuser credentials
- Verify you can access admin dashboard

---

## Alternative Deployment Options

### Option 2: Railway.app

**Pros:**
- $5 free credit monthly
- Excellent Docker support
- Automatic HTTPS
- Simple PostgreSQL provisioning
- Better performance than Render free tier

**Cons:**
- Requires credit card for free tier
- Limited free credits

**Cost:** $0-5/month (free credits)

**Quick Deploy:**
1. Install Railway CLI: `npm i -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Add PostgreSQL: `railway add --plugin postgresql`
5. Deploy: `railway up`

### Option 3: Fly.io

**Pros:**
- Excellent Docker support
- Global edge network (low latency)
- 3 shared-cpu VMs free
- 3GB storage free
- Better cold start performance

**Cons:**
- More complex configuration
- Requires credit card

**Cost:** $0/month (within free tier limits)

### Option 4: Vercel (Frontend) + Railway (Backend)

**Pros:**
- Vercel: Best-in-class frontend hosting, unlimited bandwidth
- Railway: Better backend performance than Render
- Split deployment for optimization

**Cons:**
- Managing two platforms
- More complex setup

**Cost:** $0-5/month

---

## Post-Deployment Checklist

### Security & Configuration
- [ ] All environment variables set correctly
- [ ] SECRET_KEY, JWT_SECRET_KEY, ENCRYPTION_KEY are unique and secure
- [ ] DEBUG=False in production
- [ ] ALLOWED_HOSTS configured correctly
- [ ] CORS_ALLOWED_ORIGINS set to actual frontend URL
- [ ] SSL certificates active (automatic on Render)
- [ ] Database using internal URL (not external)

### Database & Migrations
- [ ] Database migrations completed successfully
- [ ] Admin superuser created
- [ ] Database connection working
- [ ] No migration errors in logs

### Functionality Testing
- [ ] Frontend loads without errors
- [ ] API health check responds
- [ ] Lessons page displays content
- [ ] Resources page displays content
- [ ] Anonymous report submission works
- [ ] Admin panel accessible
- [ ] Admin can login
- [ ] Rate limiting active
- [ ] CORS working (no browser console errors)

### Performance & Monitoring
- [ ] Backend responds within acceptable time
- [ ] Frontend assets load quickly
- [ ] No 500 errors in backend logs
- [ ] Static files serving correctly
- [ ] Database queries optimized

### Documentation
- [ ] Update README.md with live deployment URL
- [ ] Document environment variables
- [ ] Save admin credentials securely
- [ ] Document deployment process for team

---

## Environment Variables Reference

### Backend (Django)

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| `DJANGO_SETTINGS_MODULE` | Yes | `config.settings.production` | Django settings module |
| `SECRET_KEY` | Yes | `django-insecure-xyz...` | Django secret key (50+ chars) |
| `DATABASE_URL` | Yes | `postgresql://user:pass@host/db` | PostgreSQL connection string |
| `ALLOWED_HOSTS` | Yes | `.onrender.com` | Allowed host domains |
| `DEBUG` | Yes | `False` | Debug mode (must be False) |
| `CORS_ALLOWED_ORIGINS` | Yes | `https://frontend.onrender.com` | Frontend URL for CORS |
| `JWT_SECRET_KEY` | Yes | `jwt-secret-xyz...` | JWT signing key |
| `ENCRYPTION_KEY` | Yes | `fernet-key-xyz...` | Fernet encryption key (32 bytes) |
| `RATE_LIMIT_ENABLED` | No | `True` | Enable rate limiting |
| `PORT` | No | `8000` | Server port (Render sets automatically) |

### Frontend (React)

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| `VITE_API_URL` | Yes | `https://backend.onrender.com` | Backend API base URL |
| `VITE_API_TIMEOUT` | No | `30000` | API request timeout (ms) |
| `VITE_APP_NAME` | No | `ShieldHer` | Application name |

---

## Troubleshooting

### Backend Won't Start

**Symptoms:** Service fails to deploy, shows error logs

**Solutions:**
1. Check environment variables are set correctly
2. Verify DATABASE_URL is the internal URL
3. Check Dockerfile builds locally: `docker build -t test ./backend`
4. Review deployment logs in Render dashboard
5. Ensure all requirements are in `requirements/production.txt`

### Database Connection Errors

**Symptoms:** `OperationalError: could not connect to server`

**Solutions:**
1. Use **Internal Database URL** (not External)
2. Verify database is in same region as backend
3. Check database is running (green status in Render)
4. Ensure `ssl_require=True` in production settings
5. Test connection from backend shell: `python manage.py dbshell`

### CORS Errors in Browser

**Symptoms:** `Access-Control-Allow-Origin` errors in console

**Solutions:**
1. Update `CORS_ALLOWED_ORIGINS` with actual frontend URL
2. Include protocol: `https://` not `http://`
3. No trailing slash in URL
4. Redeploy backend after changing CORS settings
5. Clear browser cache and hard refresh

### Frontend Can't Connect to Backend

**Symptoms:** API requests fail, network errors

**Solutions:**
1. Verify `VITE_API_URL` is set correctly
2. Check backend is running (visit `/api/health/`)
3. Ensure CORS is configured correctly
4. Check browser console for specific errors
5. Verify backend URL doesn't have trailing slash

### Cold Start Issues (Free Tier)

**Symptoms:** First request takes 30-60 seconds

**Solutions:**
1. This is expected on Render free tier
2. Service spins down after 15 minutes of inactivity
3. Consider upgrading to paid tier ($7/month) for always-on
4. Use a uptime monitor to ping service every 10 minutes
5. Add loading message to frontend for initial load

### Static Files Not Loading

**Symptoms:** CSS/JS missing, 404 errors

**Solutions:**
1. Verify `collectstatic` runs in Dockerfile
2. Check `STATIC_ROOT` is set correctly
3. Ensure WhiteNoise is in MIDDLEWARE
4. Check `STATICFILES_STORAGE` setting
5. Rebuild and redeploy backend

---

## Monitoring & Maintenance

### Health Checks

Set up monitoring for:
- Backend health endpoint: `/api/health/`
- Frontend availability
- Database connection
- API response times

**Recommended Tools:**
- UptimeRobot (free, 50 monitors)
- Better Uptime (free tier available)
- Render built-in health checks

### Logging

**Backend Logs:**
- Access via Render dashboard → Logs tab
- Monitor for errors, warnings
- Check rate limiting activity
- Review admin actions

**Frontend Logs:**
- Check browser console for errors
- Monitor API request failures
- Review user-reported issues

### Backups

**Database Backups:**
- Render free tier: No automatic backups
- Manual backup: Use `pg_dump` from Shell
- Consider upgrading to paid tier for automatic backups
- Export data regularly via admin panel

### Updates & Maintenance

**Regular Tasks:**
- [ ] Update dependencies monthly (security patches)
- [ ] Review logs weekly for errors
- [ ] Test all critical features after updates
- [ ] Monitor database size (free tier: 1GB limit)
- [ ] Rotate secrets every 90 days
- [ ] Review and update content (lessons, resources)

---

## Scaling Considerations

### When to Upgrade

**Indicators:**
- Consistent traffic (no cold starts needed)
- Database approaching 1GB limit
- Need for automatic backups
- Response times too slow
- Need for custom domain

### Upgrade Path (Render)

**Starter Plan ($7/month per service):**
- Always-on (no cold starts)
- 512MB RAM
- Better performance
- Custom domains

**Standard Plan ($25/month per service):**
- 2GB RAM
- Horizontal scaling
- Better for production traffic

**Database Upgrade ($7/month):**
- 1GB → 10GB storage
- Automatic daily backups
- Point-in-time recovery

### Performance Optimization

**Backend:**
- Enable database connection pooling
- Add Redis for caching (future)
- Optimize database queries
- Use CDN for static files (future)

**Frontend:**
- Enable Vite build optimizations
- Lazy load components
- Optimize images
- Use CDN for assets

---

## Security Hardening

### Pre-Deployment Security Checklist

- [ ] All secrets are unique and randomly generated
- [ ] No secrets committed to Git
- [ ] DEBUG=False in production
- [ ] SSL/HTTPS enforced
- [ ] HSTS headers enabled
- [ ] Rate limiting active
- [ ] CORS properly configured
- [ ] Admin panel uses strong password
- [ ] Database uses internal URL only
- [ ] No PII in logs

### Ongoing Security

- [ ] Monitor for suspicious activity
- [ ] Review admin access logs
- [ ] Update dependencies for security patches
- [ ] Rotate secrets quarterly
- [ ] Review rate limiting effectiveness
- [ ] Test anonymous reporting privacy
- [ ] Audit encryption implementation

---

## Cost Breakdown

### Free Tier (Render.com)

| Service | Cost | Limits |
|---------|------|--------|
| PostgreSQL | $0 | 1GB storage, expires after 90 days |
| Backend Web Service | $0 | 512MB RAM, spins down after 15min |
| Frontend Static Site | $0 | 100GB bandwidth/month |
| **Total** | **$0/month** | Suitable for demo/MVP |

### Paid Tier (Recommended for Production)

| Service | Cost | Benefits |
|---------|------|----------|
| PostgreSQL Starter | $7/month | 10GB storage, daily backups |
| Backend Starter | $7/month | Always-on, 512MB RAM |
| Frontend Static | $0 | Same as free |
| **Total** | **$14/month** | Production-ready |

### Alternative: Railway.app

| Service | Cost | Benefits |
|---------|------|----------|
| All Services | $5 credit/month | Better performance, $0.000463/GB-hour |
| Estimated Usage | ~$3-5/month | Depends on traffic |

---

## Next Steps

1. **Choose deployment platform** (Recommended: Render.com)
2. **Generate production secrets** (Step 1)
3. **Deploy database** (Step 2)
4. **Deploy backend** (Step 3)
5. **Run migrations** (Step 4)
6. **Deploy frontend** (Step 5)
7. **Update CORS** (Step 6)
8. **Test thoroughly** (Step 7)
9. **Update README** with live URLs
10. **Set up monitoring** (UptimeRobot)

---

## Support & Resources

- **Render Documentation:** https://render.com/docs
- **Django Deployment:** https://docs.djangoproject.com/en/4.2/howto/deployment/
- **Vite Production Build:** https://vitejs.dev/guide/build.html
- **PostgreSQL on Render:** https://render.com/docs/databases

---

**Deployment Prepared By:** Kiro AI Assistant  
**Date:** November 29, 2025  
**Project:** ShieldHer Platform  
**Version:** 1.0

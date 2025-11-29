# 🔧 Render Deployment Troubleshooting Guide

Quick solutions to common deployment issues.

---

## 🚨 Backend Issues

### ❌ Build Failed

**Symptoms:**
- Build logs show errors
- Service stuck in "Build failed" state

**Common Causes & Fixes:**

1. **Dockerfile not found**
   ```
   Error: Dockerfile not found at backend/Dockerfile
   ```
   **Fix:** Verify Dockerfile Path is `backend/Dockerfile` and Docker Context is `backend`

2. **Requirements installation failed**
   ```
   Error: Could not find a version that satisfies the requirement...
   ```
   **Fix:** Check `requirements/production.txt` for typos or incompatible versions

3. **Python version mismatch**
   ```
   Error: Python 3.12 not found
   ```
   **Fix:** Update Dockerfile to use available Python version

**How to check:**
1. Go to backend service
2. Click "Logs" tab
3. Look for red error messages
4. Fix the issue in your code
5. Push to GitHub (auto-redeploys)

---

### ❌ Database Connection Failed

**Symptoms:**
- Backend builds but crashes on start
- Logs show: `OperationalError: could not connect to server`

**Fix:**

1. **Verify you're using INTERNAL Database URL:**
   ```
   ✅ postgresql://user:pass@dpg-xxxxx-a/db
   ❌ postgresql://user:pass@dpg-xxxxx-a.oregon-postgres.render.com/db
   ```

2. **Check region match:**
   - Database region: Oregon
   - Backend region: Oregon ← Must match!

3. **Update DATABASE_URL:**
   - Go to backend → Environment
   - Find DATABASE_URL
   - Replace with Internal URL from database page
   - Save (will redeploy)

---

### ❌ Migrations Not Applied

**Symptoms:**
- Backend runs but API returns errors
- Logs show: `ProgrammingError: relation "table_name" does not exist`

**Fix:**

1. Go to backend service
2. Click "Shell" tab
3. Run:
   ```bash
   python manage.py migrate
   ```

4. If that fails:
   ```bash
   python manage.py migrate --run-syncdb
   ```

---

### ❌ Static Files Not Loading

**Symptoms:**
- Admin panel has no CSS
- API works but admin looks broken

**Fix:**

Already handled in Dockerfile, but if issue persists:

1. Check Dockerfile includes:
   ```dockerfile
   RUN python manage.py collectstatic --noinput --settings=config.settings.production
   ```

2. Verify WhiteNoise in settings:
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be here
       ...
   ]
   ```

3. Trigger manual deploy:
   - Go to backend service
   - Click "Manual Deploy" → "Deploy latest commit"

---

### ❌ Environment Variables Not Working

**Symptoms:**
- Backend uses fallback values
- DEBUG=True in production
- Wrong SECRET_KEY

**Fix:**

1. Go to backend → Environment tab
2. Verify ALL variables are set:
   - DJANGO_SETTINGS_MODULE
   - SECRET_KEY
   - DATABASE_URL
   - DEBUG
   - etc.

3. Check for typos in variable names

4. Save changes (will redeploy)

---

## 🚨 Frontend Issues

### ❌ Build Failed

**Symptoms:**
- Build logs show errors
- Site stuck in "Build failed" state

**Common Causes & Fixes:**

1. **Build command incorrect**
   ```
   Error: npm: command not found
   ```
   **Fix:** Build Command should be: `cd frontend && npm install && npm run build`

2. **Publish directory wrong**
   ```
   Error: No files found in publish directory
   ```
   **Fix:** Publish Directory should be: `frontend/dist`

3. **Node version mismatch**
   ```
   Error: Node version not supported
   ```
   **Fix:** Add `.node-version` file with `18` or update package.json

---

### ❌ Blank Page / White Screen

**Symptoms:**
- Frontend builds successfully
- Page loads but shows nothing
- Console shows errors

**Fix:**

1. **Check browser console (F12):**
   - Look for red errors
   - Common: "Failed to fetch" or CORS errors

2. **Verify VITE_API_URL:**
   - Go to frontend → Environment
   - Should be: `https://shieldher-backend.onrender.com`
   - No trailing slash!
   - Must include `https://`

3. **Check build logs:**
   - Look for warnings about missing files
   - Verify all imports are correct

4. **Hard refresh:**
   - Ctrl+Shift+R (Windows)
   - Cmd+Shift+R (Mac)

---

### ❌ API Calls Failing

**Symptoms:**
- Frontend loads but no data
- Console shows: "Failed to fetch"
- Network tab shows failed requests

**Fix:**

1. **Check VITE_API_URL:**
   ```
   ✅ https://shieldher-backend.onrender.com
   ❌ http://shieldher-backend.onrender.com (no https)
   ❌ https://shieldher-backend.onrender.com/ (trailing slash)
   ```

2. **Verify backend is running:**
   - Visit: `https://your-backend.onrender.com/api/health/`
   - Should return: `{"status":"healthy"}`

3. **Check CORS (see below)**

---

## 🚨 CORS Issues

### ❌ CORS Error in Console

**Symptoms:**
```
Access to fetch at 'https://backend.onrender.com/api/lessons/' 
from origin 'https://frontend.onrender.com' has been blocked by CORS policy
```

**Fix:**

1. **Update CORS_ALLOWED_ORIGINS in backend:**
   - Go to backend → Environment
   - Find CORS_ALLOWED_ORIGINS
   - Value should be: `https://shieldher-frontend.onrender.com`
   - Must include `https://`
   - No trailing slash
   - Save (will redeploy)

2. **Wait for backend to redeploy** (2-3 minutes)

3. **Clear browser cache:**
   - Ctrl+Shift+Delete
   - Clear cached images and files
   - Or use incognito mode

4. **Hard refresh frontend:**
   - Ctrl+Shift+R

**Common CORS mistakes:**

```
❌ http://frontend.onrender.com (missing https)
❌ https://frontend.onrender.com/ (trailing slash)
❌ frontend.onrender.com (missing protocol)
✅ https://frontend.onrender.com (correct!)
```

---

## 🚨 Database Issues

### ❌ Database Not Available

**Symptoms:**
- Database status shows "Creating" for too long
- Database shows "Unavailable"

**Fix:**

1. **Wait:** Initial creation takes 1-2 minutes

2. **Check Render status:**
   - Visit: https://status.render.com
   - Look for PostgreSQL outages

3. **Try different region:**
   - Delete database
   - Create new one in different region

---

### ❌ Database Full (Free Tier)

**Symptoms:**
- Error: "Disk quota exceeded"
- Database at 1GB limit

**Fix:**

1. **Clean up old data:**
   ```bash
   # In backend Shell
   python manage.py shell
   
   # Delete old reports
   from apps.reports.models import Report
   Report.objects.filter(created_at__lt='2024-01-01').delete()
   ```

2. **Upgrade to paid tier:**
   - $7/month for 10GB
   - Includes daily backups

---

## 🚨 Performance Issues

### ❌ Slow Response Times

**Symptoms:**
- Pages take 5+ seconds to load
- API calls timeout

**Causes & Fixes:**

1. **Cold start (Free tier):**
   - Service spins down after 15 minutes
   - First request takes 30-60 seconds
   - **Fix:** Upgrade to paid tier ($7/month) or accept it

2. **Database queries slow:**
   - Too many queries
   - Missing indexes
   - **Fix:** Optimize queries, add indexes

3. **Large response payloads:**
   - Returning too much data
   - **Fix:** Add pagination, limit fields

---

### ❌ Service Keeps Crashing

**Symptoms:**
- Service shows "Live" then "Deploying" repeatedly
- Logs show crashes

**Fix:**

1. **Check logs for errors:**
   - Memory errors → Upgrade plan
   - Import errors → Fix dependencies
   - Database errors → Check connection

2. **Verify health check:**
   - Render pings `/` by default
   - Ensure root URL responds with 200

3. **Check resource usage:**
   - Go to service → Metrics
   - If CPU/Memory maxed → Upgrade plan

---

## 🚨 SSL/HTTPS Issues

### ❌ SSL Certificate Error

**Symptoms:**
- Browser shows "Not Secure"
- SSL certificate warnings

**Fix:**

1. **Wait:** SSL certificates take 5-10 minutes after first deploy

2. **Check custom domain:**
   - If using custom domain, verify DNS settings
   - CNAME should point to Render

3. **Force HTTPS:**
   - Already configured in production settings
   - Verify `SECURE_SSL_REDIRECT = True`

---

## 🚨 Authentication Issues

### ❌ Can't Login to Admin

**Symptoms:**
- Admin login fails
- "Invalid credentials" error

**Fix:**

1. **Verify superuser exists:**
   ```bash
   # In backend Shell
   python manage.py createsuperuser
   ```

2. **Check credentials:**
   - Email (not username) for login
   - Password is case-sensitive

3. **Reset password:**
   ```bash
   # In backend Shell
   python manage.py changepassword admin@shieldher.com
   ```

---

### ❌ JWT Token Errors

**Symptoms:**
- API returns 401 Unauthorized
- Token validation fails

**Fix:**

1. **Verify JWT_SECRET_KEY is set:**
   - Go to backend → Environment
   - Check JWT_SECRET_KEY exists
   - Should be different from SECRET_KEY

2. **Check token expiration:**
   - Default: 60 minutes
   - May need to login again

---

## 🚨 Deployment Issues

### ❌ Auto-Deploy Not Working

**Symptoms:**
- Push to GitHub but Render doesn't deploy
- Service shows old version

**Fix:**

1. **Check auto-deploy is enabled:**
   - Go to service → Settings
   - "Auto-Deploy" should be "Yes"

2. **Verify branch:**
   - Service watches `main` branch
   - If you pushed to different branch, it won't deploy

3. **Manual deploy:**
   - Go to service
   - Click "Manual Deploy" → "Deploy latest commit"

---

### ❌ Deploy Stuck

**Symptoms:**
- Deploy shows "In progress" for 30+ minutes
- No progress in logs

**Fix:**

1. **Cancel and retry:**
   - Click "Cancel Deploy"
   - Click "Manual Deploy" → "Deploy latest commit"

2. **Check Render status:**
   - Visit: https://status.render.com

3. **Contact support:**
   - If issue persists, contact Render support

---

## 🆘 Emergency Fixes

### 🔥 Site is Down - Quick Recovery

1. **Check Render status:** https://status.render.com

2. **Check service status:**
   - All services should show "Live"
   - If not, check logs for errors

3. **Restart services:**
   - Go to service → Settings
   - Click "Suspend" then "Resume"

4. **Rollback to previous version:**
   - Go to service → Events
   - Find last successful deploy
   - Click "Rollback to this version"

---

### 🔥 Database Corrupted

1. **Don't panic!**

2. **Check database status:**
   - Should show "Available"

3. **Restore from backup:**
   - Free tier: No automatic backups
   - Paid tier: Restore from daily backup

4. **Rebuild database:**
   ```bash
   # In backend Shell
   python manage.py migrate
   python load_sample_data.py
   ```

---

## 📞 Getting Help

### Render Support

- **Docs:** https://render.com/docs
- **Community:** https://community.render.com
- **Status:** https://status.render.com
- **Support:** support@render.com (paid plans)

### Check These First

1. **Logs** - Always check logs first
2. **Status page** - Check for outages
3. **Documentation** - Search Render docs
4. **Community** - Search community forum

### Provide This Info When Asking for Help

- Service name
- Error message (exact text)
- Logs (copy relevant parts)
- What you've tried
- When it started happening

---

## 🔍 Debugging Checklist

When something goes wrong:

- [ ] Check service status (should be "Live")
- [ ] Check logs for errors
- [ ] Check environment variables
- [ ] Check Render status page
- [ ] Try manual deploy
- [ ] Clear browser cache
- [ ] Test in incognito mode
- [ ] Check CORS settings
- [ ] Verify database connection
- [ ] Check build logs
- [ ] Test API endpoints directly
- [ ] Check browser console
- [ ] Verify all URLs use HTTPS

---

## 💡 Pro Tips

1. **Always check logs first** - 90% of issues are in the logs

2. **Use incognito mode** - Eliminates caching issues

3. **Test API directly** - Use curl or Postman to isolate frontend issues

4. **Monitor after deploy** - Watch for 10-15 minutes after deployment

5. **Keep backups** - Export data regularly (especially on free tier)

6. **Document changes** - Note what you changed before issues started

7. **Test locally first** - Catch issues before deploying

---

**Remember:** Most issues are configuration errors, not code bugs. Double-check environment variables and URLs!

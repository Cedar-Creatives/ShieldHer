# ✅ Render Deployment Checklist

Print this page and check off each step as you complete it!

---

## 📦 Pre-Deployment

- [ ] Code pushed to GitHub
- [ ] `.env` in `.gitignore` (not committed)
- [ ] Render account created
- [ ] Production keys generated and saved

---

## 🗄️ Database Setup

- [ ] PostgreSQL database created
- [ ] Name: `shieldher-db`
- [ ] Region selected (Oregon recommended)
- [ ] Plan: Free
- [ ] Status: "Available"
- [ ] Internal Database URL copied

---

## 🐍 Backend Deployment

### Service Creation
- [ ] Web Service created
- [ ] Name: `shieldher-backend`
- [ ] Repository connected
- [ ] Runtime: Docker
- [ ] Dockerfile Path: `backend/Dockerfile`
- [ ] Docker Context: `backend`
- [ ] Region: Same as database
- [ ] Plan: Free

### Environment Variables
- [ ] `DJANGO_SETTINGS_MODULE` = `config.settings.production`
- [ ] `SECRET_KEY` = `<generated-key>`
- [ ] `JWT_SECRET_KEY` = `<generated-key>`
- [ ] `ENCRYPTION_KEY` = `<generated-key>`
- [ ] `DATABASE_URL` = `<internal-db-url>`
- [ ] `ALLOWED_HOSTS` = `.onrender.com`
- [ ] `DEBUG` = `False`
- [ ] `CORS_ALLOWED_ORIGINS` = `https://shieldher-frontend.onrender.com`
- [ ] `PORT` = `8000`
- [ ] `RATE_LIMIT_ENABLED` = `True`

### Deployment
- [ ] Service created
- [ ] Build completed successfully
- [ ] Status: "Live"
- [ ] Migrations run: `python manage.py migrate`
- [ ] Superuser created: `python manage.py createsuperuser`
- [ ] Sample data loaded (optional)

### Verification
- [ ] Health check works: `/api/health/`
- [ ] Admin panel accessible: `/admin/`
- [ ] Admin login works
- [ ] API endpoints respond

---

## ⚛️ Frontend Deployment

### Service Creation
- [ ] Static Site created
- [ ] Name: `shieldher-frontend`
- [ ] Repository connected
- [ ] Build Command: `cd frontend && npm install && npm run build`
- [ ] Publish Directory: `frontend/dist`

### Environment Variables
- [ ] `VITE_API_URL` = `https://shieldher-backend.onrender.com`

### Deployment
- [ ] Site created
- [ ] Build completed successfully
- [ ] Status: "Live"

### Verification
- [ ] Homepage loads
- [ ] Navigation works
- [ ] Quick Exit button visible
- [ ] No console errors

---

## 🔗 Integration

- [ ] CORS updated with actual frontend URL
- [ ] Backend redeployed
- [ ] Lessons page loads data
- [ ] Resources page loads data
- [ ] Report form works
- [ ] No CORS errors in console

---

## 🎯 Final Testing

- [ ] All pages load without errors
- [ ] API calls work
- [ ] Forms submit successfully
- [ ] Admin panel fully functional
- [ ] Mobile responsive
- [ ] Quick Exit button works
- [ ] History hiding works
- [ ] Anonymous reporting works

---

## 📝 Documentation

- [ ] README updated with live URLs
- [ ] Admin credentials saved securely
- [ ] Production keys saved in password manager
- [ ] Deployment date documented
- [ ] Team notified of live URLs

---

## 🔒 Security

- [ ] `DEBUG=False` verified
- [ ] Production keys unique (not dev keys)
- [ ] `.env` not in Git
- [ ] Database uses internal URL
- [ ] CORS properly configured
- [ ] Admin password is strong
- [ ] HTTPS active (automatic)
- [ ] Rate limiting enabled

---

## 📊 Monitoring

- [ ] Deploy notifications enabled
- [ ] Email alerts configured
- [ ] Uptime monitor set up (optional)
- [ ] Bookmark Render dashboard
- [ ] Test cold start behavior

---

## 🎉 Completion

- [ ] All services "Live"
- [ ] All tests passing
- [ ] URLs shared with team
- [ ] Deployment documented
- [ ] Celebration! 🎊

---

**Deployment Date:** _______________

**Deployed By:** _______________

**Frontend URL:** _______________

**Backend URL:** _______________

**Admin Email:** _______________

**Notes:**
_________________________________
_________________________________
_________________________________
_________________________________

---

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Complete

**For detailed instructions, see:** `RENDER_DEPLOYMENT_STEP_BY_STEP.md`

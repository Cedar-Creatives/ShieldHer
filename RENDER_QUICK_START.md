# ⚡ Render Deployment - Quick Start

**Time:** 30 minutes | **Cost:** $0 | **Difficulty:** Easy

---

## 🎯 What You'll Do

1. Generate production keys (2 min)
2. Deploy database (3 min)
3. Deploy backend (10 min)
4. Deploy frontend (5 min)
5. Connect & test (10 min)

---

## 📋 Before You Start

- [ ] Code on GitHub
- [ ] Render account created
- [ ] 30 minutes available

---

## 🚀 Step 1: Generate Keys (2 min)

```bash
cd backend
.\venv\Scripts\activate
python generate_production_keys.py
```

**Save the output!** Copy to a text file.

---

## 🗄️ Step 2: Deploy Database (3 min)

1. Go to https://dashboard.render.com
2. Click "New +" → "PostgreSQL"
3. Fill in:
   - Name: `shieldher-db`
   - Database: `shieldher`
   - User: `shieldher_user`
   - Region: Oregon
   - Plan: Free
4. Click "Create Database"
5. **Copy Internal Database URL**

---

## 🐍 Step 3: Deploy Backend (10 min)

1. Click "New +" → "Web Service"
2. Connect GitHub repo
3. Fill in:
   - Name: `shieldher-backend`
   - Runtime: Docker
   - Dockerfile Path: `backend/Dockerfile`
   - Docker Context: `backend`
   - Region: Oregon (same as database!)
   - Plan: Free

4. **Add Environment Variables:**

| Key | Value |
|-----|-------|
| DJANGO_SETTINGS_MODULE | config.settings.production |
| SECRET_KEY | [from Step 1] |
| JWT_SECRET_KEY | [from Step 1] |
| ENCRYPTION_KEY | [from Step 1] |
| DATABASE_URL | [from Step 2] |
| ALLOWED_HOSTS | .onrender.com |
| DEBUG | False |
| CORS_ALLOWED_ORIGINS | https://shieldher-frontend.onrender.com |
| PORT | 8000 |

5. Click "Create Web Service"
6. Wait for deploy (5-10 min)

7. **Run migrations:**
   - Click "Shell" tab
   - Run: `python manage.py migrate`
   - Run: `python manage.py createsuperuser`

8. **Test:** Visit `https://your-backend.onrender.com/api/health/`

---

## ⚛️ Step 4: Deploy Frontend (5 min)

1. Click "New +" → "Static Site"
2. Connect GitHub repo
3. Fill in:
   - Name: `shieldher-frontend`
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/dist`

4. **Add Environment Variable:**

| Key | Value |
|-----|-------|
| VITE_API_URL | https://shieldher-backend.onrender.com |

5. Click "Create Static Site"
6. Wait for build (3-5 min)

7. **Test:** Visit `https://your-frontend.onrender.com`

---

## 🔗 Step 5: Connect & Test (10 min)

1. **Update CORS:**
   - Go to backend → Environment
   - Update CORS_ALLOWED_ORIGINS with actual frontend URL
   - Save (will redeploy)

2. **Test Everything:**
   - [ ] Homepage loads
   - [ ] Lessons page works
   - [ ] Resources page works
   - [ ] Report form works
   - [ ] Admin panel works
   - [ ] No CORS errors

---

## ✅ Done!

**Your URLs:**
- Frontend: `https://shieldher-frontend.onrender.com`
- Backend: `https://shieldher-backend.onrender.com`
- Admin: `https://shieldher-backend.onrender.com/admin/`

---

## 🆘 Issues?

See `RENDER_TROUBLESHOOTING.md` for solutions.

**Common fixes:**
- CORS errors → Update CORS_ALLOWED_ORIGINS
- Database errors → Use Internal URL
- Build errors → Check logs

---

## 📚 Full Guides

- **Detailed Steps:** `RENDER_DEPLOYMENT_STEP_BY_STEP.md`
- **Checklist:** `RENDER_DEPLOYMENT_CHECKLIST.md`
- **Troubleshooting:** `RENDER_TROUBLESHOOTING.md`
- **Key Generation:** `GENERATE_PRODUCTION_KEYS.md`

---

**Ready? Let's deploy! 🚀**

# 🔐 How to Generate Production Keys

## Why Generate New Keys?

**NEVER reuse development keys in production!**

- ✅ Development keys are for local testing only
- ✅ Production keys must be unique and secret
- ✅ If dev keys leak, production is still secure
- ✅ Best practice for security

## 🚀 Method 1: Use the Key Generator Script (Easiest)

### Step 1: Run the Generator

```bash
cd backend
.\venv\Scripts\activate
python generate_production_keys.py
```

### Step 2: Copy the Output

The script will display something like:

```
======================================================================
🔐 ShieldHer Production Keys Generator
======================================================================

📋 Copy these values to your deployment platform:

----------------------------------------------------------------------
DJANGO_SECRET_KEY
----------------------------------------------------------------------
django-insecure-a8f3h2k9j4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z9a0b1c2d3e4f5

----------------------------------------------------------------------
JWT_SECRET_KEY
----------------------------------------------------------------------
xYz123AbC456DeF789GhI012JkL345MnO678PqR901StU234VwX567YzA890BcD123

----------------------------------------------------------------------
ENCRYPTION_KEY
----------------------------------------------------------------------
AbCdEfGhIjKlMnOpQrStUvWxYz0123456789+/=

======================================================================
```

### Step 3: Save Securely

- Copy each key to a secure password manager (1Password, LastPass, etc.)
- Or save to a secure note (encrypted)
- **DO NOT** save in a text file on your desktop
- **DO NOT** email or Slack these keys

### Step 4: Add to Render Dashboard

1. Go to https://dashboard.render.com
2. Select your backend service
3. Click "Environment" tab
4. Click "Add Environment Variable"
5. Add each key:
   - Key: `DJANGO_SECRET_KEY`, Value: `<paste from script>`
   - Key: `JWT_SECRET_KEY`, Value: `<paste from script>`
   - Key: `ENCRYPTION_KEY`, Value: `<paste from script>`
6. Click "Save Changes"

---

## 🔧 Method 2: Generate Keys Manually (One at a Time)

If you prefer to generate keys individually:

### Django Secret Key

```bash
cd backend
.\venv\Scripts\activate
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Output example:**
```
django-insecure-a8f3h2k9j4l5m6n7o8p9q0r1s2t3u4v5w6x7y8z9a0b1c2d3e4f5
```

### JWT Secret Key

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**Output example:**
```
xYz123AbC456DeF789GhI012JkL345MnO678PqR901StU234VwX567YzA890BcD123
```

### Encryption Key (Fernet)

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

**Output example:**
```
AbCdEfGhIjKlMnOpQrStUvWxYz0123456789+/=
```

---

## 🔧 Method 3: Generate All Keys at Once (PowerShell)

Copy and paste this entire block into PowerShell:

```powershell
cd backend
.\venv\Scripts\activate

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "🔐 Production Keys for ShieldHer" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "DJANGO_SECRET_KEY:" -ForegroundColor Yellow
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
Write-Host ""

Write-Host "JWT_SECRET_KEY:" -ForegroundColor Yellow
python -c "import secrets; print(secrets.token_urlsafe(50))"
Write-Host ""

Write-Host "ENCRYPTION_KEY:" -ForegroundColor Yellow
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
Write-Host ""

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "✅ Copy these values to Render dashboard" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
```

---

## 📋 Complete Production Environment Variables

When deploying to Render, set these environment variables:

### Required Variables

| Variable | Value | How to Get |
|----------|-------|------------|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` | Fixed value |
| `SECRET_KEY` | `<generated-key>` | Run generator script |
| `JWT_SECRET_KEY` | `<generated-key>` | Run generator script |
| `ENCRYPTION_KEY` | `<generated-key>` | Run generator script |
| `DATABASE_URL` | `<postgres-url>` | Provided by Render |
| `ALLOWED_HOSTS` | `.onrender.com` | Fixed value |
| `DEBUG` | `False` | Fixed value |
| `CORS_ALLOWED_ORIGINS` | `https://your-frontend.onrender.com` | Your frontend URL |

### Optional Variables

| Variable | Value | Purpose |
|----------|-------|---------|
| `PORT` | `8000` | Server port (Render sets automatically) |
| `RATE_LIMIT_ENABLED` | `True` | Enable rate limiting |
| `JWT_ACCESS_TOKEN_LIFETIME_MINUTES` | `15` | Token lifetime (shorter for production) |
| `JWT_REFRESH_TOKEN_LIFETIME_HOURS` | `168` | Refresh token lifetime (7 days) |

---

## 🎯 Step-by-Step: Render Deployment with New Keys

### Step 1: Generate Production Keys

```bash
cd backend
.\venv\Scripts\activate
python generate_production_keys.py
```

**Save the output securely!**

### Step 2: Create PostgreSQL Database on Render

1. Go to https://dashboard.render.com
2. Click "New" → "PostgreSQL"
3. Configure:
   - Name: `shieldher-db`
   - Database: `shieldher`
   - User: `shieldher_user`
   - Region: Oregon (US West)
   - Plan: Free
4. Click "Create Database"
5. **Copy the Internal Database URL** (starts with `postgresql://`)

### Step 3: Deploy Backend Service

1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - Name: `shieldher-backend`
   - Environment: Docker
   - Dockerfile Path: `backend/Dockerfile`
   - Plan: Free
4. **Add Environment Variables** (click "Add Environment Variable"):

```
DJANGO_SETTINGS_MODULE = config.settings.production
SECRET_KEY = <paste-generated-django-key>
JWT_SECRET_KEY = <paste-generated-jwt-key>
ENCRYPTION_KEY = <paste-generated-encryption-key>
DATABASE_URL = <paste-internal-database-url-from-step-2>
ALLOWED_HOSTS = .onrender.com
DEBUG = False
CORS_ALLOWED_ORIGINS = https://shieldher-frontend.onrender.com
RATE_LIMIT_ENABLED = True
PORT = 8000
```

5. Click "Create Web Service"

### Step 4: Deploy Frontend

1. Click "New" → "Static Site"
2. Connect your GitHub repository
3. Configure:
   - Name: `shieldher-frontend`
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/dist`
4. **Add Environment Variable**:

```
VITE_API_URL = https://shieldher-backend.onrender.com
```

5. Click "Create Static Site"

### Step 5: Update CORS

1. Go back to backend service
2. Update `CORS_ALLOWED_ORIGINS` with actual frontend URL
3. Save changes (backend will redeploy)

### Step 6: Run Migrations

1. Go to backend service dashboard
2. Click "Shell" tab
3. Run:
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 🔒 Security Best Practices

### ✅ DO:

1. **Generate unique keys** for each environment
   - Development keys ≠ Production keys
   - Staging keys ≠ Production keys

2. **Store keys securely**
   - Use password manager (1Password, LastPass, Bitwarden)
   - Use platform's secret management (Render dashboard)
   - Encrypt if storing in files

3. **Rotate keys regularly**
   - Every 90 days for high-security apps
   - Immediately if compromised
   - After team member leaves

4. **Limit access**
   - Only admins should see production keys
   - Use role-based access control
   - Audit who has access

5. **Use different keys per service**
   - DJANGO_SECRET_KEY ≠ JWT_SECRET_KEY
   - Each should be unique

### ❌ DON'T:

1. ❌ **Reuse development keys in production**
2. ❌ **Commit keys to Git** (even private repos)
3. ❌ **Share keys via email/Slack**
4. ❌ **Store keys in plain text files**
5. ❌ **Use simple/predictable keys**
6. ❌ **Share keys across multiple projects**
7. ❌ **Store keys in frontend code**

---

## 🆘 Troubleshooting

### "Invalid key format" error

**Cause:** Key is not properly formatted  
**Fix:** Regenerate using the script

### "Encryption key must be 32 bytes" error

**Cause:** ENCRYPTION_KEY is not a valid Fernet key  
**Fix:** Use the Fernet generator:
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

### "SECRET_KEY not set" error

**Cause:** Environment variable not set in Render  
**Fix:** Add SECRET_KEY in Render dashboard → Environment tab

### Can't decrypt existing data after key change

**Cause:** Changed ENCRYPTION_KEY after data was encrypted  
**Fix:** 
- **Prevention:** Never change ENCRYPTION_KEY in production
- **Recovery:** Restore old key or data will be lost
- **Best practice:** Backup before changing encryption keys

---

## 📝 Key Generation Checklist

Before deploying to production:

- [ ] Run `python generate_production_keys.py`
- [ ] Save keys in password manager
- [ ] Add DJANGO_SECRET_KEY to Render
- [ ] Add JWT_SECRET_KEY to Render
- [ ] Add ENCRYPTION_KEY to Render
- [ ] Set DEBUG=False
- [ ] Set DJANGO_SETTINGS_MODULE=config.settings.production
- [ ] Configure DATABASE_URL (from Render PostgreSQL)
- [ ] Configure ALLOWED_HOSTS
- [ ] Configure CORS_ALLOWED_ORIGINS
- [ ] Test deployment with new keys
- [ ] Delete keys from local clipboard/history
- [ ] Document where keys are stored (password manager)

---

## 🎓 Understanding Key Types

### DJANGO_SECRET_KEY
- **Purpose:** Signs sessions, cookies, CSRF tokens
- **Format:** 50+ random characters
- **Security:** Critical - if leaked, sessions can be hijacked
- **Rotation:** Every 90 days or if compromised

### JWT_SECRET_KEY
- **Purpose:** Signs JWT authentication tokens for admins
- **Format:** 50+ random characters (URL-safe base64)
- **Security:** Critical - if leaked, admin tokens can be forged
- **Rotation:** Every 90 days or if compromised

### ENCRYPTION_KEY
- **Purpose:** Encrypts sensitive report data at rest
- **Format:** 32-byte Fernet key (base64 encoded)
- **Security:** Critical - if leaked, encrypted data can be read
- **Rotation:** NEVER (data will be unreadable) - only if compromised

---

## 📞 Need Help?

If you have issues generating keys:

1. Check Python is activated: `.\venv\Scripts\activate`
2. Check dependencies installed: `pip list | Select-String "Django"`
3. Try manual generation (Method 2)
4. Check the `ENV_CONFIGURATION_GUIDE.md` for more details

---

**Remember:** Production keys are like passwords - keep them secret, keep them safe! 🔐

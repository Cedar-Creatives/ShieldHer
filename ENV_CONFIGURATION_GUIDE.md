# Environment Variables Configuration Guide

## 🔐 Why Environment Variables Matter

Environment variables store **sensitive configuration** that should:
- ✅ Never be committed to Git
- ✅ Be different for development vs production
- ✅ Contain secrets (API keys, passwords, encryption keys)
- ✅ Be unique per environment

## ⚠️ What Was Wrong Before

Your `.env` file had **placeholder values** that were insecure:

```env
DJANGO_SECRET_KEY=your-secret-key-here-change-in-production  ❌ INSECURE
JWT_SECRET_KEY=your-jwt-secret-key-here-change-in-production  ❌ INSECURE
ENCRYPTION_KEY=your-32-byte-fernet-key-here-change-in-production  ❌ INSECURE
```

**Why it still worked:**
Django's settings have **fallback values** when env vars aren't set:

```python
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-this-in-production')
#                                                  ↑ This fallback was being used
```

This is **OK for local testing** but **DANGEROUS for production**.

## ✅ What I Fixed

I generated **proper secure keys** for your development environment:

```env
DJANGO_SECRET_KEY=0s0+*jokg4k2**+t0+zb*t^44!+cyk)qs-exp3_cfp+n_x%^sd
JWT_SECRET_KEY=3TO7lb-YTpsiHbtOcxzUs0OoC5EUGaOyqUTyZmKcV1wAO8onNjy1KBPX-HZDlwlDD-k
ENCRYPTION_KEY=MXRZl0om8IGYdZJ2PpcZnSqj7vE9IwUanGPW5zaiCIg=
```

## 📋 Complete Environment Variables Explained

### Backend (`backend/.env`)

#### 1. Django Settings

```env
DJANGO_SECRET_KEY=0s0+*jokg4k2**+t0+zb*t^44!+cyk)qs-exp3_cfp+n_x%^sd
```
**Purpose:** Used for cryptographic signing (sessions, cookies, CSRF tokens)  
**Generate:** `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`  
**Security:** Must be unique and secret. Never share or commit to Git.

```env
DJANGO_DEBUG=True
```
**Purpose:** Enables debug mode (detailed error pages)  
**Development:** `True`  
**Production:** `False` (MUST be False in production)

```env
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```
**Purpose:** Domains allowed to access Django  
**Development:** `localhost,127.0.0.1`  
**Production:** `yourdomain.com,.onrender.com`

```env
DJANGO_SETTINGS_MODULE=config.settings.development
```
**Purpose:** Which settings file to use  
**Development:** `config.settings.development`  
**Production:** `config.settings.production`

#### 2. Database

```env
DATABASE_URL=sqlite:///db.sqlite3
```
**Purpose:** Database connection string  
**Development:** `sqlite:///db.sqlite3` (local file)  
**Production:** `postgresql://user:pass@host:port/db` (from Render)  
**Note:** In development.py, SQLite is hardcoded, so this isn't used locally

#### 3. CORS (Cross-Origin Resource Sharing)

```env
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173
```
**Purpose:** Frontend URLs allowed to call the API  
**Development:** All local ports (3000, 5173)  
**Production:** `https://your-frontend.onrender.com`  
**Note:** In development.py, `CORS_ALLOW_ALL_ORIGINS=True` overrides this

#### 4. JWT Authentication

```env
JWT_SECRET_KEY=3TO7lb-YTpsiHbtOcxzUs0OoC5EUGaOyqUTyZmKcV1wAO8onNjy1KBPX-HZDlwlDD-k
```
**Purpose:** Signs JWT tokens for admin authentication  
**Generate:** `python -c "import secrets; print(secrets.token_urlsafe(50))"`  
**Security:** Must be different from DJANGO_SECRET_KEY

```env
JWT_ACCESS_TOKEN_LIFETIME_MINUTES=60
JWT_REFRESH_TOKEN_LIFETIME_HOURS=24
```
**Purpose:** How long JWT tokens are valid  
**Development:** 60 min / 24 hours (convenient for testing)  
**Production:** 15 min / 7 days (more secure)

#### 5. Encryption

```env
ENCRYPTION_KEY=MXRZl0om8IGYdZJ2PpcZnSqj7vE9IwUanGPW5zaiCIg=
```
**Purpose:** Fernet key for field-level encryption (sensitive report data)  
**Generate:** `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`  
**Security:** Must be exactly 32 bytes (base64 encoded). Never change in production (data will be unreadable).

#### 6. Rate Limiting

```env
RATE_LIMIT_ENABLED=True
```
**Purpose:** Prevents API abuse  
**Development:** `True` (test rate limiting)  
**Production:** `True` (always enabled)

#### 7. Email (Future Use)

```env
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
**Purpose:** Email configuration (not currently used)  
**Development:** Console backend (prints to terminal)  
**Production:** SMTP backend (real email service)

### Frontend (`frontend/.env`)

```env
VITE_API_URL=http://localhost:8000
```
**Purpose:** Backend API base URL  
**Development:** `http://localhost:8000`  
**Production:** `https://your-backend.onrender.com`

```env
VITE_API_TIMEOUT=30000
```
**Purpose:** API request timeout (milliseconds)  
**Default:** 30 seconds

```env
VITE_APP_NAME=ShieldHer
VITE_APP_VERSION=1.0.0
```
**Purpose:** App metadata  
**Usage:** Display in UI, analytics

```env
VITE_ENABLE_ANALYTICS=false
VITE_ENABLE_ERROR_REPORTING=false
```
**Purpose:** Feature flags  
**Development:** `false` (no tracking)  
**Production:** `false` (privacy-first, no tracking)

## 🔄 How Environment Variables Are Used

### Development Flow

1. **You create** `.env` file with values
2. **Django reads** environment variables using `os.environ.get()`
3. **Settings files** use these values or fallbacks
4. **Application runs** with configured values

### Example from `base.py`:

```python
# Reads DJANGO_SECRET_KEY from .env
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-this-in-production')
#                            ↑ From .env file      ↑ Fallback if not set

# Reads JWT_SECRET_KEY from .env
SIMPLE_JWT = {
    'SIGNING_KEY': os.environ.get('JWT_SECRET_KEY', SECRET_KEY),
}

# Reads ENCRYPTION_KEY from .env
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', 'change-this-to-a-32-byte-fernet-key')
```

## 🚨 Security Best Practices

### ✅ DO:

1. **Generate unique keys** for each environment
   ```bash
   # Development keys
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   
   # Production keys (generate different ones!)
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Keep `.env` in `.gitignore`**
   ```gitignore
   # Already in .gitignore
   .env
   *.env
   !.env.example
   ```

3. **Use different keys** for development vs production

4. **Store production keys** securely (Render dashboard, not in code)

5. **Never commit** `.env` to Git

### ❌ DON'T:

1. ❌ Use placeholder values in production
2. ❌ Commit `.env` to Git
3. ❌ Share keys in Slack/email
4. ❌ Use same keys across environments
5. ❌ Hardcode secrets in code

## 🎯 For Different Environments

### Local Development (Current)

```env
# backend/.env
DJANGO_SECRET_KEY=0s0+*jokg4k2**+t0+zb*t^44!+cyk)qs-exp3_cfp+n_x%^sd
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

**Status:** ✅ Now properly configured

### Production (Render.com)

```env
# Set in Render dashboard, NOT in .env file
DJANGO_SECRET_KEY=<generate-new-unique-key>
DJANGO_DEBUG=False
DATABASE_URL=<provided-by-render>
ALLOWED_HOSTS=.onrender.com
CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com
JWT_SECRET_KEY=<generate-new-unique-key>
ENCRYPTION_KEY=<generate-new-unique-key>
```

**Important:** Generate **NEW** keys for production, don't reuse development keys!

## 🔧 How to Generate Keys

### Django Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### JWT Secret Key
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### Encryption Key (Fernet)
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

### All at Once
```bash
# Run in backend directory
cd backend
.\venv\Scripts\activate

echo "DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
echo "JWT_SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
echo "ENCRYPTION_KEY=$(python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())')"
```

## 📝 Checklist

### Development Environment ✅
- [x] `.env` file created
- [x] Secure keys generated
- [x] Database configured (SQLite)
- [x] CORS configured for local ports
- [x] Debug mode enabled
- [x] `.env` in `.gitignore`

### Before Production Deployment 🚀
- [ ] Generate NEW production keys (different from dev)
- [ ] Set `DJANGO_DEBUG=False`
- [ ] Configure production DATABASE_URL
- [ ] Set production ALLOWED_HOSTS
- [ ] Set production CORS_ALLOWED_ORIGINS
- [ ] Store keys in Render dashboard (not in code)
- [ ] Test with production keys in staging first

## 🆘 Troubleshooting

### "SECRET_KEY not set" error
**Cause:** `.env` file not loaded or missing  
**Fix:** Ensure `.env` exists in `backend/` directory

### "Invalid encryption key" error
**Cause:** ENCRYPTION_KEY is not a valid Fernet key  
**Fix:** Generate new key with Fernet.generate_key()

### "CORS error" in browser
**Cause:** Frontend URL not in CORS_ALLOWED_ORIGINS  
**Fix:** Add frontend URL to CORS_ALLOWED_ORIGINS or use CORS_ALLOW_ALL_ORIGINS=True in development

### Database connection error
**Cause:** DATABASE_URL incorrect or database not running  
**Fix:** For local dev, use SQLite (already configured in development.py)

## 📚 Additional Resources

- [Django Settings Best Practices](https://docs.djangoproject.com/en/4.2/topics/settings/)
- [12-Factor App Config](https://12factor.net/config)
- [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

**Your environment is now properly configured for secure local development!** 🎉

When deploying to production, remember to generate **NEW** keys and never reuse development keys.

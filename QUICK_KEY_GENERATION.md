# 🔐 Quick Key Generation Reference

## Fastest Method (Recommended)

```bash
cd backend
.\venv\Scripts\activate
python generate_production_keys.py
```

**Copy the output and paste into Render dashboard.**

---

## Individual Key Commands

### Django Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### JWT Secret Key
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### Encryption Key
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

## All Keys at Once (Copy-Paste)

```powershell
cd backend
.\venv\Scripts\activate

Write-Host "DJANGO_SECRET_KEY:" -ForegroundColor Yellow
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Write-Host "`nJWT_SECRET_KEY:" -ForegroundColor Yellow
python -c "import secrets; print(secrets.token_urlsafe(50))"

Write-Host "`nENCRYPTION_KEY:" -ForegroundColor Yellow
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

---

## Where to Use These Keys

### Development (Already Set)
✅ Keys are in `backend/.env`  
✅ Used for local testing  
✅ Never commit to Git

### Production (Generate New Ones)
🚀 Generate NEW keys (don't reuse dev keys)  
🚀 Add to Render dashboard → Environment tab  
🚀 Set `DEBUG=False`

---

## Quick Checklist

- [ ] Generate keys: `python generate_production_keys.py`
- [ ] Save in password manager
- [ ] Add to Render dashboard
- [ ] Set `DEBUG=False`
- [ ] Set `DJANGO_SETTINGS_MODULE=config.settings.production`
- [ ] Test deployment

---

**For detailed instructions, see:** `GENERATE_PRODUCTION_KEYS.md`

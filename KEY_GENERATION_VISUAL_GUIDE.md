# 🎨 Visual Guide: Generating Production Keys

## 📺 Step-by-Step with Screenshots

### Step 1: Open Terminal in Backend Directory

```
Your Project
└── backend/              ← Navigate here
    ├── venv/
    ├── generate_production_keys.py  ← The script
    └── ...
```

**Command:**
```bash
cd backend
```

---

### Step 2: Activate Virtual Environment

**Windows (PowerShell/CMD):**
```bash
.\venv\Scripts\activate
```

**You should see:**
```
(venv) PS C:\...\ShieldHer\backend>
```

---

### Step 3: Run the Key Generator

**Command:**
```bash
python generate_production_keys.py
```

**You will see:**
```
======================================================================
🔐 ShieldHer Production Keys Generator
======================================================================

⚠️  IMPORTANT:
   - These keys are for PRODUCTION use only
   - Do NOT commit these to Git
   - Store them securely in Render/Railway dashboard
   - Never reuse development keys in production

======================================================================

📋 Copy these values to your deployment platform:

----------------------------------------------------------------------
DJANGO_SECRET_KEY
----------------------------------------------------------------------
qxbe74f9v=5qbnqer(if#qtlm08m^gs3(2a*wlutwkg-1h)%og

----------------------------------------------------------------------
JWT_SECRET_KEY
----------------------------------------------------------------------
kLaxoqCjnprMXjmF9YjQM_mkLRGcd_bQrx3YxfjIiP2TZrxt6N19KWGBFePS3MY3NWI

----------------------------------------------------------------------
ENCRYPTION_KEY
----------------------------------------------------------------------
vE3js7xbDZSWlZuEftfnHtsJRRrzx9d_wwUNRAn5ihI=

======================================================================
```

---

### Step 4: Copy Each Key

**Select and copy each key value:**

1. **DJANGO_SECRET_KEY**
   ```
   qxbe74f9v=5qbnqer(if#qtlm08m^gs3(2a*wlutwkg-1h)%og
   ```
   - Select the entire line
   - Right-click → Copy (or Ctrl+C)

2. **JWT_SECRET_KEY**
   ```
   kLaxoqCjnprMXjmF9YjQM_mkLRGcd_bQrx3YxfjIiP2TZrxt6N19KWGBFePS3MY3NWI
   ```
   - Select the entire line
   - Right-click → Copy (or Ctrl+C)

3. **ENCRYPTION_KEY**
   ```
   vE3js7xbDZSWlZuEftfnHtsJRRrzx9d_wwUNRAn5ihI=
   ```
   - Select the entire line
   - Right-click → Copy (or Ctrl+C)

---

### Step 5: Save Keys Securely (IMPORTANT!)

**Option A: Password Manager (Recommended)**

1. Open your password manager (1Password, LastPass, Bitwarden, etc.)
2. Create new secure note: "ShieldHer Production Keys"
3. Paste each key with its label:
   ```
   DJANGO_SECRET_KEY: qxbe74f9v=5qbnqer(if#qtlm08m^gs3(2a*wlutwkg-1h)%og
   JWT_SECRET_KEY: kLaxoqCjnprMXjmF9YjQM_mkLRGcd_bQrx3YxfjIiP2TZrxt6N19KWGBFePS3MY3NWI
   ENCRYPTION_KEY: vE3js7xbDZSWlZuEftfnHtsJRRrzx9d_wwUNRAn5ihI=
   ```
4. Save the note

**Option B: Encrypted File**

1. Create a text file (temporarily)
2. Paste the keys
3. Encrypt with 7-Zip or similar
4. Delete the plain text file
5. Store encrypted file securely

**❌ DON'T:**
- Save in plain text on desktop
- Email to yourself
- Share via Slack/Discord
- Commit to Git

---

### Step 6: Add Keys to Render Dashboard

**Navigate to Render:**

1. Go to https://dashboard.render.com
2. Click on your backend service (e.g., "shieldher-backend")
3. Click "Environment" tab on the left

**Add Environment Variables:**

Click "Add Environment Variable" button for each key:

```
┌─────────────────────────────────────────────────────────┐
│ Add Environment Variable                                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ Key:   [DJANGO_SECRET_KEY                    ]         │
│                                                         │
│ Value: [qxbe74f9v=5qbnqer(if#qtlm08m^gs3...  ]         │
│                                                         │
│        [ ] Generate Value                               │
│                                                         │
│ [Cancel]                              [Add Variable]    │
└─────────────────────────────────────────────────────────┘
```

**Repeat for all three keys:**

| Key | Value |
|-----|-------|
| `DJANGO_SECRET_KEY` | Paste from terminal |
| `JWT_SECRET_KEY` | Paste from terminal |
| `ENCRYPTION_KEY` | Paste from terminal |

**Also add these:**

| Key | Value |
|-----|-------|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `CORS_ALLOWED_ORIGINS` | `https://your-frontend.onrender.com` |

---

### Step 7: Save and Deploy

1. Click "Save Changes" button
2. Render will automatically redeploy with new keys
3. Wait for deployment to complete (5-10 minutes)

---

## 🎯 Visual Comparison: Dev vs Production

### Development Environment (Local)

```
┌─────────────────────────────────────────┐
│ backend/.env (Local File)               │
├─────────────────────────────────────────┤
│ DJANGO_SECRET_KEY=dev-key-123...        │
│ JWT_SECRET_KEY=dev-jwt-456...           │
│ ENCRYPTION_KEY=dev-enc-789...           │
│ DEBUG=True                              │
│ DATABASE_URL=sqlite:///db.sqlite3       │
└─────────────────────────────────────────┘
         ↓
    Used for local testing only
```

### Production Environment (Render)

```
┌─────────────────────────────────────────┐
│ Render Dashboard → Environment Tab      │
├─────────────────────────────────────────┤
│ DJANGO_SECRET_KEY=prod-key-abc...       │
│ JWT_SECRET_KEY=prod-jwt-def...          │
│ ENCRYPTION_KEY=prod-enc-ghi...          │
│ DEBUG=False                             │
│ DATABASE_URL=postgresql://...           │
└─────────────────────────────────────────┘
         ↓
    Used for live production site
```

**Key Point:** These are DIFFERENT keys! Never reuse dev keys in production.

---

## 🔄 When to Regenerate Keys

### Immediately Regenerate If:

- 🚨 Keys are accidentally committed to Git
- 🚨 Keys are shared via email/Slack
- 🚨 Team member with access leaves
- 🚨 Security breach suspected
- 🚨 Keys appear in logs/error messages

### Regular Rotation Schedule:

- 📅 Every 90 days (recommended)
- 📅 Every 180 days (minimum)
- 📅 After major security updates

### How to Rotate:

1. Generate new keys: `python generate_production_keys.py`
2. Update in Render dashboard
3. Redeploy application
4. Test thoroughly
5. Delete old keys from password manager

**⚠️ EXCEPTION:** Never rotate `ENCRYPTION_KEY` unless absolutely necessary (data will be unreadable)

---

## 📊 Key Security Levels

```
┌──────────────────────────────────────────────────────┐
│ Key Type          │ Security Level │ Rotation        │
├──────────────────────────────────────────────────────┤
│ DJANGO_SECRET_KEY │ 🔴 CRITICAL    │ Every 90 days   │
│ JWT_SECRET_KEY    │ 🔴 CRITICAL    │ Every 90 days   │
│ ENCRYPTION_KEY    │ 🔴 CRITICAL    │ Only if leaked  │
└──────────────────────────────────────────────────────┘
```

**All keys are critical - protect them like passwords!**

---

## ✅ Verification Checklist

After adding keys to Render:

- [ ] All 3 keys added to Render dashboard
- [ ] Keys saved in password manager
- [ ] `DEBUG=False` set
- [ ] `DJANGO_SETTINGS_MODULE=config.settings.production` set
- [ ] Backend service redeployed successfully
- [ ] No errors in deployment logs
- [ ] API health check responds: `https://your-backend.onrender.com/api/health/`
- [ ] Admin login works: `https://your-backend.onrender.com/admin/`
- [ ] Keys deleted from terminal history
- [ ] Keys deleted from clipboard

---

## 🆘 Troubleshooting

### "Command not found: python"

**Try:**
```bash
python3 generate_production_keys.py
```

### "No module named 'django'"

**Fix:**
```bash
.\venv\Scripts\activate
pip install -r requirements/production.txt
```

### "Permission denied"

**Fix (Windows):**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Keys not showing in terminal

**Fix:**
- Scroll up in terminal
- Or redirect to file: `python generate_production_keys.py > keys.txt`
- Copy from `keys.txt`, then delete the file

---

## 📚 Additional Resources

- **Full Guide:** `GENERATE_PRODUCTION_KEYS.md`
- **Quick Reference:** `QUICK_KEY_GENERATION.md`
- **Environment Config:** `ENV_CONFIGURATION_GUIDE.md`
- **Deployment Plan:** `DEPLOYMENT_PLAN.md`

---

**Remember:** Production keys are like your house keys - keep them safe! 🔐

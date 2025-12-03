# Fix Reports on Render - Encryption Key Issue

## Problem
Reports are failing with 500 Internal Server Error because the `ENCRYPTION_KEY` environment variable is not set on Render.

## Solution

### Step 1: Generate an Encryption Key

Run this command locally to generate a secure encryption key:

```bash
cd backend
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

This will output something like:
```
gAAAAABhkL9x... (a long base64 string)
```

**IMPORTANT:** Copy this key - you'll need it for Render.

### Step 2: Add Environment Variable to Render

1. Go to your Render dashboard: https://dashboard.render.com
2. Click on your **backend service** (shieldher-backend)
3. Go to the **Environment** tab
4. Click **Add Environment Variable**
5. Add:
   - **Key:** `ENCRYPTION_KEY`
   - **Value:** (paste the key you generated)
6. Click **Save Changes**

Render will automatically redeploy your backend with the new environment variable.

### Step 3: Verify Database Migrations

Make sure all migrations are run on Render:

1. In Render dashboard, go to your backend service
2. Go to the **Shell** tab
3. Run:
   ```bash
   python manage.py migrate
   ```

### Step 4: Test the Reports

1. Go to your live site: https://shieldher.onrender.com/report
2. Fill out the report form
3. Submit
4. You should get a confirmation code

## Alternative: Use the generate_production_keys.py Script

If you prefer, you can use the existing script:

```bash
cd backend
python generate_production_keys.py
```

This will generate all necessary keys including `ENCRYPTION_KEY`.

## Environment Variables Checklist for Render

Make sure these are all set in your Render backend service:

- ✅ `DATABASE_URL` (automatically set by Render)
- ✅ `SECRET_KEY` (Django secret key)
- ✅ `ENCRYPTION_KEY` (for report encryption) **← THIS IS MISSING**
- ✅ `ALLOWED_HOSTS` (set to `.onrender.com` or your domain)
- ✅ `DJANGO_SETTINGS_MODULE` (set to `config.settings.production`)

## Quick Fix Command

If you have access to Render CLI:

```bash
# Generate key
KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

# Set on Render (replace YOUR_SERVICE_NAME)
render env set ENCRYPTION_KEY="$KEY" --service YOUR_SERVICE_NAME
```

## Troubleshooting

### Still Getting 500 Error?

1. Check Render logs:
   - Go to your backend service
   - Click on **Logs** tab
   - Look for error messages

2. Common issues:
   - `ENCRYPTION_KEY not set in settings` - Environment variable not added
   - `Invalid encryption key format` - Key is malformed
   - `Database error` - Migrations not run

### Check if Key is Set

In Render Shell, run:
```bash
python manage.py shell -c "from django.conf import settings; print('Key set:', hasattr(settings, 'ENCRYPTION_KEY'))"
```

Should output: `Key set: True`

## Security Notes

- **Never commit the encryption key to Git**
- **Use different keys for development and production**
- **Store the production key securely** (password manager)
- **If you lose the key, you cannot decrypt existing reports**

## After Fix

Once the encryption key is set:

1. Reports will be encrypted before storage
2. Only admins with the key can decrypt them
3. PII will be automatically redacted
4. Users will receive confirmation codes

## Need Help?

If you're still having issues:

1. Check the Render logs for specific error messages
2. Verify all environment variables are set
3. Ensure database migrations are complete
4. Test locally first to isolate the issue

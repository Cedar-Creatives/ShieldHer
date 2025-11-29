"""
Generate secure production keys for ShieldHer deployment.

Run this script to generate NEW keys for production deployment.
NEVER reuse development keys in production!

Usage:
    python generate_production_keys.py
"""

def generate_django_secret_key():
    """Generate Django SECRET_KEY"""
    from django.core.management.utils import get_random_secret_key
    return get_random_secret_key()


def generate_jwt_secret_key():
    """Generate JWT SECRET_KEY"""
    import secrets
    return secrets.token_urlsafe(50)


def generate_encryption_key():
    """Generate Fernet encryption key"""
    from cryptography.fernet import Fernet
    return Fernet.generate_key().decode()


def main():
    print("=" * 70)
    print("🔐 ShieldHer Production Keys Generator")
    print("=" * 70)
    print()
    print("⚠️  IMPORTANT:")
    print("   - These keys are for PRODUCTION use only")
    print("   - Do NOT commit these to Git")
    print("   - Store them securely in Render/Railway dashboard")
    print("   - Never reuse development keys in production")
    print()
    print("=" * 70)
    print()
    
    # Generate all keys
    django_key = generate_django_secret_key()
    jwt_key = generate_jwt_secret_key()
    encryption_key = generate_encryption_key()
    
    # Display keys
    print("📋 Copy these values to your deployment platform:")
    print()
    print("-" * 70)
    print("DJANGO_SECRET_KEY")
    print("-" * 70)
    print(django_key)
    print()
    
    print("-" * 70)
    print("JWT_SECRET_KEY")
    print("-" * 70)
    print(jwt_key)
    print()
    
    print("-" * 70)
    print("ENCRYPTION_KEY")
    print("-" * 70)
    print(encryption_key)
    print()
    
    print("=" * 70)
    print()
    print("📝 Next Steps:")
    print()
    print("1. Go to your Render.com dashboard")
    print("2. Navigate to your backend service")
    print("3. Go to 'Environment' tab")
    print("4. Add/Update these environment variables:")
    print()
    print("   Variable Name          | Value (copy from above)")
    print("   " + "-" * 66)
    print("   DJANGO_SECRET_KEY      | <copy DJANGO_SECRET_KEY>")
    print("   JWT_SECRET_KEY         | <copy JWT_SECRET_KEY>")
    print("   ENCRYPTION_KEY         | <copy ENCRYPTION_KEY>")
    print()
    print("5. Also set these production variables:")
    print()
    print("   DJANGO_SETTINGS_MODULE | config.settings.production")
    print("   DEBUG                  | False")
    print("   ALLOWED_HOSTS          | .onrender.com")
    print("   DATABASE_URL           | <provided by Render>")
    print("   CORS_ALLOWED_ORIGINS   | https://your-frontend.onrender.com")
    print()
    print("=" * 70)
    print()
    print("✅ Keys generated successfully!")
    print()
    print("⚠️  SECURITY REMINDER:")
    print("   - Save these keys in a secure password manager")
    print("   - Do NOT share them via email/Slack")
    print("   - Do NOT commit them to Git")
    print("   - If compromised, regenerate immediately")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate an encryption key for ShieldHer reports.
Run this and add the output to your Render environment variables.
"""

from cryptography.fernet import Fernet

# Generate a new Fernet key
key = Fernet.generate_key().decode()

print("=" * 70)
print("ENCRYPTION KEY FOR SHIELDHER")
print("=" * 70)
print()
print("Copy the key below and add it to your Render environment variables:")
print()
print(f"ENCRYPTION_KEY={key}")
print()
print("=" * 70)
print()
print("Steps to add to Render:")
print("1. Go to https://dashboard.render.com")
print("2. Click on your backend service (shieldher-backend)")
print("3. Go to Environment tab")
print("4. Click 'Add Environment Variable'")
print("5. Key: ENCRYPTION_KEY")
print("6. Value: (paste the key above)")
print("7. Click 'Save Changes'")
print()
print("⚠️  IMPORTANT: Keep this key secure! Store it in a password manager.")
print("   If you lose this key, you cannot decrypt existing reports.")
print("=" * 70)

"""
Core utilities for ShieldHer platform.
Provides encryption, validation, and helper functions.
"""

import os
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import logging

logger = logging.getLogger(__name__)


def get_encryption_key():
    """
    Get the encryption key from settings.
    Ensures the key is properly formatted for Fernet.
    """
    key = settings.ENCRYPTION_KEY
    
    # If key is not already base64 encoded, encode it
    if not key:
        raise ValueError("ENCRYPTION_KEY not set in settings")
    
    try:
        # Try to use it as-is first
        Fernet(key.encode() if isinstance(key, str) else key)
        return key.encode() if isinstance(key, str) else key
    except Exception:
        # If that fails, generate a proper key
        logger.warning("Invalid encryption key format, generating new key")
        return Fernet.generate_key()


def encrypt_field(value):
    """
    Encrypt a field value using Fernet symmetric encryption.
    
    Args:
        value (str): The value to encrypt
        
    Returns:
        str: The encrypted value as a string
    """
    if not value:
        return value
    
    try:
        key = get_encryption_key()
        f = Fernet(key)
        
        # Convert to bytes if string
        if isinstance(value, str):
            value = value.encode('utf-8')
        
        # Encrypt and return as string
        encrypted = f.encrypt(value)
        return encrypted.decode('utf-8')
    except Exception as e:
        logger.error(f"Encryption error: {e}")
        raise


def decrypt_field(encrypted_value):
    """
    Decrypt a field value using Fernet symmetric encryption.
    
    Args:
        encrypted_value (str): The encrypted value
        
    Returns:
        str: The decrypted value as a string
    """
    if not encrypted_value:
        return encrypted_value
    
    try:
        key = get_encryption_key()
        f = Fernet(key)
        
        # Convert to bytes if string
        if isinstance(encrypted_value, str):
            encrypted_value = encrypted_value.encode('utf-8')
        
        # Decrypt and return as string
        decrypted = f.decrypt(encrypted_value)
        return decrypted.decode('utf-8')
    except Exception as e:
        logger.error(f"Decryption error: {e}")
        raise


def generate_confirmation_code(prefix="SH"):
    """
    Generate a unique, non-identifying confirmation code.
    
    Args:
        prefix (str): Prefix for the code (default: "SH")
        
    Returns:
        str: A confirmation code like "SH-2025-A7B9C2"
    """
    import uuid
    from django.utils import timezone
    
    year = timezone.now().year
    random_part = uuid.uuid4().hex[:6].upper()
    
    return f"{prefix}-{year}-{random_part}"


def detect_pii(text):
    """
    Detect potential PII (Personally Identifiable Information) in text.
    
    This is a basic implementation that checks for common PII patterns:
    - Email addresses
    - Phone numbers
    - Social security numbers
    - Credit card numbers
    
    Args:
        text (str): The text to check for PII
        
    Returns:
        list: List of detected PII types, empty if none found
    """
    import re
    
    if not text:
        return []
    
    detected = []
    
    # Email pattern
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        detected.append('email')
    
    # Phone number patterns (various formats)
    phone_patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # 123-456-7890 or 1234567890
        r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',     # (123) 456-7890
        r'\+\d{1,3}\s?\d{1,14}',            # International format
    ]
    for pattern in phone_patterns:
        if re.search(pattern, text):
            detected.append('phone')
            break
    
    # SSN pattern (123-45-6789)
    if re.search(r'\b\d{3}-\d{2}-\d{4}\b', text):
        detected.append('ssn')
    
    # Credit card pattern (basic check for 13-19 digit sequences)
    if re.search(r'\b\d{13,19}\b', text):
        detected.append('credit_card')
    
    # Address patterns (basic - street numbers)
    if re.search(r'\b\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr)\b', text, re.IGNORECASE):
        detected.append('address')
    
    return list(set(detected))  # Remove duplicates



def redact_pii(text):
    """
    Redact potential PII from text by replacing it with [REDACTED].
    
    Args:
        text (str): The text to redact PII from
        
    Returns:
        str: Text with PII redacted
    """
    import re
    
    if not text:
        return text
    
    redacted_text = text
    
    # Redact email addresses
    redacted_text = re.sub(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        '[EMAIL REDACTED]',
        redacted_text
    )
    
    # Redact phone numbers
    phone_patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',
        r'\+\d{1,3}\s?\d{1,14}',
    ]
    for pattern in phone_patterns:
        redacted_text = re.sub(pattern, '[PHONE REDACTED]', redacted_text)
    
    # Redact SSN
    redacted_text = re.sub(
        r'\b\d{3}-\d{2}-\d{4}\b',
        '[SSN REDACTED]',
        redacted_text
    )
    
    # Redact potential credit card numbers
    redacted_text = re.sub(
        r'\b\d{13,19}\b',
        '[NUMBER REDACTED]',
        redacted_text
    )
    
    # Redact addresses
    redacted_text = re.sub(
        r'\b\d+\s+[A-Za-z]+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr)\b',
        '[ADDRESS REDACTED]',
        redacted_text,
        flags=re.IGNORECASE
    )
    
    return redacted_text

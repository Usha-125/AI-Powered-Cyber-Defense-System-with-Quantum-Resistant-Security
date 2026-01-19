from cryptography.fernet import Fernet

# Your security alert (from Day 9)
alert_message = """
--- SECURITY ALERT ---
Type      : Intrusion Detected
IP         : 192.168.1.5
Severity  : HIGH
Action    : Investigate Immediately
----------------------
"""

print("Original Alert:\n", alert_message)

# Generate a secret key (simulating quantum-safe key generation)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt the alert
encrypted_alert = cipher.encrypt(alert_message.encode())

print("\nEncrypted Alert (Unreadable):\n", encrypted_alert)

# Decrypt the alert (only authorized system can do this)
decrypted_alert = cipher.decrypt(encrypted_alert).decode()

print("\nDecrypted Alert (Recovered):\n", decrypted_alert)

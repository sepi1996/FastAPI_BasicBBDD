import bcrypt


def get_hashed_password(plain_text_password):
    # Encode the plain text password to bytes using UTF-8
    password_bytes = plain_text_password.encode('utf-8')
    
    # Hash the encoded password
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    # Convert the hashed password from bytes to a string for storage
    return hashed_password.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///medical_service_desk.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # Change this to a real secret key in production

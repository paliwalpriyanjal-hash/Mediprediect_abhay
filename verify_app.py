import requests

BASE_URL = "http://127.0.0.1:5000"

def test_app():
    session = requests.Session()
    
    # 1. Test Home Page
    print("Testing Home Page...")
    r = session.get(BASE_URL)
    if r.status_code == 200:
        print("Home Page: OK")
    else:
        print(f"Home Page: FAILED ({r.status_code})")
        return

    # 2. Test Registration
    print("Testing Registration...")
    reg_data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123",
        "confirm_password": "password123"
    }
    r = session.post(f"{BASE_URL}/register", data=reg_data, allow_redirects=True)
    if "Registration successful" in r.text or "Account created successfully" in r.text or r.status_code == 200:
        print("Registration: OK (or already exists)")
    else:
        print(f"Registration: FAILED")
        # print(r.text)

    # 3. Test Login
    print("Testing Login...")
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    r = session.post(f"{BASE_URL}/login", data=login_data, allow_redirects=True)
    if "Welcome back" in r.text or "predict" in r.url:
        print("Login: OK")
    else:
        print(f"Login: FAILED")
        return

    # 4. Test Predict
    print("Testing Prediction...")
    predict_data = {
        "age": "25",
        "gender": "Male",
        "symptoms": ["cough", "fever", "fatigue"]
    }
    # Flask expects multipart/form-data or form-urlencoded with multiple keys for getlist
    r = session.post(f"{BASE_URL}/predict", data=predict_data, allow_redirects=True)
    if "result" in r.url or "Prediction Result" in r.text:
        print("Prediction: OK")
    else:
        print(f"Prediction: FAILED")
        # print(r.url)
        # print(r.text)

    # 5. Test Dashboard
    print("Testing Dashboard...")
    r = session.get(f"{BASE_URL}/dashboard")
    if "History" in r.text or "Dashboard" in r.text:
        print("Dashboard: OK")
    else:
        print("Dashboard: FAILED")

if __name__ == "__main__":
    try:
        test_app()
    except Exception as e:
        print(f"An error occurred: {e}")

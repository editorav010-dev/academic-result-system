try:
    from app.main import app
    print("app.main imported successfully")
except Exception as e:
    import traceback
    traceback.print_exc()

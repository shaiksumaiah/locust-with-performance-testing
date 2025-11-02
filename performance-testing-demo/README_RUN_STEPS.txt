Quick run steps (local):

1) Create & activate venv
   python -m venv venv
   # mac/linux
   source venv/bin/activate
   # windows (PowerShell)
   # .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt

2) Start FastAPI app
   uvicorn app.main:app --reload

3) Open docs: http://127.0.0.1:8000/docs

4) Start Locust in a second terminal:
   locust -f locustfile.py
   Open http://localhost:8089
   Host: http://127.0.0.1:8000
   Number of users: 100
   Spawn rate: 10

5) View cache metrics:
   curl http://127.0.0.1:8000/cache-metrics
   Reset cache:
   curl -X POST http://127.0.0.1:8000/cache-reset

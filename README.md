### Spinning Up Project

#### Installing Python dependencies
```bash
pip install -r requirements.txt
```

#### Load Fixtures for project
```bash
python manage.py loaddata fixtures/*.json
```

### Emailing users the weather forecast
```bash
python manage.py send_user_forecasts
```
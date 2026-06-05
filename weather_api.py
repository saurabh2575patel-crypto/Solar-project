import requests
def cloud_cover(api_key,lat,lon):
    try:
        r=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}',timeout=5)
        return r.json().get('clouds',{}).get('all',0)
    except Exception:
        return 0

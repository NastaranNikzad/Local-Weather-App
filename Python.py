import requests

# جایگزین کردن با کلید API شخصی شما
API_KEY = '0efcc1a5ecfe1381d7e9d67f3424abdb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

# تابع برای دریافت داده‌های آب و هوایی
def get_weather_data(city_name):
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()

# تابع اصلی
def main():
    city_name = input("لطفا نام شهر را وارد کنید: ")
    weather_data = get_weather_data(city_name)

    if weather_data['cod'] == 200:
        # استخراج اطلاعات مورد نیاز از پاسخ
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        
        # نمایش اطلاعات آب و هوایی
        print(f"دما: {temp} کلوین")
        print(f"رطوبت: {humidity}%")
        print(f"سرعت باد: {wind_speed} متر بر ثانیه")
        print(f"توضیحات: {description}")
    else:
        print("متاسفانه اطلاعات آب و هوایی یافت نشد.")

if __name__ == '__main__':
    main()

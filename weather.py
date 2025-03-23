import requests
import json
import sys

def get_weather(city):
    """获取指定城市的天气信息"""
    api_key = "your-api-key"  # 替换为您的API密钥
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # 构建请求URL
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # 使用摄氏度
    }
    
    try:
        # 发送请求
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析响应
        weather_data = response.json()
        
        # 提取需要的信息
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        
        # 格式化输出
        print(f"\n天气信息 - {city.title()}:")
        print(f"温度: {temperature}°C")
        print(f"湿度: {humidity}%")
        print(f"天气状况: {description}")
        print(f"风速: {wind_speed} m/s\n")
        
    except requests.exceptions.RequestException as e:
        print(f"获取天气信息时出错: {e}")
        sys.exit(1)

def main():
    # 检查是否提供了城市名称
    if len(sys.argv) < 2:
        print("请提供城市名称作为参数")
        print("示例: python weather.py 北京")
        sys.exit(1)
    
    # 获取城市名称
    city = sys.argv[1]
    
    # 获取并显示天气信息
    get_weather(city)

if __name__ == "__main__":
    main()
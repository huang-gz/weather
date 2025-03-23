# Weather Application

这是一个简单的天气信息应用程序，可以查询全球各地的实时天气状况。

## 功能特点

- 支持全球城市天气查询
- 提供实时温度、风速、天气状况等信息
- 支持天气预报功能
- 支持天气预警信息查询

## 技术栈

- Python 3.x
- 依赖管理：uv/pip

## 安装

1. 克隆仓库
```bash
git clone https://github.com/huang-gz/weather.git
cd weather
```

2. 创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
uv pip install -r requirements.txt
```

## 使用方法

运行主程序：
```bash
python weather.py
```

## 配置

- 在运行程序之前，请确保已经配置好相关的API密钥和必要的环境变量。

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License
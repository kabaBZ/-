# DYfans
使用appium进行抖音粉丝的自动化获取
## 工具：
appium appium inspector 夜神模拟器或者安卓手机 mitmdump mitmproxy
推荐使用安卓5.0夜神模拟器
## 库：
appium
selenium
json
## 环境：
jdk 安卓sdk 安卓adb工具 xposed框架 安卓root权限 模拟器开放端口8888至本机
## 使用方法：
在项目源目录cmd：mitmdump -s DYFo.py -p 8888
appium inspector 添加配置：
{
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
  "noReset": true,
  "unicodekeyboard": true,
  "resetkeyboard": true,
  "automationName": "UIAutomator1"
}
pycharm运行文件appium.py
粉丝id会记录在项目根目录的文本文件中

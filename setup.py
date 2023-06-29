from setuptools import setup

setup(
    name="tvdatafeed",
    version="2.0.0",
    packages=["tvDatafeed"],
    url="https://github.com/StreamAlpha/tvdatafeed/",
    project_urls={
        "YouTube": "https://youtube.com/StreamAlpha?sub_confirmation=1",
        "Funding": "https://www.buymeacoffee.com/StreamAlpha",
        "Telegram Channel": "https://t.me/streamAlpha",
        "Source": "https://github.com/StreamAlpha/tvdatafeed/",
        "Tracker": "https://github.com/StreamAlpha/tvdatafeed/issues",
    },
    license="MIT License",
    author="@StreamAlpha",
    author_email="",
    description="TradingView historical data downloader",
    install_requires=["setuptools", "pandas", "websocket-client", "requests"],
)

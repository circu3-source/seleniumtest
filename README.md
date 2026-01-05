# Google Search Automation (Selenium)

這是一個使用 **Python** 與 **Selenium** 撰寫的自動化腳本。

##功能特點
- **反偵測設定**：使用無痕模式並隱藏 WebDriver 標記，模擬真人行為。
- **自動搜尋**：自動在 Google 輸入關鍵字並執行搜尋。
- **分頁操作**：自動定位第一個搜尋結果，並在「新分頁」中開啟。
- **自動驅動管理**：使用 `webdriver-manager` 自動下載對應版本的 ChromeDriver。

##環境需求
執行此腳本前，請確保你的電腦已安裝：
- Python 3.x
- Chrome 瀏覽器

##安裝與執行
1. **複製此專案**：
   ```bash
   git clone [https://github.com/circu3-source/seleniumtest.git](https://github.com/circu3-source/seleniumtest.git)
   cd seleniumtest

2. **安裝必要套件**：
   ```bash
   pip install selenium webdriver-manager
   
3. **執行程式**：
   ```bash
   python selenium_test002.py

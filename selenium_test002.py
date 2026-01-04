import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains # 匯入 ActionChains 模組
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 設定變數 ---
TARGET_URL = "https://www.google.com"
SEARCH_TERM = "top 10 news"
SEARCH_BOX_LOCATOR = 'q' 

# --- 步驟一：設定反偵測選項 ---
chrome_options = Options()
chrome_options.add_argument("--incognito") 
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# --- 初始化 WebDriver ---
driver = None
try:
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    driver.maximize_window() 
    print("瀏覽器成功開啟 (無痕模式)。")

    # 隱藏 WebDriver 標記
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # 步驟二：導航並執行搜尋
    driver.get(TARGET_URL)
    print(f"成功導航到：{TARGET_URL}")
    
    wait = WebDriverWait(driver, 10) 
    print("正在等待 Google 搜尋框出現...")
    
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, SEARCH_BOX_LOCATOR))
    )
    
    print(f"在搜尋框輸入：'{SEARCH_TERM}'")
    search_box.send_keys(SEARCH_TERM)
    search_box.send_keys(Keys.ENTER)
    print("成功執行搜尋！")

    # ----------------------------------------------------
    #  步驟三：在新分頁開啟第一個搜尋結果 
    # ----------------------------------------------------
    
    # 1. 等待搜尋結果頁面的主要容器 (ID 為 'rso') 出現
    wait.until(EC.presence_of_element_located((By.ID, 'rso')))
    
    # 2. 定位第一個主要的搜尋結果連結（通常是 #rso 內的第一個 <a> 標籤）
    print("正在定位第一個搜尋結果...")
    first_result_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#rso a'))
    )

    # 3. 使用 ActionChains 模擬按住 Ctrl 鍵（Windows/Linux）或 Command 鍵（macOS）並點擊
    # 由於您是 Windows 環境，我們使用 Keys.CONTROL
    ActionChains(driver).key_down(Keys.CONTROL).click(first_result_link).key_up(Keys.CONTROL).perform()
    print("成功在新分頁點擊第一個搜尋結果。")
    
    # ----------------------------------------------------
    #  步驟四：切換到新開啟的分頁 
    # ----------------------------------------------------
    
    # 1. 取得所有視窗句柄 (Handles)
    window_handles = driver.window_handles
    
    # 2. 新開啟的分頁會是 list 中的最後一個元素 (index -1)
    new_tab_handle = window_handles[-1]
    
    # 3. 將 WebDriver 的焦點切換到新分頁
    driver.switch_to.window(new_tab_handle)
    
    print(f"已切換到新分頁，當前網址為：{driver.current_url}")
    
    # 步驟五：保持開啟觀察結果
    print("\n腳本執行完畢。瀏覽器將保持開啟，直到您手動關閉視窗。")
    
except Exception as e:
    print("\n發生錯誤！")
    print(f"錯誤類型: {type(e).__name__}")
    print(f"詳細訊息: {e}")
    
finally:
    # 保持瀏覽器開啟，故註解掉 driver.quit()
    pass
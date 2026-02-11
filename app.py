import pandas as pd
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Browser Configuration
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

print("Waiting for WhatsApp Web login...")
while len(driver.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

# 2. Loading and Cleaning Data
try:
    # Reads forcing string type to avoid scientific notation (e+12)
    df = pd.read_csv("contacts.csv", sep=None, engine='python', dtype=str, encoding="latin1")
    
    # Cleans up column names: removes spaces, quotes, and converts to lowercase
    df.columns = [str(c).strip().lower().replace('"', '').replace("'", "") for c in df.columns]
    
    # Clears data from rows
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Remove empty lines
    df = df.dropna(subset=df.columns[0:2]) 

    print(f"Columns detected and cleaned: {df.columns.tolist()}")
    print("Data loaded successfully!")
except Exception as e:
    print(f"Fatal error reading CSV: {e}")
    driver.quit()
    exit()

# 3. Send Loop
for i, row in df.iterrows():
    # Secure access: retrieving by column index if the name mapping fails
    try:
        name = str(row.iloc[0])
        phone_number = str(row.iloc[1])
        
        if not phone_number or phone_number == 'nan': 
            continue

        message = f"""
Edit your message here.
        """
        link = f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(message)}"
        
        driver.get(link)
        print(f"Trying to send to: {name} ({phone_number})")
        
        # SMART WAIT: Waits up to 35 seconds for the text field to appear
        bot_wait = WebDriverWait(driver, 35)
        text_field = bot_wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        
        # Small extra human-like delay after loading
        time.sleep(random.randint(2, 5))
        
        text_field.send_keys(Keys.ENTER)
        
        print(f"✅ Sent to {name}")
        
        # Anti-Ban Delay (keep it long for safety)
        wait_time = random.randint(40, 80) # time in seconds, adjustable
        print(f"Waiting {wait_time}s for next contact...")
        time.sleep(wait_time)

    except Exception as error:
        print(f"❌ Failed to send to {name}: The chat took too long to load or the number is invalid.")

print("Process Finished!")
driver.quit()
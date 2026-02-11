# WhatsApp Bulk Messenger Automation

This Python script automates sending personalized messages via **WhatsApp Web** using Selenium. It reads contacts from a CSV file and handles browser automation with anti-ban delays.

##  Features

* **Automatic Login:** Waits for you to scan the QR Code.
* **Smart Cleaning:** Automatically cleans spaces and special characters from your CSV headers.
* **Anti-Ban Logic:** Includes randomized wait times between messages to mimic human behavior.
* **Dynamic Loading:** Waits for the chat to load before attempting to send.

---

##  Requirements

Before running the script, ensure you have the following installed:

* **Python 3.x**
* **Google Chrome** browser
* Required libraries (install via terminal):
```bash
pip install -r requirements.txt

```



---

##  Data Format (contacts.csv)

The script expects a file named `contacts.csv` in the same folder. It must use a semicolon (`;`) or comma (`,`) as a separator.

### Critical Phone Number Format

For the automation to work, numbers **must not** include dashes, spaces, or parentheses. They must follow the international standard:
`[Country Code][Area/State Code][Number]`

* **Country Code:** 1 to 3 digits (e.g., `1` for USA, `44` for UK, `55` for Brazil).
* **State/Area Code:** Usually 2 to 3 digits.
* **Number:** The full subscriber number.

**Example Table:**

| Name | Phone Number | Description |
| --- | --- | --- |
| Alice | 12125550123 | **USA:** 1 (Country) + 212 (NY State) + Number |
| Roberto | 5511988887777 | **Brazil:** 55 (Country) + 11 (SP State) + Number |
| Liam | 442071234567 | **UK:** 44 (Country) + 20 (London) + Number |

**Correct CSV Example:**

```csv
name;phone_number
Alice;12125550123
Roberto;5511988887777

```

---

##  How to Use

1. **Prepare your CSV:** Save your contacts in `contacts.csv` following the format above.
2. **Edit your Message:** Open the script and edit the `message` variable inside the loop:
```python
mensagem = f"Hello {nome}, this is a test message!"

```


3. **Run the Script:**
```bash
python your_script_name.py

```


4. **Login:** A Chrome window will open. Scan the QR Code with your phone.
5. **Relax:** The script will wait for the login to complete and then start sending messages automatically.

---

## ⚠️ Important Warnings

* **Account Safety:** Sending too many messages to people who don't have your number saved can lead to a ban. Start with small batches.
* **Speed:** Do not decrease the `time.sleep` intervals too much; WhatsApp's algorithm detects rapid-fire messaging.
* **Personal Use:** This tool is for educational purposes and personal productivity.

---

**Would you like me to add a "Safe Mode" toggle to the script that limits the total number of messages per session?**

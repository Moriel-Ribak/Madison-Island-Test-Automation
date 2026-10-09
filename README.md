[README (1).md](https://github.com/user-attachments/files/33251889/README.1.md)
<a id="top"></a>

# 🛒 Madison Island | Test Automation

**🐍 Python · 🎭 Playwright · 🧪 Pytest · 🧩 Page Object Model · 📊 Allure**

**✅ 44 Test Cases · 📂 15 Test Files · 🔄 Functional & E2E Testing**

🌍 **Language / שפה:** [🇬🇧 English](#english) · [🇮🇱 עברית](#hebrew)

📊 **[View STD on Google Sheets](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)**

---

<a id="english"></a>

## 🇬🇧 English

[🇮🇱 Read in Hebrew](#hebrew) · [📊 Open the STD file](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)

### 🚀 About this project

This project tests the **[Madison Island](https://madison-island.com/)** online store using **Python, Playwright, and Pytest**. It uses the **Page Object Model (POM)** to keep website actions separate from test cases.

The goal is to check the main website features, practice real automation skills, and keep clear test documentation. The project includes **44 test cases in 15 test files**, including tests that use different sets of data.

### 🛠️ Tools & technologies

| Tool | What I use it for |
| --- | --- |
| 🐍 **Python** | Writing the automation code |
| 🎭 **Playwright** | Browser actions and checks |
| 🧪 **Pytest** | Running tests, fixtures, and test data |
| 🧩 **POM** | Organizing code by website page |
| 📊 **Allure** | Test reports, steps, and screenshots when enabled |
| 📗 **Google Sheets / STD** | Documenting test cases and expected results |

### 📁 Project structure

```text
Madison-Island-Test-Automation/
├── components/                # Shared components, such as the header
├── pages/                     # Page objects and BasePage
├── tests/                     # Automated test files by feature
├── util/                      # Test data and helper code
├── pytest.ini                 # Pytest settings
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

> Browser fixtures and page objects are set up in `conftest.py` and `BaseTest`.

> 🔐 **Repository safety:** Do not upload real passwords, `auth.json`, or private configuration files. Share sample configuration data without secrets.

### ✅ What is tested?

| Area | Checks |
| --- | --- |
| 🏠 **Home** | Page content, collections, and slideshow |
| 🧭 **Header** | Links and navigation |
| 🛍️ **Catalog** | Product list, pagination, and price sorting |
| 👕 **Product** | Title, price, size, color, and cart details |
| 🛒 **Cart** | Empty cart, added products, and quantity |
| 🔎 **Search** | Existing and missing products |
| 🔐 **Login** | Valid/invalid login and password reset pages |
| 📝 **Registration** | Registration with valid or missing data |
| 🔄 **E2E** | Product selection and cart flows |

Some tests use **`pytest.mark.parametrize`**, so one test function can run with several data sets.

### 📗 STD — Software Test Description

**[➡️ Open the STD on Google Sheets](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)**

The STD document is hosted on Google Sheets and is available in **English and Hebrew** and contains **44 test cases**. Each case includes a test ID, test steps, test data, expected result, severity, and space to record the actual result and status.

The STD describes **what should be tested**. It does **not** mean that all tests passed.

### ⚠️ CAPTCHA limitation — Login & Registration

The website uses **CAPTCHA / anti-bot protection** on login and registration forms. Because of this, automated tests that submit these forms **may be blocked or fail**, even when the automation code is correct.

This mainly affects login, registration, and any E2E flow that requires signing in. Tests that only open the Login or Reset Password page may still work.

**This project does not bypass CAPTCHA.** A failed login or registration test should not automatically be treated as a website bug.

### ▶️ How to run the tests

**1. Install packages**

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

The browser setup uses Google Chrome (`channel="chrome"`), so Chrome must be installed locally.

**2. Check `pytest.ini`**

The test filenames use names like `cart_001.py`, so Pytest needs a matching discovery pattern:

```ini
[pytest]
testpaths = tests
python_files = *_001.py *_002.py *_003.py *_004.py
python_classes = Test*
python_functions = test_*
addopts = --alluredir=allure-results
```

**3. Run tests**

```bash
# Run all tests
python -m pytest tests/ -v

# Run one test file
python -m pytest tests/cart_page_tests/cart_001.py -v

# Check test discovery without running tests
python -m pytest --collect-only -q
```

**4. Open Allure report**

```bash
allure serve allure-results
```

Allure Commandline must be installed separately. Failed-test screenshots appear when the screenshot hook is configured in `conftest.py`.

### 🏗️ Framework design

- **BasePage** — common actions such as click, fill, and read text.
- **Page Objects** — actions for each website page.
- **BaseTest** — access to page objects inside tests.
- **conftest.py** — browser setup and Pytest fixtures.
- **Test files** — steps and assertions that check results.

### 🎯 Project purpose

This is a learning and portfolio project that shows practical work with **web automation, functional testing, E2E testing, data-driven tests, STD documentation, and Allure reporting**.

[⬆️ Back to language selection](#top)

---

<a id="hebrew"></a>

## 🇮🇱 עברית

[🇬🇧 Switch to English](#english) · [📊 פתיחת מסמך STD](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)

### 🚀 על הפרויקט

הפרויקט כולל בדיקות אוטומטיות לאתר המסחר **[Madison Island](https://madison-island.com/)** באמצעות **Python, Playwright ו־Pytest**. תשתית הבדיקות מבוססת על **Page Object Model (POM)**, כדי להפריד בין הפעולות באתר לבין קוד הבדיקות.

מטרת הפרויקט היא לבדוק את הפונקציות המרכזיות באתר, לתרגל כתיבת אוטומציה ולתעד את הבדיקות בצורה מסודרת. בפרויקט יש **44 מקרי בדיקה ב־15 קובצי בדיקות**, כולל הרצות עם נתונים שונים.

### 🛠️ טכנולוגיות וכלים

| כלי | למה הוא משמש? |
| --- | --- |
| 🐍 **Python** | כתיבת קוד האוטומציה |
| 🎭 **Playwright** | פעולות ואימותים בדפדפן |
| 🧪 **Pytest** | הרצת בדיקות, Fixtures ונתוני בדיקה |
| 🧩 **POM** | הפרדת קוד הבדיקות לפי דפי האתר |
| 📊 **Allure** | דוחות, שלבי בדיקה וצילומי מסך כשהם מוגדרים |
| 📗 **Google Sheets / STD** | תיעוד מקרי הבדיקה והתוצאות הצפויות |

### 📁 מבנה הפרויקט

```text
Madison-Island-Test-Automation/
├── components/                # רכיבים משותפים באתר
├── pages/                     # Page Objects ו-BasePage
├── tests/                     # קובצי הבדיקות לפי נושא
├── util/                      # קוד עזר ונתוני בדיקה
├── pytest.ini                 # הגדרות Pytest
├── requirements.txt           # ספריות נדרשות
└── README.md                  # תיעוד הפרויקט
```

> הגדרות הדפדפן והאובייקטים לבדיקות נמצאות ב־`conftest.py` וב־`BaseTest`.

> 🔐 **אבטחה:** אין להעלות סיסמאות אמיתיות, `auth.json` או קובצי הגדרות פרטיים. ניתן לצרף קובץ הגדרות לדוגמה ללא סודות.

### ✅ מה נבדק בפרויקט?

| אזור | מה נבדק? |
| --- | --- |
| 🏠 **Home** | תוכן דף הבית, קולקציות ומצגת תמונות |
| 🧭 **Header** | ניווט בין עמודי האתר |
| 🛍️ **Catalog** | רשימת מוצרים, מעבר עמודים ומיון לפי מחיר |
| 👕 **Product** | שם, מחיר, מידה, צבע ופרטי מוצר בעגלה |
| 🛒 **Cart** | עגלה ריקה, מוצרים שנוספו ושינוי כמות |
| 🔎 **Search** | חיפוש מוצרים קיימים ולא קיימים |
| 🔐 **Login** | התחברות תקינה/שגויה ודפי איפוס סיסמה |
| 📝 **Registration** | הרשמה עם פרטים תקינים או חסרים |
| 🔄 **E2E** | תהליכים מבחירת מוצר ועד לעגלת הקניות |

חלק מהבדיקות משתמשות ב־**`pytest.mark.parametrize`**, שמאפשר להריץ אותה פונקציה עם כמה מערכי נתונים.

### 📗 מסמך STD — Software Test Description

**[➡️ פתיחת מסמך ה־STD ב־Google Sheets](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)**

מסמך ה־STD נמצא ב־Google Sheets, קיים **בעברית ובאנגלית** ומתעד **44 מקרי בדיקה**. לכל מקרה מופיעים מזהה בדיקה, שלבים, נתוני בדיקה, תוצאה צפויה, רמת חומרה ושדות למילוי תוצאה בפועל וסטטוס.

המסמך מתאר **מה צריך לבדוק**, ולא מעיד שכל הבדיקות עברו בהצלחה.

### ⚠️ מגבלת CAPTCHA — התחברות והרשמה

באתר קיימת הגנת **CAPTCHA / Anti-Bot** בטופסי ההתחברות וההרשמה. לכן, בדיקות אוטומטיות ששולחות טפסים אלה **עלולות להיחסם או להיכשל**, גם אם קוד האוטומציה תקין.

המגבלה משפיעה בעיקר על בדיקות Login, Registration ובדיקות E2E שמחייבות התחברות. בדיקות שרק פותחות את מסכי ההתחברות או איפוס הסיסמה עשויות לפעול כרגיל.

**הפרויקט אינו עוקף CAPTCHA.** כישלון בבדיקת התחברות או הרשמה לא מעיד בהכרח על תקלה באתר.

### ▶️ איך מריצים את הבדיקות?

**1. מתקינים את הספריות**

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

הגדרות הדפדפן משתמשות ב־Google Chrome (`channel="chrome"`), ולכן צריך להתקין Chrome במחשב.

**2. מוודאים את הגדרות `pytest.ini`**

שמות קובצי הבדיקות הם למשל `cart_001.py`, ולכן צריך להגדיר ל־Pytest כיצד לזהות אותם:

```ini
[pytest]
testpaths = tests
python_files = *_001.py *_002.py *_003.py *_004.py
python_classes = Test*
python_functions = test_*
addopts = --alluredir=allure-results
```

**3. מריצים בדיקות**

```bash
# הרצת כל הבדיקות
python -m pytest tests/ -v

# הרצת קובץ אחד
python -m pytest tests/cart_page_tests/cart_001.py -v

# בדיקת זיהוי הטסטים בלי להריץ אותם
python -m pytest --collect-only -q
```

**4. פותחים דוח Allure**

```bash
allure serve allure-results
```

יש להתקין בנפרד את Allure Commandline. צילומי מסך של בדיקות שנכשלו יופיעו בדוח אם הוגדר לכך Hook ב־`conftest.py`.

### 🏗️ איך התשתית בנויה?

- **BasePage** — פעולות משותפות כמו לחיצה, הקלדה וקבלת טקסט.
- **Page Objects** — פעולות ייחודיות לכל עמוד באתר.
- **BaseTest** — גישה לאובייקטים של הדפים מתוך הטסטים.
- **conftest.py** — פתיחת דפדפן וניהול Fixtures.
- **קובצי בדיקות** — שלבים ו־Assertions לאימות תוצאות.

### 🎯 מטרת הפרויקט

זהו פרויקט לימודי ופרויקט פורטפוליו שמציג עבודה מעשית ב־**אוטומציה ל־Web, בדיקות פונקציונליות, בדיקות E2E, בדיקות מבוססות נתונים, תיעוד STD ודוחות Allure**.

[⬆️ חזרה לבחירת שפה](#top)

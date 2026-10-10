<a id="top"></a>

# 🛒 Madison Island — Test Automation

**Python · Playwright · Pytest · Page Object Model (POM) · Allure**  
**44 Test Cases · 15 Test Files · Functional & E2E Testing**

🌐 **Language / שפה:** [English](#english) · [עברית](#hebrew)

---

## 📌 Project Resources | קישורים חשובים

> [!IMPORTANT]
> **📋 [OPEN THE STD — TEST CASE DOCUMENTATION](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit)**  
> 44 documented test cases, including steps, test data, expected results, and severity. Available in English and Hebrew.
>
> **📈 [OPEN THE LIVE ALLURE TEST REPORT](https://moriel-ribak.github.io/Madison-Island-Test-Automation/)**  
> Published automation results, execution steps, and failure information on GitHub Pages.

---

<a id="english"></a>
## 🇬🇧 English

### Overview

An automation testing project for the **[Madison Island](https://madison-island.com/)** e-commerce website, built with **Python, Playwright, and Pytest**.

The framework follows the **Page Object Model (POM)** pattern to separate browser interactions from test logic. It includes **44 test cases across 15 test files**, covering core shopping flows, negative scenarios, and data-driven tests.

### Tech Stack

| Technology | Purpose |
| --- | --- |
| **Python** | Test automation and supporting logic |
| **Playwright** | Browser interaction and UI assertions |
| **Pytest** | Test execution, fixtures, and parametrization |
| **Page Object Model** | Reusable, maintainable page-level actions |
| **Allure** | Execution reports and test steps; screenshots when configured |
| **Google Sheets (STD)** | Test cases, expected results, and test documentation |
| **GitHub Actions** | Automated execution and report publishing workflow |

### Test Coverage

| Area | Main scenarios |
| --- | --- |
| **Home & Header** | Homepage content, collections, slideshow, and navigation |
| **Catalog** | Product listing, pagination, and price sorting |
| **Product Details** | Product title, price, size, color, and cart details |
| **Shopping Cart** | Empty cart, adding products, and quantities |
| **Search** | Existing and non-existing products |
| **Login & Registration** | Form validation and password reset navigation (see CAPTCHA note) |
| **E2E** | Product selection through cart flows |

Some tests use **`pytest.mark.parametrize`** to run the same scenario against multiple data sets.

### Framework Structure

```text
Madison-Island-Test-Automation/
├── components/           # Shared UI components
├── pages/                # Page objects and BasePage
├── tests/                # Tests organized by feature
├── util/                 # Test data and helpers
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

**How the pieces fit together:** `BasePage` holds common browser actions; Page Objects define page-specific actions; `BaseTest` exposes page objects; `conftest.py` manages browser setup and fixtures; and test files contain assertions.

### Run Locally

**1. Install dependencies and the browser:**

```bash
python -m pip install -r requirements.txt
python -m playwright install chrome
```

The current browser setup uses **Google Chrome** (`channel="chrome"`). If you change the code to use Playwright's bundled Chromium instead, install it with `python -m playwright install chromium`.

**2. Run the tests:**

```bash
# Run the full suite
python -m pytest tests/ -v

# Run one test file
python -m pytest tests/cart_page_tests/cart_001.py -v

# Verify test discovery without running tests
python -m pytest --collect-only -q
```

If Pytest does not discover files such as `cart_001.py`, check the `python_files` patterns in `pytest.ini`.

**3. View an Allure report locally (optional):**

```bash
python -m pytest tests/ --alluredir=allure-results
allure serve allure-results
```

The **Allure Commandline** must be installed separately to use `allure serve`.

### Documentation & CI

- **[STD — Software Test Description](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit):** Bilingual documentation of 44 test cases, with IDs, steps, test data, expected results, severity, and fields for actual results/status. The STD describes the intended checks; it does **not** mean all cases passed.
- **[Live Allure report](https://moriel-ribak.github.io/Madison-Island-Test-Automation/):** Published test outcomes and execution details. Its content reflects the latest successfully published report.
- **GitHub Actions:** The repository includes a workflow to run Pytest and publish Allure results to GitHub Pages. The workflow's triggers are configured in `.github/workflows/`.

### Known Limitation: CAPTCHA

> [!WARNING]
> The website uses **CAPTCHA / anti-bot protection** on login and registration. Automated form submissions may be blocked even when the test code is correct. This project **does not bypass CAPTCHA**, so a failed login or registration scenario does not necessarily indicate a product defect.

### Project Purpose

This portfolio project demonstrates **web automation, reusable test architecture, functional and E2E scenarios, data-driven testing, STD documentation, and reporting**.

[↑ Back to top](#top) · [🇮🇱 עברית](#hebrew)

---

<a id="hebrew"></a>
## 🇮🇱 עברית

### על הפרויקט

פרויקט אוטומציה לבדיקת אתר המסחר **[Madison Island](https://madison-island.com/)**, שפותח באמצעות **Python, Playwright ו־Pytest**.

התשתית מבוססת על **Page Object Model (POM)**, שמפריד בין פעולות באתר לבין הלוגיקה של הבדיקות. הפרויקט כולל **44 מקרי בדיקה ב־15 קובצי בדיקות**, ובהם בדיקות פונקציונליות, תרחישים שליליים ובדיקות עם נתונים משתנים.

### טכנולוגיות וכלים

| טכנולוגיה | שימוש |
| --- | --- |
| **Python** | פיתוח הבדיקות והלוגיקה התומכת |
| **Playwright** | פעולות בדפדפן ואימותי UI |
| **Pytest** | הרצה, Fixtures ו־Parametrize |
| **Page Object Model** | הפרדת הפעולות לפי דפי האתר ושימוש חוזר בקוד |
| **Allure** | דוחות הרצה ושלבי בדיקה; צילומי מסך אם הוגדרו |
| **Google Sheets / STD** | תיעוד מקרי בדיקה ותוצאות צפויות |
| **GitHub Actions** | הרצת אוטומציה ופרסום דוחות |

### כיסוי הבדיקות

| אזור | תרחישים מרכזיים |
| --- | --- |
| **Home & Header** | תוכן דף הבית, קולקציות, מצגת תמונות וניווט |
| **Catalog** | מוצרים, מעבר בין עמודים ומיון לפי מחיר |
| **Product** | שם, מחיר, מידה, צבע ופרטי המוצר בעגלה |
| **Cart** | עגלה ריקה, הוספת מוצרים וכמויות |
| **Search** | חיפוש מוצר קיים או לא קיים |
| **Login & Registration** | בדיקות טפסים וניווט לאיפוס סיסמה (ראו מגבלת CAPTCHA) |
| **E2E** | תהליכים מבחירת מוצר ועד לעגלת הקניות |

חלק מהבדיקות משתמשות ב־**`pytest.mark.parametrize`** כדי להריץ תרחיש אחד עם כמה מערכי נתונים.

### מבנה התשתית

```text
Madison-Island-Test-Automation/
├── components/           # רכיבים משותפים
├── pages/                # Page Objects ו-BasePage
├── tests/                # בדיקות לפי אזור באתר
├── util/                 # נתוני בדיקה וכלי עזר
├── pytest.ini            # הגדרות Pytest
├── requirements.txt      # ספריות הפרויקט
└── README.md             # תיעוד
```

**חלוקת האחריות:** `BasePage` מכיל פעולות משותפות; ה־Page Objects מכילים פעולות לכל עמוד; `BaseTest` מנגיש את האובייקטים; `conftest.py` אחראי על Fixtures והקמת הדפדפן; וקובצי הבדיקה מכילים את התרחישים וה־Assertions.

### הרצה מקומית

**1. מתקינים ספריות ואת הדפדפן:**

```bash
python -m pip install -r requirements.txt
python -m playwright install chrome
```

ההגדרה הנוכחית משתמשת ב־**Google Chrome** (`channel="chrome"`). אם משנים את הקוד להשתמש ב־Chromium של Playwright, יש להריץ `python -m playwright install chromium`.

**2. מריצים בדיקות:**

```bash
# כל הבדיקות
python -m pytest tests/ -v

# קובץ בדיקה בודד
python -m pytest tests/cart_page_tests/cart_001.py -v

# בדיקת זיהוי הטסטים ללא הרצה
python -m pytest --collect-only -q
```

אם Pytest לא מזהה קבצים כגון `cart_001.py`, יש לבדוק את הגדרת `python_files` בקובץ `pytest.ini`.

**3. מפיקים דוח Allure מקומי (אופציונלי):**

```bash
python -m pytest tests/ --alluredir=allure-results
allure serve allure-results
```

לפקודה `allure serve` נדרשת התקנה נפרדת של **Allure Commandline**.

### מסמכי בדיקה ודוחות

- **📋 [STD — מסמך תסריטי הבדיקה](https://docs.google.com/spreadsheets/d/1tyiiqwEpemVRStThYWVBv-qlzWfjO6tPZAw8LPBS0RA/edit):** מסמך בעברית ובאנגלית המכיל 44 מקרי בדיקה עם מזהה, שלבים, נתונים, תוצאה צפויה, חומרה ושדות לתוצאה בפועל וסטטוס. המסמך מתאר **מה אמורים לבדוק**, ולא מעיד שכל הבדיקות עברו.
- **📈 [דוח Allure לצפייה](https://moriel-ribak.github.io/Madison-Island-Test-Automation/):** תוצאות ההרצות ושלבי הבדיקה, בהתאם לדוח האחרון שפורסם בהצלחה.
- **GitHub Actions:** תהליך להרצת Pytest ולפרסום הדוח ב־GitHub Pages. הגדרת זמני ההפעלה נמצאת ב־`.github/workflows/`.

### מגבלה ידועה: CAPTCHA

> [!WARNING]
> באתר קיימת הגנת **CAPTCHA / Anti-Bot** בטופסי ההתחברות וההרשמה. שליחה אוטומטית של הטפסים עלולה להיחסם גם כשהקוד תקין. הפרויקט **אינו עוקף CAPTCHA**, ולכן כישלון בתרחיש התחברות או הרשמה לא בהכרח מעיד על תקלה באתר.

### מטרת הפרויקט

הפרויקט מיועד להציג בתיק עבודות ניסיון מעשי ב־**בדיקות Web אוטומטיות, תשתית מבוססת POM, תרחישי Functional ו־E2E, בדיקות מבוססות נתונים, תיעוד STD ודוחות Allure**.

[↑ חזרה לראש העמוד](#top) · [🇬🇧 English](#english)

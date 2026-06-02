# פרויקט "מערכת ניהול כטח אדם יחידתי"

## מבנה הפרויקט:
```text
project/
│
├── main.py              # Endpoint server FastAPI
├── logger_config.py     # Create logger configuration
├── soldiers.json        # Database storage (JSON)
├── system.log           # Output log file
├── requirements.txt     # External libraries
├── readme.md            # Project documentation
│
└── utils/               # Internal utilities folder
    ├── io.py            # JSON read/write operations
    └── helper.py        # Business logic & helper 
```

# מבנה הנתונים של החילים:
המידע של החילים נשמרים בקובץ json כרשימה של מילונים
```text
[
    {
        "id": 1,
        "name": "Shlomi Kaufman",
        "email": "shlomikaufman91@gmail.com"
    }
]
```

להשים לב כי ID הוא דינמי, כלומר הוא לוקח את ID הבא מהכי גדול

---

## טבלת CURD

| HTTP Method | Function Name | Endpoint Path | Request Parameters / Body | Response Body | HTTP Status Code |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `get_all_soldiers` | `/api/soldiers` | NONE | `[ { "id": int, "full_name": str, "personal_number": str, "rank": str, "role": str, "unit": str, "status": str } ]` | `200 OK OR 404` |
| **GET** | `get_soldier` | `/api/soldiers/{id}` | `id`: `int` (Path) | `{ "id": int, "full_name": str, "personal_number": str, "rank": str, "role": str, "unit": str, "status": str }` | `200 OK OR 404` |
| **POST** | `create_soldier` | `/api/soldiers` | `soldier`: `dict` (Body) | `{"message": "Soldier created successfully"}` | `201 Created OR 404` |
| **PUT** | `update_soldier` | `/api/soldiers/{id}` | `id`: `int` (Path),<br>`new_data`: `dict` (Body) | `{"message": "Soldier {id} updated successfully"}` | `200 OK OR 404` |
| **DELETE** | `delete_soldier` | `/api/soldiers/{id}` | `id`: `int` (Path) | `{"message": "Soldier {id} deleted successfully"}` | `200 OK OR 404 |

---

# בעיות שנתקלתי בהם במהלך הבנייה
1. שגיאה ב data לחיילים כלומר פיספסתי פסיק אחרי ערך במילון
2. אני כתבתי שהפונקציה מקבלת פרמטר למציאת חייל לפי ID, בצורה id_ ושכחתי לעשות בניתוב גם id_
3. ניהול חריגות, כלומר הפונקציה update_soldier זרקה שגיאה keyError כי שכחתי לעשות חזרה אחרי מציאת ID


## הרצת התוכנית:
צריך להתקין ספריות חיצוניות, בשביל זה צריך להכניס את הפקודה הבאה ב git bash:
```text
pip install -r requirements.txt
```

לאחר מכן כדי להריץ את התכנית צריך להכניס את הפקודה:
```text
uvicorn main:app
```
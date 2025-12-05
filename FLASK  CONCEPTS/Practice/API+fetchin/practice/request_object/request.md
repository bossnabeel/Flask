Ahhh bro 😎 perfect, ab tu Flask me **`request` object** samajh le — ye **client se data access karne ka tarika** hai (GET, POST, PUT, DELETE sab me).

---

## 🔹 `request` object basics

Flask me ye import hota hai:

```python
from flask import request
```

`request` object ke andar bohot saare useful attributes aur methods hain:

---

### 1️⃣ `request.args`

* GET request me **query parameters** access karne ke liye
* Example: `/search?query=python`

```python
@app.route("/search")
def search():
    q = request.args.get("query")
    return f"Search query: {q}"
```

---

### 2️⃣ `request.form`

* POST request me **form-data** access karne ke liye (HTML forms)

```python
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    return f"Username: {username}, Password: {password}"
```

---

### 3️⃣ `request.json`

* POST/PUT request me **JSON data** access karne ke liye
* REST APIs me mostly ye use hota hai

```python
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    return f"Created user: {username}"
```

---

### 4️⃣ `request.data`

* Raw request body access karne ke liye (binary/other formats)

```python
@app.route("/raw", methods=["POST"])
def raw():
    raw_data = request.data
    return f"Raw length: {len(raw_data)}"
```

---

### 5️⃣ `request.method`

* Kaunsa HTTP method call hua check karne ke liye

```python
@app.route("/check", methods=["GET", "POST"])
def check():
    return f"Request method: {request.method}"
```

---

### 6️⃣ `request.headers`

* Client ke headers access karne ke liye

```python
@app.route("/headers")
def headers():
    user_agent = request.headers.get("User-Agent")
    return f"User Agent: {user_agent}"
```

---

### 🔹 Summary Table

| Attribute | Use case             |
| --------- | -------------------- |
| `args`    | GET query parameters |
| `form`    | POST form data       |
| `json`    | JSON payload         |
| `data`    | Raw request body     |
| `method`  | HTTP method          |
| `headers` | Request headers      |

---

Bro, agar tu chaahe mai tujhe **Flask CRUD + request objects ka full example** bana dun, jisme GET, POST, PUT, DELETE + request.json + args sab use ho, taake tu **real-world backend practice** start kar sake.

Banau?

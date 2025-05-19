# 🩸 OneDrop Portal

A **Streamlit-based Admin Dashboard** for the [OneDrop](https://onedrops.online) project — a blood donation platform to manage **donors**, **requests**, and **community reports**.

This portal is designed to be used by admins or moderators to view data, generate insights, moderate users, and monitor activities within the OneDrop ecosystem.


---

## 🚀 Features

### 🔍 Dashboard
- Welcome section and metrics overview.
- Total number of blood donors and blood requests.
- Blood group distribution pie chart using Plotly.
- Donor availability bar chart (Available vs Not Available).

### 💉 Donor Management
- Fetch and display all blood donors from the backend.
- Analyze distribution of blood groups.
- Monitor availability status for active/inactive donors.

### 🆘 Blood Request Overview
- Fetch and display all blood requests from the backend.
- Metrics for total requests.

### ⚠️ Report Management (Moderation)
- View all user-submitted reports.
- Displays:
  - Reported user’s name and number
  - Reason & description
  - Screenshot (if attached)
  - Timestamp (formatted as `dd Month yyyy`)
  - Report status (`Pending`, `Resolved`, etc.)
- Admin controls:
  - Change status using dropdown.
  - Delete report after confirmation dialog.

---

## 🧱 Tech Stack

| Layer               | Technology                         |
|--------------------|-------------------------------------|
| Frontend (Dashboard) | 🧪 [Streamlit](https://streamlit.io) |
| Charts & Graphs    | 📊 [Plotly](https://plotly.com/python/) |
| Backend API        | ⚙️ Ktor / REST |
| Data Storage       | 🗃️ MongoDB                         |
| Models             | 🐍 Pydantic models (`report_model.py`) |

---

## 📦 Folder Structure

```
.
├── app.py                    # Main entry point
├── api.py                   # API interaction layer
├── app_pages/
│   └── banner.png           # Banner
├── app_pages/
│   └── home.py              # Home Page
│   └── BloodDonor.py        # Blood Donor Page
│   └── BloodRequests.py     # Blood Request Page
│   └── Report.py            # Reports moderation page
├── models/
│   └── BloodGroup.py        # Blood Groups List
│   └── BloodRequestModel.py # BloodRequest model with Pydantic Basemodel
│   └── donor.py             # Donors model with Pydantic Basemodel
│   └── report_model.py      # Report model with Pydantic Basemodel
│   └── NotificationScpe.py  # Notification model with enums
├── utils/
│   └── utils.py             # Common utilities like confirm dialog
├── .venv/                   # Virtual environment
└── README.md
```

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/onedrop-portal.git
cd onedrop-portal
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set API Base URL

Inside `api.py`, configure your backend API base URL:

```python
BASE_URL = "https://api.onedrops.online"
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🛠️ Utilities & Models

### ReportModel (`models/report_model.py`)

A Pydantic model representing a user report with:

- `reportId`
- `reportedName`
- `reportedMobileNumber`
- `reason`, `description`, `timestamp`
- `screenshot` (optional)
- `reportStatus` enum (`Pending`, `Resolved`, etc.)

### Confirm Dialog (`utils/utils.py`)

Custom reusable confirmation dialog using Streamlit session state to confirm before destructive actions (like delete).

---

## 📅 Timestamp Formatting

Timestamps like:

```json
"2025-05-06T15:04:21.735Z"
```

...are parsed and displayed in a readable format using:

```python
from datetime import datetime

dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
formatted_dt = dt.strftime("%d %B %Y")  # e.g. "06 May 2025"
```

---

## 🧹 Error Handling

The project safely handles cases where:
- The API returns empty data or no JSON
- `requests.exceptions.JSONDecodeError` is thrown
- Backend server is unreachable

Implemented via:

```python
if response.status_code == 204 or not response.text.strip():
    return []
```

---

## 📈 Visualizations

### Blood Group Pie Chart

```python
fig = px.pie(names=list(bg_counts.keys()), values=list(bg_counts.values()), title="Blood Group Distribution")
```

### Donor Availability Bar Chart

```python
fig = px.bar(
    names=["Available", "Not Available"],
    values=[available_count, not_available_count],
    title="Donor Availability"
)
```

---

## ✅ To-Do / Future Improvements

- [ ] Add search and filters for reports.
- [ ] Allow report download/export.
- [ ] Implement pagination for large datasets.
- [ ] Role-based access control (admin vs viewer).
- [ ] Email notification integration for new reports.
- [ ] Add ability to manually add donors or requests.

---

## 👤 Author

**Hazrat Ummar Shaikh**  
Discord & Android Dev • Stream Overlay Specialist • Backend Engineer  
📍 India  
🌐 [onedrops.online](https://onedrops.online)

---

## 📝 License

This project is for educational and personal use only. Commercial use is prohibited without permission.
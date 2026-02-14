# Global NEXUS - Medical Data Portal

A Flask-based medical data management system for storing, viewing, and editing patient records with admin authentication.

## Features

- **Data Entry Form**: Easy-to-use form for entering patient medical information
- **Admin Dashboard**: Secure login system to view all patient records
- **Edit Records**: Admin can edit existing patient records
- **Database Storage**: SQLite database for persistent data storage
- **Responsive Design**: Bootstrap-based responsive UI

## Project Structure

```
medical-portal/
├── app.py                 # Main Flask application
├── medical.db            # SQLite database (auto-created)
├── templates/
│   ├── index.html        # Patient data entry form
│   ├── login.html        # Admin login page
│   ├── view.html         # View all medical records
│   └── edit.html         # Edit patient record
└── README.md             # This file
```

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/jasonjose007/global-nexus.git
cd global-nexus
```

2. **Create Virtual Environment**
```bash
python -m venv .venv
```

3. **Activate Virtual Environment**
   - On Windows:
   ```bash
   .venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Install Dependencies**
```bash
pip install flask
```

## Usage

1. **Start the Application**
```bash
python app.py
```

2. **Access the Application**
   - Open your browser and go to: `http://127.0.0.1:5000`

3. **Submit Patient Data**
   - Fill out the form with patient information and click "Submit Data"
   - Data will be saved to the database

4. **View Records (Admin)**
   - Click "Admin → View All Records"
   - Enter password: `admin2026` (change this in production!)
   - View all stored patient records

5. **Edit Records**
   - From the records page, click the "Edit" button on any patient record
   - Modify the information and click "Save Changes"

## Database Schema

The `patients` table contains the following fields:
- `id` - Patient ID (auto-incremented)
- `name` - Patient's full name
- `age` - Patient's age
- `gender` - Patient's gender
- `weight` - Patient's weight in kg
- `height` - Patient's height in cm
- `conditions` - Medical conditions/illnesses
- `allergies` - Known allergies
- `medications` - Current medications
- `entry_date` - Date/time of entry

## Security Notes

⚠️ **Important**: This is a development application. For production use:
- Change the default admin password in `app.py` line 76
- Use a production WSGI server (e.g., Gunicorn)
- Enable HTTPS
- Add proper authentication and session management
- Store sensitive data securely

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite3
- **Frontend**: HTML, CSS, Bootstrap 5
- **Templating**: Jinja2

## License

This project is open source and available under the MIT License.

## Author

Created by Jason Jose

## Support

For issues or questions, please visit: https://github.com/jasonjose007/global-nexus

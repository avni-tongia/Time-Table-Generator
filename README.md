# Time Table Generator
Here is a sample README file for your **Time Table Generator** application:

---

# Time Table Generator

A Python-based application designed to simplify and automate the process of creating, managing, and viewing time tables for educational institutions. Built using `tkinter` for GUI and `MySQL` for database management, this program offers a user-friendly interface and robust functionality.

---

## Features

- **User Authentication**: Secure sign-up and login for users.
- **Customizable Input**: Input details for subjects, classes, teachers, and school timing.
- **Time Slot Management**: Automated slot creation based on user-defined criteria.
- **Data Persistence**: Stores user information and configurations using MySQL and Pickle.
- **Interactive GUI**: Easy-to-navigate interface built with `tkinter`.
- **Multi-layer Functionality**: Handle class and teacher assignments, linking, and time table visualization.

---

## Prerequisites

Before running the application, ensure the following:

- Python 3.x installed on your system.
- Required Python libraries: `tkinter`, `mysql-connector-python`, and `datetime`.
- A MySQL server running on `localhost`.

---

## Installation

1. Clone the repository or download the project files.
2. Install dependencies using pip:
   ```bash
   pip install mysql-connector-python
   ```
3. Configure your MySQL credentials in the application when prompted.
4. Run the application:
   ```bash
   python Time_Table_Generator.py
   ```

---

## How to Use

1. **Launch the Program**: Run the script in your Python environment.
2. **Sign Up/Login**: Use the GUI to sign up or log in with your credentials.
3. **Configure Inputs**: Define:
   - School timings and lecture durations.
   - Classes and sections.
   - Subjects and teacher assignments.
4. **View or Update Time Table**: Generate, view, or modify the time table as needed.

---

## File Structure

- **Time_Table_Generator.py**: Main application file.
- **user_info.txt**: Serialized user data for authentication.
- **School_slot_timings.txt**: Pickled slot configuration for the institution.
- **School_Days.txt**: Serialized school days and organizational data.

---

## Authors

- Avni Tongia
- Rupal Shah

---

### Notes

- Ensure all dependencies are properly installed before running the program.
- For troubleshooting, refer to the log or error messages displayed during runtime.

Let me know if you'd like to customize further! 

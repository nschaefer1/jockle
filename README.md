# Jockle

### Project Purpose

**Jockle** is a Windows desktop application designed to assist with inventory management for *Dungeons & Dragons: Pathfinder* campaigns.  

The project is evolving and new features will be added over time, but the initial **v1.0.0 release** is focused on providing a simple yet functional inventory tool for players. The Player vs. DM option will appear in the interface as a placeholder for future development, but DM-specific functionality will not be available until later versions.


**Planned Features for v1.0**
- **Role Selection**: Choose whether you’re a Player or a DM.
- **Player Selection**: Choose a specific player that you are editing.
- **Startup Screen**: Begin at a campaign selection screen.
- **Campaign Management**: Create and select campaigns.
- **Character Management**: Create and select characters.
- **Inventory Management**: View, add, and remove items from a character’s inventory.
- **Local Database**: Store campaign and character data in a local relational database.

### Tech Stack

- **Frontend:** HTML & CSS (user interface)
- **Middleware:** JavaScript (handling interactions between UI and API)
- **API**: Python (application logic)
- **Entry point**: Python (app launch mechanism)
- **Database**: SQLite (local relational data storage)
- **Wrapper**: PyWebview (connects Python backend with HTML/CSS/JS frontend in a native desktop window)

### DEVELOPER ONLY: Getting Started

**Prerequisites**
- **Python 3.11** (recommended)
- **pip** (Python package manager)
- **Windows OS** (Jockle is currently Windows-only)

**Installation**  
1. Clone the repository:
```
git clone [this repository link]
cd [path to cloned location]
```
2. Create and activate a virtual environment (recommended)
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. Install dependencies:
```
pip install -r requirements.txt
```

**Running the App**  
1. Start the application via the terminal (the window will open with the startup screen)
```
python main.py
```

### Project Structure

```
Jockle/
├── backend/                # Python API and Backend Logic
├── frontend/               # HTML/CSS/JS and assets for the UI
├── sql/                    # SQL scripts/schema definitions
├── utils/                  # Utility/helper Python Modules
├── app_context.py          # Global Application Instance
├── main.py                 # Entry point of the application
├── CHANGELOG.md            # Project changelog
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

*Additional directories like `build/`, `dist/`, `secret/` and `database.db` are generated locally or ignored via `.gitignore` and are not included in the repository*

### PyWebview Deployment

Jockle is a Python + PyWewbview application. To distribute it as a standalone executable for Windows, you can use *PyInstaller*.

**Build Steps**
1. Install PyInstaller (if not already installed):
```
pip install pyinstaller
```
2. From the project root, run:
```
pyinstaller --noconfirm --onefile --windowed main.py
```
- `--onefile` bundles everything into a single `.exe`
- `--windowed` runs without opening a terminal window

3. The generated executable will be in the `dist/` folder

**Notes**
- The `assets/`, `frontend/`, and `sql/` folders may need to be included explicitly in the build. You can configure this in a `.spec` file if required.
- If you're using local SQLite (`database.db`), ensure the app knows where to create or access this file on first run.
- For more advanced distribution (e.g., installers), consider using tools like **Inno Setup** or **NSIS** once the `.exe` is stable.
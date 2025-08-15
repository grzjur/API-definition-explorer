# API Definition Explorer

A graphical application for exploring and analyzing OpenAPI/Swagger API definitions. The application provides easy browsing of API endpoints and detailed information about their structure.

## Features

- 🌐 **OpenAPI Definition Fetching** - directly from URL
- 📋 **Endpoint Listing** - clear display of all available endpoints with HTTP methods
- 🔍 **Detailed Definitions** - display complete endpoint definitions in JSON format
- 🏗️ **Automatic Schema Expansion** - collecting and displaying related data schemas
- 🖥️ **Intuitive Interface** - graphical user interface based on PySide6


## Installation

### Requirements

- Python 3.x
- Conda (recommended)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd API-definition-explorer
   ```

2. **Create virtual environment:**
   ```bash
   # For fish shell users:
   chmod +x venv.sh
   ./venv.sh
   
   # Or manually:
   conda create -p ./.venv python -c conda-forge
   conda activate ./.venv
   pip install -r requirements.txt
   ```

3. **Activate environment:**
   ```bash
   conda activate ./.venv
   ```

## Usage

### Running the Application

```bash
python src/main.py
```


## License

This project is open source and available under the [MIT License](LICENSE).

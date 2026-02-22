#!/usr/bin/env python3
"""
Run the ResQ Sentinel backend (with frontend UI served at /app/).
From the project root, run: python run_backend_with_ui.py

Then open http://localhost:8000 in your browser (redirects to /app/).
"""
import os
import sys
from pathlib import Path

# Project root = directory containing this script
ROOT = Path(__file__).resolve().parent
BACKEND_DIR = ROOT / "Rapid-Post-Disaster-Infrastructure-Damage-Detection-main" / "backend"
FRONTEND_DIR = ROOT / "rapid-damage-detection-ui-integration-main" / "frontend-ui"

if not BACKEND_DIR.is_dir():
    print("Backend not found at", BACKEND_DIR)
    sys.exit(1)

# So the backend can find the frontend when not using FRONTEND_DIR env
if FRONTEND_DIR.is_dir():
    os.environ["FRONTEND_DIR"] = str(FRONTEND_DIR)

os.chdir(BACKEND_DIR)
sys.path.insert(0, str(BACKEND_DIR))

import uvicorn
uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

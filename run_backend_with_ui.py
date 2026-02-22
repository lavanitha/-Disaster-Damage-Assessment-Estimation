#!/usr/bin/env python3
"""
Run the ResQ Sentinel backend (with frontend UI served at /app/).
From this folder, run: python run_backend_with_ui.py
Then open http://localhost:8000 in your browser.
"""
import os
import sys
from pathlib import Path

# This script: at workspace root OR inside rapid-damage-detection-ui-integration-main
ROOT = Path(__file__).resolve().parent
# Backend can be at ROOT/.../backend or ROOT/rapid-damage-detection-ui-integration-main/.../backend
BACKEND_DIR = ROOT / "Rapid-Post-Disaster-Infrastructure-Damage-Detection-main" / "backend"
if not BACKEND_DIR.is_dir():
    BACKEND_DIR = ROOT / "rapid-damage-detection-ui-integration-main" / "Rapid-Post-Disaster-Infrastructure-Damage-Detection-main" / "backend"
FRONTEND_DIR = ROOT / "frontend-ui"
if not FRONTEND_DIR.is_dir():
    FRONTEND_DIR = ROOT / "rapid-damage-detection-ui-integration-main" / "frontend-ui"

if not BACKEND_DIR.is_dir():
    print("Backend not found at", BACKEND_DIR)
    sys.exit(1)

if FRONTEND_DIR.is_dir():
    os.environ["FRONTEND_DIR"] = str(FRONTEND_DIR)

os.chdir(BACKEND_DIR)
sys.path.insert(0, str(BACKEND_DIR))

import uvicorn
uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

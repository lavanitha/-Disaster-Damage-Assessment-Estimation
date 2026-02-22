# ResQ Sentinel - Frontend UI

Standalone frontend interface for the ResQ Sentinel AI Damage Detection System.

## 🎨 Design

**Neumorphic Desktop Console** - High-tech, scientific-tool aesthetic with soft shadows and minimal colors.

## 🚀 Quick Start

### Prerequisites

- FastAPI backend running at `http://localhost:8000`
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Running the Frontend (with Backend)

**Option A – One server (recommended)**  
From the project root (parent of `frontend-ui` and `Rapid-Post-Disaster-Infrastructure-Damage-Detection-main`):

```bash
python run_backend_with_ui.py
```

Then open **http://localhost:8000** in your browser. You’ll be redirected to the UI at `/app/`. The same server serves both the API and the frontend.

**Option B – Frontend only (backend already running)**  
1. Open `index.html` in your browser, or run a local server:
   ```bash
   cd frontend-ui
   python -m http.server 8080
   # Then open http://localhost:8080
   ```
2. Set the backend URL in the sidebar to `http://localhost:8000` if needed.

**Option C – Backend only (serve UI from backend)**  
From the backend directory, set the frontend path and run:

```bash
cd Rapid-Post-Disaster-Infrastructure-Damage-Detection-main/backend
set FRONTEND_DIR=C:\path\to\rapid-damage-detection-ui-integration-main\frontend-ui
uvicorn main:app --host 0.0.0.0 --port 8000
```

Then open http://localhost:8000 (redirects to `/app/`).

3. **Configure Backend URL** (if different from default)
   - Use the sidebar input to set your backend URL
   - Default: `http://localhost:8000`

3. **Verify Connection**
   - Check the health indicator in the top-right
   - Should show "Health: Online" when backend is running

## 📋 Features

### Change Detection
- Upload pre/post disaster satellite images
- Run ChangeFormerV6 inference
- View damage percentage, confidence, and heatmap mask

### Single Image Segmentation
- Upload a single satellite image
- Get damage segmentation with zone analysis
- View building/infrastructure/debris breakdown

### Damage Estimation
- Comprehensive damage assessment
- Zone-based analysis (damaged vs safe zones)
- Severity classification

## 🔌 API Integration

The frontend calls these backend endpoints:

- `POST /analyze/change-detection` - Pre/post comparison
- `POST /analyze/segmentation` - Single image segmentation
- `POST /analyze/damage-estimation` - Full damage assessment
- `GET /health` - Backend health check

All responses are rendered **exactly as returned** by the backend. No mock data or client-side calculations.

## 📁 File Structure

```
frontend-ui/
├── index.html              # Main HTML structure
├── styles/
│   └── neumorphism.css    # Neumorphic design system
├── js/
│   ├── api.js             # Backend API connector
│   ├── upload.js          # File upload handler
│   ├── render.js          # Result renderer
│   └── app.js             # Main orchestrator
└── README.md              # This file
```

## 🎯 Usage Flow

1. **Select Analysis Mode** (sidebar)
   - Change Detection
   - Single Image Segmentation
   - Damage Estimation

2. **Upload Images**
   - Drag & drop or click to browse
   - Images preview immediately

3. **Run Analysis**
   - Click the "Run..." button
   - Loading overlay appears
   - Backend processes images

4. **View Results**
   - Metrics displayed in cards
   - Visualizations rendered from backend
   - All values come directly from API responses

## ⚙️ Configuration

Backend URL is stored in `localStorage` and persists across sessions.

To change:
- Use the sidebar input field
- Click "Set" or press Enter
- Health check runs automatically

## 🐛 Troubleshooting

**"Health: Offline"**
- Ensure backend is running at configured URL
- Check CORS settings if using different ports
- Verify backend `/health` endpoint responds

**Images not uploading**
- Check browser console for errors
- Ensure images are valid image files (JPG, PNG, etc.)
- Check file size limits

**No results displayed**
- Check browser console for API errors
- Verify backend returned valid JSON
- Ensure response format matches expected structure

## 📝 Notes

- **No frameworks** - Pure HTML/CSS/JavaScript
- **No build step** - Open and run
- **No mock data** - All data from backend
- **No calculations** - Only renders backend responses

## 🔒 Backend Requirements

The backend must:
- Accept multipart/form-data for image uploads
- Return JSON with expected fields
- Include base64 image data in responses (for visualizations)
- Handle CORS if frontend served from different origin

---

**Built for ResQ Sentinel AI System**  
*Desktop-style console interface for satellite damage analysis*

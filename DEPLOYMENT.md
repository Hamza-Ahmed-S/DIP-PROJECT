# Bioinformatics Web App - Deployment Guide

## 🚀 Quick Start (Local)

### 1. Install Dependencies

```bash
pip install -r requirements_web.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## ☁️ Deploy to Streamlit Cloud (Free!)

### Prerequisites
- GitHub account
- Your code pushed to GitHub repository

### Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add interactive web app"
   git push origin main
   ```

2. **Visit Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

3. **Deploy**
   - Click "New app"
   - Select your repository: `Hamza-Ahmed-S/DIP-PROJECT`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Your App is Live! 🎉**
   - URL will be: `https://your-app-name.streamlit.app`
   - Share this URL with everyone!

### Configuration

The app uses `requirements_web.txt` for dependencies. Streamlit Cloud will automatically install these.

---

## 🔧 Alternative Deployment Options

### Option 1: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 2: Railway

1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Railway auto-detects Streamlit
4. Deploy!

### Option 3: Render

1. Go to [render.com](https://render.com)
2. New Web Service
3. Connect repository
4. Build command: `pip install -r requirements_web.txt`
5. Start command: `streamlit run app.py --server.port=$PORT`

---

## 📊 Managing Analytics Data

Analytics are stored in `data/analytics.json` (excluded from Git).

### On Streamlit Cloud

Analytics reset when the app restarts. For persistent storage:

1. **Use Streamlit Secrets** (for small data)
2. **Use a database** (Firebase, MongoDB, etc.)
3. **Use cloud storage** (AWS S3, Google Cloud Storage)

### To Clear Local Analytics

```bash
rm data/analytics.json
```

The file will be recreated automatically on next use.

---

## 🐛 Troubleshooting

### App won't start locally
```bash
# Make sure you're in the project directory
cd "d:\Others\VS CODE\DIP PROJECT"

# Install dependencies
pip install -r requirements_web.txt

# Run app
streamlit run app.py
```

### Import errors
Make sure all Python files are in the correct structure:
```
DIP-PROJECT/
├── app.py
├── analytics.py
├── codon_table.py
├── pages/
├── utils/
└── data/
```

### Port already in use
```bash
streamlit run app.py --server.port=8502
```

---

## 📝 Environment Variables

For production, you can set:

```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## 🎯 Next Steps After Deployment

1. Share your app URL!
2. Monitor analytics dashboard
3. Collect user feedback
4. Iterate and improve features

---

**Made with ❤️ for Bioinformatics Education**

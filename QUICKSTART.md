# 🚀 Quick Start Guide - Interactive Web App

## ⚡ Get Started in 2 Minutes!

### Step 1: Install Dependencies (First Time Only)

Open terminal in project directory and run:

```bash
pip install -r requirements_web.txt
```

This installs:
- Streamlit (web framework)
- Plotly (interactive charts)
- Pandas (data handling)

⏱️ Takes about 1-2 minutes

---

### Step 2: Launch the App

```bash
streamlit run app.py
```

✅ The app will automatically open in your browser at `http://localhost:8501`

---

## 🎯 What You Can Do

### Try These Features:

1. **🧪 ATP Hydrolysis Analysis**
   - Adjust tissue concentration sliders
   - See real-time energy calculations
   - Compare results with interactive charts

2. **🧬 DNA & Protein Analysis**
   - Use sample sequences or upload your own
   - View color-coded sequences
   - Get GC content and ORF detection

3. **🔬 Advanced Analysis**
   - 4 powerful tools in one page
   - ORF finder, codon distance, translation
   - Extract hydrophobic fragments

4. **📊 N50 Calculator**
   - Calculate genome assembly quality
   - Upload contig files
   - View cumulative distribution charts

5. **📈 Analytics Dashboard**
   - See live community statistics
   - View usage patterns
   - Read recent feedback

---

## ⭐ Rate Features

After using any tool:
1. Scroll to bottom of page
2. Rate 1-5 stars
3. (Optional) Leave feedback
4. Click "Submit Rating"

Your ratings appear on the **Analytics Dashboard**! 📊

---

## 🌍 Share With Others

### Option 1: Local Network
```bash
streamlit run app.py --server.address=0.0.0.0
```
Others on your network can access via your IP

### Option 2: Deploy Online (FREE!)

See [DEPLOYMENT.md](DEPLOYMENT.md) for:
- Streamlit Cloud (recommended)
- Heroku, Railway, Render

Get a public URL like: `https://your-app.streamlit.app`

---

## 🐛 Troubleshooting

### App won't start?
```bash
# Make sure you're in the right directory
cd "d:\Others\VS CODE\DIP PROJECT"

# Try running with full path
python -m streamlit run app.py
```

### Import errors?
```bash
# Reinstall dependencies
pip install --upgrade -r requirements_web.txt
```

### Port already in use?
```bash
# Use different port
streamlit run app.py --server.port=8502
```

---

## 📝 Tips

- **Refresh** browser to reset analytics (development only)
- **Stop app**: Press `Ctrl+C` in terminal
- **View logs**: Check terminal for debugging info
- **Sample data**: Always available in dropdown menus

---

## 🎓 For Your Presentation

Show these impressive features:

1. **Live Statistics** - Homepage dashboard updates in real-time
2. **Interactive Sliders** - ATP hydrolysis tissue comparison
3. **Color Sequences** - DNA/protein visualizations
4. **Real Charts** - N50 cumulative distribution
5. **Community Analytics** - Engagement tracking

---

## 🎉 You're Ready!

Run `streamlit run app.py` and start exploring!

For public rating collection, deploy to Streamlit Cloud and share the URL.

**Questions?** Check [walkthrough.md](file:///C:/Users/Hp/.gemini/antigravity/brain/e4d1395f-407c-49a3-a799-b1671807c672/walkthrough.md) for detailed documentation.

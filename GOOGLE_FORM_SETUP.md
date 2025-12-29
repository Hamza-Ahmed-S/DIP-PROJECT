# Setting Up Google Form for Exit Feedback

## 📋 Step 1: Create Your Google Form

1. **Go to Google Forms**
   - Visit: https://forms.google.com
   - Click **"+ Blank"** or use a template

2. **Add Your Questions**
   
   **Suggested Questions:**
   - **Overall Rating**: 1-5 stars (Linear scale)
   - **Most Useful Feature**: Multiple choice
     - ATP Hydrolysis Analysis
     - DNA & Protein Analysis
     - Advanced Analysis
     - N50 Calculator
   - **Ease of Use**: 1-5 stars
   - **Suggestions for Improvement**: Long answer
   - **Would you recommend this to others?**: Yes/No
   - **Your Role/Field**: Short answer (optional)

3. **Customize Form Design**
   - Click the palette icon
   - Choose colors matching your app theme (purple #667eea)
   - Add your project title

4. **Get Shareable Link**
   - Click **"Send"** button (top right)
   - Click the **link icon** 
   - Click **"Shorten URL"**
   - Copy the link (e.g., `https://forms.gle/ABC123xyz`)

---

## 🔧 Step 2: Add Form URL to Your App

1. **Open** `app.py` file

2. **Find this line** (around line 28):
   ```python
   const GOOGLE_FORM_URL = "https://forms.gle/YOUR_FORM_ID_HERE";
   ```

3. **Replace** with your actual Google Form URL:
   ```python
   const GOOGLE_FORM_URL = "https://forms.gle/ABC123xyz";
   ```

4. **Save** the file

5. **Refresh** your browser - Streamlit will auto-reload!

---

## 🎯 How It Works

### Two Feedback Triggers:

**1. Exit Intent Modal (Mouse leaving top of page)**
   - Beautiful custom popup appears
   - "Fill Feedback Form" button
   - "Maybe Later" option
   - Auto-closes after 10 seconds

**2. Browser Close Confirmation**
   - Standard browser confirmation dialog
   - Asks user before leaving
   - Opens Google Form in new tab if they click OK

---

## 🧪 Testing the Feature

### Test Exit Intent Modal:
1. Open your app
2. Move mouse cursor to the **very top** of the browser window (like closing the tab)
3. Modal should appear!

### Test Browser Close:
1. Try closing the browser tab/window
2. Browser asks: "Leave site?"
3. If you stay, a confirm dialog appears
4. Clicking OK opens the Google Form

**Note:** Some browsers block the `beforeunload` prompt on certain actions.

---

## 📊 Example Google Form Structure

```
📝 Bioinformatics Toolkit - User Feedback

1. How would you rate your overall experience? *
   ⭐⭐⭐⭐⭐ (1-5 scale)

2. Which feature did you find most useful? *
   ○ ATP Hydrolysis Analysis
   ○ DNA & Protein Analysis  
   ○ Advanced Analysis
   ○ N50 Calculator
   ○ Analytics Dashboard

3. How easy was the app to use? *
   Very Difficult 1-2-3-4-5 Very Easy

4. What could we improve?
   [Long answer text]

5. Would you recommend this tool to others? *
   ○ Yes
   ○ No

6. What's your role/field? (Optional)
   [Short answer]

7. Any additional comments?
   [Long answer text]
```

---

## 🎨 Customization Options

### Change Modal Text:
Edit lines in `app.py`:
```javascript
<h2 style="color: #667eea; margin-bottom: 1rem;">⭐ Wait! Before You Go...</h2>
<p style="margin-bottom: 1.5rem; color: #333; font-size: 1.1rem;">
    Help us improve by sharing your experience! 
    It takes less than 1 minute.
</p>
```

### Change Button Colors:
```javascript
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adjust Modal Trigger Sensitivity:
```javascript
if (e.clientY < 10 && !exitIntentShown) {
    // Change "10" to higher number (e.g., 50) for easier triggering
}
```

---

## 📈 Viewing Responses

1. **Open your Google Form**
2. Click **"Responses"** tab
3. View:
   - Summary charts
   - Individual responses
   - Download as CSV

---

## 💡 Pro Tips

- **Keep form short** (5-7 questions max) for better completion rate
- **Make rating required** but keep text optional
- **Add progress bar** in Google Forms settings
- **Enable email collection** if you want to follow up
- **Test the form yourself** before deploying

---

## ⚠️ Important Notes

- The exit modal only shows **once per session** (won't annoy users)
- Browser close confirmation may be blocked by some browsers (security feature)
- Users can always click "Maybe Later" to skip
- Form opens in **new tab** so they don't lose the app

---

## 🚀 Ready to Deploy!

Once you add your Google Form URL, users will automatically see the feedback prompt when they try to leave your app!

**Your current setup:**
- ✅ Exit intent detection
- ✅ Browser close handling  
- ✅ Beautiful modal design
- ⏳ Waiting for your Google Form URL!

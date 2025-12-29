# 📋 Copy-Paste Questions for Your Google Form

## Form Title
**Bioinformatics Toolkit - User Feedback**

## Form Description
Help us improve the Bioinformatics Toolkit! Your feedback is valuable and takes less than 2 minutes.

---

## Questions to Add (Copy each one):

### Question 1: Overall Rating
**Question:** 
**Type:** Linear scale
**Range:** 1 to 5
**Labels:** 
- 1 = Poor
- 5 = Excellent
**Required:** Yes

---

### Question 2: Most Useful Feature
**Question:** Which feature did you find MOST useful?
**Type:** Multiple choice
**Options:**
- 🧪 ATP Hydrolysis Analysis
- 🧬 DNA & Protein Sequence Analysis
- 🔬 Advanced DNA/Protein Analysis
- 📊 N50 Genome Assembly Calculator
- 📈 Analytics Dashboard
- I didn't use any features
**Required:** Yes

---

### Question 3: Ease of Use
**Question:** How easy was the app to navigate and use?
**Type:** Linear scale
**Range:** 1 to 5
**Labels:**
- 1 = Very Difficult
- 5 = Very Easy
**Required:** Yes

---

### Question 4: Visual Design
**Question:** How would you rate the visual design and user interface?
**Type:** Linear scale
**Range:** 1 to 5
**Labels:**
- 1 = Poor
- 5 = Excellent
**Required:** No

---

### Question 5: Features Used
**Question:** Which features did you try? (Select all that apply)
**Type:** Checkboxes
**Options:**
- ATP Hydrolysis thermodynamic calculations
- DNA sequence analysis (GC content, ORF)
- Protein sequence analysis
- Advanced ORF detection
- DNA to protein translation
- Hydrophobic fragment extraction
- N50 assembly statistics
- Analytics dashboard
- None, just browsed
**Required:** No

---

### Question 6: Improvements
**Question:** What could we improve or add to make this tool better?
**Type:** Paragraph (Long answer)
**Required:** No

---

### Question 7: Recommendation
**Question:** Would you recommend this tool to others in bioinformatics/education?
**Type:** Multiple choice
**Options:**
- Yes, definitely
- Probably yes
- Not sure
- Probably not
- No
**Required:** Yes

---

### Question 8: Use Case
**Question:** What is your primary role or reason for using this tool? (Optional)
**Type:** Short answer
**Required:** No

---

### Question 9: Technical Issues
**Question:** Did you experience any technical issues or errors?
**Type:** Multiple choice
**Options:**
- No issues at all
- Minor issues (didn't affect usage)
- Some significant issues
- Major issues (couldn't use features)
**Required:** No

---

### Question 10: Additional Comments
**Question:** Any other comments, suggestions, or feedback?
**Type:** Paragraph (Long answer)
**Required:** No

---

## Quick Setup Steps:

1. ✅ Google Forms is opening in your browser
2. Click **"+ Blank"** to create new form
3. Copy the title and description above
4. Add each question one by one (copy-paste from above)
5. Click **"Settings"** ⚙️ and enable:
   - ✅ Collect email addresses (optional)
   - ✅ Limit to 1 response (prevents spam)
   - ✅ Show progress bar
6. Click **"Customize theme"** 🎨:
   - Choose purple color (#667eea)
   - Select a clean font
7. Click **"Send"** → Get link → **Shorten URL**
8. Copy the link (e.g., `https://forms.gle/ABC123xyz`)
9. Paste into `app.py` line 28

---

## Your Form URL Will Look Like:
```
https://forms.gle/ABC123xyz
```

Copy this and replace in app.py:
```python
const GOOGLE_FORM_URL = "https://forms.gle/ABC123xyz";
```

**That's it! Your feedback form will be ready!** 🎉

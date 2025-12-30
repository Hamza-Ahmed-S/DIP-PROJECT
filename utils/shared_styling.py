"""
Shared styling for all pages
Import this in every page file
"""

import streamlit as st

def apply_common_styling():
    """Apply common CSS styling to all pages"""
    
    # Remove keyboard_arrow with ULTRA-AGGRESSIVE JavaScript
    st.components.v1.html("""
    <script>
        // ULTRA AGGRESSIVE collapse button removal
        function nukeCollapseButton() {
            // Method 1: Remove by data-testid
            const collapseBtn = document.querySelector('[data-testid="collapsedControl"]');
            if (collapseBtn) {
                collapseBtn.remove();
            }
            
            // Method 2: Remove any button in sidebar
            const sidebarButtons = document.querySelectorAll('[data-testid="stSidebar"] button');
            sidebarButtons.forEach(btn => {
                if (btn.textContent.includes('keyboard') || 
                    btn.textContent.includes('<<') || 
                    btn.textContent.includes('key') ||
                    btn.getAttribute('aria-label')?.includes('collapse')) {
                    btn.remove();
                }
            });
            
            // Method 3: Hide any element containing "keyboard" text
            const allElements = document.querySelectorAll('*');
            allElements.forEach(el => {
                const text = el.textContent || '';
                if (text.includes('keyboard') && 
                    el.tagName !== 'A' && 
                    el.tagName !== 'SCRIPT' &&
                    !el.classList.contains('main')) {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                    el.style.opacity = '0';
                    el.style.width = '0';
                    el.style.height = '0';
                    el.remove();
                }
            });
            
            // Method 4: Target specific classes
            const badClasses = [
                '.css-1544g2n',
                '.css-pkbazv',
                '[class*="collaps"]',
                '[class*="Collaps"]'
            ];
            badClasses.forEach(selector => {
                document.querySelectorAll(selector).forEach(el => el.remove());
            });
        }
        
        // Run immediately
        nukeCollapseButton();
        
        // Run multiple times
        setTimeout(nukeCollapseButton, 50);
        setTimeout(nukeCollapseButton, 100);
        setTimeout(nukeCollapseButton, 200);
        setTimeout(nukeCollapseButton, 500);
        setTimeout(nukeCollapseButton, 1000);
        setTimeout(nukeCollapseButton, 2000);
        
        // Watch for DOM changes
        const observer = new MutationObserver(nukeCollapseButton);
        observer.observe(document.body, { 
            childList: true, 
            subtree: true,
            attributes: true,
            characterData: true
        });
        
        // Also run on window load
        window.addEventListener('load', nukeCollapseButton);
    </script>
    """, height=0)
    
    
    # Apply CSS
    st.markdown("""
    <style>
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Hide collapse button - AGGRESSIVE */
        [data-testid="collapsedControl"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            width: 0 !important;
            height: 0 !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        /* Hide any button with << or keyboard text */
        button:has-text("<<"), 
        button:has-text("keyboard"),
        [class*="collaps"] {
            display: none !important;
        }
        
        /* Animated Gradient Background */
        .stApp {
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Main Content - Glassmorphism */
        .main .block-container {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2);
            padding: 3rem !important;
            margin-top: 2rem;
        }
        
        
        /* SIDEBAR STYLING */
        [data-testid="stSidebar"] {
            width: 350px !important;
            min-width: 350px !important;
        }
        
        [data-testid="stSidebar"] > div:first-child {
            width: 350px !important;
            min-width: 350px !important;
        }
        
        .css-1d391kg, [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(102, 126, 234, 0.98) 0%, rgba(118, 75, 162, 0.98) 100%) !important;
        }
        
        [data-testid="stSidebarNav"] {
            padding: 2rem 1rem !important;
        }
        
        
        [data-testid="stSidebarNav"] a {
            background: rgba(255, 255, 255, 0.15) !important;
            border-radius: 15px !important;
            padding: 1.2rem 1.5rem !important;
            margin: 0.8rem 0 !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            color: white !important;
            border: 2px solid rgba(255, 255, 255, 0.2) !important;
            transition: all 0.3s ease !important;
            display: flex !important;
            align-items: center !important;
            gap: 1.2rem !important;
            min-height: 60px !important;
        }
        
        [data-testid="stSidebarNav"] a:hover {
            background: rgba(255, 255, 255, 0.25) !important;
            transform: translateX(8px) !important;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2) !important;
        }
        
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: rgba(255, 255, 255, 0.3) !important;
            border-color: rgba(255, 255, 255, 0.5) !important;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Fix emoji and text spacing */
        [data-testid="stSidebarNav"] a > div {
            display: flex !important;
            align-items: center !important;
            gap: 1rem !important;
            width: 100% !important;
        }
        
        /* Emoji container - give it fixed width */
        [data-testid="stSidebarNav"] a span:first-child {
            font-size: 1.5rem !important;
            min-width: 2.5rem !important;
            display: inline-flex !important;
            justify-content: center !important;
            align-items: center !important;
        }
        
        /* Text - prevent overlap */
        [data-testid="stSidebarNav"] a span:last-child {
            font-size: 1.1rem !important;
            color: white !important;
            flex: 1 !important;
            white-space: nowrap !important;
        }
        
        
        .css-1d391kg *, [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 700;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: rgba(255, 255, 255, 0.6);
            border-radius: 15px;
            padding: 8px;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)

import os

slides_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"
os.makedirs(slides_dir, exist_ok=True)

def generate_slide(slide_num, title, custom_css, body_html):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0B1F3A;
            --accent: #2563EB;
            --text-dark: #1F2937;
            --text-light: #6B7280;
            --bg-white: #FFFFFF;
            --bg-gray: #F5F7FA;
            --border-light: #E5E7EB;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-white);
            color: var(--text-dark);
            width: 1280px;
            height: 720px;
            overflow: hidden;
            display: flex;
            position: relative;
        }}
        .slide-container {{
            width: 100%;
            height: 100%;
            padding: 80px 100px;
            display: flex;
            flex-direction: column;
            position: relative;
        }}
        /* Typography */
        .title {{ font-size: 44px; font-weight: 600; color: var(--primary); letter-spacing: -0.01em; line-height: 1.2; }}
        .heading {{ font-size: 28px; font-weight: 600; color: var(--primary); margin-bottom: 32px; line-height: 1.3; }}
        .body-text {{ font-size: 18px; color: var(--text-dark); line-height: 1.6; font-weight: 400; }}
        .body-text-light {{ font-size: 16px; color: var(--text-light); line-height: 1.6; font-weight: 400; }}
        .number-highlight {{ font-size: 40px; font-weight: 700; color: var(--primary); }}
        
        .accent-text {{ color: var(--accent); font-weight: 600; }}
        
        /* Layout utilities */
        .flex-row {{ display: flex; gap: 40px; }}
        .flex-col {{ display: flex; flex-direction: column; gap: 24px; }}
        .items-center {{ align-items: center; }}
        .justify-center {{ justify-content: center; }}
        .justify-between {{ justify-content: space-between; }}
        .text-center {{ text-align: center; }}
        .w-half {{ width: 50%; }}
        .w-full {{ width: 100%; }}
        .h-full {{ height: 100%; }}
         
        /* Visual elements */
        .divider-bottom {{ border-bottom: 2px solid var(--primary); padding-bottom: 16px; margin-bottom: 40px; }}
        .divider-left {{ border-left: 4px solid var(--accent); padding-left: 24px; }}
        .gray-box {{ background-color: var(--bg-gray); border: 1px solid var(--border-light); padding: 40px; border-radius: 4px; display: flex; flex-direction: column; }}
        .icon-line {{ font-size: 32px; color: var(--primary); margin-bottom: 20px; font-weight: 300; display: block; }}
        
        /* Lists */
        ul.clean-list {{ list-style-type: none; }}
        ul.clean-list li {{ position: relative; padding-left: 28px; margin-bottom: 20px; font-size: 18px; color: var(--text-dark); line-height: 1.6; }}
        ul.clean-list li::before {{ content: "•"; color: var(--accent); font-weight: bold; position: absolute; left: 0; font-size: 24px; top: -4px; }}
        
        /* Footer */
        .footer {{ position: absolute; bottom: 40px; left: 100px; right: 100px; display: flex; justify-content: space-between; font-size: 14px; color: var(--text-light); border-top: 1px solid var(--border-light); padding-top: 20px; }}
        
        {custom_css}
    </style>
</head>
<body>
    <div class="slide-container">
        {body_html}
        <div class="footer">
            <span>Sketch Brains</span>
            <span>Confidential</span>
        </div>
    </div>
    <!-- PDF Capture Bridge script -->
    <script src="../../js/capture_helper.js"></script>
</body>
</html>"""
    
    filepath = os.path.join(slides_dir, f'slide_{slide_num}.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

def build_slides():
    # SLIDE 1: TITLE
    generate_slide(1, "Title", """
        .slide-1-wrapper { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .slide-1-title { font-size: 56px; margin-bottom: 24px; }
        .slide-1-subtitle { font-size: 24px; color: var(--text-light); margin-bottom: 40px; max-width: 800px; }
        .slide-1-statement { font-size: 20px; font-weight: 500; color: var(--primary); padding: 20px 40px; border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); }
    """, """
        <div class="slide-1-wrapper">
            <h1 class="title slide-1-title">Sketch Brains</h1>
            <p class="slide-1-subtitle">A structured pipeline for pre-trained, job-ready talent.</p>
            <p class="slide-1-statement">Reduce hiring cycles. Eliminate training overhead.</p>
        </div>
    """)

    # SLIDE 2: PROBLEM
    generate_slide(2, "Hiring Reality", """
        .big-number-block { display: flex; flex-direction: column; justify-content: center; height: 100%; border-left: 1px solid var(--border-light); padding-left: 60px; }
        .number-pair { margin-bottom: 40px; }
        .number-pair:last-child { margin-bottom: 0; }
        .big-txt { font-size: 44px; font-weight: 700; color: var(--primary); line-height: 1.1; margin-bottom: 8px;}
        .big-lbl { font-size: 20px; color: var(--text-light); font-weight: 500; }
    """, """
        <h2 class="heading divider-bottom">Hiring freshers is high effort, low efficiency</h2>
        <div class="flex-row h-full">
            <div class="w-half" style="padding-top: 20px;">
                <ul class="clean-list">
                    <li>300–500 applications per role</li>
                    <li>&lt;10% candidates meet expectations</li>
                    <li>Multiple interview rounds</li>
                    <li>Weeks spent on screening</li>
                </ul>
            </div>
            <div class="w-half big-number-block">
                <div class="number-pair">
                    <div class="big-txt">300–500</div>
                    <div class="big-lbl">Applicants</div>
                </div>
                <div class="number-pair">
                    <div class="big-txt accent-text">&lt;10%</div>
                    <div class="big-lbl">Qualified</div>
                </div>
            </div>
        </div>
    """)

    # SLIDE 3: COST
    generate_slide(3, "Hidden Cost", """
        .cost-wrapper { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .cost-hero { font-size: 64px; font-weight: 700; color: var(--primary); margin: 40px 0; border: 1px solid var(--border-light); padding: 60px; background: var(--bg-gray); width: 100%; }
        .cost-sub { font-size: 24px; color: var(--text-dark); font-weight: 500; display: flex; gap: 40px; justify-content: center; }
        .cost-sub-item { display: flex; align-items: center; gap: 12px; }
        .cost-footer { font-size: 18px; color: var(--text-light); margin-top: 20px; }
    """, """
        <h2 class="heading" style="text-align: center;">The real cost of hiring freshers</h2>
        <div class="cost-wrapper">
            <div class="cost-sub">
                <div class="cost-sub-item"><i class="fa-regular fa-clock" style="color: var(--accent);"></i> 2–3 months training</div>
                <div class="cost-sub-item"><i class="fa-solid fa-indian-rupee-sign" style="color: var(--accent);"></i> ₹30K–₹50K stipend/month</div>
            </div>
            <div class="cost-hero">
                ₹30–75 Lakhs spent <br> <span style="font-size: 24px; font-weight: 400; color: var(--text-light);">(per 50 hires)</span>
            </div>
            <p class="cost-footer">Before candidates become productive</p>
        </div>
    """)

    # SLIDE 4: CORE PROBLEM
    generate_slide(4, "Core Problem", """
        .split-grid { display: flex; height: 100%; gap: 60px; align-items: center; margin-bottom: 60px; }
        .split-box { flex: 1; padding: 60px 40px; background-color: var(--bg-gray); border-top: 4px solid var(--primary); text-align: center; }
        .split-box.blue { border-top-color: var(--accent); }
        .split-box h3 { font-size: 24px; color: var(--text-dark); margin-bottom: 24px; font-weight: 500;}
        .split-box .result { font-size: 28px; font-weight: 600; color: var(--primary); }
        .bottom-line { text-align: center; padding: 24px; border: 1px solid var(--border-light); font-size: 20px; font-weight: 500; background: var(--bg-white); }
        .arrow-center { font-size: 32px; color: var(--border-light); }
    """, """
        <div style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div class="split-grid">
                <div class="split-box">
                    <h3>Students learn</h3>
                    <i class="fa-solid fa-arrow-down" style="color: var(--border-light); margin-bottom: 24px; font-size: 24px;"></i>
                    <div class="result">Generic skills</div>
                </div>
                <div class="arrow-center"><i class="fa-solid fa-xmark" style="color: #EF4444;"></i></div>
                <div class="split-box blue">
                    <h3>Companies need</h3>
                    <i class="fa-solid fa-arrow-down" style="color: var(--border-light); margin-bottom: 24px; font-size: 24px;"></i>
                    <div class="result accent-text">Specific tools & workflows</div>
                </div>
            </div>
            <div class="bottom-line">Mismatch leads to low productivity and longer ramp-up time</div>
        </div>
    """)

    # SLIDE 5: APPROACH
    generate_slide(5, "Our Approach", """
        .flow-container { display: flex; align-items: center; justify-content: space-between; height: 100%; padding: 0 40px; }
        .flow-step { flex: 1; text-align: center; padding: 40px 20px; }
        .flow-arrow { font-size: 24px; color: var(--border-light); }
        .step-label { font-size: 28px; font-weight: 700; color: var(--primary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 2px;}
        .step-desc { font-size: 16px; color: var(--text-dark); line-height: 1.5; }
        .step-icon { font-size: 40px; margin-bottom: 24px; color: var(--accent); }
    """, """
        <h2 class="heading divider-bottom">We reverse the hiring pipeline</h2>
        <div class="flow-container">
            <div class="flow-step">
                <i class="fa-regular fa-clipboard step-icon"></i>
                <div class="step-label">Define</div>
                <div class="step-desc">Define requirements</div>
            </div>
            <i class="fa-solid fa-arrow-right flow-arrow"></i>
            <div class="flow-step">
                <i class="fa-solid fa-laptop-code step-icon"></i>
                <div class="step-label">Train</div>
                <div class="step-desc">Train on exact stack</div>
            </div>
            <i class="fa-solid fa-arrow-right flow-arrow"></i>
            <div class="flow-step">
                <i class="fa-regular fa-handshake step-icon"></i>
                <div class="step-label">Hire</div>
                <div class="step-desc">Hire from pre-vetted pool</div>
            </div>
        </div>
    """)

    # SLIDE 6: WHAT CHANGES
    generate_slide(6, "What Changes", """
        .grid-2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; height: 100%; margin-top: 40px; }
        .grid-box { border-top: 2px solid var(--accent); background: var(--bg-gray); padding: 40px; display: flex; align-items: center; justify-content: center; text-align: center; font-size: 24px; font-weight: 500; line-height: 1.4; color: var(--primary); }
    """, """
        <h2 class="heading divider-bottom">What Changes</h2>
        <div class="grid-2x2">
            <div class="grid-box">Reduced screening effort</div>
            <div class="grid-box">No early-stage interviews</div>
            <div class="grid-box">No internal training cycles</div>
            <div class="grid-box accent-text" style="border-top-color: var(--primary);">Focus only on final selection</div>
        </div>
    """)

    # SLIDE 7: IMPACT
    generate_slide(7, "Impact", """
        .metrics-grid { display: grid; grid-template-columns: 1fr; gap: 24px; margin-top: 20px; }
        .metric-row { display: flex; align-items: center; padding: 24px 32px; background: var(--bg-gray); border-left: 4px solid var(--primary); }
        .metric-icon { width: 40px; font-size: 24px; color: var(--accent); }
        .metric-text { font-size: 20px; font-weight: 500; color: var(--text-dark); }
        .footer-note { font-size: 14px; color: var(--text-light); margin-top: 40px; font-style: italic; }
    """, """
        <h2 class="heading divider-bottom">Measurable impact</h2>
        <div class="metrics-grid">
            <div class="metric-row">
                <div class="metric-icon"><i class="fa-solid fa-bolt"></i></div>
                <div class="metric-text"><span class="number-highlight" style="font-size: 28px; margin-right: 12px;">40–70%</span> faster hiring cycles</div>
            </div>
            <div class="metric-row">
                <div class="metric-icon"><i class="fa-solid fa-arrow-trend-down"></i></div>
                <div class="metric-text">Lower cost-per-hire</div>
            </div>
            <div class="metric-row">
                <div class="metric-icon"><i class="fa-regular fa-clock"></i></div>
                <div class="metric-text">Reduced training dependency</div>
            </div>
            <div class="metric-row">
                <div class="metric-icon"><i class="fa-solid fa-crosshairs"></i></div>
                <div class="metric-text">Better candidate-job alignment</div>
            </div>
        </div>
        <div class="footer-note">Based on structured pre-training models</div>
    """)

    # SLIDE 8: PROCESS
    generate_slide(8, "How It Works", """
        .process-container { display: flex; flex-direction: column; gap: 32px; justify-content: center; height: 100%; padding-top: 20px; }
        .process-step { display: flex; align-items: center; border: 1px solid var(--border-light); padding: 32px; background: var(--bg-white); }
        .step-num { width: 60px; height: 60px; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 700; border-radius: 4px; margin-right: 32px; flex-shrink: 0; }
        .step-txt { font-size: 24px; font-weight: 500; color: var(--text-dark); }
    """, """
        <h2 class="heading divider-bottom">How It Works</h2>
        <div class="process-container">
            <div class="process-step">
                <div class="step-num">1</div>
                <div class="step-txt">You define requirements</div>
            </div>
            <div class="process-step">
                <div class="step-num" style="background: var(--accent);">2</div>
                <div class="step-txt">We train & assess candidates</div>
            </div>
            <div class="process-step">
                <div class="step-num">3</div>
                <div class="step-txt">You interview and hire</div>
            </div>
        </div>
    """)

    # SLIDE 9: RISK-FREE
    generate_slide(9, "Low Risk Model", """
        .risk-wrapper { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .big-statement { font-size: 48px; font-weight: 700; color: var(--primary); margin-bottom: 60px; line-height: 1.2; max-width: 900px; }
        .bullet-container { display: flex; gap: 60px; }
        .bullet-box { padding: 24px 40px; border-left: 2px solid var(--accent); text-align: left; font-size: 20px; font-weight: 500;}
    """, """
        <div class="risk-wrapper">
            <div class="big-statement">No upfront cost. <br>No hiring obligation.</div>
            <div class="bullet-container">
                <div class="bullet-box">Pilot-based engagement</div>
                <div class="bullet-box">You control final selection</div>
            </div>
        </div>
    """)

    # SLIDE 10: USE CASES
    generate_slide(10, "Ideal Use Cases", """
        .use-case-container { display: flex; height: 100%; align-items: center; }
        .use-list { margin-top: 40px; }
        .use-list li { font-size: 24px !important; margin-bottom: 32px !important; padding-left: 40px !important; font-weight: 500; }
        .use-list li::before { font-size: 32px !important; top: -6px !important; }
    """, """
        <h2 class="heading divider-bottom">Ideal Use Cases</h2>
        <div class="use-case-container">
            <ul class="clean-list use-list">
                <li>Batch hiring of freshers</li>
                <li>Campus hiring programs</li>
                <li>Roles requiring training</li>
                <li>Recurring hiring needs</li>
            </ul>
        </div>
    """)

    # SLIDE 11: CTA
    generate_slide(11, "Closing / CTA", """
        .cta-wrapper { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .cta-line-1 { font-size: 32px; color: var(--text-dark); max-width: 900px; line-height: 1.5; margin-bottom: 40px; font-weight: 400; }
        .cta-line-2 { font-size: 24px; color: var(--primary); font-weight: 600; padding: 24px 40px; background: var(--bg-gray); border-radius: 4px; border: 1px solid var(--border-light); }
    """, """
        <div class="cta-wrapper">
            <div class="cta-line-1">If hiring freshers is taking more time, cost, and effort than expected — we can help streamline it.</div>
            <div class="cta-line-2">Let’s run a pilot cohort aligned to your requirements.</div>
        </div>
    """)

if __name__ == "__main__":
    build_slides()
    print("Successfully built 11 McKinsey-style slides.")

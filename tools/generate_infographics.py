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
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0B1F3A;
            --accent: #2563EB;
            --text-dark: #1F2937;
            --text-light: #6B7280;
            --bg-white: #FFFFFF;
            --bg-gray: #F5F7FA;
            --border-light: #E5E7EB;
            --border-med: #D1D5DB;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-gray); /* Outer boundary */
            width: 1280px;
            height: 720px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .slide-container {{
            width: 1280px;
            height: 720px;
            background-color: var(--bg-white);
            padding: 70px 90px;
            display: flex;
            flex-direction: column;
            position: relative;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05); /* very subtle framing */
        }}
        
        /* Corporate Tracker / Kicker */
        .kicker {{
            position: absolute;
            top: 40px;
            left: 90px;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--accent);
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .kicker::before {{
            content: '';
            display: block;
            width: 30px;
            height: 2px;
            background-color: var(--accent);
        }}

        /* Typography - Enterprise Grade */
        .heading {{ 
            font-size: 38px; 
            font-weight: 800; 
            color: var(--primary); 
            margin-top: 20px;
            margin-bottom: 40px; 
            line-height: 1.2; 
            letter-spacing: -1px;
        }}
        .body-text {{ font-size: 18px; color: var(--text-dark); line-height: 1.6; font-weight: 400; }}
        
        /* Info-graphic Helpers */
        .flex {{ display: flex; }}
        .flex-col {{ display: flex; flex-direction: column; }}
        .items-center {{ align-items: center; }}
        .justify-center {{ justify-content: center; }}
        .justify-between {{ justify-content: space-between; }}
        .w-full {{ width: 100%; }}
        .h-full {{ height: 100%; }}
        .gap-4 {{ gap: 16px; }}
        .gap-6 {{ gap: 24px; }}
        .gap-10 {{ gap: 40px; }}
        
        /* Grid system */
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 60px; height: 100%; }}
        
        /* Footer */
        .footer {{ 
            position: absolute; 
            bottom: 30px; 
            left: 90px; 
            right: 90px; 
            display: flex; 
            justify-content: space-between; 
            font-size: 13px; 
            color: var(--text-light); 
            border-top: 1px solid var(--border-light); 
            padding-top: 15px; 
            font-weight: 500;
        }}
        
        {custom_css}
    </style>
</head>
<body>
    <div class="slide-container">
        {body_html}
        <div class="footer">
            <span>Sketch Brains</span>
            <span>Confidential & Proprietary</span>
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
        .title-wrapper { height: 100%; display: flex; flex-direction: column; justify-content: center; position: relative; padding-left: 60px; }
        .title-wrapper::before { content: ''; position: absolute; left: 0; top: 15%; height: 70%; width: 8px; background-color: var(--accent); }
        .hero-title { font-size: 72px; font-weight: 900; color: var(--primary); letter-spacing: -2px; line-height: 1; margin-bottom: 24px; }
        .hero-subtitle { font-size: 32px; font-weight: 400; color: var(--text-dark); margin-bottom: 40px; max-width: 800px; line-height: 1.3; }
        .hero-statement { display: inline-block; font-size: 18px; font-weight: 600; color: var(--bg-white); background-color: var(--primary); padding: 16px 32px; letter-spacing: 1px; }
    """, """
        <div class="title-wrapper">
            <div class="hero-title">Sketch Brains</div>
            <div class="hero-subtitle">A structured pipeline for pre-trained, job-ready talent.</div>
            <div>
                <div class="hero-statement">Reduce hiring cycles. Eliminate training overhead.</div>
            </div>
        </div>
    """)

    # SLIDE 2: PROBLEM (Hiring Reality + Funnel Infographic)
    generate_slide(2, "Hiring Reality", """
        .funnel-container { display: flex; flex-direction: column; align-items: flex-end; justify-content: center; height: 100%; padding-right: 40px;}
        .funnel-layer { display: flex; align-items: center; justify-content: flex-end; margin-bottom: 16px; position: relative; }
        .funnel-bar { height: 60px; background-color: var(--bg-gray); border-right: 6px solid var(--primary); display: flex; align-items: center; padding: 0 20px; transition: 0.3s; }
        .funnel-bar.top { width: 400px; background-color: var(--border-light); border-right-color: var(--primary); }
        .funnel-bar.mid { width: 250px; background-color: var(--border-med); border-right-color: var(--primary); }
        .funnel-bar.bot { width: 120px; background-color: var(--accent); border-right-color: var(--accent); color: white;}
        .funnel-text { font-size: 38px; font-weight: 800; color: var(--primary); margin-right: 24px; text-align: right; line-height: 1; }
        .funnel-sub { font-size: 16px; color: var(--text-light); text-transform: uppercase; letter-spacing: 1px; }
        
        .bullets { list-style: none; margin-top: 40px; }
        .bullets li { display: flex; align-items: flex-start; margin-bottom: 24px; font-size: 20px; color: var(--text-dark); line-height: 1.5; font-weight: 500;}
        .bullets li i { color: var(--accent); font-size: 24px; margin-right: 16px; margin-top: 4px; }
    """, """
        <div class="kicker">Market Reality</div>
        <h2 class="heading">Hiring freshers is high effort, low efficiency</h2>
        
        <div class="grid-2">
            <div class="flex-col justify-center">
                <ul class="bullets">
                    <li><i class="fa-solid fa-file-lines"></i> 300–500 applications per role</li>
                    <li><i class="fa-solid fa-filter"></i> Multiple interview rounds required</li>
                    <li><i class="fa-solid fa-clock-rotate-left"></i> Weeks spent on purely screening</li>
                    <li><i class="fa-solid fa-triangle-exclamation" style="color:#EF4444;"></i> &lt;10% candidates meet baseline expectations</li>
                </ul>
            </div>
            
            <div class="funnel-container">
                <div class="funnel-layer">
                    <div style="text-align: right; margin-right: 24px;">
                        <div class="funnel-text">300–500</div>
                        <div class="funnel-sub">Applicants</div>
                    </div>
                    <div class="funnel-bar top"></div>
                </div>
                <div class="funnel-layer">
                    <div style="text-align: right; margin-right: 24px;">
                        <div class="funnel-text" style="font-size: 28px;">Multiple</div>
                        <div class="funnel-sub">Interviews</div>
                    </div>
                    <div class="funnel-bar mid"></div>
                </div>
                <div class="funnel-layer">
                    <div style="text-align: right; margin-right: 24px;">
                        <div class="funnel-text" style="color: var(--accent); font-size: 56px;">&lt;10%</div>
                        <div class="funnel-sub">Qualified</div>
                    </div>
                    <div class="funnel-bar bot"></div>
                </div>
            </div>
        </div>
    """)

    # SLIDE 3: COST (Ledger / Dashboard Metric)
    generate_slide(3, "Hidden Cost", """
        .cost-dashboard { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; width: 100%; }
        .metric-cards { display: flex; gap: 40px; width: 100%; margin-bottom: 40px; }
        .scard { flex: 1; background: var(--bg-gray); border: 1px solid var(--border-light); padding: 40px; text-align: center; border-top: 4px solid var(--primary); }
        .scard-icon { font-size: 32px; color: var(--accent); margin-bottom: 16px; }
        .scard-val { font-size: 28px; font-weight: 700; color: var(--primary); margin-bottom: 8px; }
        .scard-txt { font-size: 16px; color: var(--text-light); text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
        
        .huge-cost {
            background: var(--primary); color: white; width: 100%; padding: 60px; text-align: center;
            border-radius: 8px; position: relative; overflow: hidden;
        }
        .huge-cost::after { content: '\\f0d6'; font-family: 'Font Awesome 6 Free'; font-weight: 900; position: absolute; right: -20px; bottom: -40px; font-size: 200px; color: rgba(255,255,255,0.05); }
        .hc-val { font-size: 72px; font-weight: 900; letter-spacing: -2px; margin-bottom: 12px; color: #FFFFFF; }
        .hc-sub { font-size: 24px; color: #9CA3AF; font-weight: 400; }
        .hc-foot { font-size: 16px; color: var(--accent); margin-top: 24px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; }
    """, """
        <div class="kicker">Financial Impact</div>
        <h2 class="heading text-center" style="margin-bottom: 50px;">The real cost of hiring freshers</h2>
        
        <div class="cost-dashboard">
            <div class="metric-cards">
                <div class="scard">
                    <i class="fa-regular fa-calendar-xmark scard-icon"></i>
                    <div class="scard-val">2–3 Months</div>
                    <div class="scard-txt">Lost to Training</div>
                </div>
                <div class="scard">
                    <i class="fa-solid fa-money-bill-transfer scard-icon"></i>
                    <div class="scard-val">₹30K–₹50K</div>
                    <div class="scard-txt">Stipend / Month</div>
                </div>
            </div>
            
            <div class="huge-cost">
                <div class="hc-val">₹30–75 Lakhs</div>
                <div class="hc-sub">capital burned per 50 hires</div>
                <div class="hc-foot">Before candidates become productive</div>
            </div>
        </div>
    """)

    # SLIDE 4: PROBLEM INSIGHT (Split Comparison Infographic)
    generate_slide(4, "Core Problem", """
        .gap-diagram { display: flex; align-items: center; justify-content: space-between; height: 100%; width: 100%; padding-bottom: 80px; }
        .col-block { width: 400px; }
        .c-head { font-size: 20px; font-weight: 700; color: var(--text-light); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; text-align: center;}
        .c-box { background: var(--bg-gray); border: 2px solid var(--border-light); padding: 50px 30px; text-align: center; height: 250px; display: flex; flex-direction: column; justify-content: center; position: relative;}
        .c-box.left { border-left: 8px solid var(--text-light); }
        .c-box.right { border-right: 8px solid var(--accent); background: #EFF6FF; border-color: #BFDBFE; }
        .c-val { font-size: 32px; font-weight: 800; color: var(--primary); line-height: 1.2; }
        
        .bridge-gap { position: relative; width: 150px; height: 250px; display: flex; align-items: center; justify-content: center; }
        .bridge-gap i { font-size: 64px; color: #EF4444; }
        .bridge-gap::before { content: ''; position: absolute; left: 0; width: 40%; height: 4px; background: var(--border-light); z-index: 1; }
        .bridge-gap::after { content: ''; position: absolute; right: 0; width: 40%; height: 4px; background: var(--accent); z-index: 1; }
        
        .bottom-alert { position: absolute; bottom: 80px; left: 90px; right: 90px; background: var(--primary); color: white; padding: 24px; text-align: center; font-size: 22px; font-weight: 600; letter-spacing: 0.5px; }
    """, """
        <div class="kicker">The Alignment Gap</div>
        <h2 class="heading text-center">The fundamental mismatch</h2>
        
        <div class="gap-diagram">
            <div class="col-block">
                <div class="c-head">Students Learn</div>
                <div class="c-box left">
                    <i class="fa-solid fa-graduation-cap" style="font-size: 40px; color: var(--text-light); margin-bottom: 20px;"></i>
                    <div class="c-val" style="color: var(--text-dark);">Generic Skills<br>& Theory</div>
                </div>
            </div>
            
            <div class="bridge-gap">
                <i class="fa-solid fa-bolt"></i>
            </div>
            
            <div class="col-block">
                <div class="c-head" style="color: var(--accent);">Companies Need</div>
                <div class="c-box right">
                    <i class="fa-solid fa-briefcase" style="font-size: 40px; color: var(--accent); margin-bottom: 20px;"></i>
                    <div class="c-val">Specific Tools<br>& Workflows</div>
                </div>
            </div>
        </div>
        
        <div class="bottom-alert">
            Mismatch leads to low productivity and longer ramp-up time
        </div>
    """)

    # SLIDE 5: SOLUTION (Consulting Chevrons)
    generate_slide(5, "Our Approach", """
        .chevron-container { display: flex; width: 100%; height: 200px; margin-top: 80px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.05)); }
        
        .chevron {
            flex: 1;
            position: relative;
            background: var(--bg-gray);
            color: var(--primary);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-right: 4px;
            padding-left: 40px;
        }
        
        /* The pointy bit */
        .chevron::after {
            content: '';
            position: absolute;
            top: 0;
            right: -40px;
            width: 0;
            height: 0;
            border-top: 100px solid transparent;
            border-bottom: 100px solid transparent;
            border-left: 40px solid var(--bg-gray);
            z-index: 2;
        }
        /* The indent bit */
        .chevron::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 0;
            height: 0;
            border-top: 100px solid transparent;
            border-bottom: 100px solid transparent;
            border-left: 40px solid var(--bg-white);
            z-index: 1;
        }
        
        /* First child has no indent */
        .chevron:first-child { padding-left: 0; background: var(--primary); color: white;}
        .chevron:first-child::before { display: none; }
        .chevron:first-child::after { border-left-color: var(--primary); }
        
        /* Last child is accent */
        .chevron:last-child { background: var(--accent); color: white; margin-right: 0;}
        .chevron:last-child::after { display: none; }
        
        .c-icon { font-size: 32px; margin-bottom: 16px; }
        .c-title { font-size: 28px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;}
        .c-desc { font-size: 16px; font-weight: 500; opacity: 0.9; }
    """, """
        <div class="kicker">The Methodology</div>
        <h2 class="heading text-center">We reverse the hiring pipeline</h2>
        
        <div class="chevron-container">
            <div class="chevron">
                <i class="fa-solid fa-crosshairs c-icon"></i>
                <div class="c-title">Define</div>
                <div class="c-desc">Define precise requirements</div>
            </div>
            <div class="chevron">
                <i class="fa-solid fa-code c-icon"></i>
                <div class="c-title">Train</div>
                <div class="c-desc">Train on exact tech stack</div>
            </div>
            <div class="chevron">
                <i class="fa-solid fa-user-check c-icon" style="color: white;"></i>
                <div class="c-title" style="color: white;">Hire</div>
                <div class="c-desc" style="color: white;">Hire from pre-vetted pool</div>
            </div>
        </div>
    """)

    # SLIDE 6: VALUE (2x2 Matrix)
    generate_slide(6, "What Changes", """
        .matrix-wrapper { height: 100%; display: flex; align-items: center; padding-top: 20px;}
        .matrix { display: grid; grid-template-columns: 1fr 1fr; width: 100%; height: 400px; border: 1px solid var(--border-light); }
        .m-quad { padding: 40px; display: flex; flex-direction: column; justify-content: center; position: relative; background: var(--bg-white); }
        .m-quad:nth-child(1) { border-right: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); }
        .m-quad:nth-child(2) { border-bottom: 1px solid var(--border-light); }
        .m-quad:nth-child(3) { border-right: 1px solid var(--border-light); }
        .m-quad:nth-child(4) { background: var(--primary); color: white; }
        
        .mq-icon { font-size: 32px; color: var(--accent); margin-bottom: 20px; }
        .mq-text { font-size: 28px; font-weight: 600; color: var(--primary); line-height: 1.3; }
        .m-quad:nth-child(4) .mq-text { color: white; }
        .m-quad:nth-child(4) .mq-icon { color: var(--accent); }
    """, """
        <div class="kicker">Operational Shift</div>
        <h2 class="heading">What Changes</h2>
        
        <div class="matrix-wrapper">
            <div class="matrix">
                <div class="m-quad">
                    <i class="fa-solid fa-compress mq-icon"></i>
                    <div class="mq-text">Reduced screening effort</div>
                </div>
                <div class="m-quad">
                    <i class="fa-regular fa-comments mq-icon"></i>
                    <div class="mq-text">No early-stage interviews</div>
                </div>
                <div class="m-quad">
                    <i class="fa-solid fa-chalkboard-user mq-icon"></i>
                    <div class="mq-text">No internal training cycles</div>
                </div>
                <div class="m-quad">
                    <i class="fa-solid fa-bullseye mq-icon" style="color: #60A5FA;"></i>
                    <div class="mq-text">Focus entirely on final selection</div>
                </div>
            </div>
        </div>
    """)

    # SLIDE 7: IMPACT (Bar Chart Metrics)
    generate_slide(7, "Impact", """
        .impact-list { display: flex; flex-direction: column; gap: 30px; margin-top: 40px;}
        .impact-item { display: flex; align-items: center; }
        
        .imp-left { width: 350px; font-size: 22px; font-weight: 600; color: var(--primary); }
        .imp-bar-container { flex: 1; height: 32px; background: var(--bg-gray); border-radius: 16px; overflow: hidden; position: relative; }
        .imp-bar { height: 100%; background: var(--accent); display: flex; align-items: center; padding-left: 20px; color: white; font-weight: 700; font-size: 16px; }
        
        .imp-1 { width: 85%; }
        .imp-2 { width: 70%; background: var(--primary); }
        .imp-3 { width: 90%; background: #3B82F6; }
        .imp-4 { width: 100%; background: var(--primary); }
        
        .imp-stat { font-family: monospace; font-size: 28px; font-weight: 800; color: var(--accent); width: 140px; text-align: right; }
        
        .foot-note { position: absolute; bottom: 80px; left: 90px; font-size: 15px; color: var(--text-light); font-style: italic; border-left: 3px solid var(--accent); padding-left: 16px; }
    """, """
        <div class="kicker">Measurable Outcomes</div>
        <h2 class="heading">Measurable impact</h2>
        
        <div class="impact-list">
            <div class="impact-item">
                <div class="imp-left">Hiring Cycles</div>
                <div class="imp-bar-container"><div class="imp-bar imp-1">40–70% Faster</div></div>
            </div>
            <div class="impact-item">
                <div class="imp-left">Cost-per-Hire</div>
                <div class="imp-bar-container"><div class="imp-bar imp-2">Significantly Lower</div></div>
            </div>
            <div class="impact-item">
                <div class="imp-left">Training Dependency</div>
                <div class="imp-bar-container"><div class="imp-bar imp-3">Drastically Reduced</div></div>
            </div>
            <div class="impact-item">
                <div class="imp-left">Job Alignment</div>
                <div class="imp-bar-container"><div class="imp-bar imp-4">Perfectly Aligned</div></div>
            </div>
        </div>
        
        <div class="foot-note">Based on structured pre-training empirical models.</div>
    """)

    # SLIDE 8: PROCESS (Staircase / Step flow)
    generate_slide(8, "Process", """
        .staircase { display: flex; align-items: flex-end; height: 400px; gap: 20px; padding-top: 40px; border-bottom: 2px solid var(--primary); padding-bottom: 24px;}
        .stair { flex: 1; background: var(--bg-gray); display: flex; flex-direction: column; position: relative; border-top: 4px solid var(--primary); }
        .s-1 { height: 40%; }
        .s-2 { height: 70%; border-top-color: var(--accent); background: #EFF6FF; }
        .s-3 { height: 100%; border-top-color: var(--primary); }
        
        .stair-num { position: absolute; top: -30px; left: 24px; font-size: 64px; font-weight: 900; color: rgba(11, 31, 58, 0.1); line-height: 1; }
        .s-2 .stair-num { color: rgba(37, 99, 235, 0.15); }
        
        .stair-content { padding: 40px 30px; display: flex; flex-direction: column; justify-content: flex-end; height: 100%; z-index: 2; position: relative;}
        .stair-title { font-size: 24px; font-weight: 700; color: var(--primary); line-height: 1.3; }
        .s-2 .stair-title { color: var(--accent); }
    """, """
        <div class="kicker">The Execution</div>
        <h2 class="heading">How It Works</h2>
        
        <div class="staircase">
            <div class="stair s-1">
                <div class="stair-num">1</div>
                <div class="stair-content">
                    <div class="stair-title">You define requirements</div>
                </div>
            </div>
            <div class="stair s-2">
                <div class="stair-num">2</div>
                <div class="stair-content">
                    <div class="stair-title">We train & assess candidates</div>
                </div>
            </div>
            <div class="stair s-3">
                <div class="stair-num">3</div>
                <div class="stair-content">
                    <div class="stair-title">You interview and hire</div>
                </div>
            </div>
        </div>
    """)

    # SLIDE 9: RISK-FREE (Big layout)
    generate_slide(9, "Low Risk Model", """
        .risk-center { height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
        .zero-graphic { 
            position: relative;
            width: 200px; height: 200px; 
            border: 16px solid var(--accent);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 80px; font-weight: 900; color: var(--primary);
            margin-bottom: 40px;
        }
        .zero-graphic::after {
            content: '';
            position: absolute;
            width: 210px; height: 16px;
            background: var(--bg-white);
            transform: rotate(-45deg);
        }
        
        .huge-title { font-size: 56px; font-weight: 800; color: var(--primary); line-height: 1.1; margin-bottom: 40px; }
        
        .risk-bullets { display: flex; gap: 60px; }
        .rb-item { font-size: 22px; font-weight: 600; color: var(--text-dark); display: flex; align-items: center; gap: 16px; }
        .rb-item i { color: var(--accent); font-size: 28px; }
    """, """
        <div class="kicker">Commercial Model</div>
        <div class="risk-center">
            
            <div class="huge-title">No upfront cost.<br>No hiring obligation.</div>
            
            <div class="risk-bullets">
                <div class="rb-item"><i class="fa-solid fa-check-circle"></i> Pilot-based engagement</div>
                <div class="rb-item"><i class="fa-solid fa-check-circle"></i> You control final selection</div>
            </div>
        </div>
    """)

    # SLIDE 10: IDEAL USE CASES (Target Infographic Grid)
    generate_slide(10, "Ideal Use Cases", """
        .target-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 40px; }
        .uc-card { background: var(--bg-gray); padding: 40px; display: flex; align-items: center; gap: 24px; border: 1px solid var(--border-light); }
        .uc-icon { width: 60px; height: 60px; background: var(--bg-white); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; color: var(--accent); box-shadow: 0 4px 6px rgba(0,0,0,0.05); flex-shrink: 0;}
        .uc-text { font-size: 24px; font-weight: 600; color: var(--primary); }
    """, """
        <div class="kicker">Application Focus</div>
        <h2 class="heading">Ideal Configuration</h2>
        
        <div class="target-grid">
            <div class="uc-card">
                <div class="uc-icon"><i class="fa-solid fa-layer-group"></i></div>
                <div class="uc-text">Batch hiring of freshers</div>
            </div>
            <div class="uc-card">
                <div class="uc-icon"><i class="fa-solid fa-building-columns"></i></div>
                <div class="uc-text">Campus hiring programs</div>
            </div>
            <div class="uc-card">
                <div class="uc-icon"><i class="fa-solid fa-chalkboard-user"></i></div>
                <div class="uc-text">Roles requiring training</div>
            </div>
            <div class="uc-card">
                <div class="uc-icon"><i class="fa-solid fa-rotate"></i></div>
                <div class="uc-text">Recurring hiring needs</div>
            </div>
        </div>
    """)

    # SLIDE 11: CTA (Full bleed dark block)
    generate_slide(11, "Closing", """
        .cta-dark-box { background: var(--primary); color: white; border-radius: 8px; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; position: relative; overflow: hidden; }
        
        .cta-dark-box::before { content: ''; position: absolute; left: 0; top: 0; width: 8px; height: 100%; background: var(--accent); }
        
        .cta-big { font-size: 36px; font-weight: 500; color: #F3F4F6; line-height: 1.4; margin-bottom: 60px; }
        .cta-big .hl { color: white; font-weight: 700; border-bottom: 2px solid var(--accent); }
        
        .cta-btn { background: var(--accent); color: white; padding: 20px 40px; font-size: 22px; font-weight: 700; border-radius: 4px; display: inline-flex; align-items: center; gap: 16px; letter-spacing: 0.5px; }
    """, """
        <div style="height: 100%; padding: 40px 0;">
            <div class="cta-dark-box">
                <div class="cta-big">
                    If hiring freshers is taking <span class="hl">more time, cost, and effort</span> than expected — we can help streamline it.
                </div>
                
                <div class="cta-btn">
                    Let’s run a pilot cohort <i class="fa-solid fa-arrow-right"></i>
                </div>
            </div>
        </div>
    """)

if __name__ == "__main__":
    build_slides()
    print("Successfully built 11 McKinsey-style Enterprise Infographic slides.")

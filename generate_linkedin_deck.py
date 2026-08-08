import os
import re

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\linkedin_optimization_deck"
slides_dir = os.path.join(base_dir, "slides")
os.makedirs(slides_dir, exist_ok=True)

# Common HTML Template for slides
def get_slide_html(title, content_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta content="width=1280, height=720" name="viewport" />
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet" />
    <style>
        body, html {{
            margin: 0; padding: 0; width: 1280px; height: 720px; overflow: hidden;
            font-family: 'Inter', sans-serif; background: #FFFDF9; color: #111111;
        }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Poppins', sans-serif; color: #111111; }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(220, 38, 38, 0.15);
            border-radius: 16px;
            box-shadow: 0 10px 30px -10px rgba(220, 38, 38, 0.05);
        }}
        
        .accent-text {{ color: #DC2626; }}
        .emerald-text {{ color: #111111; }}
        
        .gradient-bg {{
            background: radial-gradient(circle at top right, rgba(220, 38, 38, 0.08), transparent 45%),
                        radial-gradient(circle at bottom left, rgba(17, 17, 17, 0.05), transparent 45%),
                        #FFFDF9;
        }}
    
        /* Brand Light Theme Utility Overrides */
        .text-white {{ color: #111111 !important; }}
        .text-slate-100 {{ color: #111111 !important; }}
        .text-slate-200 {{ color: #1F2937 !important; }}
        .text-slate-300 {{ color: #4B5563 !important; }}
        .text-slate-400 {{ color: #6B7280 !important; }}
        .text-slate-500 {{ color: #9CA3AF !important; }}
        
        /* Accent elements map to brand Red & Black */
        .text-blue-400 {{ color: #B91C1C !important; }}
        .text-emerald-400 {{ color: #111111 !important; }}
        .text-purple-400 {{ color: #991B1B !important; }}
        .text-yellow-400 {{ color: #DC2626 !important; }}
        .text-red-400 {{ color: #DC2626 !important; }}
        .text-pink-400 {{ color: #B91C1C !important; }}
        
        .bg-blue-500\/10 {{ background-color: rgba(220, 38, 38, 0.08) !important; }}
        .bg-emerald-500\/10 {{ background-color: rgba(17, 17, 17, 0.05) !important; }}
        .bg-purple-500\/10 {{ background-color: rgba(185, 28, 28, 0.08) !important; }}
        .bg-yellow-500\/10 {{ background-color: rgba(220, 38, 38, 0.08) !important; }}
        .bg-red-950\/20 {{ background-color: rgba(220, 38, 38, 0.05) !important; }}
        .bg-red-950\/5 {{ background-color: rgba(220, 38, 38, 0.03) !important; }}
        .bg-emerald-950\/5 {{ background-color: rgba(17, 17, 17, 0.03) !important; }}
        .bg-blue-950\/20 {{ background-color: rgba(220, 38, 38, 0.05) !important; }}
        .bg-yellow-950\/10 {{ background-color: rgba(220, 38, 38, 0.08) !important; }}
        .bg-yellow-950\/5 {{ background-color: rgba(220, 38, 38, 0.04) !important; }}
        .bg-purple-950\/20 {{ background-color: rgba(185, 28, 28, 0.05) !important; }}
        
        .bg-slate-900 {{ background-color: #FAF6EE !important; border: 1px solid rgba(220, 38, 38, 0.1) !important; }}
        .bg-slate-900\/50 {{ background-color: rgba(255, 255, 255, 0.6) !important; }}
        .bg-slate-900\/30 {{ background-color: rgba(255, 255, 255, 0.5) !important; }}
        .bg-slate-800 {{ background-color: #FAF6EE !important; border: 1px solid rgba(220, 38, 38, 0.1) !important; }}
        .bg-slate-800\/50 {{ background-color: rgba(255, 255, 255, 0.5) !important; }}
        .bg-slate-950\/20 {{ background-color: rgba(17, 17, 17, 0.02) !important; }}
        
        .border-slate-700 {{ border-color: rgba(220, 38, 38, 0.15) !important; }}
        .border-slate-700\/50 {{ border-color: rgba(220, 38, 38, 0.1) !important; }}
        
        .border-t-blue-500 {{ border-top-color: #DC2626 !important; }}
        .border-t-emerald-500 {{ border-top-color: #111111 !important; }}
        .border-t-purple-500 {{ border-top-color: #B91C1C !important; }}
        .border-t-yellow-500 {{ border-top-color: #DC2626 !important; }}
        .border-t-blue-400 {{ border-top-color: #DC2626 !important; }}
        .border-t-emerald-400 {{ border-top-color: #111111 !important; }}
        .border-t-purple-400 {{ border-top-color: #B91C1C !important; }}
        .border-t-yellow-400 {{ border-top-color: #DC2626 !important; }}
        .border-t-pink-400 {{ border-top-color: #991B1B !important; }}
        
        .border-l-blue-500 {{ border-left-color: #DC2626 !important; }}
        .border-l-emerald-500 {{ border-left-color: #111111 !important; }}
        .border-l-purple-500 {{ border-left-color: #B91C1C !important; }}
        .border-l-yellow-500 {{ border-left-color: #DC2626 !important; }}
        .border-l-red-500 {{ border-left-color: #DC2626 !important; }}
        .border-l-blue-400 {{ border-left-color: #DC2626 !important; }}
        
        .divide-slate-800 > :not([hidden]) ~ :not([hidden]) {{
            border-color: rgba(220, 38, 38, 0.1) !important;
        }}
        
        body.light-mode {{
            background: #FFFDF9 !important;
            color: #111111 !important;
        }}
    </style>
</head>
<body class="gradient-bg flex items-center justify-center">
    {content_html}
    <script src="../../js/capture_helper.js"></script>
    <script src="../../js/theme_helper.js"></script>
</body>
</html>"""

slides_data = {
    # 1. Title Slide
    "slide_1.html": ("Your Digital Identity Gets You the Interview", """
        <div class="text-center max-w-4xl px-8">
            <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-slate-700 bg-slate-800/50 text-slate-300 text-sm mb-6 uppercase tracking-wider">
                <i class="fab fa-linkedin text-blue-400 text-lg"></i> LinkedIn Optimization Session
            </div>
            <h1 class="text-6xl font-extrabold mb-6 tracking-tight leading-tight">
                Your Digital Identity <br><span class="text-blue-400">Gets You the Interview</span>
            </h1>
            <div class="w-32 h-1 bg-gradient-to-r from-blue-500 to-emerald-400 mx-auto mb-8 rounded-full"></div>
            <p class="text-2xl font-light text-slate-300 mb-12 tracking-wide">
                Resume × LinkedIn × GitHub × <span class="font-semibold text-white">Proof of Work</span>
            </p>
            
            <div class="glass-card p-6 max-w-2xl mx-auto italic text-slate-300 border-l-4 border-l-blue-500">
                "Today, I am not going to teach you how to make your LinkedIn profile look good. I am going to show you how a recruiter can decide whether you are worth talking to — before you ever enter the interview room."
            </div>
        </div>
    """),

    # 2. Reality Check (Part 1)
    "slide_2.html": ("Start with the Harsh Reality", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-10">
                <h2 class="text-4xl font-bold border-l-8 border-blue-500 pl-6">Start with the Harsh Reality</h2>
                <span class="text-slate-400 text-sm font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">Checklist Part 1</span>
            </div>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full">
                <div class="glass-card p-6 flex items-start gap-4 hover:border-blue-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400 flex-shrink-0">
                        <i class="fab fa-linkedin text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">LinkedIn Presence</h3>
                        <p class="text-slate-300 text-sm">"How many of you actually have a LinkedIn profile?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-blue-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400 flex-shrink-0">
                        <i class="fas fa-user-circle text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Profile Photo</h3>
                        <p class="text-slate-300 text-sm">"How many of you have a professional profile picture?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-blue-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400 flex-shrink-0">
                        <i class="fas fa-image text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Profile Banner</h3>
                        <p class="text-slate-300 text-sm">"How many have a proper, meaningful banner?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-blue-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400 flex-shrink-0">
                        <i class="fas fa-pen-nib text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">About Section</h3>
                        <p class="text-slate-300 text-sm">"How many have written a structured, personal About section?"</p>
                    </div>
                </div>
            </div>
        </div>
    """),

    # 3. Reality Check (Part 2)
    "slide_3.html": ("The Technical Gap Check", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-10">
                <h2 class="text-4xl font-bold border-l-8 border-emerald-500 pl-6 font-poppins">The Technical Gap Check</h2>
                <span class="text-slate-400 text-sm font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">Checklist Part 2</span>
            </div>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full">
                <div class="glass-card p-6 flex items-start gap-4 hover:border-emerald-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400 flex-shrink-0">
                        <i class="fas fa-tools text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Built & Shared</h3>
                        <p class="text-slate-300 text-sm">"How many have posted something that you actually built?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-emerald-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400 flex-shrink-0">
                        <i class="fas fa-award text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Beyond Certificates</h3>
                        <p class="text-slate-300 text-sm">"How many have posted something OTHER than a certificate?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-emerald-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400 flex-shrink-0">
                        <i class="fab fa-github text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">GitHub Presence</h3>
                        <p class="text-slate-300 text-sm">"How many of you actually have a GitHub profile?"</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-start gap-4 hover:border-emerald-500 transition-all">
                    <div class="w-12 h-12 rounded-lg bg-emerald-500/10 flex items-center justify-center text-emerald-400 flex-shrink-0">
                        <i class="fas fa-code-branch text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold text-white mb-2">Pushed Code</h3>
                        <p class="text-slate-300 text-sm">"How many have actually pushed their projects to GitHub?"</p>
                    </div>
                </div>
            </div>
        </div>
    """),

    # 4. The Invisible Effort
    "slide_4.html": ("The Invisible Effort", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-12 text-slate-100">The Problem of <span class="text-red-400">Invisible Effort</span></h2>
            
            <div class="grid grid-cols-5 gap-8 items-center max-w-5xl">
                <div class="col-span-2 glass-card p-8 text-center border-t-4 border-t-blue-500">
                    <span class="text-slate-400 uppercase tracking-widest text-xs font-semibold block mb-2">Structured Training</span>
                    <span class="text-6xl font-extrabold text-blue-400 block mb-4">150+ <span class="text-2xl font-semibold">Hours</span></span>
                    <span class="text-slate-200 font-medium">Learning Excel, SQL, Python & Power BI</span>
                </div>
                
                <div class="col-span-3 text-left space-y-6">
                    <p class="text-2xl font-light leading-relaxed text-slate-200">
                        "But if <span class="font-semibold text-white border-b-2 border-b-yellow-500 pb-1">nobody can see</span> what you are learning, what you are building and how you think..."
                    </p>
                    <div class="glass-card p-6 bg-red-950/20 border-red-500/20 flex gap-4 items-center">
                        <i class="fas fa-eye-slash text-red-400 text-3xl"></i>
                        <span class="text-xl font-bold text-red-400">...then a large part of that effort remains invisible.</span>
                    </div>
                </div>
            </div>
        </div>
    """),

    # 5. Behind the Scenes - Screening Funnel
    "slide_5.html": ("Behind the Scenes: Screening Funnel", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 text-center">Behind the Scenes: The Screening Funnel</h2>
            
            <div class="grid grid-cols-3 gap-8 max-w-5xl mx-auto w-full relative">
                <!-- Funnel Step 1 -->
                <div class="glass-card p-6 text-center flex flex-col justify-between border-t-4 border-t-blue-500">
                    <div>
                        <div class="w-12 h-12 bg-blue-500/10 rounded-full flex items-center justify-center mx-auto text-blue-400 font-bold mb-4">1</div>
                        <h3 class="text-2xl font-bold text-white mb-4">Resume Screening</h3>
                        <p class="text-slate-300 text-sm mb-4">"Your resume may get only a few seconds of initial attention."</p>
                    </div>
                    <ul class="text-left text-xs space-y-2 border-t border-slate-700/50 pt-4 text-slate-400">
                        <li class="flex items-center gap-2"><i class="fas fa-check text-blue-400"></i> Is it relevant?</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-blue-400"></i> Is it readable?</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-blue-400"></i> Suitable layout?</li>
                    </ul>
                </div>
                
                <!-- Funnel Step 2 -->
                <div class="glass-card p-6 text-center flex flex-col justify-between border-t-4 border-t-emerald-500 transform scale-105 shadow-xl bg-slate-900/50">
                    <div>
                        <div class="w-12 h-12 bg-emerald-500/10 rounded-full flex items-center justify-center mx-auto text-emerald-400 font-bold mb-4">2</div>
                        <h3 class="text-2xl font-bold text-emerald-400 mb-4">Digital Presence</h3>
                        <p class="text-slate-200 text-sm mb-4">Recruiter searches your name online to verify background.</p>
                    </div>
                    <ul class="text-left text-xs space-y-2 border-t border-emerald-500/20 pt-4 text-slate-300">
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> LinkedIn Professional Profile</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> GitHub Active Code</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Case Studies & Proof of Work</li>
                    </ul>
                </div>
                
                <!-- Funnel Step 3 -->
                <div class="glass-card p-6 text-center flex flex-col justify-between border-t-4 border-t-purple-500">
                    <div>
                        <div class="w-12 h-12 bg-purple-500/10 rounded-full flex items-center justify-center mx-auto text-purple-400 font-bold mb-4">3</div>
                        <h3 class="text-2xl font-bold text-white mb-4">The Interview</h3>
                        <p class="text-slate-300 text-sm mb-4">The final step to prove capability and culture fit.</p>
                    </div>
                    <ul class="text-left text-xs space-y-2 border-t border-slate-700/50 pt-4 text-slate-400">
                        <li class="flex items-center gap-2"><i class="fas fa-check text-purple-400"></i> Technical Validation</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-purple-400"></i> Communication & Thinking</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-purple-400"></i> Alignment check</li>
                    </ul>
                </div>
            </div>
        </div>
    """),

    # 6. Candidate A vs Candidate B
    "slide_6.html": ("Candidate A vs Candidate B", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 text-center">Same GPA, Same Skills. <span class="text-blue-400">Who Gets the Call?</span></h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full">
                <!-- Candidate A -->
                <div class="glass-card p-6 border-l-4 border-l-red-500">
                    <div class="flex items-center gap-3 mb-4">
                        <i class="fas fa-user-slash text-red-500 text-2xl"></i>
                        <h3 class="text-xl font-bold text-slate-200">Candidate A (No Evidence)</h3>
                    </div>
                    <ul class="space-y-3 text-sm text-slate-400">
                        <li class="flex items-center gap-2"><i class="fas fa-times text-red-500"></i> LinkedIn → 0 posts</li>
                        <li class="flex items-center gap-2"><i class="fas fa-times text-red-500"></i> Empty/No About section</li>
                        <li class="flex items-center gap-2"><i class="fas fa-times text-red-500"></i> Casual profile photo</li>
                        <li class="flex items-center gap-2"><i class="fas fa-times text-red-500"></i> No projects uploaded</li>
                        <li class="flex items-center gap-2"><i class="fas fa-times text-red-500"></i> No GitHub activity / link</li>
                    </ul>
                </div>
                
                <!-- Candidate B -->
                <div class="glass-card p-6 border-l-4 border-l-emerald-500 bg-emerald-950/5">
                    <div class="flex items-center gap-3 mb-4">
                        <i class="fas fa-user-check text-emerald-400 text-2xl"></i>
                        <h3 class="text-xl font-bold text-white">Candidate B (Evidence-Driven)</h3>
                    </div>
                    <ul class="space-y-3 text-sm text-slate-200">
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> LinkedIn → Professional Profile</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Clear & Structured About Section</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Weekly Data Analysis posts</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Public GitHub with code repositories</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Case studies & Hackathon participations</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center bg-blue-950/20 py-4 max-w-5xl mx-auto w-full rounded-xl border border-blue-500/20">
                <span class="text-slate-300">Both candidates completed the same courses. But Candidate B has:</span>
                <span class="font-extrabold text-2xl text-blue-400 ml-2 tracking-wider">EVIDENCE.</span>
            </div>
        </div>
    """),

    # 7. LinkedIn is NOT your online resume
    "slide_7.html": ("LinkedIn is NOT Your Online Resume", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">Understanding the Identity</h2>
            
            <div class="grid grid-cols-2 gap-8 items-center max-w-5xl">
                <div class="space-y-4">
                    <div class="glass-card p-5 border-l-4 border-l-red-500 flex items-center gap-4 bg-red-950/5">
                        <i class="fas fa-times-circle text-red-500 text-2xl"></i>
                        <span class="text-lg font-semibold text-slate-300">LinkedIn is NOT a Certificate Gallery</span>
                    </div>
                    
                    <div class="glass-card p-5 border-l-4 border-l-red-500 flex items-center gap-4 bg-red-950/5">
                        <i class="fas fa-times-circle text-red-500 text-2xl"></i>
                        <span class="text-lg font-semibold text-slate-300">LinkedIn is NOT Instagram</span>
                    </div>
                    
                    <div class="glass-card p-5 border-l-4 border-l-red-500 flex items-center gap-4 bg-red-950/5">
                        <i class="fas fa-times-circle text-red-500 text-2xl"></i>
                        <span class="text-lg font-semibold text-slate-300">LinkedIn is NOT an Online Resume</span>
                    </div>
                </div>
                
                <div class="glass-card p-8 border-t-4 border-t-emerald-500 bg-slate-900/50 space-y-4">
                    <div class="flex items-center gap-3">
                        <i class="fas fa-check-circle text-emerald-400 text-3xl"></i>
                        <h3 class="text-2xl font-bold text-white">The Truth</h3>
                    </div>
                    <p class="text-xl font-light text-slate-200 leading-relaxed">
                        LinkedIn is your <span class="font-bold text-emerald-400">Professional Identity</span>, your interactive <span class="font-bold text-emerald-400">Proof of Work</span>, and your live <span class="font-bold text-emerald-400">Professional Network</span>.
                    </p>
                </div>
            </div>
        </div>
    """),

    # 8. The Evidence Matrix
    "slide_8.html": ("The Evidence Matrix", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-12 text-center">The Evidence Matrix</h2>
            
            <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto w-full">
                <div class="glass-card p-6 text-center border-b-4 border-b-blue-500">
                    <i class="fas fa-award text-3xl text-blue-400 mb-4 block"></i>
                    <h3 class="font-bold text-lg text-white mb-2">Certificates</h3>
                    <div class="h-px bg-slate-700 my-3"></div>
                    <p class="text-slate-300 text-sm">Proof that you completed something.</p>
                </div>
                
                <div class="glass-card p-6 text-center border-b-4 border-b-emerald-500">
                    <i class="fas fa-project-diagram text-3xl text-emerald-400 mb-4 block"></i>
                    <h3 class="font-bold text-lg text-white mb-2">Projects</h3>
                    <div class="h-px bg-slate-700 my-3"></div>
                    <p class="text-slate-300 text-sm">Proof that you can apply something.</p>
                </div>
                
                <div class="glass-card p-6 text-center border-b-4 border-b-purple-500">
                    <i class="fas fa-lightbulb text-3xl text-purple-400 mb-4 block"></i>
                    <h3 class="font-bold text-lg text-white mb-2">Posts</h3>
                    <div class="h-px bg-slate-700 my-3"></div>
                    <p class="text-slate-300 text-sm">Proof of how you think.</p>
                </div>
                
                <div class="glass-card p-6 text-center border-b-4 border-b-yellow-500">
                    <i class="fab fa-github text-3xl text-yellow-400 mb-4 block"></i>
                    <h3 class="font-bold text-lg text-white mb-2">GitHub</h3>
                    <div class="h-px bg-slate-700 my-3"></div>
                    <p class="text-slate-300 text-sm">Proof that you actually built it.</p>
                </div>
            </div>
            
            <div class="mt-8 text-center italic text-slate-400">
                Stop posting endless certifications alone. Mix them with built projects and conceptual writing.
            </div>
        </div>
    """),

    # 9. Fix the Foundation - Profile Photo
    "slide_9.html": ("Profile Photo Guidelines", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">Fix the Foundation: Profile Photo</h2>
            
            <div class="grid grid-cols-2 gap-12 max-w-5xl items-center">
                <div class="glass-card p-6 border-l-4 border-l-red-500 bg-red-950/5 space-y-4">
                    <h3 class="font-bold text-lg text-slate-200 flex items-center gap-2"><i class="fas fa-times-circle text-red-500"></i> What to Avoid</h3>
                    <ul class="grid grid-cols-2 gap-3 text-xs text-slate-400">
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Sunglasses / Hats</li>
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Casual Selfies</li>
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Wedding/Event pics</li>
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Cropped groups</li>
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Instagram poses</li>
                        <li class="flex items-center gap-2"><i class="fas fa-minus text-red-400"></i> Gaming / Anime</li>
                    </ul>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-emerald-500 bg-emerald-950/5 space-y-4">
                    <h3 class="font-bold text-lg text-white flex items-center gap-2"><i class="fas fa-check-circle text-emerald-400"></i> The Standard</h3>
                    <ul class="space-y-2 text-sm text-slate-200">
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Good natural lighting or soft ring light</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Clean, neutral background</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Face takes up 60% of the frame</li>
                        <li class="flex items-center gap-2"><i class="fas fa-check text-emerald-400"></i> Professional or smart casual clothing</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center text-xl font-semibold text-slate-300">
                Core Question: <span class="text-blue-400">"Would I be comfortable placing this photograph next to my resume?"</span>
            </div>
        </div>
    """),

    # 10. AI Headshot Demo
    "slide_10.html": ("AI Headshot Demo", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-purple-500 pl-6">AI Headshots: Enhance, Don't Invent</h2>
            
            <div class="grid grid-cols-5 gap-8 max-w-5xl items-center">
                <div class="col-span-2 glass-card p-6 text-center border-t-4 border-t-purple-500 space-y-4">
                    <div class="text-5xl text-purple-400"><i class="fas fa-magic"></i></div>
                    <h3 class="font-bold text-xl text-white">AI Tools Can Help</h3>
                    <p class="text-xs text-slate-400">Optimize background, lighting, and clothing in seconds using AI editing tools.</p>
                </div>
                
                <div class="col-span-3 space-y-6">
                    <h3 class="text-2xl font-bold text-white">Correct AI Usage Parameters:</h3>
                    
                    <div class="grid grid-cols-2 gap-4 text-sm">
                        <div class="glass-card p-4">
                            <span class="text-emerald-400 font-bold block mb-1">✅ DO ENHANCE</span>
                            <span class="text-slate-300 text-xs">Lighting, backgrounds, background noise, framing, or clothing formal wear.</span>
                        </div>
                        <div class="glass-card p-4">
                            <span class="text-red-400 font-bold block mb-1">❌ DO NOT GENERATE</span>
                            <span class="text-slate-300 text-xs">A completely different person or an unrealistic caricature of yourself.</span>
                        </div>
                    </div>
                    
                    <div class="bg-purple-950/20 border border-purple-500/20 p-4 rounded-xl text-center text-purple-300 italic font-medium">
                        "Recruiters should recognize you immediately when they see you in the interview room."
                    </div>
                </div>
            </div>
        </div>
    """),

    # 11. LinkedIn Banner
    "slide_11.html": ("LinkedIn Banner Blueprint", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Fix the Foundation: LinkedIn Banner</h2>
            
            <div class="glass-card p-8 max-w-5xl mx-auto w-full space-y-6">
                <div class="text-center pb-4 border-b border-slate-700/50">
                    <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block mb-2">The Formula</span>
                    <span class="text-2xl font-bold text-white">WHO YOU ARE  +  WHAT YOU DO  +  WHERE YOU ARE GOING</span>
                </div>
                
                <div class="space-y-4">
                    <span class="text-xs uppercase tracking-widest text-blue-400 font-semibold block">Realistic Example:</span>
                    <div class="bg-slate-900 border border-slate-700 p-6 rounded-xl relative overflow-hidden flex flex-col justify-between min-h-[140px] text-center">
                        <div class="absolute inset-0 bg-gradient-to-r from-blue-900/10 to-transparent"></div>
                        <div class="text-xl font-bold text-white tracking-wide">ASPIRING DATA ANALYST</div>
                        <div class="text-sm text-slate-400 mt-2 font-medium">Excel | SQL | Python | Power BI</div>
                        <div class="text-emerald-400 text-sm mt-3 font-semibold">"Turning Data → Insights → Decisions"</div>
                    </div>
                </div>
                
                <div class="grid grid-cols-2 gap-6 text-xs text-slate-400">
                    <div class="flex items-center gap-2"><i class="fas fa-info-circle text-blue-400"></i> Include your portfolio, Github URL, or area of specialization.</div>
                    <div class="flex items-center gap-2"><i class="fas fa-exclamation-triangle text-yellow-500"></i> Avoid using generic motivational quote wallpapers. Keep it professional.</div>
                </div>
            </div>
        </div>
    """),

    # 12. Headline
    "slide_12.html": ("The Headline Formula", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Fix the Foundation: Headline</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl items-center">
                <div class="space-y-6">
                    <div class="glass-card p-6 border-l-4 border-l-red-500 bg-red-950/5">
                        <span class="text-red-400 font-bold block mb-2 uppercase text-xs tracking-wider">❌ Wasted Space Headline</span>
                        <span class="text-xl font-medium text-slate-300">"Student at KPRIT"</span>
                        <p class="text-xs text-slate-500 mt-2">Tells recruiters nothing about your capabilities or interests.</p>
                    </div>
                    
                    <div class="glass-card p-6 border-l-4 border-l-emerald-500 bg-emerald-950/5">
                        <span class="text-emerald-400 font-bold block mb-2 uppercase text-xs tracking-wider">✅ Structured Formula</span>
                        <div class="text-sm text-slate-300 font-semibold bg-slate-900 p-3 rounded-lg border border-slate-700">
                            [Current Identity]  |  [Skills]  |  [Area of Interest]  |  [Proof/Goal]
                        </div>
                    </div>
                </div>
                
                <div class="glass-card p-8 border-t-4 border-t-blue-500 space-y-4">
                    <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block">Full Example:</span>
                    <h3 class="text-2xl font-bold text-white leading-normal">
                        "B.Tech Student | Aspiring Data Analyst | Excel • SQL • Python • Power BI | Building Data Projects"
                    </h3>
                    <div class="h-px bg-slate-700/50 my-4"></div>
                    <p class="text-xs text-slate-400">
                        This tells the recruiter exactly what you do, what tools you are training in, and your career direction.
                    </p>
                </div>
            </div>
        </div>
    """),

    # 13. About Section
    "slide_13.html": ("The About Section", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-emerald-500 pl-6">Fix the Foundation: About Section</h2>
            
            <div class="grid grid-cols-5 gap-8 max-w-5xl items-center">
                <div class="col-span-3 space-y-4">
                    <h3 class="text-2xl font-bold text-white mb-2">Write with a clear flow:</h3>
                    
                    <div class="grid grid-cols-2 gap-4 text-xs font-semibold uppercase tracking-wider text-center">
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg text-slate-300">1. Who I Am</div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg text-slate-300">2. What I Know</div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg text-slate-300">3. What I am Building</div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg text-slate-300">4. What I Seek</div>
                    </div>
                </div>
                
                <div class="col-span-2 glass-card p-6 border-t-4 border-t-blue-500 space-y-4 bg-slate-900/50">
                    <span class="text-blue-400 font-bold block uppercase text-xs tracking-wider">The Payoff</span>
                    <p class="text-slate-200 text-sm leading-relaxed">
                        "You don't need to write this from scratch. Your <span class="font-bold text-white">Student DNA Report</span> will give you a personalized starting point."
                    </p>
                    <div class="text-xs text-slate-400 border-t border-slate-800 pt-3">
                        Use it as a base, then rewrite in your personal voice.
                    </div>
                </div>
            </div>
        </div>
    """),

    # 14. Education Entry
    "slide_14.html": ("Education Entry Details", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Fix the Foundation: Education</h2>
            
            <div class="grid grid-cols-3 gap-8 max-w-5xl mx-auto w-full">
                <!-- College (Dominate) -->
                <div class="glass-card p-6 border-t-4 border-t-blue-500 col-span-1 flex flex-col justify-between bg-slate-900/50">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-blue-400 font-semibold block mb-2">Dominates Entry</span>
                        <h3 class="text-xl font-bold text-white mb-4">College Entry</h3>
                    </div>
                    <ul class="text-xs space-y-2 text-slate-300">
                        <li><i class="fas fa-check text-blue-400 mr-2"></i> Degree & Field of Study</li>
                        <li><i class="fas fa-check text-blue-400 mr-2"></i> Start / End Year</li>
                        <li><i class="fas fa-check text-blue-400 mr-2"></i> Relevant Activities</li>
                        <li><i class="fas fa-check text-blue-400 mr-2"></i> Core Achievements / Clubs</li>
                    </ul>
                </div>
                
                <!-- Intermediate / 12th -->
                <div class="glass-card p-6 border-t-4 border-t-slate-500 col-span-1 flex flex-col justify-between opacity-80 hover:opacity-100 transition-opacity">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block mb-2">For completeness</span>
                        <h3 class="text-xl font-bold text-slate-200 mb-4">Intermediate / 12th</h3>
                    </div>
                    <ul class="text-xs space-y-2 text-slate-400">
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> School / College</li>
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> Stream details</li>
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> Years active</li>
                    </ul>
                </div>
                
                <!-- Schooling -->
                <div class="glass-card p-6 border-t-4 border-t-slate-500 col-span-1 flex flex-col justify-between opacity-80 hover:opacity-100 transition-opacity">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block mb-2">For completeness</span>
                        <h3 class="text-xl font-bold text-slate-200 mb-4">Schooling</h3>
                    </div>
                    <ul class="text-xs space-y-2 text-slate-400">
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> School name</li>
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> Stream details</li>
                        <li><i class="fas fa-check text-slate-500 mr-2"></i> Years active</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center text-slate-400 text-sm italic">
                College entry dominates. Intermediate and school entries are there for credibility, not as major selling points.
            </div>
        </div>
    """),

    # 15. Skills: Relevance Over Quantity
    "slide_15.html": ("Skills Selection", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Fix the Foundation: Skills</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl items-center">
                <div class="glass-card p-6 border-l-4 border-l-red-500 bg-red-950/5">
                    <span class="text-red-400 font-bold block mb-2 uppercase text-xs tracking-wider">❌ Avoid Random Lists</span>
                    <div class="flex flex-wrap gap-2 text-xs text-slate-500">
                        <span class="border border-slate-700 px-2 py-1 rounded">C</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">HTML</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">CSS</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">Java</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">Python</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">MS Word</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">Teamwork</span>
                        <span class="border border-slate-700 px-2 py-1 rounded">Communication</span>
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-emerald-500 bg-emerald-950/5 space-y-4">
                    <span class="text-emerald-400 font-bold block uppercase text-xs tracking-wider">✅ Relevant Skills (AnalytIQ)</span>
                    <div class="flex flex-wrap gap-2 text-xs text-slate-200">
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">Microsoft Excel</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">SQL</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">Python</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">Power BI</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">Data Cleaning</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">Data Visualization</span>
                        <span class="bg-emerald-500/10 border border-emerald-500/30 px-2 py-1 rounded">EDA</span>
                    </div>
                </div>
            </div>
            
            <div class="mt-8 text-center text-slate-400 text-sm">
                Your skills section should support the professional identity you want to be hired for. <span class="text-white font-bold">Relevance > Quantity</span>.
            </div>
        </div>
    """),

    # 16. Profile Hierarchy
    "slide_16.html": ("Profile Hierarchy", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 text-center">Profile Content Hierarchy</h2>
            
            <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto w-full">
                <div class="glass-card p-6 border-t-4 border-t-blue-500 text-center flex flex-col justify-between">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-blue-400 font-semibold block mb-2">Strongest</span>
                        <h3 class="text-xl font-bold text-white mb-4">Experience</h3>
                    </div>
                    <p class="text-slate-400 text-xs">Work experience, internships, or structured co-op roles.</p>
                </div>
                
                <div class="glass-card p-6 border-t-4 border-t-emerald-500 text-center flex flex-col justify-between">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-emerald-400 font-semibold block mb-2">High Strength</span>
                        <h3 class="text-xl font-bold text-white mb-4">Projects</h3>
                    </div>
                    <p class="text-slate-400 text-xs">Structured, end-to-end built applications or dashboard projects.</p>
                </div>
                
                <div class="glass-card p-6 border-t-4 border-t-purple-500 text-center flex flex-col justify-between">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-purple-400 font-semibold block mb-2">Medium Strength</span>
                        <h3 class="text-xl font-bold text-white mb-4">Achievements</h3>
                    </div>
                    <p class="text-slate-400 text-xs">Hackathons, case study competitions, or academic wins.</p>
                </div>
                
                <div class="glass-card p-6 border-t-4 border-t-slate-500 text-center flex flex-col justify-between opacity-80">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block mb-2">Supporting</span>
                        <h3 class="text-xl font-bold text-white mb-4">Certifications</h3>
                    </div>
                    <p class="text-slate-400 text-xs">Completed courses and certifications that support your skills.</p>
                </div>
            </div>
        </div>
    """),

    # 17. What Should You Post? The Story of Data
    "slide_17.html": ("The Story of Data", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 text-center">What Should You Post? The Story of Data</h2>
            
            <div class="grid grid-cols-5 gap-4 max-w-5xl mx-auto w-full text-center">
                <div class="glass-card p-4 flex flex-col justify-between min-h-[140px] border-b-4 border-b-slate-600">
                    <span class="text-xs uppercase font-bold text-slate-400">Step 1</span>
                    <span class="text-xl font-bold text-slate-200">Raw Data</span>
                    <p class="text-slate-400 text-xs">Unstructured rows and columns.</p>
                </div>
                
                <div class="glass-card p-4 flex flex-col justify-between min-h-[140px] border-b-4 border-b-blue-500">
                    <span class="text-xs uppercase font-bold text-blue-400">Step 2</span>
                    <span class="text-xl font-bold text-blue-400">Sorted</span>
                    <p class="text-slate-400 text-xs">Arranged by hierarchies.</p>
                </div>
                
                <div class="glass-card p-4 flex flex-col justify-between min-h-[140px] border-b-4 border-b-purple-500">
                    <span class="text-xs uppercase font-bold text-purple-400">Step 3</span>
                    <span class="text-xl font-bold text-purple-400">Arranged</span>
                    <p class="text-slate-400 text-xs">Structured for correlation.</p>
                </div>
                
                <div class="glass-card p-4 flex flex-col justify-between min-h-[140px] border-b-4 border-b-emerald-500">
                    <span class="text-xs uppercase font-bold text-emerald-400">Step 4</span>
                    <span class="text-xl font-bold text-emerald-400">Visualized</span>
                    <p class="text-slate-400 text-xs">Clear chart representation.</p>
                </div>
                
                <div class="glass-card p-4 flex flex-col justify-between min-h-[140px] border-b-4 border-b-yellow-500 bg-yellow-950/10">
                    <span class="text-xs uppercase font-bold text-yellow-400">Step 5</span>
                    <span class="text-xl font-bold text-yellow-400">Tells a Story</span>
                    <p class="text-slate-400 text-xs">Reveals actionable business insights.</p>
                </div>
            </div>
            
            <div class="mt-10 text-center bg-blue-950/20 py-4 max-w-4xl mx-auto w-full rounded-xl border border-blue-500/20">
                <span class="text-slate-300">Your profile path should follow this transition:</span>
                <span class="font-extrabold text-white ml-2">Student → Learner → Builder → Analyst → Professional.</span>
            </div>
        </div>
    """),

    # 18. Post Categories 1 & 2
    "slide_18.html": ("7 Post Categories (Part 1)", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">Post Categories (Part 1)</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl">
                <!-- Learning Posts -->
                <div class="glass-card p-6 border-l-4 border-l-blue-500 bg-slate-900/50 space-y-4">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-blue-500/10 rounded-lg flex items-center justify-center text-blue-400 font-bold">1</div>
                        <h3 class="text-xl font-bold text-white">① Learning Posts</h3>
                    </div>
                    <p class="text-sm text-slate-300">Something concrete you understood in class.</p>
                    <div class="bg-slate-900 border border-slate-700/50 p-4 rounded-lg text-xs italic text-slate-400">
                        "Today I finally understood why XLOOKUP is more robust than VLOOKUP..."
                    </div>
                </div>
                
                <!-- Project Posts -->
                <div class="glass-card p-6 border-l-4 border-l-emerald-500 bg-slate-900/50 space-y-4">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-emerald-500/10 rounded-lg flex items-center justify-center text-emerald-400 font-bold">2</div>
                        <h3 class="text-xl font-bold text-white">② Project Posts</h3>
                    </div>
                    <p class="text-sm text-slate-300">Walkthrough of something you built.</p>
                    <div class="bg-slate-900 border border-slate-700/50 p-4 rounded-lg text-xs font-mono text-slate-400 space-y-1">
                        <span class="text-emerald-400 block font-bold">Problem → Dataset → Approach → Insights</span>
                        <span>Avoid generic "Happy to share completed project" templates.</span>
                    </div>
                </div>
            </div>
        </div>
    """),

    # 19. Post Category 3 - Case Studies
    "slide_19.html": ("7 Post Categories (Part 2)", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-purple-500 pl-6">Post Categories (Part 2)</h2>
            
            <div class="grid grid-cols-5 gap-8 items-center max-w-5xl">
                <div class="col-span-3 space-y-4">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 bg-purple-500/10 rounded-lg flex items-center justify-center text-purple-400 font-bold">3</div>
                        <h3 class="text-2xl font-bold text-white">③ Case Study Posts</h3>
                    </div>
                    <p class="text-slate-300 text-sm">Push beyond simple student content. Analyze hypothetical business cases using public datasets.</p>
                    
                    <ul class="text-xs space-y-2 text-slate-400">
                        <li><i class="fas fa-chevron-right text-purple-400 mr-2"></i> "What can Netflix learn from its viewing data?"</li>
                        <li><i class="fas fa-chevron-right text-purple-400 mr-2"></i> "How would a supermarket identify profitable customers?"</li>
                        <li><i class="fas fa-chevron-right text-purple-400 mr-2"></i> "What metrics would I track as an analyst at Deloitte?"</li>
                    </ul>
                </div>
                
                <div class="col-span-2 glass-card p-6 border-t-4 border-t-purple-500 bg-slate-900/50">
                    <span class="text-purple-400 font-bold block mb-2 uppercase text-xs">How to label:</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        You don't need internal company access. Create analysis exercises using public datasets and label them clearly: <span class="font-bold text-white">"Case Study Exercise"</span>.
                    </p>
                </div>
            </div>
        </div>
    """),

    # 20. Excel Content Ideas
    "slide_20.html": ("Excel Post Ideas", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-4xl font-bold border-l-8 border-blue-500 pl-6">Excel Content (Start Right Now)</h2>
                <span class="text-slate-400 text-xs font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">Excel Track</span>
            </div>
            
            <div class="grid grid-cols-3 gap-6 max-w-5xl mx-auto w-full text-xs">
                <div class="glass-card p-4 space-y-2 border-l-2 border-l-blue-400 bg-slate-900/30">
                    <h3 class="font-bold text-white text-sm">Beginner & Intermediate</h3>
                    <ul class="space-y-1.5 text-slate-300">
                        <li>• VLOOKUP vs XLOOKUP comparison</li>
                        <li>• Why Pivot Tables are powerful</li>
                        <li>• VLOOKUP limitations in big files</li>
                    </ul>
                </div>
                
                <div class="glass-card p-4 space-y-2 border-l-2 border-l-blue-400 bg-slate-900/30">
                    <h3 class="font-bold text-white text-sm">Data Cleaning</h3>
                    <ul class="space-y-1.5 text-slate-300">
                        <li>• 5 mistakes I made while cleaning data</li>
                        <li>• How I cleaned a messy dataset</li>
                        <li>• Transforming 10,000 messy rows</li>
                    </ul>
                </div>
                
                <div class="glass-card p-4 space-y-2 border-l-2 border-l-blue-400 bg-slate-900/30">
                    <h3 class="font-bold text-white text-sm">Business Insights</h3>
                    <ul class="space-y-1.5 text-slate-300">
                        <li>• From raw Excel data to dashboard</li>
                        <li>• Using Excel to answer business questions</li>
                        <li>• Why Excel is still relevant in 2026</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center bg-red-950/20 border border-red-500/20 py-3 rounded-lg max-w-4xl mx-auto w-full text-red-400 font-bold text-sm">
                ⚠️ Avoid making generic "10 Excel formulas everyone should know" content farm posts. Make them think!
            </div>
        </div>
    """),

    # 21. SQL Content Ideas
    "slide_21.html": ("SQL Post Ideas", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-4xl font-bold border-l-8 border-emerald-500 pl-6">SQL Content Ideas</h2>
                <span class="text-slate-400 text-xs font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">SQL Track</span>
            </div>
            
            <div class="grid grid-cols-2 gap-6 max-w-5xl mx-auto w-full text-sm">
                <div class="glass-card p-6 space-y-3">
                    <h3 class="font-bold text-emerald-400 text-lg">Solving Business Problems</h3>
                    <ul class="space-y-2 text-slate-300 text-xs">
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> "How I solved a customer retention problem using SQL"</li>
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> SQL Joins explained through a real business example</li>
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> Finding top and repeat customers from transactional DBs</li>
                    </ul>
                </div>
                
                <div class="glass-card p-6 space-y-3">
                    <h3 class="font-bold text-emerald-400 text-lg">Query Concepts & Optimization</h3>
                    <ul class="space-y-2 text-slate-300 text-xs">
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> WHERE vs HAVING: The execution sequence difference</li>
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> What GROUP BY actually does under the hood</li>
                        <li><i class="fas fa-code text-slate-500 mr-2"></i> One SQL bug I struggled with and how I fixed it</li>
                    </ul>
                </div>
            </div>
        </div>
    """),

    # 22. Python Content Ideas
    "slide_22.html": ("Python Post Ideas", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-4xl font-bold border-l-8 border-purple-500 pl-6">Python Content Ideas</h2>
                <span class="text-slate-400 text-xs font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">Python Track</span>
            </div>
            
            <div class="grid grid-cols-3 gap-6 max-w-5xl mx-auto w-full text-xs">
                <div class="glass-card p-5 border-t-2 border-t-purple-500 space-y-3">
                    <h4 class="font-bold text-white">Pandas vs Excel</h4>
                    <p class="text-slate-400 text-xs">Explain when to use Pandas libraries and when Excel is faster.</p>
                </div>
                
                <div class="glass-card p-5 border-t-2 border-t-purple-500 space-y-3">
                    <h4 class="font-bold text-white">Automating Tasks</h4>
                    <p class="text-slate-400 text-xs">Explain how you automated a repetitive data scrubbing task using python scripts.</p>
                </div>
                
                <div class="glass-card p-5 border-t-2 border-t-purple-500 space-y-3">
                    <h4 class="font-bold text-white">Notebook Walkthroughs</h4>
                    <p class="text-slate-400 text-xs">Share screenshots of your first Exploratory Data Analysis notebook on clean datasets.</p>
                </div>
            </div>
        </div>
    """),

    # 23. Power BI Content Ideas
    "slide_23.html": ("Power BI Post Ideas", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center justify-between mb-8">
                <h2 class="text-4xl font-bold border-l-8 border-yellow-500 pl-6">Power BI Content Ideas</h2>
                <span class="text-slate-400 text-xs font-semibold uppercase tracking-widest bg-slate-800 px-4 py-2 rounded-lg">Power BI Track</span>
            </div>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full text-sm">
                <div class="glass-card p-6 border-l-4 border-l-yellow-500 space-y-4">
                    <h3 class="font-bold text-white">Highly Visual Posts</h3>
                    <ul class="space-y-3 text-slate-300 text-xs">
                        <li><i class="fas fa-image text-yellow-500 mr-2"></i> Before → After dashboard redesign comparison</li>
                        <li><i class="fas fa-image text-yellow-500 mr-2"></i> The conceptual data model behind my dashboard</li>
                        <li><i class="fas fa-image text-yellow-500 mr-2"></i> Why I chose these specific KPIs for my business case</li>
                    </ul>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-yellow-500 space-y-4">
                    <h3 class="font-bold text-white">Technical Deep Dives</h3>
                    <ul class="space-y-3 text-slate-300 text-xs">
                        <li><i class="fas fa-calculator text-yellow-500 mr-2"></i> A DAX context calculation problem I solved today</li>
                        <li><i class="fas fa-calculator text-yellow-500 mr-2"></i> Power Query data transformation pipelines</li>
                        <li><i class="fas fa-calculator text-yellow-500 mr-2"></i> Turning a request query into an active visual card</li>
                    </ul>
                </div>
            </div>
        </div>
    """),

    # 24. Non-Technical & Humanity Posts
    "slide_24.html": ("Humanizing Your Profile", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-emerald-500 pl-6">Humanizing Your Profile</h2>
            
            <div class="grid grid-cols-5 gap-8 max-w-5xl items-center">
                <div class="col-span-3 space-y-4">
                    <p class="text-lg text-slate-200">Don't post only code. Show the human behind the keyboard:</p>
                    
                    <div class="grid grid-cols-2 gap-3 text-xs text-slate-400">
                        <div class="glass-card p-3"><i class="fas fa-users text-emerald-400 mr-2"></i> Class participation photos</div>
                        <div class="glass-card p-3"><i class="fas fa-trophy text-emerald-400 mr-2"></i> Hackathon / Team builds</div>
                        <div class="glass-card p-3"><i class="fas fa-comments text-emerald-400 mr-2"></i> Mentor sessions & keynotes</div>
                        <div class="glass-card p-3"><i class="fas fa-lightbulb text-emerald-400 mr-2"></i> Weekly learning reflections</div>
                    </div>
                </div>
                
                <div class="col-span-2 glass-card p-6 border-t-4 border-t-emerald-500 bg-slate-900/50 space-y-3">
                    <span class="text-emerald-400 font-bold block uppercase text-xs">Post Example:</span>
                    <p class="text-xs italic text-slate-300 leading-relaxed font-mono">
                        "I spent 2 hours trying to fix a dashboard today and realized the problem wasn't Power BI. My data model was wrong..."
                    </p>
                    <div class="text-[10px] text-slate-500">
                        *This is far better than "Successfully completed dashboard" posts.*
                    </div>
                </div>
            </div>
        </div>
    """),

    # 25. Build in Public
    "slide_25.html": ("Build in Public", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 text-center">The "Build in Public" Strategy</h2>
            
            <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto w-full text-center">
                <div class="glass-card p-5 flex flex-col justify-between min-h-[160px] border-t-4 border-t-blue-500">
                    <div>
                        <span class="text-blue-400 font-bold text-xs uppercase block mb-1">Week 1-2</span>
                        <h4 class="font-bold text-white text-sm">Documenting Excel</h4>
                    </div>
                    <p class="text-[11px] text-slate-400">"Started learning data cleaning structures."</p>
                </div>
                
                <div class="glass-card p-5 flex flex-col justify-between min-h-[160px] border-t-4 border-t-emerald-500">
                    <div>
                        <span class="text-emerald-400 font-bold text-xs uppercase block mb-1">Week 3-4</span>
                        <h4 class="font-bold text-white text-sm">First Dashboard</h4>
                    </div>
                    <p class="text-[11px] text-slate-400">"Built my first analytical workbook dashboard."</p>
                </div>
                
                <div class="glass-card p-5 flex flex-col justify-between min-h-[160px] border-t-4 border-t-purple-500">
                    <div>
                        <span class="text-purple-400 font-bold text-xs uppercase block mb-1">Month 2</span>
                        <h4 class="font-bold text-white text-sm">Starting SQL Queries</h4>
                    </div>
                    <p class="text-[11px] text-slate-400">"Learning relational queries to fetch DB data."</p>
                </div>
                
                <div class="glass-card p-5 flex flex-col justify-between min-h-[160px] border-t-4 border-t-yellow-500 bg-yellow-950/5">
                    <div>
                        <span class="text-yellow-400 font-bold text-xs uppercase block mb-1">Month 3</span>
                        <h4 class="font-bold text-white text-sm">End-to-End Build</h4>
                    </div>
                    <p class="text-[11px] text-slate-400">"Built my first full database analyst workbook."</p>
                </div>
            </div>
            
            <div class="mt-8 text-center text-slate-300 text-sm">
                Recruiters checking your profile see a timeline of <span class="text-emerald-400 font-bold">continuous progress</span>, not a stale student page.
            </div>
        </div>
    """),

    # 26. AnalytIQ as Content Engine
    "slide_26.html": ("AnalytIQ Content Engine", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">AnalytIQ as Your Content Engine</h2>
            
            <div class="grid grid-cols-5 gap-8 max-w-5xl items-center">
                <div class="col-span-3 space-y-4">
                    <p class="text-lg text-slate-200">Your structured schedule literally feeds you topics:</p>
                    
                    <div class="grid grid-cols-2 gap-3 text-xs font-semibold">
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg">
                            <span class="text-blue-400 block mb-1">Tuesday</span>
                            Class → Learning Post
                        </div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg">
                            <span class="text-blue-400 block mb-1">Wednesday</span>
                            Practice → Insight Post
                        </div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg">
                            <span class="text-blue-400 block mb-1">Thursday</span>
                            Class → Learning Post
                        </div>
                        <div class="bg-slate-900 border border-slate-700 p-4 rounded-lg">
                            <span class="text-blue-400 block mb-1">Saturday</span>
                            Case Study / Reflection
                        </div>
                    </div>
                </div>
                
                <div class="col-span-2 glass-card p-6 border-t-4 border-t-emerald-500 bg-emerald-950/5 text-center space-y-4">
                    <span class="text-emerald-400 font-bold block uppercase text-xs tracking-wider">Sustainable Goal</span>
                    <span class="text-4xl font-extrabold text-white block">2 Posts / <span class="text-lg font-normal text-slate-400">Week</span></span>
                    <p class="text-xs text-slate-400">Avoid daily posting. Focus on quality to avoid burnout within two weeks.</p>
                </div>
            </div>
        </div>
    """),

    # 27. Class Photo Strategy
    "slide_27.html": ("Class Photo Strategy", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">The Class Photo Strategy</h2>
            
            <div class="grid grid-cols-5 gap-8 items-center max-w-5xl">
                <div class="col-span-2 glass-card p-6 text-center border-t-4 border-t-blue-500 space-y-4">
                    <div class="text-5xl text-blue-400"><i class="fas fa-camera"></i></div>
                    <h3 class="font-bold text-xl text-white">Leverage Discord Assets</h3>
                    <p class="text-xs text-slate-400">The Sketch Brains team uploads classroom photos to Discord regularly. Use them!</p>
                </div>
                
                <div class="col-span-3 space-y-4">
                    <h3 class="text-2xl font-bold text-white">How to structure your post:</h3>
                    
                    <div class="bg-slate-900 border border-slate-700/50 p-5 rounded-lg text-xs space-y-2 text-slate-300 font-mono">
                        <div><span class="text-emerald-400">Line 1:</span> "Day 6 of my AnalytIQ journey..."</div>
                        <div><span class="text-emerald-400">Line 2:</span> "Today we worked on [Topic/Formula]..."</div>
                        <div><span class="text-emerald-400">Line 3:</span> "The most interesting thing I understood was..."</div>
                        <div><span class="text-emerald-400">Line 4:</span> "One thing I initially struggled with was..."</div>
                    </div>
                    
                    <p class="text-xs text-slate-400 italic">This instantly forms a timeline of active academic development.</p>
                </div>
            </div>
        </div>
    """),

    # 28. Connections Strategy
    "slide_28.html": ("Connections: Build a Network", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Connections: Build a Relevant Network</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full items-center">
                <div class="space-y-4">
                    <h3 class="text-xl font-bold text-white mb-2">1. Target Audience Priority:</h3>
                    <div class="flex flex-wrap gap-2 text-xs">
                        <span class="bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-full text-slate-300">1. Batchmates</span>
                        <span class="bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-full text-slate-300">2. Seniors</span>
                        <span class="bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-full text-slate-300">3. Alumni</span>
                        <span class="bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-full text-slate-300">4. Industry Professionals</span>
                        <span class="bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-full text-slate-300">5. Recruiters</span>
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-blue-500 space-y-4 bg-slate-900/50">
                    <span class="text-blue-400 font-bold block uppercase text-xs">Personalized Connection Request:</span>
                    <p class="text-[11px] italic text-slate-300 leading-relaxed font-mono">
                        "Hi Rahul, I came across your profile while exploring alumni working in analytics. I'm currently developing my skills in Excel, SQL, Python, and Power BI through the AnalytIQ program. I'd be glad to connect and learn from your journey."
                    </p>
                    <div class="text-[10px] text-slate-500">*Avoid generic "Hi, connect with me" notes.*</div>
                </div>
            </div>
        </div>
    """),

    # 29. GitHub - The Verification Vault
    "slide_29.html": ("GitHub Repository Structure", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-emerald-500 pl-6">GitHub: The Verification Vault</h2>
            
            <div class="grid grid-cols-5 gap-8 max-w-5xl items-center">
                <div class="col-span-2 glass-card p-6 space-y-4 bg-slate-900/50">
                    <h3 class="font-bold text-white text-sm">Suggested Structure:</h3>
                    <ul class="space-y-2 text-xs text-slate-300 font-mono">
                        <li>📁 /Excel <span class="text-slate-500">(sheets, dashboards)</span></li>
                        <li>📁 /SQL <span class="text-slate-500">(queries, case studies)</span></li>
                        <li>📁 /Python <span class="text-slate-500">(notebooks, scripts)</span></li>
                        <li>📁 /PowerBI <span class="text-slate-500">(PBIX files, screenshots)</span></li>
                    </ul>
                </div>
                
                <div class="col-span-3 space-y-4">
                    <h3 class="text-2xl font-bold text-white">Every project needs a robust README:</h3>
                    <div class="grid grid-cols-2 gap-3 text-xs text-slate-400">
                        <div class="glass-card p-3"><i class="fas fa-tag text-emerald-400 mr-2"></i> Problem Statement</div>
                        <div class="glass-card p-3"><i class="fas fa-database text-emerald-400 mr-2"></i> Dataset Description</div>
                        <div class="glass-card p-3"><i class="fas fa-toolbox text-emerald-400 mr-2"></i> Tools & Techniques</div>
                        <div class="glass-card p-3"><i class="fas fa-chart-line text-emerald-400 mr-2"></i> Analysis & Key Insights</div>
                    </div>
                </div>
            </div>
        </div>
    """),

    # 30. Student DNA Report
    "slide_30.html": ("The Student DNA Report", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-purple-500 pl-6 font-poppins text-white">The Student DNA Report</h2>
            
            <div class="grid grid-cols-2 gap-12 max-w-5xl items-center">
                <div class="space-y-4">
                    <p class="text-xl font-light text-slate-200 leading-relaxed">
                        "Everything I just showed you isn't theoretical. Our team has already looked at your profiles."
                    </p>
                    <div class="bg-purple-950/20 border border-purple-500/20 p-4 rounded-xl text-center text-purple-300 font-bold text-lg">
                        Today, every one of you receives your report!
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-purple-500 space-y-4 bg-slate-900/50">
                    <span class="text-purple-400 font-bold block uppercase text-xs tracking-wider">What you will find inside:</span>
                    <ul class="text-xs space-y-2 text-slate-300">
                        <li><i class="fas fa-info-circle text-purple-400 mr-2"></i> **Your Current Profile:** A snapshot of today.</li>
                        <li><i class="fas fa-exclamation-triangle text-purple-400 mr-2"></i> **Your Gaps:** Missing profile segments.</li>
                        <li><i class="fas fa-check-circle text-purple-400 mr-2"></i> **Personalized Recommendations:** Exact changes to make.</li>
                        <li><i class="fas fa-magic text-purple-400 mr-2"></i> **Custom Bio / Headlines:** Ready to copy and refine.</li>
                    </ul>
                </div>
            </div>
        </div>
    """),

    # 31. Connect back to Sketch Brains
    "slide_31.html": ("Connect Back to Sketch Brains", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-10 border-l-8 border-blue-500 pl-6">Connect Back to Sketch Brains</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl mx-auto w-full items-center">
                <div class="space-y-4 text-slate-200">
                    <p class="text-lg">We are going to train you technically over the next few months.</p>
                    <p class="text-sm text-slate-400 leading-relaxed">
                        But we don't want to create students who know Excel and SQL and then disappear into the crowd. We want your work, thinking, and progress to be highly visible.
                    </p>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-blue-500 space-y-3 bg-slate-900/50">
                    <span class="text-blue-400 font-bold block uppercase text-xs">Use us. Ask us any questions:</span>
                    <ul class="text-xs space-y-1.5 text-slate-300">
                        <li>• "I don't know how to write this LinkedIn post..."</li>
                        <li>• "I don't know how to push code to GitHub..."</li>
                        <li>• "How do I structure my project repository?"</li>
                        <li>• "I don't know what topic to post on..."</li>
                    </ul>
                    <div class="text-[10px] text-slate-500 pt-2 border-t border-slate-800">No question is too simple. We are here to support your execution.</div>
                </div>
            </div>
        </div>
    """),

    # 32. ChatGPT Workflow
    "slide_32.html": ("ChatGPT Optimization Workflow", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-6 border-l-8 border-purple-500 pl-6">How to Use AI Correctly</h2>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl">
                <!-- Bad way -->
                <div class="glass-card p-5 border-t-4 border-t-red-500 bg-red-950/5 space-y-2">
                    <span class="text-red-400 font-bold text-xs uppercase block">❌ The Bad Prompt Way</span>
                    <div class="bg-slate-900 p-3 rounded text-[11px] font-mono text-slate-400">
                        "Write me a LinkedIn post about Excel."
                    </div>
                    <p class="text-xs text-slate-500">Result: Generates generic corporate text that reads exactly like everyone else's.</p>
                </div>
                
                <!-- Good way -->
                <div class="glass-card p-5 border-t-4 border-t-emerald-500 bg-emerald-950/5 space-y-2 text-xs">
                    <span class="text-emerald-400 font-bold text-xs uppercase block">✅ The 4-Step Prompt Workflow</span>
                    <ol class="space-y-1.5 text-slate-300 font-mono text-[10px]">
                        <li><span class="text-emerald-400">1. Think:</span> Select a specific topic (e.g. VLOOKUP limits).</li>
                        <li><span class="text-emerald-400">2. Write thoughts:</span> Note down raw facts, findings, frustrations.</li>
                        <li><span class="text-emerald-400">3. Structure:</span> Ask ChatGPT to organize preserving your voice.</li>
                        <li><span class="text-emerald-400">4. Humanize:</span> "Make it sound like a student sharing learnings."</li>
                    </ol>
                </div>
            </div>
            
            <div class="mt-6 text-center text-lg font-bold bg-purple-950/20 border border-purple-500/20 py-3 rounded-lg max-w-4xl mx-auto w-full text-purple-300">
                "AI should amplify your thinking. It should not replace your thinking."
            </div>
        </div>
    """),

    # 33. The LinkedIn Challenge
    "slide_33.html": ("Today's LinkedIn Challenge", """
        <div class="w-full h-full px-20 flex flex-col justify-center text-center">
            <div class="inline-block px-4 py-1.5 bg-yellow-500/10 border border-yellow-500/30 rounded-full text-yellow-400 text-sm font-semibold mb-6 uppercase tracking-wider">
                🚀 Action Required
            </div>
            <h2 class="text-5xl font-extrabold mb-8 text-white">Today's LinkedIn Challenge</h2>
            
            <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto w-full text-xs mb-10">
                <div class="glass-card p-4 border-b-2 border-b-yellow-500">
                    <div class="w-8 h-8 rounded-full bg-yellow-500/10 text-yellow-400 font-bold flex items-center justify-center mx-auto mb-2 text-sm">1</div>
                    <h3 class="font-bold text-white text-sm mb-1">Choose Topic</h3>
                    <p class="text-slate-400 text-[10px]">Pick 1 from the 15 specific prompts.</p>
                </div>
                
                <div class="glass-card p-4 border-b-2 border-b-yellow-500">
                    <div class="w-8 h-8 rounded-full bg-yellow-500/10 text-yellow-400 font-bold flex items-center justify-center mx-auto mb-2 text-sm">2</div>
                    <h3 class="font-bold text-white text-sm mb-1">Write Post</h3>
                    <p class="text-slate-400 text-[10px]">Explain, format professionally, use your voice.</p>
                </div>
                
                <div class="glass-card p-4 border-b-2 border-b-yellow-500">
                    <div class="w-8 h-8 rounded-full bg-yellow-500/10 text-yellow-400 font-bold flex items-center justify-center mx-auto mb-2 text-sm">3</div>
                    <h3 class="font-bold text-white text-sm mb-1">Publish</h3>
                    <p class="text-slate-400 text-[10px]">Add relevant visuals and post live on LinkedIn.</p>
                </div>
                
                <div class="glass-card p-4 border-b-2 border-b-yellow-500 bg-yellow-950/10">
                    <div class="w-8 h-8 rounded-full bg-yellow-500/10 text-yellow-400 font-bold flex items-center justify-center mx-auto mb-2 text-sm">4</div>
                    <h3 class="font-bold text-yellow-400 text-sm mb-1">Submit</h3>
                    <p class="text-slate-200 text-[10px]">Copy link to Discord. Earn leaderboard points!</p>
                </div>
            </div>
        </div>
    """),

    # 34. 15 challenge topics
    "slide_34.html": ("15 Challenge Topics", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-3xl font-poppins font-bold mb-6 border-l-8 border-blue-500 pl-4 text-white">Choose Your LinkedIn Challenge Topic</h2>
            
            <div class="grid grid-cols-5 gap-4 max-w-5xl mx-auto w-full text-[10px]">
                <!-- Excel -->
                <div class="glass-card p-3 space-y-2 border-t-2 border-t-blue-400">
                    <h4 class="font-bold text-blue-400 text-xs">Excel Track</h4>
                    <ul class="space-y-1 text-slate-300">
                        <li>01. Cleaned a messy dataset: what surprised me.</li>
                        <li>02. Pivot Tables are more powerful than I thought.</li>
                        <li>03. Answered a business question using Excel.</li>
                        <li>04. Excel: From 10k rows of data to 5 decisions.</li>
                    </ul>
                </div>
                
                <!-- Data Thinking -->
                <div class="glass-card p-3 space-y-2 border-t-2 border-t-emerald-400">
                    <h4 class="font-bold text-emerald-400 text-xs">Data Thinking</h4>
                    <ul class="space-y-1 text-slate-300">
                        <li>05. Beautiful dashboards are not always useful.</li>
                        <li>06. Difference between data and information.</li>
                        <li>07. How one dataset tells different stories.</li>
                        <li>08. What business metrics to track for e-commerce.</li>
                    </ul>
                </div>
                
                <!-- Career / Industry -->
                <div class="glass-card p-3 space-y-2 border-t-2 border-t-purple-400">
                    <h4 class="font-bold text-purple-400 text-xs">Career & Industry</h4>
                    <ul class="space-y-1 text-slate-300">
                        <li>09. Why analysts need business context over coding.</li>
                        <li>10. Why companies still rely heavily on Excel.</li>
                        <li>11. What elements form a good analytics dashboard.</li>
                    </ul>
                </div>
                
                <!-- Personal Learning -->
                <div class="glass-card p-3 space-y-2 border-t-2 border-t-yellow-400">
                    <h4 class="font-bold text-yellow-400 text-xs">Personal Learning</h4>
                    <ul class="space-y-1 text-slate-300">
                        <li>12. The biggest mistake I made while learning Excel.</li>
                        <li>13. 3 things I understand differently after starting.</li>
                        <li>14. What I learned from building my first project.</li>
                    </ul>
                </div>
                
                <!-- Storytelling -->
                <div class="glass-card p-3 space-y-2 border-t-2 border-t-pink-400">
                    <h4 class="font-bold text-pink-400 text-xs">Storytelling</h4>
                    <ul class="space-y-1 text-slate-300">
                        <li>15. Take a messy dataset and tell a story with it.</li>
                    </ul>
                </div>
            </div>
        </div>
    """),

    # 35. Milestone Evidence Table
    "slide_35.html": ("Repeatable Evidence System", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h2 class="text-4xl font-bold mb-8 border-l-8 border-blue-500 pl-6">Repeatable Evidence System</h2>
            
            <div class="glass-card overflow-hidden max-w-5xl mx-auto w-full">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="bg-slate-900 border-b border-slate-700 text-slate-300 uppercase tracking-wider font-semibold">
                            <th class="p-4">Program Milestone (Activity)</th>
                            <th class="p-4">Expected Output (Evidence Location)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-800 text-slate-200">
                        <tr>
                            <td class="p-3 font-semibold">Excel Classes / Practices</td>
                            <td class="p-3 text-slate-400">LinkedIn weekly learning posts</td>
                        </tr>
                        <tr class="bg-slate-950/20">
                            <td class="p-3 font-semibold">Excel Portfolio Project</td>
                            <td class="p-3 text-slate-300"><i class="fab fa-linkedin text-blue-400 mr-1"></i> LinkedIn walkthrough + <i class="fab fa-github text-white mr-1"></i> GitHub repository</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold">SQL Project / Python Notebooks</td>
                            <td class="p-3 text-slate-300"><i class="fab fa-linkedin text-blue-400 mr-1"></i> LinkedIn breakdown + <i class="fab fa-github text-white mr-1"></i> GitHub repository</td>
                        </tr>
                        <tr class="bg-slate-950/20">
                            <td class="p-3 font-semibold">Power BI Dashboards</td>
                            <td class="p-3 text-slate-300"><i class="fab fa-linkedin text-blue-400 mr-1"></i> Dashboard video + <i class="fab fa-github text-white mr-1"></i> GitHub PBIX</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold">Hackathons / Competitions</td>
                            <td class="p-3 text-slate-400">LinkedIn highlight (what you built, team photo)</td>
                        </tr>
                        <tr class="bg-slate-950/20">
                            <td class="p-3 font-semibold">Final Capstone Project</td>
                            <td class="p-3 text-slate-300"><i class="fab fa-linkedin text-blue-400 mr-1"></i> LinkedIn + <i class="fab fa-github text-white mr-1"></i> GitHub + Personal Portfolio site</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    """),

    # 36. The Last 60 Seconds
    "slide_36.html": ("The Last 60 Seconds", """
        <div class="w-full h-full px-20 flex flex-col justify-center text-center">
            <h2 class="text-4xl font-extrabold mb-10 text-blue-400">Document the Person You Are Becoming Today</h2>
            
            <div class="glass-card p-8 max-w-4xl mx-auto w-full space-y-6 text-left">
                <p class="text-xl font-light leading-relaxed text-slate-200">
                    "Recruiters will not see the 150+ hours you spent sitting in classrooms. They won't see the query you spent two hours fixing. <span class="font-bold text-white border-b-2 border-b-blue-500 pb-0.5">Unless you show them.</span>"
                </p>
                <p class="text-sm text-slate-400 leading-normal">
                    Your resume claims. Your LinkedIn presents. Your GitHub verifies. Your projects demonstrate. Together, they create your professional evidence.
                </p>
            </div>
            
            <div class="mt-8 text-center text-emerald-400 font-bold text-lg">
                👉 "Open your Student DNA Report today. Find your gaps. Fix them. And publish your first post before this week ends."
            </div>
        </div>
    """)
}

# Write each slide file
for filename, (title, content) in slides_data.items():
    filepath = os.path.join(slides_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(get_slide_html(title, content))
    print(f"Created slide: {filename}")

print(f"Successfully generated {len(slides_data)} slides.")

# Now write the main index.html for linkedin_optimization_deck
index_html_content = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LinkedIn Optimization Session - Sketch Brains</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@300;400;600&display=swap"
        rel="stylesheet">
    <style>
        :root {
            --primary-color: #DC2626; /* Brand Red */
            --bg-color: #FFFDF9; /* Cream background */
            --text-color: #111111; /* Black text */
            --control-bg: #FAF6EE; /* Warm cream */
            --control-hover: rgba(220, 38, 38, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        /* Main Viewport */
        .deck-container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            padding: 20px;
            background-image: radial-gradient(rgba(220, 38, 38, 0.12) 1px, transparent 1px);
            background-size: 40px 40px;
            opacity: 1;
        }

        .slide-frame {
            position: absolute;
            left: 50%;
            top: 50%;
            width: 1280px;
            height: 720px;
            border: none;
            border-radius: 12px;
            background-color: white;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            transition: opacity 0.3s ease;
            transform-origin: center center;
        }

        /* Loading Overlay */
        .loading-overlay {
            position: absolute;
            inset: 0;
            background: var(--bg-color);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 50;
            transition: opacity 0.5s ease;
        }

        .loading-spinner {
            width: 50px;
            height: 50px;
            border: 4px solid #1e293b;
            border-top: 4px solid var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }
        }

        /* Controls */
        .controls-bar {
            height: 80px;
            background-color: #FAF6EE;
            border-top: 1px solid rgba(220, 38, 38, 0.15);
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            padding: 0 40px;
            z-index: 100;
        }

        .controls-left {
            display: flex;
            align-items: center;
            justify-content: flex-start;
        }

        .controls-center {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .controls-right {
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }

        .deck-info {
            display: flex;
            flex-direction: column;
        }

        .deck-title {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            color: #111111;
        }

        .deck-subtitle {
            font-size: 0.85rem;
            color: var(--primary-color);
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .nav-btn {
            background-color: #FAF6EE;
            color: #111111;
            border: 1px solid rgba(220, 38, 38, 0.2);
            width: 48px;
            height: 48px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 1.2rem;
        }

        .nav-btn:hover:not(:disabled) {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(220, 38, 38, 0.3);
        }

        .nav-btn:disabled {
            opacity: 0.4;
            cursor: not-allowed;
            background-color: #F5F2EB;
            color: #9CA3AF;
            border-color: rgba(220, 38, 38, 0.05);
        }

        .slide-counter {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            color: #111111;
            min-width: 60px;
            text-align: center;
        }

        .progress-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background-color: #F5F2EB;
        }

        .progress-bar {
            height: 100%;
            background-color: var(--primary-color);
            width: 0%;
            transition: width 0.3s ease;
            box-shadow: 0 0 10px var(--primary-color);
        }

        .fullscreen-btn {
            background: transparent;
            border: 1px solid transparent;
            color: #94a3b8;
            padding: 8px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .fullscreen-btn:hover {
            color: white;
            background-color: #334155;
        }

        /* Sidebar */
        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 280px;
            height: 100%;
            background-color: #FAF6EE;
            border-right: 1px solid rgba(220, 38, 38, 0.15);
            z-index: 1000;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            padding: 24px;
            box-shadow: 4px 0 15px rgba(220, 38, 38, 0.05);
        }

        .sidebar.open {
            transform: translateX(0);
        }

        .sidebar-header {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            color: #111111;
            font-size: 1.25rem;
            margin-bottom: 32px;
            padding-bottom: 16px;
            border-bottom: 1px solid rgba(220, 38, 38, 0.15);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .close-sidebar-btn {
            background: none;
            border: none;
            color: #6B7280;
            cursor: pointer;
            font-size: 1.2rem;
        }

        .close-sidebar-btn:hover {
            color: #111111;
        }

        .deck-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 12px;
            overflow-y: auto;
        }

        .deck-link {
            display: flex;
            align-items: center;
            padding: 12px 16px;
            border-radius: 8px;
            color: #4B5563;
            text-decoration: none;
            transition: all 0.2s;
            font-size: 0.95rem;
            border: 1px solid transparent;
        }

        .deck-link:hover {
            background-color: rgba(220, 38, 38, 0.05);
            color: #DC2626;
        }

        .deck-link.active {
            background-color: rgba(220, 38, 38, 0.08);
            border-color: var(--primary-color);
            color: var(--primary-color);
            font-weight: 600;
        }

        .deck-link i {
            margin-right: 12px;
            width: 20px;
            text-align: center;
        }

        .overlay {
            position: fixed;
            inset: 0;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 999;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            backdrop-filter: blur(2px);
        }

        .overlay.open {
            opacity: 1;
            pointer-events: auto;
        }

        .menu-toggle-btn {
            background: transparent;
            border: none;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            margin-right: 16px;
            padding: 8px;
            border-radius: 8px;
            transition: background 0.2s;
        }

        .menu-toggle-btn:hover {
            background-color: #334155;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .controls-bar {
                padding: 0 20px;
            }

            .deck-title {
                font-size: 0.9rem;
            }

            .deck-subtitle {
                display: none;
            }

            .slide-frame {
                border-radius: 0;
            }
        }
    </style>
</head>

<body>

    <!-- Sidebar Overlay -->
    <div class="overlay" id="sidebarOverlay"></div>

    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <span>Pitch Decks</span>
            <button class="close-sidebar-btn" id="closeSidebarBtn"><i class="fas fa-times"></i></button>
        </div>
        <ul class="deck-list" id="sidebarDeckList">
            <!-- Sidebar links will be dynamically populated/aligned -->
        </ul>
    </aside>

    <!-- Progress Bar -->
    <div class="progress-container">
        <div class="progress-bar" id="progressBar"></div>
    </div>

    <!-- Main Content -->
    <div class="deck-container">
        <div class="loading-overlay" id="loader">
            <div class="loading-spinner"></div>
        </div>
        <!-- Double buffer frames for smooth transitions and preloading -->
        <iframe class="slide-frame" id="slideFrameA" src="" title="Presentation Slide"></iframe>
        <iframe class="slide-frame" id="slideFrameB" src="" title="Presentation Slide"
            style="display: none; opacity: 0; position: absolute;"></iframe>

    </div>

    <!-- Controls -->
    <footer class="controls-bar">
        <div class="controls-left">
            <button class="menu-toggle-btn" id="menuToggleBtn" title="Open Menu">
                <i class="fas fa-bars"></i>
            </button>
            <div class="deck-info">
                <span class="deck-title">LinkedIn Optimization</span>
                <span class="deck-subtitle">Personal Identity & Evidence</span>
            </div>
        </div>

        <div class="controls-center nav-controls">
            <button class="nav-btn" id="prevBtn" title="Previous Slide (Arrow Left)">
                <i class="fas fa-arrow-left"></i>
            </button>

            <div class="slide-counter">
                <span id="currentSlideNum">1</span> / <span id="totalSlidesNum">--</span>
            </div>

            <button class="nav-btn" id="nextBtn" title="Next Slide (Arrow Right)">
                <i class="fas fa-arrow-right"></i>
            </button>

            <!-- Theme Toggle -->
            <button class="nav-btn" id="themeBtn" title="Toggle Dark Mode">
                <i class="fas fa-moon"></i>
            </button>

            <!-- Download PDF -->
            <button class="nav-btn" id="downloadBtn" title="Download PDF of all slides">
                <i class="fas fa-file-download"></i>
            </button>
        </div>

        <div class="controls-right">
            <button class="fullscreen-btn" id="fullscreenBtn" title="Toggle Fullscreen (F)">
                <i class="fas fa-expand"></i>
            </button>
        </div>
    </footer>

    <!-- PDF Tools Dependencies -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="../js/pdf_generator.js"></script>

    <script>
        const TOTAL_SLIDES = 36;
        let currentSlide = 1;
        let isDarkTheme = false; // Start in light brand theme
        let activeFrameId = 'slideFrameA';
        let preloadFrameId = 'slideFrameB';

        const LIGHT_THEME_CSS = `
            html { 
                filter: invert(1) hue-rotate(180deg); 
            }
            img, video, .no-invert { 
                filter: invert(1) hue-rotate(180deg); 
            }
            html { transition: filter 0.3s ease; }
        `;

        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const themeBtn = document.getElementById('themeBtn');
        const downloadBtn = document.getElementById('downloadBtn');
        const currentNumEl = document.getElementById('currentSlideNum');
        const totalNumEl = document.getElementById('totalSlidesNum');
        const progressBar = document.getElementById('progressBar');
        const loader = document.getElementById('loader');
        const fullscreenBtn = document.getElementById('fullscreenBtn');
        const menuToggleBtn = document.getElementById('menuToggleBtn');
        const closeSidebarBtn = document.getElementById('closeSidebarBtn');
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebarOverlay');

        document.addEventListener('DOMContentLoaded', () => {
            totalNumEl.textContent = TOTAL_SLIDES;
            loadSlideIntoFrame(activeFrameId, currentSlide, true);
            preloadNext();
            updateUI();
            themeBtn.querySelector('i').className = 'fas fa-moon';
            populateSidebar();
        });

        function getActiveFrame() { return document.getElementById(activeFrameId); }
        function getPreloadFrame() { return document.getElementById(preloadFrameId); }

        function loadSlideIntoFrame(frameId, slideIndex, isVisible) {
            const frame = document.getElementById(frameId);
            // Add cache buster query parameter to force reloading updated slides
            frame.src = `slides/slide_${slideIndex}.html?v=` + new Date().getTime();

            frame.onload = () => {
                const cssToSend = isDarkTheme ? LIGHT_THEME_CSS : '';
                sendThemeMessageToFrame(frame, cssToSend);

                try {
                    const iframeDoc = frame.contentDocument || frame.contentWindow.document;
                    iframeDoc.addEventListener('keydown', handleKeyDown);
                    if (isVisible) window.focus();
                } catch (e) { }
            };
        }

        function switchFrames() {
            const active = getActiveFrame();
            const preload = getPreloadFrame();

            const temp = activeFrameId;
            activeFrameId = preloadFrameId;
            preloadFrameId = temp;

            active.style.opacity = '0';
            setTimeout(() => { active.style.display = 'none'; }, 300);

            preload.style.display = 'block';
            void preload.offsetWidth;
            preload.style.opacity = '1';

            const cssToSend = isDarkTheme ? LIGHT_THEME_CSS : '';
            sendThemeMessageToFrame(preload, cssToSend);
        }

        function preloadNext() {
            if (currentSlide < TOTAL_SLIDES) {
                loadSlideIntoFrame(preloadFrameId, currentSlide + 1, false);
            }
        }

        function preloadPrev() {
            if (currentSlide > 1) {
                loadSlideIntoFrame(preloadFrameId, currentSlide - 1, false);
            }
        }

        function toggleTheme() {
            isDarkTheme = !isDarkTheme;
            const icon = themeBtn.querySelector('i');
            // Show sun icon if in dark mode, moon icon if in light mode
            icon.className = isDarkTheme ? 'fas fa-sun' : 'fas fa-moon';
            const cssToSend = isDarkTheme ? LIGHT_THEME_CSS : '';
            sendThemeMessageToFrame(getActiveFrame(), cssToSend);
            sendThemeMessageToFrame(getPreloadFrame(), cssToSend);
        }

        function sendThemeMessageToFrame(frame, css) {
            if (frame && frame.contentWindow) {
                frame.contentWindow.postMessage({
                    type: 'theme-update',
                    isDark: isDarkTheme,
                    css: css
                }, '*');
            }
        }

        function updateUI() {
            currentNumEl.textContent = currentSlide;
            const percentage = ((currentSlide - 1) / (TOTAL_SLIDES - 1)) * 100;
            progressBar.style.width = `${percentage}%`;
            prevBtn.disabled = currentSlide === 1;
            nextBtn.disabled = currentSlide === TOTAL_SLIDES;
        }

        function goToNext() {
            if (currentSlide < TOTAL_SLIDES) {
                currentSlide++;
                const nextFrame = getPreloadFrame();
                if (!nextFrame.src.includes(`slide_${currentSlide}.html`)) {
                    loadSlideIntoFrame(preloadFrameId, currentSlide, false);
                }
                switchFrames();
                preloadNext();
                updateUI();
            }
        }

        function goToPrev() {
            if (currentSlide > 1) {
                currentSlide--;
                const nextFrame = getPreloadFrame();
                if (!nextFrame.src.includes(`slide_${currentSlide}.html`)) {
                    loadSlideIntoFrame(preloadFrameId, currentSlide, false);
                }
                switchFrames();
                preloadPrev();
                updateUI();
            }
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
                fullscreenBtn.innerHTML = '<i class="fas fa-compress"></i>';
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                    fullscreenBtn.innerHTML = '<i class="fas fa-expand"></i>';
                }
            }
        }

        function handleKeyDown(e) {
            if (e.key === 'ArrowRight' || e.key === 'Space') {
                goToNext();
            } else if (e.key === 'ArrowLeft') {
                goToPrev();
            } else if (e.key.toLowerCase() === 'f') {
                toggleFullscreen();
            }
        }

        function downloadPitchDeck() {
            if (window.PDFTools) {
                const workerFrame = document.getElementById(preloadFrameId);
                window.PDFTools.generate(TOTAL_SLIDES, 'LinkedIn_Optimization_Session', 'slides/', workerFrame);
            } else {
                alert('PDF Tool not loaded correctly.');
            }
        }

        prevBtn.addEventListener('click', goToPrev);
        nextBtn.addEventListener('click', goToNext);
        fullscreenBtn.addEventListener('click', toggleFullscreen);
        themeBtn.addEventListener('click', toggleTheme);
        downloadBtn.addEventListener('click', downloadPitchDeck);
        document.addEventListener('keydown', handleKeyDown);

        function toggleSidebar() {
            sidebar.classList.toggle('open');
            sidebarOverlay.classList.toggle('open');
        }

        menuToggleBtn.addEventListener('click', toggleSidebar);
        closeSidebarBtn.addEventListener('click', toggleSidebar);
        sidebarOverlay.addEventListener('click', toggleSidebar);

        function resizeSlides() {
            const container = document.querySelector('.deck-container');
            const frames = document.querySelectorAll('.slide-frame');
            if (!container || frames.length === 0) return;

            const contentW = 1280;
            const contentH = 720;
            const availableW = container.clientWidth - 20;
            const availableH = container.clientHeight - 20;

            const scaleX = availableW / contentW;
            const scaleY = availableH / contentH;
            const scale = Math.min(scaleX, scaleY, 1.5);

            frames.forEach(frame => {
                frame.style.transform = `translate(-50%, -50%) scale(${scale})`;
            });
        }

        window.addEventListener('resize', resizeSlides);
        resizeSlides();
        setTimeout(resizeSlides, 100);

        setTimeout(() => {
            loader.style.opacity = '0';
            loader.style.pointerEvents = 'none';
        }, 800);

        const DECKS_LIST = [
            { path: "../cokarma_deck/index.html", title: "CoKarma Deck", icon: "fas fa-layer-group" },
            { path: "../hr_deck/index.html", title: "HR Deck", icon: "fas fa-users" },
            { path: "../faculty_deck/index.html", title: "Faculty Deck", icon: "fas fa-university" },
            { path: "../faculty_deck_2/index.html", title: "Faculty Deck 2", icon: "fas fa-chalkboard-teacher" },
            { path: "../smallcase_deck/index.html", title: "FactorLab Smallcase", icon: "fas fa-chart-line" },
            { path: "../sketch_brains_deck/index.html", title: "Sketch Brains (Student)", icon: "fas fa-brain" },
            { path: "../sketch_brains_investor_deck/index.html", title: "Sketch Brains Investor Deck", icon: "fas fa-wallet" },
            { path: "../sketch_brains_kprit_deck/index.html", title: "SB x KPRIT Keynote", icon: "fas fa-graduation-cap" },
            { path: "../sketch_brains_x_task_deck/index.html", title: "SB x TASK Blueprint", icon: "fas fa-rocket" },
            { path: "../sketch_brains_x_villa_marie_deck/index.html", title: "SB x Villa Marie", icon: "fas fa-graduation-cap" },
            { path: "../sketch_brains_x_company_deck/index.html", title: "SB x Company Pipeline", icon: "fas fa-handshake" },
            { path: "../hiring_hackathon_company_invite/index.html", title: "Hiring Hackathon Invitation", icon: "fas fa-building" },
            { path: "#", title: "LinkedIn Optimization", icon: "fab fa-linkedin text-red-500", active: true }
        ];

        function populateSidebar() {
            const listEl = document.getElementById('sidebarDeckList');
            listEl.innerHTML = '';
            DECKS_LIST.forEach(d => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = d.path;
                a.className = 'deck-link' + (d.active ? ' active' : '');
                a.innerHTML = `<i class="${d.icon}"></i> ${d.title}`;
                li.appendChild(a);
                listEl.appendChild(li);
            });
        }
    </script>
</body>

</html>
"""

index_filepath = os.path.join(base_dir, "index.html")
with open(index_filepath, "w", encoding="utf-8") as f:
    f.write(index_html_content)
print("Created new index.html for linkedin_optimization_deck")

# Define unified sidebars list
unified_decks_def = [
    {"folder": "cokarma_deck", "title": "CoKarma Deck", "icon": "fas fa-layer-group"},
    {"folder": "hr_deck", "title": "HR Deck", "icon": "fas fa-users"},
    {"folder": "faculty_deck", "title": "Faculty Deck", "icon": "fas fa-university"},
    {"folder": "faculty_deck_2", "title": "Faculty Deck 2", "icon": "fas fa-chalkboard-teacher"},
    {"folder": "smallcase_deck", "title": "FactorLab Smallcase", "icon": "fas fa-chart-line"},
    {"folder": "sketch_brains_deck", "title": "Sketch Brains (Student)", "icon": "fas fa-brain"},
    {"folder": "sketch_brains_investor_deck", "title": "Sketch Brains Investor Deck", "icon": "fas fa-wallet"},
    {"folder": "sketch_brains_kprit_deck", "title": "SB x KPRIT Keynote", "icon": "fas fa-graduation-cap"},
    {"folder": "sketch_brains_x_task_deck", "title": "SB x TASK Blueprint", "icon": "fas fa-rocket"},
    {"folder": "sketch_brains_x_villa_marie_deck", "title": "SB x Villa Marie", "icon": "fas fa-graduation-cap"},
    {"folder": "sketch_brains_x_company_deck", "title": "SB x Company Pipeline", "icon": "fas fa-handshake"},
    {"folder": "hiring_hackathon_company_invite", "title": "Hiring Hackathon Invitation", "icon": "fas fa-building"},
    {"folder": "linkedin_optimization_deck", "title": "LinkedIn Optimization", "icon": "fab fa-linkedin"}
]

# Update sidebars in all existing index.html files
root_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck"

for deck in unified_decks_def:
    folder = deck["folder"]
    target_idx = os.path.join(root_dir, folder, "index.html")
    if not os.path.exists(target_idx):
        print(f"Index file not found for updating: {target_idx}")
        continue
    
    with open(target_idx, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate <ul class="deck-list" ...> or just search for list block in sidebar
    # Let's search for <ul class="deck-list">...</ul> and replace it with a unified menu
    sidebar_match = re.search(r'<ul class="deck-list"[^>]*>([\s\S]*?)</ul>', content)
    if not sidebar_match:
        # Some might not have id or class exactly matching. Let's see if we can find it
        print(f"Could not locate sidebar deck-list in {target_idx}")
        continue
    
    # Generate custom list items for this index file.
    # The active one should have href="#" class="deck-link active"
    # Others should have href="../folder/index.html" class="deck-link"
    new_items_html = ""
    for idx_item in unified_decks_def:
        item_folder = idx_item["folder"]
        item_title = idx_item["title"]
        item_icon = idx_item["icon"]
        
        if item_folder == folder:
            # Active deck
            new_items_html += f"""            <li>
                <a href="#" class="deck-link active">
                    <i class="{item_icon}"></i>
                    {item_title}
                </a>
            </li>\n"""
        else:
            new_items_html += f"""            <li>
                <a href="../{item_folder}/index.html" class="deck-link">
                    <i class="{item_icon}"></i>
                    {item_title}
                </a>
            </li>\n"""
            
    # Keep attributes of the ul tag if there are any
    ul_tag_match = re.search(r'<ul class="deck-list"[^>]*>', content)
    ul_tag = ul_tag_match.group(0)
    
    replacement = f"{ul_tag}\n{new_items_html}        </ul>"
    content = content.replace(sidebar_match.group(0), replacement)
    
    with open(target_idx, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated sidebar in {target_idx}")

# Also update the root index.html to add the new LinkedIn card!
root_index_path = os.path.join(root_dir, "index.html")
if os.path.exists(root_index_path):
    with open(root_index_path, "r", encoding="utf-8") as f:
        root_content = f.read()
        
    # Check if LinkedIn Optimization card is already in root_content
    if "linkedin_optimization_deck" not in root_content:
        # We find the last card (e.g. Hiring Hackathon) or the end of the grid (before </div>\n\n    </div>\n\n</body>)
        # In root index.html, we saw the cards are inside <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        # Let's append the card right before the closing </div> of the grid.
        # Find the last closing tag.
        # A safer regex or replace: we saw the last card is:
        #             <!-- Hiring Hackathon Company Invite -->
        #             <a href="hiring_hackathon_company_invite/index.html"
        #                 ...
        #             </a>
        # Let's replace the closing grid division.
        # Let's search for "Hiring Hackathon Invitation</h3>" and trace to its closing "</a>"
        invite_card_match = re.search(r'<a href="hiring_hackathon_company_invite/index.html"[\s\S]*?</a>', root_content)
        if invite_card_match:
            linkedin_card_html = """
            
            <!-- LinkedIn Optimization Deck -->
            <a href="linkedin_optimization_deck/index.html"
                class="group block p-6 bg-slate-800/50 hover:bg-slate-800 border border-slate-700/50 hover:border-blue-500 rounded-2xl transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl hover:shadow-blue-900/20">
                <div
                    class="w-16 h-16 bg-blue-950/5 rounded-xl flex items-center justify-center mb-6 text-blue-400 group-hover:scale-110 transition-transform mx-auto">
                    <i class="fab fa-linkedin text-3xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-2 font-montserrat">LinkedIn Optimization</h3>
                <p class="text-sm text-slate-400 group-hover:text-blue-200/70">Personal Digital Identity & Proof of Work Workshop.</p>
            </a>"""
            
            new_root_content = root_content.replace(
                invite_card_match.group(0),
                invite_card_match.group(0) + linkedin_card_html
            )
            
            with open(root_index_path, "w", encoding="utf-8") as f:
                f.write(new_root_content)
            print("Successfully added LinkedIn Optimization card to root index.html")
        else:
            print("Could not find Hiring Hackathon invitation card in root index.html to insert after.")
else:
    print("Root index.html not found.")

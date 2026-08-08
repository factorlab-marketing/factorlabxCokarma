
import os

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides"
os.makedirs(base_dir, exist_ok=True)

# Common HTML Template (Same as Part 1)
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
            font-family: 'Inter', sans-serif; background: #0F172A; color: white;
        }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Poppins', sans-serif; }}
        
        .glass-card {{
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }}
        
        .accent-text {{ color: #3B82F6; }}
        .emerald-text {{ color: #10B981; }}
        
        .gradient-bg {{
            background: radial-gradient(circle at top right, rgba(59, 130, 246, 0.15), transparent 40%),
                        radial-gradient(circle at bottom left, rgba(16, 185, 129, 0.1), transparent 40%);
        }}
    </style>
</head>
<body class="gradient-bg flex items-center justify-center">
    {content_html}
</body>
</html>"""

slides_data = {
    "slide_15.html": ("6 Month Roadmap", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">The 6-Month Execution Roadmap</h1>
            
            <div class="w-full max-w-5xl relative">
                <div class="absolute top-1/2 left-0 right-0 h-1 bg-slate-700 transform -translate-y-1/2 z-0"></div>
                
                <div class="grid grid-cols-4 gap-4 relative z-10">
                    <div class="flex flex-col items-center group">
                        <div class="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center font-bold text-white mb-4 border-4 border-[#0F172A] shadow-lg group-hover:scale-110 transition-transform">1</div>
                        <div class="glass-card p-6 text-center w-full h-40 flex flex-col justify-center group-hover:border-blue-500 transition-colors">
                            <span class="text-blue-400 font-bold mb-1 uppercase text-xs tracking-wider">Month 1-2</span>
                            <span class="text-xl font-bold text-white">Foundations</span>
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-center group">
                        <div class="w-10 h-10 bg-indigo-500 rounded-full flex items-center justify-center font-bold text-white mb-4 border-4 border-[#0F172A] shadow-lg group-hover:scale-110 transition-transform">2</div>
                        <div class="glass-card p-6 text-center w-full h-40 flex flex-col justify-center group-hover:border-indigo-500 transition-colors">
                            <span class="text-indigo-400 font-bold mb-1 uppercase text-xs tracking-wider">Month 3-4</span>
                            <span class="text-xl font-bold text-white">Build 2 Projects</span>
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-center group">
                        <div class="w-10 h-10 bg-purple-500 rounded-full flex items-center justify-center font-bold text-white mb-4 border-4 border-[#0F172A] shadow-lg group-hover:scale-110 transition-transform">3</div>
                        <div class="glass-card p-6 text-center w-full h-40 flex flex-col justify-center group-hover:border-purple-500 transition-colors">
                            <span class="text-purple-400 font-bold mb-1 uppercase text-xs tracking-wider">Month 5</span>
                            <span class="text-xl font-bold text-white">Improve & Deploy</span>
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-center group">
                        <div class="w-10 h-10 bg-emerald-500 rounded-full flex items-center justify-center font-bold text-white mb-4 border-4 border-[#0F172A] shadow-lg group-hover:scale-110 transition-transform">4</div>
                        <div class="glass-card p-6 text-center w-full h-40 flex flex-col justify-center group-hover:border-emerald-500 transition-colors">
                            <span class="text-emerald-400 font-bold mb-1 uppercase text-xs tracking-wider">Month 6</span>
                            <span class="text-xl font-bold text-white">Resume + Apply</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-16 text-center">
                <span class="text-3xl font-light text-slate-300">Consistency beats <span class="font-bold text-white">intensity.</span></span>
            </div>
        </div>
    """),

    "slide_16.html": ("Choosing Between the 3 Roles", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h1 class="text-4xl font-bold mb-12 text-center">Which Role is Yours?</h1>
            
            <div class="grid grid-cols-3 gap-8 mb-12">
                <div class="glass-card p-8 hover:bg-white/5 transition-colors cursor-pointer group">
                    <h3 class="text-xl font-bold mb-4 text-blue-400 group-hover:text-blue-300">Software Engineer</h3>
                    <p class="text-slate-300 mb-6 text-sm">You like valid logic, building things from scratch, and seeing immediate results.</p>
                    <div class="bg-blue-500/10 p-3 rounded text-center text-blue-300 font-medium text-sm">"I like building apps"</div>
                </div>
                
                <div class="glass-card p-8 hover:bg-white/5 transition-colors cursor-pointer group">
                    <h3 class="text-xl font-bold mb-4 text-emerald-400 group-hover:text-emerald-300">Data Analyst</h3>
                    <p class="text-slate-300 mb-6 text-sm">You enjoy spotting patterns, organizing chaos, and influencing decisions with facts.</p>
                    <div class="bg-emerald-500/10 p-3 rounded text-center text-emerald-300 font-medium text-sm">"I like insights"</div>
                </div>
                
                <div class="glass-card p-8 hover:bg-white/5 transition-colors cursor-pointer group">
                    <h3 class="text-xl font-bold mb-4 text-purple-400 group-hover:text-purple-300">AI/ML Engineer</h3>
                    <p class="text-slate-300 mb-6 text-sm">You are curious about how machines learn, possess strong math/logic skills, and want to build the future.</p>
                    <div class="bg-purple-500/10 p-3 rounded text-center text-purple-300 font-medium text-sm">"I like intelligent systems"</div>
                </div>
            </div>
            
            <div class="text-center">
                <p class="text-slate-400 uppercase tracking-widest text-sm mb-4">Choose based on:</p>
                <div class="inline-flex space-x-8 text-xl font-semibold">
                    <span class="text-white">Interest</span>
                    <span class="text-white">Strength</span>
                    <span class="text-white">Learning Speed</span>
                </div>
                <p class="text-red-400 font-medium mt-4 text-sm">NOT TREND.</p>
            </div>
        </div>
    """),

    "slide_17.html": ("Resume Essentials (2026)", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">Resume Essentials <span class="text-blue-500">2026</span></h1>
            
            <div class="grid grid-cols-2 gap-16 max-w-5xl w-full">
                <div class="relative">
                    <div class="absolute -top-4 -left-4 bg-red-500 text-white font-bold px-3 py-1 rounded text-sm uppercase tracking-wider shadow-lg">Remove</div>
                    <div class="glass-card p-8 border border-red-500/30 h-full flex flex-col justify-center bg-red-900/5">
                        <ul class="space-y-6">
                            <li class="flex items-center text-lg text-slate-300"><i class="fas fa-times text-red-500 mr-4 text-xl"></i> Generic Objectives</li>
                            <li class="flex items-center text-lg text-slate-300"><i class="fas fa-times text-red-500 mr-4 text-xl"></i> School Achievements</li>
                            <li class="flex items-center text-lg text-slate-300"><i class="fas fa-times text-red-500 mr-4 text-xl"></i> Irrelevant Certificates</li>
                        </ul>
                    </div>
                </div>
                
                <div class="relative">
                    <div class="absolute -top-4 -left-4 bg-emerald-500 text-white font-bold px-3 py-1 rounded text-sm uppercase tracking-wider shadow-lg">Add</div>
                    <div class="glass-card p-8 border border-emerald-500/30 h-full flex flex-col justify-center bg-emerald-900/5">
                        <ul class="space-y-6">
                            <li class="flex items-center text-lg text-white font-medium"><i class="fas fa-check text-emerald-500 mr-4 text-xl"></i> 2-3 Strong Projects</li>
                            <li class="flex items-center text-lg text-white font-medium"><i class="fas fa-check text-emerald-500 mr-4 text-xl"></i> Tools Used Clearly</li>
                            <li class="flex items-center text-lg text-white font-medium"><i class="fas fa-check text-emerald-500 mr-4 text-xl"></i> Results Achieved</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center">
                <span class="text-2xl font-light text-slate-400">Short. Clean. <span class="font-bold text-white">Impactful.</span></span>
            </div>
        </div>
    """),

    "slide_18.html": ("Resume Structure", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">The 1-Page Structure</h1>
            
            <div class="w-full max-w-3xl glass-card p-2 relative shadow-2xl bg-white/5 mx-auto rounded-none">
                <div class="w-32 h-1 bg-slate-700 mx-auto my-2 rounded"></div>
                <div class="mock-resume bg-white h-[400px] w-full p-8 text-slate-800 flex flex-col">
                    <div class="h-6 w-1/3 bg-slate-200 mb-6"></div>
                    
                    <div class="mb-4">
                        <div class="h-4 w-24 bg-blue-100 mb-2"></div> <!-- Skills Header -->
                        <div class="flex gap-2">
                            <div class="h-2 w-16 bg-slate-100"></div><div class="h-2 w-16 bg-slate-100"></div><div class="h-2 w-16 bg-slate-100"></div>
                        </div>
                    </div>
                    
                    <div class="mb-4 flex-1">
                        <div class="h-4 w-24 bg-blue-100 mb-2"></div> <!-- Projects Header -->
                        <div class="space-y-3">
                            <div><div class="h-3 w-1/2 bg-slate-200 mb-1"></div><div class="h-2 w-full bg-slate-50"></div><div class="h-2 w-3/4 bg-slate-50"></div></div>
                            <div><div class="h-3 w-1/2 bg-slate-200 mb-1"></div><div class="h-2 w-full bg-slate-50"></div><div class="h-2 w-3/4 bg-slate-50"></div></div>
                        </div>
                    </div>

                    <div class="mb-4">
                        <div class="h-4 w-24 bg-blue-100 mb-2"></div> <!-- Education -->
                        <div class="h-3 w-full bg-slate-50"></div>
                    </div>
                </div>
                
                <!-- Annotations -->
                <div class="absolute top-20 right-[-140px] text-white text-sm font-bold flex items-center"><i class="fas fa-arrow-left mr-2 text-blue-400"></i> Role-Specific Skills</div>
                <div class="absolute top-48 right-[-140px] text-white text-sm font-bold flex items-center"><i class="fas fa-arrow-left mr-2 text-blue-400"></i> Projects (Core)</div>
            </div>
            
            <p class="mt-8 text-slate-400 font-medium uppercase tracking-widest text-sm">1 Page. No Clutter.</p>
        </div>
    """),

    "slide_19.html": ("LinkedIn Optimization", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12"><i class="fab fa-linkedin text-blue-500 mr-3"></i> LinkedIn Optimization</h1>
            
            <div class="max-w-4xl w-full">
                <!-- Bad Example -->
                <div class="glass-card p-6 mb-6 opacity-60 border border-red-500/20">
                    <div class="flex items-center mb-2">
                        <i class="fas fa-times-circle text-red-500 mr-2"></i>
                        <span class="text-sm font-bold uppercase tracking-wider text-red-400">Bad Headline</span>
                    </div>
                    <p class="text-xl text-slate-300 font-serif">"Final Year Student"</p>
                </div>
                
                <!-- Good Example -->
                <div class="glass-card p-8 border-l-4 border-l-emerald-500 bg-emerald-900/10 shadow-lg transform scale-105">
                    <div class="flex items-center mb-4">
                        <i class="fas fa-check-circle text-emerald-500 mr-2"></i>
                        <span class="text-sm font-bold uppercase tracking-wider text-emerald-400">Better Headline</span>
                    </div>
                    <p class="text-2xl text-white font-medium">"Aspiring Data Analyst | Built 3 Business Dashboards"</p>
                </div>
                
                <div class="grid grid-cols-2 gap-8 mt-12">
                    <div class="text-center">
                        <div class="w-12 h-12 bg-blue-500/20 rounded-full flex items-center justify-center mx-auto mb-4 text-blue-400"><i class="fas fa-image"></i></div>
                        <h3 class="font-bold text-white mb-2">Banner</h3>
                        <p class="text-sm text-slate-400">Role-focused, not generic scenery.</p>
                    </div>
                    <div class="text-center">
                        <div class="w-12 h-12 bg-blue-500/20 rounded-full flex items-center justify-center mx-auto mb-4 text-blue-400"><i class="fas fa-pen-fancy"></i></div>
                        <h3 class="font-bold text-white mb-2">Activity</h3>
                        <p class="text-sm text-slate-400">Post learning insights weekly.</p>
                    </div>
                </div>
            </div>
        </div>
    """),

    "slide_20.html": ("GitHub / Portfolio Basics", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12"><i class="fab fa-github text-white mr-3"></i> GitHub / Portfolio Basics</h1>
            
            <div class="grid grid-cols-2 gap-12 max-w-5xl">
                <div class="glass-card p-8">
                    <h3 class="text-xl font-bold text-slate-200 mb-6 border-b border-slate-700 pb-4">Must Haves</h3>
                    <ul class="space-y-4">
                        <li class="flex items-center text-slate-300"><i class="fas fa-folder text-blue-400 mr-3"></i> Clean Project Names</li>
                        <li class="flex items-center text-slate-300"><i class="fas fa-book text-blue-400 mr-3"></i> Proper README.md</li>
                        <li class="flex items-center text-slate-300"><i class="fas fa-image text-blue-400 mr-3"></i> Screenshots of output</li>
                        <li class="flex items-center text-slate-300"><i class="fas fa-paragraph text-blue-400 mr-3"></i> Simple Explanation</li>
                    </ul>
                </div>
                
                <div class="flex flex-col justify-center">
                    <div class="bg-white/5 p-6 rounded-lg border border-dashed border-slate-600 text-center mb-6">
                        <span class="text-slate-400 italic">"project_final_v2_new"</span>
                        <i class="fas fa-arrow-right mx-3 text-slate-600"></i>
                        <span class="text-emerald-400 font-mono font-bold">"e-commerce-sentiment-analysis"</span>
                    </div>
                    <p class="text-xl font-light text-slate-300 text-center">
                        Recruiters check <span class="text-white font-bold decoration-blue-500 underline decoration-2">seriousness</span> through structure.
                    </p>
                </div>
            </div>
        </div>
    """),

    "slide_21.html": ("Common Mistakes Students Make", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-16 text-center">Common Mistakes Students Make</h1>
            
            <div class="grid grid-cols-5 gap-4 w-full">
                <div class="glass-card p-6 flex flex-col items-center text-center hover:bg-red-500/10 transition-colors border-t-4 border-t-transparent hover:border-t-red-500">
                    <i class="fas fa-spinner text-3xl text-slate-500 mb-4"></i>
                    <p class="text-sm font-medium text-slate-300">Too many unfinished courses</p>
                </div>
                
                <div class="glass-card p-6 flex flex-col items-center text-center hover:bg-red-500/10 transition-colors border-t-4 border-t-transparent hover:border-t-red-500">
                    <i class="fas fa-copy text-3xl text-slate-500 mb-4"></i>
                    <p class="text-sm font-medium text-slate-300">Copy-paste projects</p>
                </div>
                
                <div class="glass-card p-6 flex flex-col items-center text-center hover:bg-red-500/10 transition-colors border-t-4 border-t-transparent hover:border-t-red-500">
                    <i class="fas fa-binoculars text-3xl text-slate-500 mb-4"></i>
                    <p class="text-sm font-medium text-slate-300">No clarity of role</p>
                </div>
                
                <div class="glass-card p-6 flex flex-col items-center text-center hover:bg-red-500/10 transition-colors border-t-4 border-t-transparent hover:border-t-red-500">
                    <i class="fas fa-hourglass-half text-3xl text-slate-500 mb-4"></i>
                    <p class="text-sm font-medium text-slate-300">Waiting for campus only</p>
                </div>
                
                <div class="glass-card p-6 flex flex-col items-center text-center hover:bg-red-500/10 transition-colors border-t-4 border-t-transparent hover:border-t-red-500">
                    <i class="fas fa-couch text-3xl text-slate-500 mb-4"></i>
                    <p class="text-sm font-medium text-slate-300">No internship attempts</p>
                </div>
            </div>
            
            <div class="mt-16 text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
                Execution separates the top 10%.
            </div>
        </div>
    """),

    "slide_22.html": ("Internship Strategy", """
        <div class="w-full h-full px-20 flex justify-center items-center">
            <div class="w-1/2 pr-12">
                <h1 class="text-5xl font-bold mb-6">Internship Strategy</h1>
                <p class="text-xl text-slate-400 mb-8">Start applying early. Don't wait for the 'perfect' brand.</p>
                
                <div class="inline-block px-6 py-3 border border-emerald-500 text-emerald-400 rounded-lg text-lg font-medium bg-emerald-900/20">
                    Even unpaid short internships build credibility.
                </div>
            </div>
            
            <div class="w-1/2 flex flex-col gap-6">
                <div class="glass-card p-6 flex items-center hover:translate-x-2 transition-transform cursor-default">
                    <div class="w-12 h-12 bg-blue-500/20 rounded-lg flex items-center justify-center mr-6 text-blue-400 text-xl"><i class="fas fa-rocket"></i></div>
                    <div>
                        <h3 class="text-xl font-bold text-white">Startups</h3>
                        <p class="text-sm text-slate-400">High learning curve, more responsibility.</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-center hover:translate-x-2 transition-transform cursor-default">
                    <div class="w-12 h-12 bg-indigo-500/20 rounded-lg flex items-center justify-center mr-6 text-indigo-400 text-xl"><i class="fas fa-building"></i></div>
                    <div>
                        <h3 class="text-xl font-bold text-white">Mid-sized Firms</h3>
                        <p class="text-sm text-slate-400">Structured processes, good mentorship.</p>
                    </div>
                </div>
                
                <div class="glass-card p-6 flex items-center hover:translate-x-2 transition-transform cursor-default">
                    <div class="w-12 h-12 bg-purple-500/20 rounded-lg flex items-center justify-center mr-6 text-purple-400 text-xl"><i class="fas fa-laptop-house"></i></div>
                    <div>
                        <h3 class="text-xl font-bold text-white">Remote Roles</h3>
                        <p class="text-sm text-slate-400">Access opportunities beyond your city.</p>
                    </div>
                </div>
            </div>
        </div>
    """),

    "slide_23.html": ("Hiring Cycle Awareness", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">Hiring Cycle Awareness</h1>
            
            <div class="flex items-center justify-center w-full max-w-5xl">
                <!-- Cycle 1 -->
                <div class="glass-card p-8 flex-1 h-64 flex flex-col items-center justify-center text-center relative border-b-8 border-b-blue-500 rounded-b-lg">
                    <div class="text-sm font-bold text-slate-400 uppercase tracking-widest mb-2">Jan - March</div>
                    <div class="text-2xl font-bold text-white mb-4">New Budgets</div>
                    <p class="text-xs text-slate-400">Companies define roles for the year.</p>
                </div>
                
                <i class="fas fa-chevron-right text-slate-600 text-2xl mx-4"></i>
                
                <!-- Cycle 2 -->
                <div class="glass-card p-8 flex-1 h-64 flex flex-col items-center justify-center text-center relative border-b-8 border-b-emerald-500 rounded-b-lg bg-emerald-900/5 scale-110 z-10 shadow-2xl">
                    <div class="text-sm font-bold text-emerald-400 uppercase tracking-widest mb-2">May - July</div>
                    <div class="text-2xl font-bold text-white mb-4">Internships</div>
                    <p class="text-xs text-slate-400">Conversion season. Peak hiring for freshers.</p>
                </div>
                
                <i class="fas fa-chevron-right text-slate-600 text-2xl mx-4"></i>
                
                <!-- Cycle 3 -->
                <div class="glass-card p-8 flex-1 h-64 flex flex-col items-center justify-center text-center relative border-b-8 border-b-indigo-500 rounded-b-lg">
                    <div class="text-sm font-bold text-slate-400 uppercase tracking-widest mb-2">Sept - Nov</div>
                    <div class="text-2xl font-bold text-white mb-4">Graduate Hiring</div>
                    <p class="text-xs text-slate-400">Campus drives & off-campus surge.</p>
                </div>
            </div>
            
            <p class="mt-12 text-xl font-light text-slate-300">Plan your 6 months accordingly.</p>
        </div>
    """),

    "slide_24.html": ("6 Month Blueprint Template", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-8">Your 6-Month Blueprint</h1>
            
            <div class="glass-card p-12 max-w-3xl w-full border border-slate-600 bg-slate-800/50 shadow-2xl relative">
                <!-- Tape effect top center -->
                <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 w-24 h-6 bg-yellow-500/20 rotate-1"></div>
                
                <h3 class="text-center font-mono text-slate-400 text-sm mb-8 uppercase tracking-widest">Commitment Contract</h3>
                
                <div class="space-y-6">
                    <div class="flex items-end">
                        <span class="text-slate-400 w-48 font-mono">My Target Role:</span>
                        <div class="flex-1 border-b border-slate-500 border-dashed"></div>
                    </div>
                    <div class="flex items-end">
                        <span class="text-slate-400 w-48 font-mono">My Required Skills:</span>
                        <div class="flex-1 border-b border-slate-500 border-dashed"></div>
                    </div>
                    <div class="flex items-end">
                        <span class="text-slate-400 w-48 font-mono">My 2 Projects:</span>
                        <div class="flex-1 border-b border-slate-500 border-dashed"></div>
                    </div>
                    <div class="flex items-end">
                        <span class="text-slate-400 w-48 font-mono">Month I Start Applying:</span>
                        <div class="flex-1 border-b border-slate-500 border-dashed"></div>
                    </div>
                    <div class="flex items-end">
                        <span class="text-slate-400 w-48 font-mono">Target Companies:</span>
                        <div class="flex-1 border-b border-slate-500 border-dashed"></div>
                    </div>
                </div>
                
                <div class="mt-10 text-right">
                    <span class="text-xs text-slate-500">Signature: ______________________</span>
                </div>
            </div>
            
            <p class="mt-8 text-slate-400 font-medium italic">This creates ownership.</p>
        </div>
    """),

    "slide_25.html": ("Reality Check", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">Reality Check</h1>
            
            <div class="w-full max-w-4xl space-y-4">
                <!-- Bar 1 -->
                <div class="flex items-center">
                    <div class="w-32 text-right mr-4 font-bold text-emerald-400">Top 10%</div>
                    <div class="flex-1 bg-slate-800 rounded-r-lg overflow-hidden h-16 flex relative">
                        <div class="bg-emerald-500 w-[10%] h-full flex items-center justify-center text-white font-bold text-xl"></div>
                        <div class="ml-4 flex items-center text-slate-300">Consistent + Clear + Visible Work</div>
                    </div>
                </div>
                
                <!-- Bar 2 -->
                <div class="flex items-center">
                    <div class="w-32 text-right mr-4 font-bold text-slate-400">Middle 60%</div>
                    <div class="flex-1 bg-slate-800 rounded-r-lg overflow-hidden h-16 flex relative">
                        <div class="bg-slate-500 w-[60%] h-full flex items-center justify-center text-slate-200 font-bold text-xl"></div>
                        <div class="absolute left-4 top-1/2 transform -translate-y-1/2 text-white font-medium drop-shadow-md">Inconsistent Effort</div>
                    </div>
                </div>
                
                <!-- Bar 3 -->
                <div class="flex items-center">
                    <div class="w-32 text-right mr-4 font-bold text-red-400">Bottom 30%</div>
                    <div class="flex-1 bg-slate-800 rounded-r-lg overflow-hidden h-16 flex relative">
                        <div class="bg-red-500 w-[30%] h-full flex items-center justify-center text-white font-bold text-xl"></div>
                        <div class="absolute left-4 top-1/2 transform -translate-y-1/2 text-white font-medium drop-shadow-md">Wait for luck</div>
                    </div>
                </div>
            </div>
            
            <p class="mt-12 text-2xl font-bold text-white">Your category is decided <span class="bg-blue-600 px-2 py-1">weekly.</span></p>
        </div>
    """),

    "slide_26.html": ("For Tier 2 / Tier 3 Students", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h1 class="text-4xl font-bold mb-10 text-center">For Tier 2 / Tier 3 Students</h1>
            
            <div class="flex items-center justify-center mb-12">
                <div class="text-3xl font-light text-slate-400 mx-8 opacity-50 strike-through line-through decoration-red-500 decoration-4">Brand</div>
                <i class="fas fa-arrow-right text-slate-600 text-2xl"></i>
                <div class="text-5xl font-extrabold text-white mx-8 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">PROOF</div>
            </div>
            
            <div class="grid grid-cols-4 gap-6 max-w-5xl mx-auto w-full">
                <div class="glass-card p-6 text-center border-t-4 border-t-blue-500">
                    <i class="fas fa-globe text-2xl text-blue-400 mb-4"></i>
                    <h3 class="font-bold">Build Publicly</h3>
                </div>
                <div class="glass-card p-6 text-center border-t-4 border-t-indigo-500">
                    <i class="fas fa-network-wired text-2xl text-indigo-400 mb-4"></i>
                    <h3 class="font-bold">Network Online</h3>
                </div>
                <div class="glass-card p-6 text-center border-t-4 border-t-purple-500">
                    <i class="fas fa-microphone text-2xl text-purple-400 mb-4"></i>
                    <h3 class="font-bold">Improve Comm.</h3>
                </div>
                <div class="glass-card p-6 text-center border-t-4 border-t-emerald-500">
                    <i class="fas fa-redo text-2xl text-emerald-400 mb-4"></i>
                    <h3 class="font-bold">Stay Consistent</h3>
                </div>
            </div>
            
            <div class="text-center mt-12">
                <span class="text-xl text-slate-300 font-serif italic">"Industry respects skill."</span>
            </div>
        </div>
    """),

    "slide_27.html": ("Strategic Partner Slide", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-2">We Are Here To Strengthen</h1>
            <p class="text-slate-400 mb-12">Not to criticize.</p>
            
            <div class="glass-card p-12 max-w-4xl w-full flex items-center justify-between relative overflow-hidden">
                <div class="absolute -right-20 -top-20 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl"></div>
                
                <div class="text-center z-10">
                    <div class="text-2xl font-bold text-white mb-2">Institution</div>
                    <div class="w-16 h-1 bg-white mx-auto rounded"></div>
                </div>
                
                <div class="text-3xl text-emerald-400 font-bold z-10">+</div>
                
                <div class="text-center z-10">
                    <div class="text-2xl font-bold text-white mb-2">Industry</div>
                    <div class="w-16 h-1 bg-white mx-auto rounded"></div>
                </div>
                
                <div class="text-3xl text-emerald-400 font-bold z-10">=</div>
                
                <div class="flex flex-col space-y-4 z-10">
                    <div class="bg-emerald-500/20 px-6 py-2 rounded-lg text-emerald-300 font-bold border border-emerald-500/30">Better Placements</div>
                    <div class="bg-emerald-500/20 px-6 py-2 rounded-lg text-emerald-300 font-bold border border-emerald-500/30">Stronger Confidence</div>
                    <div class="bg-emerald-500/20 px-6 py-2 rounded-lg text-emerald-300 font-bold border border-emerald-500/30">Long-term Reputation</div>
                </div>
            </div>
        </div>
    """),
    
    "slide_28.html": ("Closing Slide", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center text-center">
            <h1 class="text-5xl font-bold mb-12 tracking-tight">Your Career Is Not Built In Final Year.</h1>
            
            <div class="flex items-center space-x-6 text-xl text-slate-300 mb-16">
                <span>Clarity</span>
                <i class="fas fa-arrow-right text-slate-600 text-sm"></i>
                <span>Structure</span>
                <i class="fas fa-arrow-right text-slate-600 text-sm"></i>
                <span>Execution</span>
                <i class="fas fa-arrow-right text-slate-600 text-sm"></i>
                <span class="text-white font-bold border-b-2 border-emerald-500 pb-1">Consistency</span>
            </div>
            
            <h2 class="text-3xl font-light text-white mb-8">It is built <span class="text-blue-500 font-bold">every week.</span></h2>
            
            <div class="mt-8 opacity-70">
                <img src="https://via.placeholder.com/150x50?text=Sketch+Brains" alt="" class="h-12 opacity-50 grayscale hover:grayscale-0 transition-all mx-auto">
            </div>
        </div>
    """),
}

for filename, (title, content) in slides_data.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(get_slide_html(title, content))

print("Part 2: Slides 15-28 created successfully.")


import os

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_deck\slides"
os.makedirs(base_dir, exist_ok=True)

# Common HTML Template
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
    "slide_1.html": ("Future-Ready Careers 2026", """
        <div class="text-center max-w-4xl">
            <h1 class="text-7xl font-extrabold mb-6 tracking-tight leading-tight">
                Future-Ready Careers <span class="accent-text">2026</span>
            </h1>
            <div class="w-32 h-1 bg-gradient-to-r from-blue-500 to-emerald-400 mx-auto mb-8 rounded-full"></div>
            <p class="text-3xl font-light text-slate-300 mb-12 tracking-wide">
                Clarity. Capability. <span class="font-semibold text-white">Career Execution.</span>
            </p>
            <div class="inline-block px-8 py-3 rounded-full border border-slate-700 bg-slate-800/50 text-slate-400 text-lg">
                For Tech & Business Students
            </div>
        </div>
    """),

    "slide_2.html": ("The Honest Question", """
        <div class="flex flex-col items-center justify-center h-full w-full px-20 text-center">
            <h1 class="text-5xl font-bold mb-16 text-slate-100">What actually gets you hired in <span class="text-blue-500">2026?</span></h1>
            
            <div class="grid grid-cols-4 gap-8 w-full max-w-5xl">
                <div class="glass-card p-8 flex flex-col items-center opacity-60 hover:opacity-100 transition-opacity">
                    <i class="fas fa-graduation-cap text-4xl mb-4 text-slate-400"></i>
                    <span class="text-xl font-medium">High marks?</span>
                </div>
                <div class="glass-card p-8 flex flex-col items-center opacity-60 hover:opacity-100 transition-opacity">
                    <i class="fas fa-certificate text-4xl mb-4 text-slate-400"></i>
                    <span class="text-xl font-medium">Many certificates?</span>
                </div>
                <div class="glass-card p-8 flex flex-col items-center opacity-60 hover:opacity-100 transition-opacity">
                    <i class="fas fa-code text-4xl mb-4 text-slate-400"></i>
                    <span class="text-xl font-medium">Just coding?</span>
                </div>
                <div class="glass-card p-8 flex flex-col items-center border-l-4 border-l-emerald-500 bg-white/5 opacity-100 transform scale-105 shadow-xl">
                    <i class="fas fa-question text-4xl mb-4 text-emerald-400"></i>
                    <span class="text-xl font-bold text-emerald-400">Or something else?</span>
                </div>
            </div>
            
            <div class="mt-12 text-slate-500 italic text-lg tracking-widest uppercase">Pause & Think</div>
        </div>
    """),

    "slide_3.html": ("What You’ll Walk Away With", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h1 class="text-4xl font-bold mb-12 border-l-8 border-blue-600 pl-6">What You’ll Walk Away With</h1>
            
            <div class="grid grid-cols-2 gap-8 max-w-5xl">
                <div class="glass-card p-8 flex items-start">
                    <div class="bg-blue-500/10 p-4 rounded-lg mr-6 text-blue-400">
                        <i class="fas fa-eye text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">Role Clarity</h3>
                        <p class="text-slate-400">Clear understanding of 3 high-demand roles.</p>
                    </div>
                </div>
                
                <div class="glass-card p-8 flex items-start">
                    <div class="bg-emerald-500/10 p-4 rounded-lg mr-6 text-emerald-400">
                        <i class="fas fa-map-signs text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">6-Month Roadmap</h3>
                        <p class="text-slate-400">A structured path from foundation to job-ready.</p>
                    </div>
                </div>
                
                <div class="glass-card p-8 flex items-start">
                    <div class="bg-purple-500/10 p-4 rounded-lg mr-6 text-purple-400">
                        <i class="fas fa-building text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">Company Expectations</h3>
                        <p class="text-slate-400">Clarity on what companies really expect.</p>
                    </div>
                </div>
                
                <div class="glass-card p-8 flex items-start">
                    <div class="bg-amber-500/10 p-4 rounded-lg mr-6 text-amber-400">
                        <i class="fas fa-cogs text-2xl"></i>
                    </div>
                    <div>
                        <h3 class="text-xl font-bold mb-2">Employability System</h3>
                        <p class="text-slate-400">A practical execution framework.</p>
                    </div>
                </div>
            </div>
        </div>
    """),

    "slide_4.html": ("The 2026 Hiring Reality", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <div class="glass-card p-12 max-w-5xl w-full text-center mb-12">
                <h1 class="text-4xl font-bold mb-4">The market is not shrinking.</h1>
                <h2 class="text-3xl font-light text-slate-400">It is becoming <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 font-bold">selective.</span></h2>
            </div>
            
            <div class="grid grid-cols-3 gap-8 w-full max-w-5xl">
                <div class="border border-slate-700/50 rounded-xl p-8 text-center bg-slate-900/30">
                    <div class="text-4xl font-bold text-red-400 mb-2">Fewer</div>
                    <div class="text-lg text-slate-400">Candidates</div>
                </div>
                <div class="border border-slate-700/50 rounded-xl p-8 text-center bg-slate-900/30">
                    <div class="text-4xl font-bold text-blue-400 mb-2">Better</div>
                    <div class="text-lg text-slate-400">Prepared</div>
                </div>
                <div class="border border-emerald-500/30 rounded-xl p-8 text-center bg-emerald-900/10 shadow-lg shadow-emerald-500/5">
                    <div class="text-4xl font-bold text-emerald-400 mb-2">Proof</div>
                    <div class="text-lg text-slate-400">Of Skills</div>
                </div>
            </div>
            
            <div class="mt-12 flex items-center justify-center space-x-4 bg-white/5 px-8 py-3 rounded-full border border-white/10">
                <span class="text-slate-400">Degrees are common.</span>
                <i class="fas fa-arrow-right text-slate-600"></i>
                <span class="text-white font-bold">Execution is rare.</span>
            </div>
        </div>
    """),
    
    "slide_5.html": ("The 3 Roles That Dominate Hiring", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <h1 class="text-4xl font-bold mb-12 text-center">We Focus Only On 3 Core Roles</h1>
            
            <div class="grid grid-cols-3 gap-8 h-80">
                <div class="glass-card p-8 flex flex-col items-center justify-center hover:bg-white/5 transition-colors group cursor-default">
                    <div class="w-20 h-20 bg-blue-500/10 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-laptop-code text-3xl text-blue-400"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-2">Software Engineer</h3>
                    <div class="w-12 h-1 bg-blue-500 rounded-full"></div>
                </div>
                
                <div class="glass-card p-8 flex flex-col items-center justify-center hover:bg-white/5 transition-colors group cursor-default relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-b from-transparent to-emerald-500/5 pointer-events-none"></div>
                    <div class="w-20 h-20 bg-emerald-500/10 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-chart-pie text-3xl text-emerald-400"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-2">Data Analyst</h3>
                    <div class="w-12 h-1 bg-emerald-500 rounded-full"></div>
                </div>
                
                <div class="glass-card p-8 flex flex-col items-center justify-center hover:bg-white/5 transition-colors group cursor-default">
                    <div class="w-20 h-20 bg-purple-500/10 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                        <i class="fas fa-brain text-3xl text-purple-400"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-2">AI/ML Engineer</h3>
                    <div class="w-12 h-1 bg-purple-500 rounded-full"></div>
                </div>
            </div>
            
            <div class="mt-12 flex justify-center space-x-8 text-slate-400 text-sm font-medium uppercase tracking-widest">
                <span class="flex items-center"><i class="fas fa-check text-green-500 mr-2"></i> High Demand</span>
                <span class="flex items-center"><i class="fas fa-check text-green-500 mr-2"></i> Clear Skill Path</span>
                <span class="flex items-center"><i class="fas fa-check text-green-500 mr-2"></i> Good Growth</span>
            </div>
        </div>
    """),
    
    "slide_6.html": ("Role 1: Software Engineer", """
        <div class="w-full h-full p-16 flex">
            <div class="w-1/3 flex flex-col justify-center border-r border-slate-700 pr-12">
                <div class="w-16 h-16 bg-blue-500/20 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-code text-3xl text-blue-400"></i>
                </div>
                <h1 class="text-4xl font-bold mb-2 text-white">Software Engineer</h1>
                <p class="text-blue-400 font-medium">Builders of the digital world.</p>
            </div>
            
            <div class="w-2/3 pl-12 flex flex-col justify-center">
                <div class="grid grid-cols-2 gap-8 mb-10">
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">What They Do</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="fas fa-terminal mt-1 mr-3 text-blue-500 text-xs"></i> Build applications</li>
                            <li class="flex items-start"><i class="fas fa-terminal mt-1 mr-3 text-blue-500 text-xs"></i> Solve real user problems</li>
                            <li class="flex items-start"><i class="fas fa-terminal mt-1 mr-3 text-blue-500 text-xs"></i> Work in teams</li>
                            <li class="flex items-start"><i class="fas fa-terminal mt-1 mr-3 text-blue-500 text-xs"></i> Deploy products</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">Is It For You?</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> Logical thinkers</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> People who enjoy building</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> Structured problem solvers</li>
                        </ul>
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-blue-500">
                    <span class="font-bold text-white block mb-1">Reality Check:</span>
                    <span class="text-slate-400">It’s not just coding. It’s <span class="text-white">Designing + Building + Deploying.</span></span>
                </div>
            </div>
        </div>
    """),
    
    "slide_7.html": ("Role 2: Data Analyst", """
        <div class="w-full h-full p-16 flex">
            <div class="w-1/3 flex flex-col justify-center border-r border-slate-700 pr-12">
                <div class="w-16 h-16 bg-emerald-500/20 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-chart-bar text-3xl text-emerald-400"></i>
                </div>
                <h1 class="text-4xl font-bold mb-2 text-white">Data Analyst</h1>
                <p class="text-emerald-400 font-medium">Translators of numbers to strategy.</p>
            </div>
            
            <div class="w-2/3 pl-12 flex flex-col justify-center">
                <div class="grid grid-cols-2 gap-8 mb-10">
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">What They Do</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="fas fa-search mt-1 mr-3 text-emerald-500 text-xs"></i> Work with data</li>
                            <li class="flex items-start"><i class="fas fa-search mt-1 mr-3 text-emerald-500 text-xs"></i> Find insights</li>
                            <li class="flex items-start"><i class="fas fa-search mt-1 mr-3 text-emerald-500 text-xs"></i> Drive business decisions</li>
                            <li class="flex items-start"><i class="fas fa-search mt-1 mr-3 text-emerald-500 text-xs"></i> Build dashboards</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">Is It For You?</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-blue-400 text-xs"></i> Analytical thinkers</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-blue-400 text-xs"></i> B.Com, BBA, B.Sc Students</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-blue-400 text-xs"></i> Comfortable with numbers</li>
                        </ul>
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-emerald-500">
                    <span class="font-bold text-white block mb-1">Reality Check:</span>
                    <span class="text-slate-400">It’s not heavy coding. It’s <span class="text-white">Structured Thinking + Business Understanding.</span></span>
                </div>
            </div>
        </div>
    """),

    "slide_8.html": ("Role 3: AI/ML Engineer", """
        <div class="w-full h-full p-16 flex">
            <div class="w-1/3 flex flex-col justify-center border-r border-slate-700 pr-12">
                <div class="w-16 h-16 bg-purple-500/20 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-brain text-3xl text-purple-400"></i>
                </div>
                <h1 class="text-4xl font-bold mb-2 text-white">AI/ML Engineer</h1>
                <p class="text-purple-400 font-medium">Architects of intelligence.</p>
            </div>
            
            <div class="w-2/3 pl-12 flex flex-col justify-center">
                <div class="grid grid-cols-2 gap-8 mb-10">
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">What They Do</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="fas fa-project-diagram mt-1 mr-3 text-purple-500 text-xs"></i> Build intelligent systems</li>
                            <li class="flex items-start"><i class="fas fa-project-diagram mt-1 mr-3 text-purple-500 text-xs"></i> Train models</li>
                            <li class="flex items-start"><i class="fas fa-project-diagram mt-1 mr-3 text-purple-500 text-xs"></i> Automate decision-making</li>
                            <li class="flex items-start"><i class="fas fa-project-diagram mt-1 mr-3 text-purple-500 text-xs"></i> Improve product intelligence</li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold text-slate-300 mb-4 uppercase tracking-wide border-b border-slate-700 pb-2">Is It For You?</h3>
                        <ul class="space-y-3 text-slate-400">
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> Curious minds</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> Strong logic & basic math</li>
                            <li class="flex items-start"><i class="far fa-check-circle mt-1 mr-3 text-emerald-500 text-xs"></i> Future-facing tech interest</li>
                        </ul>
                    </div>
                </div>
                
                <div class="glass-card p-6 border-l-4 border-l-purple-500">
                    <span class="font-bold text-white block mb-1">Reality Check:</span>
                    <span class="text-slate-400">AI is not magic. It’s <span class="text-white">Structured Data + Models + Deployment.</span></span>
                </div>
            </div>
        </div>
    """),

    "slide_9.html": ("How Companies Evaluate Freshers", """
        <div class="w-full h-full px-20 flex flew-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">How Companies Evaluate Freshers</h1>
            
            <div class="grid grid-cols-2 gap-16 max-w-6xl w-full">
                <div>
                    <h3 class="text-xl font-bold text-emerald-400 mb-6 flex items-center"><i class="fas fa-check-square mr-3"></i> The Checklist</h3>
                    <div class="space-y-4">
                        <div class="glass-card p-4 flex items-center">
                            <i class="fas fa-puzzle-piece text-slate-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-slate-200">Can you solve problems?</span>
                        </div>
                        <div class="glass-card p-4 flex items-center">
                            <i class="fas fa-hammer text-slate-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-slate-200">Can you build something real?</span>
                        </div>
                        <div class="glass-card p-4 flex items-center">
                            <i class="fas fa-bullhorn text-slate-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-slate-200">Can you explain your work?</span>
                        </div>
                        <div class="glass-card p-4 flex items-center">
                            <i class="fas fa-sync text-slate-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-slate-200">Are you consistent?</span>
                        </div>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-xl font-bold text-red-400 mb-6 flex items-center"><i class="fas fa-times-circle mr-3"></i> Why Students Fail</h3>
                    <div class="space-y-4">
                        <div class="border border-red-500/20 bg-red-500/5 rounded-xl p-4 flex items-center">
                            <i class="fas fa-ban text-red-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-red-200">No real projects</span>
                        </div>
                        <div class="border border-red-500/20 bg-red-500/5 rounded-xl p-4 flex items-center">
                            <i class="fas fa-fog text-red-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-red-200">No clarity</span>
                        </div>
                        <div class="border border-red-500/20 bg-red-500/5 rounded-xl p-4 flex items-center">
                            <i class="fas fa-water text-red-400 mr-4 w-6 text-center"></i>
                            <span class="text-lg text-red-200">No depth</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """),

    "slide_10.html": ("The 3-Level Skill Model", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-4">The Skill Progression Model</h1>
            <p class="text-slate-400 mb-16 uppercase tracking-widest text-sm">Not random learning. Structured evolution.</p>
            
            <div class="relative flex items-end justify-center space-x-4">
                <!-- Step 1 -->
                <div class="flex flex-col items-center">
                    <div class="glass-card w-64 h-32 flex flex-col justify-center items-center text-center border-b-4 border-b-blue-500 rounded-b-none mb-2">
                        <span class="text-2xl font-bold text-white mb-1">Foundational</span>
                        <span class="text-xs text-blue-400 uppercase font-bold tracking-wider">Months 1-2</span>
                    </div>
                </div>
                
                <!-- Step 2 -->
                <div class="flex flex-col items-center">
                    <div class="glass-card w-64 h-48 flex flex-col justify-center items-center text-center border-b-4 border-b-indigo-500 rounded-b-none mb-2 relative top-0 bg-white/5">
                        <span class="text-2xl font-bold text-white mb-1">Intermediate</span>
                        <span class="text-xs text-indigo-400 uppercase font-bold tracking-wider">Months 3-4</span>
                    </div>
                </div>
                
                <!-- Step 3 -->
                <div class="flex flex-col items-center">
                    <div class="glass-card w-64 h-64 flex flex-col justify-center items-center text-center border-b-4 border-b-emerald-500 rounded-b-none mb-2 bg-white/10 shadow-[0_0_30px_rgba(16,185,129,0.2)]">
                        <span class="text-2xl font-bold text-white mb-1">Industry-Ready</span>
                        <span class="text-xs text-emerald-400 uppercase font-bold tracking-wider">Months 5-6</span>
                    </div>
                </div>
            </div>
            
            <div class="w-full max-w-3xl h-1 bg-gradient-to-r from-blue-500 via-indigo-500 to-emerald-500 rounded-full mt-0"></div>
            <p class="mt-8 text-xl font-medium text-slate-300">This is your career ladder.</p>
        </div>
    """),

    "slide_11.html": ("Foundational Level (Months 1–2)", """
        <div class="w-full h-full px-20 flex flex-col justify-center">
            <div class="flex items-center mb-10">
                <div class="bg-blue-500 text-white font-bold py-1 px-3 rounded text-sm uppercase mr-4">Phase 1</div>
                <h1 class="text-4xl font-bold">Foundational Level <span class="text-slate-500 text-2xl font-normal ml-2">(Months 1–2)</span></h1>
            </div>
            
            <div class="flex gap-12">
                <div class="w-1/2">
                    <p class="text-lg text-slate-300 mb-6">Common for all 3 roles. Building the bedrock.</p>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="glass-card p-4 flex items-center"><i class="fab fa-python text-blue-400 mr-3 text-xl"></i> Python Basics</div>
                        <div class="glass-card p-4 flex items-center"><i class="fas fa-database text-blue-400 mr-3 text-xl"></i> SQL Basics</div>
                        <div class="glass-card p-4 flex items-center"><i class="fas fa-brain text-blue-400 mr-3 text-xl"></i> Problem Solving</div>
                        <div class="glass-card p-4 flex items-center"><i class="fas fa-table text-blue-400 mr-3 text-xl"></i> Excel Basics</div>
                        <div class="glass-card p-4 flex items-center"><i class="fas fa-comments text-blue-400 mr-3 text-xl"></i> Communication</div>
                        <div class="glass-card p-4 flex items-center"><i class="fab fa-git-alt text-blue-400 mr-3 text-xl"></i> Git Basics</div>
                    </div>
                </div>
                
                <div class="w-1/2 flex items-center justify-center">
                    <div class="glass-card p-10 border-l-4 border-l-blue-500 bg-blue-900/10">
                        <h3 class="text-2xl font-bold text-blue-400 mb-2">Phase Focus</h3>
                        <p class="text-xl text-white">Understanding, not rushing.</p>
                        <p class="text-slate-400 mt-4 text-sm">Don't jump to frameworks before knowing the language.</p>
                    </div>
                </div>
            </div>
        </div>
    """),
    
    "slide_12.html": ("Intermediate Level (Months 3–4)", """
        <div class="w-full h-full px-20 pt-16">
            <div class="flex items-center mb-8">
                <div class="bg-indigo-500 text-white font-bold py-1 px-3 rounded text-sm uppercase mr-4">Phase 2</div>
                <h1 class="text-3xl font-bold">Intermediate Level <span class="text-slate-500 text-xl font-normal ml-2">(Months 3–4)</span></h1>
            </div>
            
            <div class="grid grid-cols-3 gap-6 h-96">
                <!-- Software Engineer -->
                <div class="glass-card p-6 border-t-4 border-t-blue-500 flex flex-col">
                    <h3 class="font-bold text-lg mb-4 text-blue-400 flex items-center"><i class="fas fa-code mr-2"></i> Software Engineer</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 mr-2"></span>Backend/Full-Stack Framework</li>
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 mr-2"></span>REST APIs</li>
                        <li class="flex items-start font-bold text-white"><span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-2 mr-2"></span>Build 1 Real Project</li>
                    </ul>
                </div>
                
                <!-- Data Analyst -->
                <div class="glass-card p-6 border-t-4 border-t-emerald-500 flex flex-col">
                    <h3 class="font-bold text-lg mb-4 text-emerald-400 flex items-center"><i class="fas fa-chart-bar mr-2"></i> Data Analyst</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-emerald-500 rounded-full mt-2 mr-2"></span>Advanced SQL Queries</li>
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-emerald-500 rounded-full mt-2 mr-2"></span>Excel Advanced</li>
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-emerald-500 rounded-full mt-2 mr-2"></span>Power BI / Tableau</li>
                        <li class="flex items-start font-bold text-white"><span class="w-1.5 h-1.5 bg-emerald-500 rounded-full mt-2 mr-2"></span>1 Dashboard Project</li>
                    </ul>
                </div>
                
                <!-- AI/ML -->
                <div class="glass-card p-6 border-t-4 border-t-purple-500 flex flex-col">
                    <h3 class="font-bold text-lg mb-4 text-purple-400 flex items-center"><i class="fas fa-brain mr-2"></i> AI/ML Engineer</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 mr-2"></span>Python Deep Dive</li>
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 mr-2"></span>Basic Statistics</li>
                        <li class="flex items-start"><span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 mr-2"></span>Intro to ML Libraries</li>
                        <li class="flex items-start font-bold text-white"><span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-2 mr-2"></span>1 Prediction Project</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center bg-white/5 py-4 rounded-lg border border-white/10">
                <span class="text-indigo-400 font-bold uppercase tracking-wider text-sm mr-2">Phase Focus:</span>
                <span class="text-white font-medium text-lg">Build and Complete.</span>
            </div>
        </div>
    """),

    "slide_13.html": ("Industry-Ready Level (Months 5–6)", """
        <div class="w-full h-full px-20 pt-16">
            <div class="flex items-center mb-8">
                <div class="bg-emerald-500 text-white font-bold py-1 px-3 rounded text-sm uppercase mr-4">Phase 3</div>
                <h1 class="text-3xl font-bold">Industry-Ready Level <span class="text-slate-500 text-xl font-normal ml-2">(Months 5–6)</span></h1>
            </div>
            
            <div class="grid grid-cols-3 gap-6 h-96">
                <!-- Software Engineer -->
                <div class="glass-card p-6 border-t-4 border-t-blue-500 flex flex-col bg-blue-900/5">
                    <h3 class="font-bold text-lg mb-4 text-blue-400 flex items-center"><i class="fas fa-rocket mr-2"></i> Software Engineer</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Deploy Project Online</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Clean Documentation</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Basic System Design</li>
                    </ul>
                </div>
                
                <!-- Data Analyst -->
                <div class="glass-card p-6 border-t-4 border-t-emerald-500 flex flex-col bg-emerald-900/5">
                    <h3 class="font-bold text-lg mb-4 text-emerald-400 flex items-center"><i class="fas fa-presentation mr-2"></i> Data Analyst</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Case-Study Analysis</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Business Storytelling</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Portfolio Dashboard</li>
                    </ul>
                </div>
                
                <!-- AI/ML -->
                <div class="glass-card p-6 border-t-4 border-t-purple-500 flex flex-col bg-purple-900/5">
                    <h3 class="font-bold text-lg mb-4 text-purple-400 flex items-center"><i class="fas fa-robot mr-2"></i> AI/ML Engineer</h3>
                    <ul class="space-y-3 text-sm text-slate-300 flex-1">
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Model Deployment</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Explainability</li>
                        <li class="flex items-start"><i class="fas fa-check text-emerald-500 mt-1 mr-2 text-xs"></i> Real-World Dataset</li>
                    </ul>
                </div>
            </div>
            
            <div class="mt-8 text-center bg-emerald-900/20 py-4 rounded-lg border border-emerald-500/20 shadow-[0_0_20px_rgba(16,185,129,0.1)]">
                <span class="text-emerald-400 font-bold uppercase tracking-wider text-sm mr-2">Phase Focus:</span>
                <span class="text-white font-medium text-lg">Proof of Work.</span>
            </div>
        </div>
    """),

    "slide_14.html": ("What Makes a Strong Project", """
        <div class="w-full h-full px-20 flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold mb-12">What Makes a Strong Project?</h1>
            
            <div class="glass-card p-10 max-w-4xl w-full relative">
                <div class="absolute -top-6 -left-6 w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold text-xl shadow-lg">!</div>
                
                <div class="grid grid-cols-2 gap-x-12 gap-y-8">
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center mr-4 text-blue-400 text-sm"><i class="fas fa-bullseye"></i></div>
                        <span class="text-lg text-slate-200">Clear Problem Statement</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center mr-4 text-blue-400 text-sm"><i class="fas fa-user-tag"></i></div>
                        <span class="text-lg text-slate-200">Target User</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center mr-4 text-blue-400 text-sm"><i class="fas fa-tools"></i></div>
                        <span class="text-lg text-slate-200">Tools Used</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center mr-4 text-blue-400 text-sm"><i class="fas fa-flag-checkered"></i></div>
                        <span class="text-lg text-slate-200">Outcome/Result</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center mr-4 text-emerald-400 text-sm"><i class="fas fa-laptop"></i></div>
                        <span class="text-lg text-white font-semibold">Live Demo / Dashboard</span>
                    </div>
                    <div class="flex items-center">
                        <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center mr-4 text-emerald-400 text-sm"><i class="fas fa-file-alt"></i></div>
                        <span class="text-lg text-white font-semibold">Clean Documentation</span>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center">
                <p class="text-2xl font-light text-slate-400">If it’s not visible online,</p>
                <p class="text-3xl font-bold text-red-400 mt-2">It doesn’t count strongly.</p>
            </div>
        </div>
    """),
}

for filename, (title, content) in slides_data.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(get_slide_html(title, content))

print("Part 1: Slides 1-14 created successfully.")

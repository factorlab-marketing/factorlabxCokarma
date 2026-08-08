import os

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

slide_4_html = """
    <div class="bg-grid"></div>
    <div class="blob blob-blue opacity-50"></div><div class="blob blob-emerald opacity-40"></div>
    <div class="content-layer w-full h-full p-20 flex flex-col justify-center relative z-10">
        <div class="text-center mb-12">
            <h2 class="animate-up font-serif text-5xl font-bold text-slate-900 mb-4">The Paradigm Shift</h2>
            <p class="animate-up delay-100 text-xl text-blue-600 font-semibold tracking-wide">Transitioning from reactive sourcing to proactive talent manufacturing.</p>
        </div>
        <div class="flex space-x-8 w-full animate-up delay-200">
            <!-- Old Way -->
            <div class="w-1/2 bg-white rounded-[32px] p-10 border border-slate-200 shadow-lg">
                <h3 class="text-3xl font-bold text-rose-500 mb-6 border-b border-slate-100 pb-4"><i class="fa-solid fa-magnifying-glass mr-3"></i> The Old Way: Sourcing</h3>
                <ul class="space-y-6 text-slate-600">
                    <li class="flex items-start bg-rose-50/50 p-4 rounded-xl border border-rose-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-xmark text-rose-500 mt-1 text-2xl"></i></div>
                        <div><p class="font-bold text-slate-800 text-lg">Bidding Wars</p><p class="text-sm mt-1 leading-relaxed">Endlessly competing and inflating salaries for generic talent available on the open market.</p></div>
                    </li>
                    <li class="flex items-start bg-rose-50/50 p-4 rounded-xl border border-rose-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-xmark text-rose-500 mt-1 text-2xl"></i></div>
                        <div><p class="font-bold text-slate-800 text-lg">Filtering Debt</p><p class="text-sm mt-1 leading-relaxed">Burning hundreds of internal engineering hours on technical screening and interviews.</p></div>
                    </li>
                    <li class="flex items-start bg-rose-50/50 p-4 rounded-xl border border-rose-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-xmark text-rose-500 mt-1 text-2xl"></i></div>
                        <div><p class="font-bold text-slate-800 text-lg">Onboarding Guesswork</p><p class="text-sm mt-1 leading-relaxed">Hoping candidates can adapt to your internal, undocumented frameworks after hiring.</p></div>
                    </li>
                </ul>
            </div>
            <!-- New Way -->
            <div class="w-1/2 bg-white rounded-[32px] p-10 border border-blue-200 shadow-2xl relative overflow-hidden ring-4 ring-blue-50">
                <div class="absolute right-0 top-0 w-48 h-48 bg-blue-50 rounded-bl-full z-0 opacity-50"></div>
                <h3 class="text-3xl font-bold text-blue-600 mb-6 border-b border-blue-100 pb-4 relative z-10"><i class="fa-solid fa-industry mr-3"></i> The New Way: Manufacturing</h3>
                <ul class="space-y-6 text-slate-700 relative z-10">
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl border border-blue-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-check text-blue-500 mt-1 text-2xl font-bold"></i></div>
                        <div><p class="font-bold text-slate-900 text-lg">Absolute Specifications</p><p class="text-sm mt-1 leading-relaxed text-slate-600">You dictate the exact curriculum, proprietary tech stack, and required agile workflows from day zero.</p></div>
                    </li>
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl border border-blue-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-check text-blue-500 mt-1 text-2xl font-bold"></i></div>
                        <div><p class="font-bold text-slate-900 text-lg">Custom Built Cohorts</p><p class="text-sm mt-1 leading-relaxed text-slate-600">We train a dedicated 40-person cohort exclusively in your environment over an intensive 3-6 month period.</p></div>
                    </li>
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl border border-blue-100/50">
                        <div class="w-8 flex shrink-0"><i class="fa-solid fa-check text-blue-500 mt-1 text-2xl font-bold"></i></div>
                        <div><p class="font-bold text-slate-900 text-lg">Interview for Validation</p><p class="text-sm mt-1 leading-relaxed text-slate-600">You only interview the top 10% proven performers, validating cultural fit rather than basic syntax.</p></div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
"""

slide_7_html = """
    <div class="bg-grid"></div>
    <div class="blob blob-blue opacity-30"></div><div class="blob blob-emerald opacity-20"></div>
    <div class="content-layer flex flex-col justify-center px-16 py-12">
        <div class="text-center mb-10 animate-up">
            <div class="animate-up mb-4 px-4 py-1.5 bg-emerald-100 text-emerald-700 rounded-full text-xs font-extrabold inline-block uppercase tracking-widest shadow-sm">The Guarantee</div>
            <h2 class="font-serif text-5xl font-bold text-slate-900 mb-4">The Zero-Risk Proposition</h2>
            <p class="text-xl text-slate-500 max-w-3xl mx-auto">You don't pay for sourcing. You don't pay for training. You partner completely dynamically on successful hires.</p>
        </div>
        
        <div class="flex w-[1000px] mx-auto animate-up delay-200 bg-white shadow-[0_20px_50px_-12px_rgba(0,0,0,0.1)] rounded-[32px] overflow-hidden border border-slate-200 relative">
            <!-- Divider -->
            <div class="absolute left-1/2 top-12 bottom-12 w-px bg-slate-200 z-10"></div>
            
            <!-- Traditional Column -->
            <div class="w-1/2 p-12 text-center relative bg-white">
                <h3 class="font-bold text-3xl text-slate-800 mb-2">Standard Agencies</h3>
                <div class="inline-block px-4 py-1 bg-rose-50 text-rose-600 rounded-full text-sm font-bold mb-8 border border-rose-100">High Upfront Financial Risk</div>
                
                <ul class="text-left space-y-6 text-slate-600 mb-10 w-full font-medium">
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-2xl mt-0.5 mr-4"></i><span class="flex-1 pb-1">Retainer fees paid upfront before results</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-2xl mt-0.5 mr-4"></i><span class="flex-1 pb-1">Massive internal engineering hours wasted interviewing randoms</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-2xl mt-0.5 mr-4"></i><span class="flex-1 pb-1">Zero technical pre-training specific to your tech stack</span></li>
                </ul>
                <div class="pt-8 border-t border-slate-100">
                    <div class="text-slate-400 font-bold uppercase tracking-widest text-sm mb-1">Financial Structure</div>
                    <div class="text-4xl font-extrabold text-slate-300">Guaranteed Spend</div>
                </div>
            </div>
            
            <!-- Sketch Brains Column -->
            <div class="w-1/2 p-12 text-center bg-emerald-50/30 relative">
                <div class="absolute -right-10 -top-10 w-32 h-32 bg-emerald-100 rounded-full z-0 opacity-50 blur-2xl"></div>
                <h3 class="font-bold text-3xl text-emerald-900 mb-2 relative z-10 flex items-center justify-center"><i class="fa-solid fa-shield-check text-emerald-500 mr-3 text-2xl"></i>Sketch Brains</h3>
                <div class="inline-block px-4 py-1 bg-emerald-100 text-emerald-700 rounded-full text-sm font-bold mb-8 border border-emerald-200 relative z-10">Utterly De-risked Pipeline</div>
                
                <ul class="text-left space-y-6 text-slate-800 mb-10 w-full font-bold relative z-10">
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-2xl mt-0.5 mr-4 font-black"></i><span class="flex-1 pb-1">No upfront sourcing costs or retainers whatsoever</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-2xl mt-0.5 mr-4 font-black"></i><span class="flex-1 pb-1">You interview a curated, proven shortlist (top 10%)</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-2xl mt-0.5 mr-4 font-black"></i><span class="flex-1 pb-1">Candidates are fully trained on your proprietary stack</span></li>
                </ul>
                <div class="pt-8 border-t border-emerald-200/50 relative z-10">
                    <div class="text-emerald-600 font-extrabold uppercase tracking-widest text-sm mb-1">Financial Structure</div>
                    <div class="text-4xl font-black text-emerald-500">Pay ONLY on Hire</div>
                </div>
            </div>
        </div>
    </div>
"""

slide_8_html = """
    <div class="bg-grid"></div>
    <div class="blob blob-blue opacity-20"></div><div class="blob blob-emerald opacity-20"></div>
    <div class="content-layer flex flex-col justify-center items-center px-16">
        <div class="text-center mb-16 animate-up">
            <div class="animate-up mb-4 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider border border-blue-200">The ROI</div>
            <h2 class="font-serif text-5xl font-bold text-slate-900 mb-4">Enterprise Impact Metrics</h2>
            <p class="text-xl text-slate-600">Data compiled from across our active B2B enterprise partnerships.</p>
        </div>
        
        <div class="flex space-x-6 w-full animate-up delay-200">
            <!-- Stat 1 -->
            <div class="flex-1 bg-white p-8 rounded-3xl border border-slate-200 flex flex-col shadow-xl">
                <div class="bg-amber-50 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-amber-100"><i class="fa-solid fa-bolt text-3xl text-amber-500"></i></div>
                <div class="text-6xl font-black text-slate-900 mb-2 tracking-tighter">-70%</div>
                <div class="text-xl font-bold text-amber-600 border-b border-slate-100 pb-4 mb-4">Time to Productivity</div>
                <p class="text-sm text-slate-600 leading-relaxed font-medium">Our candidates bypass the standard 6-month conceptual ramp-up. They contribute to mock versions of your actual codebase during their final sprint.</p>
            </div>
            
            <!-- Stat 2 -->
            <div class="flex-1 bg-white p-8 rounded-3xl border border-slate-200 flex flex-col shadow-2xl relative border-t-8 border-t-blue-500 z-10 transform scale-105">
                <div class="bg-blue-50 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-blue-100"><i class="fa-solid fa-users-viewfinder text-3xl text-blue-600"></i></div>
                <div class="text-6xl font-black text-slate-900 mb-2 tracking-tighter">100%</div>
                <div class="text-xl font-bold text-blue-600 border-b border-slate-100 pb-4 mb-4">Tech Stack Match</div>
                <p class="text-sm text-slate-600 leading-relaxed font-medium">Because you dictate the curriculum on Day 1, there is zero translation error. They learn exactly the microservices pattern your environment relies on.</p>
            </div>
            
            <!-- Stat 3 -->
            <div class="flex-1 bg-white p-8 rounded-3xl border border-slate-200 flex flex-col shadow-xl">
                <div class="bg-emerald-50 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-emerald-100"><i class="fa-solid fa-chart-line text-3xl text-emerald-500"></i></div>
                <div class="text-6xl font-black text-slate-900 mb-2 tracking-tighter">3x</div>
                <div class="text-xl font-bold text-emerald-600 border-b border-slate-100 pb-4 mb-4">Retention Rate</div>
                <p class="text-sm text-slate-600 leading-relaxed font-medium">Employees who are specifically cultivated and successfully placed into an ecosystem they already understand demonstrate drastically higher long-term loyalty.</p>
            </div>
        </div>
    </div>
"""

base_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet"/>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body, html { margin:0; padding:0; font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; }
        .slide { width: 1280px; height: 720px; position: relative; overflow: hidden; background: #F8FAFC; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: inset 0 0 0 1px #E2E8F0; }
        .font-serif { font-family: 'Playfair Display', serif; }
        .bg-grid { background-image: radial-gradient(#CBD5E1 1px, transparent 1px); background-size: 32px 32px; opacity: 0.3; position: absolute; inset: 0; pointer-events: none; }
        .animate-up { animation: fadeUp 1s ease-out forwards; opacity: 0; transform: translateY(30px); }
        .delay-100 { animation-delay: 0.1s; } .delay-200 { animation-delay: 0.2s; } .delay-300 { animation-delay: 0.3s; } .delay-400 { animation-delay: 0.4s; }
        @keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
        .blob { position: absolute; border-radius: 50%; filter: blur(80px); z-index: 0; opacity: 0.4; }
        .blob-blue { background: #3B82F6; width: 600px; height: 600px; top: -100px; left: -100px; }
        .blob-emerald { background: #10B981; width: 500px; height: 500px; bottom: -100px; right: -100px; }
        .content-layer { z-index: 10; position: relative; width: 100%; height: 100%; display: flex; }
    </style>
</head>
<body>
<div class="slide">
{content}
</div>
</body>
</html>
"""

def update_slide(num, content):
    filepath = os.path.join(slide_dir, f"slide_{num}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(base_head.replace('{content}', content))

update_slide(4, slide_4_html)
update_slide(7, slide_7_html)
update_slide(8, slide_8_html)

print("Slides 4, 7, and 8 updated!")

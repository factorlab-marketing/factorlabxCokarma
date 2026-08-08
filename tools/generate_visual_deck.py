import os

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

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
        .slide { width: 1280px; height: 720px; position: relative; overflow: hidden; background: #FFFFFF; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: inset 0 0 0 1px #E2E8F0; }
        .font-serif { font-family: 'Playfair Display', serif; }
        .bg-grid { background-image: radial-gradient(#CBD5E1 1px, transparent 1px); background-size: 32px 32px; opacity: 0.3; position: absolute; inset: 0; pointer-events: none; }
        .animate-up { animation: fadeUp 1s ease-out forwards; opacity: 0; transform: translateY(30px); }
        .delay-100 { animation-delay: 0.1s; } .delay-200 { animation-delay: 0.2s; } .delay-300 { animation-delay: 0.3s; } .delay-400 { animation-delay: 0.4s; }
        @keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
        /* Beautiful glass blobs */
        .blob { position: absolute; border-radius: 50%; filter: blur(80px); z-index: 0; opacity: 0.4; }
        .blob-blue { background: #3B82F6; width: 600px; height: 600px; top: -100px; left: -100px; }
        .blob-emerald { background: #10B981; width: 500px; height: 500px; bottom: -100px; right: -100px; }
        .content-layer { z-index: 10; position: relative; width: 100%; height: 100%; display: flex; }
    </style>
</head>
<body>
"""

slides = {}

# Slide 1: Title (Enriched)
slides[1] = """<div class="slide">
    <div class="bg-grid"></div>
    <div class="blob blob-blue"></div><div class="blob blob-emerald"></div>
    <div class="content-layer flex items-center justify-between w-full h-full px-20">
        <div class="w-7/12 pr-12">
            <div class="animate-up mb-6 px-4 py-2 rounded-full border border-blue-200 bg-blue-50 text-blue-700 font-semibold tracking-widest uppercase text-xs inline-block shadow-sm">Sketch Brains x Enterprise Partner</div>
            <h1 class="animate-up delay-100 font-serif text-7xl font-bold text-slate-900 leading-tight mb-6">Stop Searching.<br>Start Building.</h1>
            <p class="animate-up delay-200 text-xl text-slate-600 mb-8 leading-relaxed">Stop competing for generic market talent. We custom-train elite engineering cohorts entirely on your proprietary tech stack, processes, and culture—delivering Day-1 ready hires before you even open a requisition.</p>
        </div>
        <div class="w-5/12 animate-up delay-300">
            <div class="bg-white/90 backdrop-blur-xl p-8 rounded-[32px] border border-white shadow-xl relative overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-emerald-100 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <h3 class="font-bold text-slate-800 text-xl mb-6 relative z-10 flex items-center"><i class="fa-solid fa-layer-group text-blue-500 mr-3"></i> The Pre-Trained Pipeline</h3>
                <ul class="space-y-6 relative z-10">
                    <li class="flex items-start bg-slate-50 p-4 rounded-2xl border border-slate-100">
                        <i class="fa-solid fa-circle-check text-emerald-500 mt-1 mr-4 text-xl"></i>
                        <div><span class="font-bold text-slate-800">Day-1 Productivity</span><p class="text-sm text-slate-500 mt-1">Candidates bypass typical 6-month conceptual ramp-ups.</p></div>
                    </li>
                    <li class="flex items-start bg-slate-50 p-4 rounded-2xl border border-slate-100">
                        <i class="fa-solid fa-circle-check text-emerald-500 mt-1 mr-4 text-xl"></i>
                        <div><span class="font-bold text-slate-800">Zero Training Burden</span><p class="text-sm text-slate-500 mt-1">Your senior engineers stay fully focused on building features.</p></div>
                    </li>
                    <li class="flex items-start bg-slate-50 p-4 rounded-2xl border border-slate-100">
                        <i class="fa-solid fa-circle-check text-emerald-500 mt-1 mr-4 text-xl"></i>
                        <div><span class="font-bold text-slate-800">Zero Financial Risk</span><p class="text-sm text-slate-500 mt-1">No upfront costs. You pay absolutely nothing unless you hire.</p></div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
"""

# Slide 2: The Problem (Bar Chart) - Explicitly stated Problem statement
slides[2] = """<div class="slide bg-slate-50">
    <div class="content-layer flex px-20 py-20 items-center">
        <div class="w-1/2 pr-16 border-r border-slate-200">
            <div class="animate-up mb-4 px-3 py-1 bg-rose-100 text-rose-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider">The Problem</div>
            <h2 class="animate-up delay-100 font-serif text-5xl font-bold text-slate-900 mb-6">The True Cost of Empty Seats</h2>
            <p class="animate-up delay-200 text-xl text-slate-600 mb-8 leading-relaxed">Traditional hiring acts as a massive financial drain. Agency fees, diverted engineering hours for interviews, and months of unproductive onboarding drastically inflate your Customer Acquisition Cost for talent.</p>
            <div class="animate-up delay-300 flex items-start space-x-4 mb-6 bg-white p-4 rounded-xl shadow-sm border border-slate-100">
                <i class="fa-solid fa-triangle-exclamation text-rose-500 text-2xl mt-1 w-8"></i>
                <div><h3 class="font-bold text-lg text-slate-800">Productivity Lag</h3><p class="text-slate-500 text-sm mt-1">A generic fresher takes approximately 6 months to output reliable, ship-ready code in a modern enterprise framework.</p></div>
            </div>
            <div class="animate-up delay-400 flex items-start space-x-4 bg-white p-4 rounded-xl shadow-sm border border-slate-100">
                <i class="fa-solid fa-clock text-amber-500 text-2xl mt-1 w-8"></i>
                <div><h3 class="font-bold text-lg text-slate-800">Senior Distraction</h3><p class="text-slate-500 text-sm mt-1">Your most expensive, high-leverage developers are spending dozens of hours training juniors instead of shipping roadmap features.</p></div>
            </div>
        </div>
        <div class="w-1/2 pl-12 animate-up delay-200">
            <div class="bg-white p-8 rounded-3xl shadow-xl border border-slate-100 h-full flex flex-col justify-center">
                <h3 class="text-center font-bold text-slate-800 text-xl mb-6">CapEx vs OpEx: Wasted Capital (per hire)</h3>
                <canvas id="costChart" width="100" height="70"></canvas>
            </div>
        </div>
    </div>
    <script>
        const ctx = document.getElementById('costChart');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Sourcing / Agencies', 'Internal Interview Time', 'Training Delay', 'Immediate Value Delivered'],
                datasets: [{
                    label: 'Financial Cost in $',
                    data: [5000, 8000, 15000, -2800],
                    backgroundColor: ['#FCA5A5', '#FCD34D', '#F87171', '#34D399'],
                    borderRadius: 8
                }]
            },
            options: { plugins: { legend: { display:false } }, scales: { y: { beginAtZero: true } } }
        });
    </script>
</div>
"""

# Slide 3: The Broken Funnel (Doughnut Chart) - Clear metrics
slides[3] = """<div class="slide">
    <div class="content-layer flex px-20 py-20 items-center justify-between">
        <div class="w-1/2 pr-12">
            <div class="animate-up mb-4 px-3 py-1 bg-amber-100 text-amber-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider">The Process Bottleneck</div>
            <h2 class="animate-up delay-100 font-serif text-5xl font-bold text-slate-900 mb-6">The Broken Filter Method</h2>
            <p class="animate-up delay-200 text-xl text-slate-600 mb-8 leading-relaxed">Companies currently filter out noise rather than selecting for excellence. The "Spray and Pray" model guarantees 95% of your recruiting effort is entirely wasted sorting through misaligned profiles.</p>
            <div class="animate-up delay-300 bg-slate-50 border border-slate-200 p-8 rounded-3xl shadow-sm">
                <h3 class="font-bold text-slate-800 mb-6 border-b border-slate-200 pb-2">The Standard Funnel Mathematics</h3>
                <div class="flex items-center space-x-4 mb-5">
                    <div class="w-5 h-5 rounded-full bg-slate-300"></div><div><p class="font-bold text-xl text-slate-700">80% Resume Rejections</p><p class="text-sm text-slate-500">Missing basic technical prerequisites.</p></div>
                </div>
                <div class="flex items-center space-x-4 mb-5">
                    <div class="w-5 h-5 rounded-full bg-rose-400"></div><div><p class="font-bold text-xl text-slate-700">15% Failed Interviews</p><p class="text-sm text-slate-500">Know theory, but fail practical application.</p></div>
                </div>
                <div class="flex items-center space-x-4">
                    <div class="w-5 h-5 rounded-full bg-emerald-500 shadow-lg shadow-emerald-500/50"></div><div><p class="font-bold text-3xl text-emerald-600">5% Actual Hires</p><p class="text-sm text-emerald-600 font-semibold">The needle in the haystack.</p></div>
                </div>
            </div>
        </div>
        <div class="w-5/12 animate-up delay-100 flex justify-center">
            <div class="w-[500px] relative bg-white p-10 rounded-full shadow-[0_0_60px_-15px_rgba(0,0,0,0.1)] border border-slate-50">
                <canvas id="funnelChart"></canvas>
                <div class="absolute inset-0 flex items-center justify-center flex-col pointer-events-none text-center">
                    <span class="text-5xl font-extrabold text-rose-600 tracking-tight">5%</span>
                    <span class="text-slate-500 font-bold uppercase tracking-widest text-sm mt-1">Efficiency</span>
                </div>
            </div>
        </div>
    </div>
    <script>
        const ctx = document.getElementById('funnelChart');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Resume Drop', 'Interview Fail', 'Hires'],
                datasets: [{
                    data: [80, 15, 5],
                    backgroundColor: ['#E2E8F0', '#FB7185', '#10B981'],
                    borderWidth: 2,
                    borderColor: '#FFFFFF',
                    cutout: '75%'
                }]
            },
            options: { plugins: { legend: { display:false } }, animation: { animateScale: true } }
        });
    </script>
</div>
"""

# Slide 4: The Paradigm Shift (Comparative Analysis)
slides[4] = """<div class="slide bg-slate-900 text-white overflow-hidden">
    <div class="blob blob-blue opacity-30"></div><div class="blob blob-emerald opacity-20" style="mix-blend-mode: color-dodge;"></div>
    <div class="content-layer w-full h-full p-20 flex flex-col justify-center relative z-10">
        <div class="text-center mb-12">
            <h2 class="animate-up font-serif text-5xl font-bold text-white mb-4">The Paradigm Shift</h2>
            <p class="animate-up delay-100 text-xl text-blue-200">Transitioning from reactive sourcing to proactive talent manufacturing.</p>
        </div>
        <div class="flex space-x-8 w-full animate-up delay-200">
            <!-- Old Way -->
            <div class="w-1/2 bg-slate-800/60 backdrop-blur-xl rounded-[32px] p-10 border border-slate-700/50 shadow-2xl">
                <h3 class="text-3xl font-bold text-rose-300 mb-6 border-b border-rose-300/20 pb-4"><i class="fa-solid fa-magnifying-glass mr-3"></i> The Old Way: Sourcing</h3>
                <ul class="space-y-6 text-slate-300">
                    <li class="flex items-start bg-slate-800/40 p-4 rounded-xl">
                        <i class="fa-solid fa-xmark text-rose-400 mt-1 mr-4 text-xl"></i>
                        <div><p class="font-bold text-slate-100">Bidding Wars</p><p class="text-sm mt-1 leading-relaxed">Endlessly competing and inflating salaries for generic talent available on the open market.</p></div>
                    </li>
                    <li class="flex items-start bg-slate-800/40 p-4 rounded-xl">
                        <i class="fa-solid fa-xmark text-rose-400 mt-1 mr-4 text-xl"></i>
                        <div><p class="font-bold text-slate-100">Filtering Debt</p><p class="text-sm mt-1 leading-relaxed">Burning hundreds of internal engineering hours on technical screening and interviews.</p></div>
                    </li>
                    <li class="flex items-start bg-slate-800/40 p-4 rounded-xl">
                        <i class="fa-solid fa-xmark text-rose-400 mt-1 mr-4 text-xl"></i>
                        <div><p class="font-bold text-slate-100">Onboarding Guesswork</p><p class="text-sm mt-1 leading-relaxed">Hoping candidates can adapt to your internal, undocumented frameworks after hiring.</p></div>
                    </li>
                </ul>
            </div>
            <!-- New Way -->
            <div class="w-1/2 bg-white rounded-[32px] p-10 border border-blue-200 shadow-[0_0_80px_-15px_rgba(59,130,246,0.5)] relative overflow-hidden transform scale-[1.02]">
                <div class="absolute right-0 top-0 w-48 h-48 bg-blue-50 rounded-bl-full z-0 opacity-50"></div>
                <h3 class="text-3xl font-bold text-blue-600 mb-6 border-b border-blue-100 pb-4 relative z-10"><i class="fa-solid fa-industry mr-3"></i> The New Way: Manufacturing</h3>
                <ul class="space-y-6 text-slate-700 relative z-10">
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl">
                        <i class="fa-solid fa-check text-emerald-500 mt-1 mr-4 text-xl font-bold"></i>
                        <div><p class="font-bold text-slate-900">Absolute Specifications</p><p class="text-sm mt-1 leading-relaxed text-slate-600">You dictate the exact curriculum, proprietary tech stack, and required agile workflows from day zero.</p></div>
                    </li>
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl">
                        <i class="fa-solid fa-check text-emerald-500 mt-1 mr-4 text-xl font-bold"></i>
                        <div><p class="font-bold text-slate-900">Custom Built Cohorts</p><p class="text-sm mt-1 leading-relaxed text-slate-600">We train a dedicated 40-person cohort exclusively in your environment over an intensive 3-6 month period.</p></div>
                    </li>
                    <li class="flex items-start bg-blue-50/50 p-4 rounded-xl">
                        <i class="fa-solid fa-check text-emerald-500 mt-1 mr-4 text-xl font-bold"></i>
                        <div><p class="font-bold text-slate-900">Interview for Validation</p><p class="text-sm mt-1 leading-relaxed text-slate-600">You only interview the top 10% proven performers, validating cultural fit rather than basic syntax.</p></div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
"""

# Slide 5: The Workflow (Pure CSS Flow)
slides[5] = """<div class="slide">
    <div class="bg-grid"></div>
    <div class="content-layer flex flex-col justify-center px-16 py-12">
        <div class="animate-up text-center mb-16">
            <h2 class="font-serif text-5xl font-bold text-slate-900 mb-4">The Implementation Playbook</h2>
            <p class="text-xl text-slate-500">A clean, transparent, and entirely predictable three-step pipeline.</p>
        </div>
        <div class="flex items-start justify-between w-full space-x-6 relative">
            <!-- Connecting Line Background -->
            <div class="absolute top-[48px] left-24 right-24 h-2 bg-slate-100 rounded-full z-0 pointer-events-none"></div>
            
            <!-- Step 1 -->
            <div class="animate-up delay-100 w-1/3 flex flex-col items-center text-center relative z-10">
                <div class="w-24 h-24 bg-white border-4 border-slate-200 text-slate-600 rounded-full flex items-center justify-center text-3xl mb-8 shadow-xl"><i class="fa-solid fa-clipboard-check"></i></div>
                <h3 class="font-bold text-3xl mb-4 text-slate-800 bg-white px-4">1. Define</h3>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-left w-full h-full">
                    <p class="text-slate-600 mb-3"><span class="font-bold text-slate-800">You outline the exact need.</span> We map out the curriculum required to fulfill it.</p>
                    <ul class="text-sm text-slate-500 space-y-2">
                        <li><i class="fa-solid fa-angle-right text-slate-300 mr-2"></i> Document tech stack & versions</li>
                        <li><i class="fa-solid fa-angle-right text-slate-300 mr-2"></i> Define "Day-1" core tasks</li>
                        <li><i class="fa-solid fa-angle-right text-slate-300 mr-2"></i> Set interview and selection rubrics</li>
                    </ul>
                </div>
            </div>
            
            <!-- Step 2 -->
            <div class="animate-up delay-300 w-1/3 flex flex-col items-center text-center relative z-10">
                <div class="w-24 h-24 bg-blue-50 border-4 border-blue-400 text-blue-600 rounded-full flex items-center justify-center text-3xl mb-8 shadow-xl shadow-blue-500/20"><i class="fa-solid fa-laptop-code"></i></div>
                <h3 class="font-bold text-3xl mb-4 text-blue-900 bg-white px-4">2. Train</h3>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-blue-100 text-left w-full h-full">
                    <p class="text-slate-600 mb-3"><span class="font-bold text-slate-800">We execute the build phase.</span> 30-40 top-tier students train intensively on your stack.</p>
                    <ul class="text-sm text-slate-500 space-y-2">
                        <li><i class="fa-solid fa-angle-right text-blue-300 mr-2"></i> Hands-on intensive coding sprints</li>
                        <li><i class="fa-solid fa-angle-right text-blue-300 mr-2"></i> Mock projects mirroring your systems</li>
                        <li><i class="fa-solid fa-angle-right text-blue-300 mr-2"></i> Weekly performance benchmarking</li>
                    </ul>
                </div>
            </div>
            
            <!-- Step 3 -->
            <div class="animate-up delay-500 w-1/3 flex flex-col items-center text-center relative z-10">
                <div class="w-24 h-24 bg-emerald-50 border-4 border-emerald-500 text-emerald-600 rounded-full flex items-center justify-center text-3xl mb-8 shadow-xl shadow-emerald-500/20"><i class="fa-solid fa-handshake"></i></div>
                <h3 class="font-bold text-3xl mb-4 text-emerald-900 bg-white px-4">3. Hire</h3>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-emerald-100 text-left w-full h-full">
                    <p class="text-slate-600 mb-3"><span class="font-bold text-slate-800">You select the cream of the crop.</span> Only the highest performers progress to your team.</p>
                    <ul class="text-sm text-slate-500 space-y-2">
                        <li><i class="fa-solid fa-angle-right text-emerald-300 mr-2"></i> Pre-qualified, stack-fluent candidates</li>
                        <li><i class="fa-solid fa-angle-right text-emerald-300 mr-2"></i> High offer acceptance rates</li>
                        <li><i class="fa-solid fa-angle-right text-emerald-300 mr-2"></i> Immediate integration onto projects</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
"""

# Slide 6: The "Day-1 Ready" Stack (Radar Chart)
slides[6] = """<div class="slide bg-slate-50">
    <div class="content-layer flex px-20 py-16 items-center">
        <div class="w-1/2 pr-12">
            <div class="animate-up mb-4 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider">The Delta</div>
            <h2 class="animate-up font-serif text-5xl font-bold text-slate-900 mb-6">Actual "Day-1 Ready"</h2>
            <p class="animate-up delay-100 text-xl text-slate-600 mb-8 leading-relaxed">Generic Computer Science curriculums fail to map to enterprise realities. Our framework is a hyper-targeted mirror of your organization's daily workflows.</p>
            
            <div class="animate-up delay-200 bg-white p-6 rounded-2xl border border-slate-200 shadow-[0_4px_20px_-5px_rgba(0,0,0,0.05)] mb-5 flex items-start">
                <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex justify-center items-center text-xl mr-5 shrink-0"><i class="fa-solid fa-cubes"></i></div>
                <div>
                    <h4 class="font-bold text-slate-900 text-xl border-b border-slate-100 pb-2 mb-2">Your Proprietary Frameworks</h4>
                    <p class="text-slate-500 text-sm leading-relaxed">React, Spring Boot, AWS configuration, Kubernetes scaling—Whatever you use in production, they build with it in training.</p>
                </div>
            </div>
            
            <div class="animate-up delay-300 bg-white p-6 rounded-2xl border border-slate-200 shadow-[0_4px_20px_-5px_rgba(0,0,0,0.05)] flex items-start">
                <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex justify-center items-center text-xl mr-5 shrink-0"><i class="fa-solid fa-code-branch"></i></div>
                <div>
                    <h4 class="font-bold text-slate-900 text-xl border-b border-slate-100 pb-2 mb-2">Your Operational Processes</h4>
                    <p class="text-slate-500 text-sm leading-relaxed">Agile sprint cycles, strict Git branching models, and CI/CD pipeline deployments are ingrained by muscle memory.</p>
                </div>
            </div>
        </div>
        <div class="w-1/2 animate-up delay-400 flex justify-center bg-white p-10 rounded-[32px] shadow-2xl border border-slate-100 relative">
            <div class="absolute inset-0 bg-gradient-to-tr from-blue-50/50 to-transparent rounded-[32px] pointer-events-none"></div>
            <div class="w-full relative z-10">
                <h3 class="text-center font-bold text-slate-600 mb-4 tracking-widest uppercase text-sm">Capability Matrix Check</h3>
                <canvas id="radarChart"></canvas>
            </div>
        </div>
    </div>
    <script>
        const ctx = document.getElementById('radarChart');
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Algorithms', 'System Design', 'Your Specific Stack', 'CI/CD Flow', 'Agile/Scrum', 'Team Communication'],
                datasets: [{
                    label: 'Sketch Brains Graduate',
                    data: [85, 80, 100, 95, 90, 85],
                    fill: true,
                    backgroundColor: 'rgba(59, 130, 246, 0.25)',
                    borderColor: '#3B82F6',
                    pointBackgroundColor: '#3B82F6',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#3B82F6'
                }, {
                    label: 'Standard University Fresher',
                    data: [80, 50, 25, 10, 20, 50],
                    fill: true,
                    backgroundColor: 'rgba(226, 232, 240, 0.4)',
                    borderColor: '#94A3B8',
                    pointBackgroundColor: '#94A3B8'
                }]
            },
            options: { elements: { line: { borderWidth: 3 } }, scales: { r: { angleLines: { display: true }, suggestedMin: 0, suggestedMax: 100 } }, plugins: { legend: { position: 'bottom' } } }
        });
    </script>
</div>
"""

# Slide 7: Zero Risk Model (Comparison Table)
slides[7] = """<div class="slide">
    <div class="blob blob-blue opacity-10"></div>
    <div class="content-layer flex flex-col justify-center px-24 py-16">
        <div class="text-center mb-12 animate-up">
            <div class="animate-up mb-4 px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider">The Guarantee</div>
            <h2 class="font-serif text-5xl font-bold text-slate-900 mb-4">The Zero-Risk Proposition</h2>
            <p class="text-xl text-slate-500 max-w-2xl mx-auto">You don't pay for sourcing. You don't pay for training. You only partner dynamically on successful outcomes.</p>
        </div>
        
        <div class="flex space-x-0 w-[960px] mx-auto animate-up delay-200 shadow-2xl rounded-[32px] overflow-hidden">
            <!-- Traditional Column -->
            <div class="w-1/2 bg-slate-50 p-12 py-14 text-center border border-slate-200">
                <h3 class="font-bold text-2xl text-slate-700 mb-2">Traditional Staffing Agency</h3>
                <div class="inline-block px-4 py-1 bg-rose-100 text-rose-700 rounded-full text-sm font-bold mb-8">High Overhead</div>
                
                <ul class="text-left space-y-6 text-slate-600 mb-10 w-full font-medium">
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-xmark text-rose-400 text-xl"></i></div><span class="flex-1 border-b border-slate-200 pb-2">Retainer fees paid upfront</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-xmark text-rose-400 text-xl"></i></div><span class="flex-1 border-b border-slate-200 pb-2">Zero technical pre-training</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-xmark text-rose-400 text-xl"></i></div><span class="flex-1 border-b border-slate-200 pb-2">Hours wasted interviewing randoms</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-xmark text-rose-400 text-xl"></i></div><span class="flex-1 border-b border-slate-200 pb-2">No guarantee of cultural fit</span></li>
                </ul>
                <div class="text-slate-400 font-bold uppercase tracking-widest text-sm">Financial Structure</div>
                <div class="text-4xl font-extrabold text-slate-300 mt-2">Guaranteed Spend</div>
            </div>
            
            <!-- Sketch Brains Column -->
            <div class="w-1/2 bg-white p-12 py-14 text-center border-t-8 border-t-emerald-500 relative border-r border-b border-slate-200">
                <div class="absolute -right-10 -top-10 w-32 h-32 bg-emerald-50 rounded-full z-0 opacity-50"></div>
                <h3 class="font-bold text-2xl text-emerald-900 mb-2 relative z-10">Sketch Brains Model</h3>
                <div class="inline-block px-4 py-1 bg-emerald-100 text-emerald-700 rounded-full text-sm font-bold mb-8 relative z-10">Utterly De-risked</div>
                
                <ul class="text-left space-y-6 text-slate-800 mb-10 w-full font-bold relative z-10">
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-check text-emerald-500 text-xl"></i></div><span class="flex-1 border-b border-slate-100 pb-2">No upfront sourcing costs or retainers</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-check text-emerald-500 text-xl"></i></div><span class="flex-1 border-b border-slate-100 pb-2">Candidates fully trained on your stack</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-check text-emerald-500 text-xl"></i></div><span class="flex-1 border-b border-slate-100 pb-2">You interview a curated, proven shortlist</span></li>
                    <li class="flex items-center"><div class="w-8 flex justify-center"><i class="fa-solid fa-check text-emerald-500 text-xl"></i></div><span class="flex-1 border-b border-slate-100 pb-2">You pay ONLY for the candidates you hire</span></li>
                </ul>
                <div class="text-emerald-500 font-bold uppercase tracking-widest text-sm relative z-10">Financial Structure</div>
                <div class="text-4xl font-extrabold text-slate-900 mt-2 relative z-10">Pay on Success</div>
            </div>
        </div>
    </div>
</div>
"""

# Slide 8: The ROI (Big Numbers + Detailed Support)
slides[8] = """<div class="slide bg-slate-900 text-white">
    <div class="blob blob-blue opacity-30"></div><div class="blob blob-emerald opacity-20"></div>
    <div class="content-layer flex flex-col justify-center items-center px-16">
        <div class="text-center mb-16 animate-up">
            <div class="animate-up mb-4 px-3 py-1 bg-blue-900/50 text-blue-300 rounded-full text-xs font-bold inline-block uppercase tracking-wider border border-blue-500/30">The ROI</div>
            <h2 class="font-serif text-5xl font-bold mb-4">Enterprise Impact Metrics</h2>
            <p class="text-xl text-slate-400">Data compiled from across our active B2B enterprise partnerships.</p>
        </div>
        
        <div class="flex space-x-6 w-full animate-up delay-200">
            <!-- Stat 1 -->
            <div class="flex-1 bg-white/5 backdrop-blur-xl p-8 rounded-3xl border border-white/10 flex flex-col shadow-[0_20px_40px_-15px_rgba(0,0,0,0.5)]">
                <div class="bg-amber-400/20 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-amber-400/30"><i class="fa-solid fa-bolt text-3xl text-amber-400"></i></div>
                <div class="text-6xl font-extrabold text-white mb-2 tracking-tighter">-70%</div>
                <div class="text-xl font-bold text-amber-400 border-b border-white/10 pb-4 mb-4">Time to Productivity</div>
                <p class="text-sm text-slate-300 leading-relaxed font-medium">Our candidates bypass the standard 6-month conceptual ramp-up period by contributing to mock versions of your actual codebase during their final intensive training sprint.</p>
            </div>
            
            <!-- Stat 2 -->
            <div class="flex-1 bg-white/5 backdrop-blur-xl p-8 rounded-3xl border border-white/10 flex flex-col shadow-[0_20px_40px_-15px_rgba(0,0,0,0.5)] transform scale-[1.05] z-10 border-t-4 border-t-blue-500">
                <div class="bg-blue-400/20 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-blue-400/30"><i class="fa-solid fa-users-viewfinder text-3xl text-blue-400"></i></div>
                <div class="text-6xl font-extrabold text-white mb-2 tracking-tighter">100%</div>
                <div class="text-xl font-bold text-blue-400 border-b border-white/10 pb-4 mb-4">Tech Stack Match</div>
                <p class="text-sm text-slate-300 leading-relaxed font-medium">Because you dictate the curriculum on Day 1, there is zero translation error. If your environment relies on a highly obscure microservices pattern, they learn exactly that pattern.</p>
            </div>
            
            <!-- Stat 3 -->
            <div class="flex-1 bg-white/5 backdrop-blur-xl p-8 rounded-3xl border border-white/10 flex flex-col shadow-[0_20px_40px_-15px_rgba(0,0,0,0.5)]">
                <div class="bg-emerald-400/20 w-16 h-16 rounded-2xl flex items-center justify-center mb-6 border border-emerald-400/30"><i class="fa-solid fa-chart-line text-3xl text-emerald-400"></i></div>
                <div class="text-6xl font-extrabold text-white mb-2 tracking-tighter">3x</div>
                <div class="text-xl font-bold text-emerald-400 border-b border-white/10 pb-4 mb-4">Retention Rate Increase</div>
                <p class="text-sm text-slate-300 leading-relaxed font-medium">Employees who are specifically cultivated and successfully placed into an ecosystem they already understand demonstrate drastically higher long-term loyalty and job satisfaction.</p>
            </div>
        </div>
    </div>
</div>
"""

# Slide 9: CTA (Roadmap & Contact)
slides[9] = """<div class="slide">
    <div class="bg-grid"></div>
    <div class="content-layer w-full flex h-full p-20 items-center">
        <!-- The Roadmap -->
        <div class="w-1/2 pr-12 border-r border-slate-200">
            <div class="animate-up mb-4 px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold inline-block uppercase tracking-wider">Next Steps</div>
            <h2 class="animate-up delay-100 font-serif text-5xl font-bold text-slate-900 mb-6 leading-tight">Activating Your Zero-Risk Pilot</h2>
            <p class="animate-up delay-200 text-xl text-slate-500 mb-10 leading-relaxed">Choose a single role causing hiring bottlenecks within your organization and let us prove the mathematical efficiency of the pipeline model.</p>
            
            <div class="space-y-6 animate-up delay-300 relative">
                <!-- Vertical connecting line -->
                <div class="absolute left-6 top-6 bottom-6 w-1 bg-slate-100 z-0"></div>
                
                <div class="flex items-center relative z-10"><div class="w-12 h-12 rounded-full bg-white border-4 border-slate-200 text-slate-400 flex justify-center items-center font-bold mr-6 shadow-sm"><i class="fa-solid fa-list-check"></i></div><div><p class="font-bold text-slate-800 text-xl mb-1">Define Target Role</p><p class="text-sm text-slate-500 font-medium">Scoping call to identify stack and bottlenecks.</p></div></div>
                <div class="flex items-center relative z-10"><div class="w-12 h-12 rounded-full bg-blue-50 border-4 border-blue-200 text-blue-500 flex justify-center items-center font-bold mr-6 shadow-sm"><i class="fa-solid fa-pen-ruler"></i></div><div><p class="font-bold text-slate-800 text-xl mb-1">Curriculum Design</p><p class="text-sm text-slate-500 font-medium">We map a custom 3-month cohort syllabus.</p></div></div>
                <div class="flex items-center relative z-10"><div class="w-12 h-12 rounded-full bg-blue-500 border-4 border-blue-600 text-white flex justify-center items-center font-bold mr-6 shadow-lg shadow-blue-500/30"><i class="fa-solid fa-users-gear"></i></div><div><p class="font-bold text-slate-800 text-xl mb-1">Cohort Launch</p><p class="text-sm text-slate-500 font-medium">30+ top-tier candidates begin intensive training.</p></div></div>
                <div class="flex items-center relative z-10"><div class="w-12 h-12 rounded-full bg-emerald-50 border-4 border-emerald-200 text-emerald-500 flex justify-center items-center font-bold mr-6 shadow-sm"><i class="fa-solid fa-handshake"></i></div><div><p class="font-bold text-slate-800 text-xl mb-1">Interviews & Hiring</p><p class="text-sm text-slate-500 font-medium">You selectively hire only the absolute best.</p></div></div>
            </div>
        </div>
        
        <!-- The Action Button -->
        <div class="w-1/2 pl-16 flex flex-col justify-center items-center animate-up delay-400">
            <div class="bg-white p-10 rounded-[32px] shadow-2xl border border-slate-100 w-full text-center relative overflow-hidden transform hover:scale-[1.02] transition duration-500">
                <div class="absolute -right-16 -top-16 w-48 h-48 bg-blue-50 rounded-full blur-3xl z-0"></div>
                <i class="fa-solid fa-paper-plane text-5xl text-blue-500 mb-8 relative z-10 drop-shadow-md"></i>
                <h3 class="font-serif text-4xl font-bold text-slate-900 mb-4 relative z-10">Bypass the Bottleneck.</h3>
                <p class="text-slate-500 mb-10 relative z-10 text-lg">Schedule a 15-minute scoping call to explore our capability to map your specific engineering roles.</p>
                <div class="bg-blue-600 text-white w-full py-5 rounded-2xl font-bold text-xl cursor-pointer hover:bg-blue-700 hover:shadow-xl hover:shadow-blue-600/20 transition duration-300 relative z-10 flex items-center justify-center"><span>Schedule Scoping Call</span><i class="fa-solid fa-arrow-right ml-3"></i></div>
                <p class="mt-6 text-sm text-slate-400 font-bold tracking-wider uppercase relative z-10">contact@sketchbrains.com</p>
            </div>
        </div>
    </div>
</div>
"""

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(base_head + slides[i] + "\n</body>\n</html>")

print("Generated content-rich, mathematically-perfect 'Goldilocks' visually-stunning pitch deck.")

import os

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

slide_7_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet"/>
    <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet"/>
    <style>
        body, html { margin:0; padding:0; font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; }
        .slide { width: 1280px; height: 720px; position: relative; overflow: hidden; background: #F8FAFC; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: inset 0 0 0 1px #E2E8F0; }
        .font-serif { font-family: 'Playfair Display', serif; }
        .bg-grid { background-image: radial-gradient(#CBD5E1 1px, transparent 1px); background-size: 32px 32px; opacity: 0.3; position: absolute; inset: 0; pointer-events: none; }
        .animate-up { animation: fadeUp 1s ease-out forwards; opacity: 0; transform: translateY(30px); }
        .delay-100 { animation-delay: 0.1s; } .delay-200 { animation-delay: 0.2s; }
        @keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
        .blob { position: absolute; border-radius: 50%; filter: blur(80px); z-index: 0; opacity: 0.4; }
        .blob-blue { background: #3B82F6; width: 600px; height: 600px; top: -100px; left: -100px; }
        .blob-emerald { background: #10B981; width: 500px; height: 500px; bottom: -100px; right: -100px; }
        .content-layer { z-index: 10; position: relative; width: 100%; height: 100%; display: flex; }
    </style>
</head>
<body>
<div class="slide">
    <div class="bg-grid"></div>
    <div class="blob blob-blue opacity-30"></div><div class="blob blob-emerald opacity-20"></div>
    <div class="content-layer flex flex-col justify-center px-16 py-8">
        <div class="text-center mb-6 animate-up">
            <div class="mb-3 px-4 py-1.5 bg-emerald-50 text-emerald-700 rounded-full text-xs font-bold inline-block uppercase tracking-widest border border-emerald-200 shadow-sm">Zero-Risk Contract</div>
            <h2 class="font-serif text-5xl font-bold text-slate-900 mb-3">The Commercial Structure</h2>
            <p class="text-xl text-slate-500 max-w-3xl mx-auto">No sourcing fees. No training costs. You leverage a dynamic partnership entirely based on successful hires.</p>
        </div>
        
        <div class="flex justify-between items-center w-[980px] mx-auto animate-up delay-200 relative">
            
            <!-- VS Badge -->
            <div class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 z-20 w-14 h-14 bg-white rounded-full flex items-center justify-center text-slate-400 font-black shadow-lg border border-slate-100 italic text-xl">VS</div>

            <!-- Traditional Column -->
            <div class="w-[48%] bg-white p-8 rounded-3xl border border-slate-200 text-center shadow-lg relative transform scale-[0.98] transition-all hover:scale-100">
                <h3 class="font-bold text-2xl text-slate-600 mb-4">Standard Agency</h3>
                <div class="inline-block px-3 py-1 bg-slate-50 text-slate-500 rounded-full text-xs font-bold mb-6 border border-slate-200">High Risk & High Cost</div>
                
                <ul class="text-left space-y-4 text-slate-500 mb-6 w-full text-sm font-medium">
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-lg mt-0.5 mr-3"></i><span class="flex-1">Retainer fees paid upfront before results.</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-lg mt-0.5 mr-3"></i><span class="flex-1">Massive internal engineering hours wasted interviewing randoms.</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-xmark text-rose-400 text-lg mt-0.5 mr-3"></i><span class="flex-1">Zero technical pre-training specific to your tech.</span></li>
                </ul>
                <div class="pt-6 border-t border-slate-100">
                    <div class="text-slate-400 font-bold uppercase tracking-widest text-xs mb-1">Financial Outcome</div>
                    <div class="text-2xl font-extrabold text-slate-400">Guaranteed Spend</div>
                </div>
            </div>
            
            <!-- Sketch Brains Column -->
            <div class="w-[48%] bg-white p-8 rounded-3xl border-2 border-emerald-500 text-center shadow-[0_20px_40px_-15px_rgba(16,185,129,0.3)] relative z-10 overflow-hidden transform scale-100">
                <div class="absolute -right-6 -top-6 w-32 h-32 bg-emerald-50 rounded-full z-0 opacity-50 blur-xl"></div>
                <h3 class="font-bold text-2xl text-emerald-900 mb-4 relative z-10 flex items-center justify-center"><i class="fa-solid fa-shield-check text-emerald-500 mr-2"></i> Sketch Brains Model</h3>
                <div class="inline-block px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold mb-6 border border-emerald-200 relative z-10">Utterly De-risked Pipeline</div>
                
                <ul class="text-left space-y-4 text-slate-800 mb-6 w-full text-sm font-bold relative z-10">
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-lg mt-0.5 mr-3 font-black"></i><span class="flex-1">No upfront sourcing costs or retainers whatsoever.</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-lg mt-0.5 mr-3 font-black"></i><span class="flex-1">You only interview a curated, proven shortlist.</span></li>
                    <li class="flex items-start"><i class="fa-solid fa-check text-emerald-500 text-lg mt-0.5 mr-3 font-black"></i><span class="flex-1">Candidates are fully trained on your proprietary stack.</span></li>
                </ul>
                <div class="pt-6 border-t border-emerald-100 relative z-10">
                    <div class="text-emerald-600 font-extrabold uppercase tracking-widest text-xs mb-1">Financial Outcome</div>
                    <div class="text-3xl font-black text-emerald-500">Pay ONLY on Hire</div>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>"""

filepath = os.path.join(slide_dir, "slide_7.html")
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(slide_7_html)

print("Slide 7 elegantly redesigned to stay within bounds and pop visually.")

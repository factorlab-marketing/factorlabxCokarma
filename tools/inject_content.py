import os
import re
from bs4 import BeautifulSoup

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

def restore_elegant_typography(html):
    html = re.sub(r'\btext-7xl\b', 'text-5xl', html)
    html = re.sub(r'\btext-6xl\b', 'text-4xl', html)
    html = re.sub(r'\btext-5xl\b', 'text-3xl', html)
    html = re.sub(r'\btext-4xl\b', 'text-2xl', html)
    html = re.sub(r'\btext-2xl\b', 'text-xl', html)
    html = re.sub(r'\bh-\[580px\]\b', '', html)
    # Remove justify-center tight clustering to let flex items space out with new content
    html = re.sub(r'\bjustify-center\b', '', html)
    return html

s1_content = """
<div class="my-6 p-6 rounded-3xl bg-white shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100 relative overflow-hidden animate-fade-up delay-400">
    <div class="absolute right-0 top-0 w-32 h-32 bg-blue-50 rounded-full blur-2xl -mr-10 -mt-10"></div>
    <h3 class="text-xl font-serif text-slate-800 mb-2">The Paradigm Shift</h3>
    <p class="text-slate-500 text-sm leading-relaxed mb-5">Instead of endlessly filtering through candidates who lack the exact skills you need, we manufacture the exact talent pool to your precise specifications. You control the curriculum, we shoulder the training risk.</p>
    <div class="flex flex-col space-y-3">
        <div class="flex items-center text-sm text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-100"><i class="fa-solid fa-layer-group text-blue-500 mr-3 text-lg"></i> 100% Stack Alignment</div>
        <div class="flex items-center text-sm text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-100"><i class="fa-solid fa-bolt text-amber-500 mr-3 text-lg"></i> Zero Sourcing Lag</div>
    </div>
</div>
"""

s2_content = """
<div class="my-6 flex flex-col space-y-3 animate-fade-up delay-400">
    <div class="p-4 rounded-2xl bg-rose-50 border border-rose-100 flex items-center justify-between">
        <div class="flex items-center space-x-4">
            <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm text-rose-500"><i class="fa-solid fa-search"></i></div>
            <div><p class="text-rose-900 font-bold text-base">Sourcing Phase</p><p class="text-rose-600 text-xs">Spray and pray approach</p></div>
        </div>
        <div class="px-3 py-1 bg-white rounded-full text-rose-700 text-xs font-bold shadow-sm">80% Drop-off</div>
    </div>
    <div class="flex items-center justify-center"><div class="w-1 h-6 bg-rose-200 rounded-full"></div></div>
    <div class="p-4 rounded-2xl bg-amber-50 border border-amber-100 flex items-center justify-between">
        <div class="flex items-center space-x-4">
            <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm text-amber-500"><i class="fa-solid fa-code"></i></div>
            <div><p class="text-amber-900 font-bold text-base">Technical Interviews</p><p class="text-amber-600 text-xs">Testing generic algorithms</p></div>
        </div>
        <div class="px-3 py-1 bg-white rounded-full text-amber-700 text-xs font-bold shadow-sm">15% Pass</div>
    </div>
    <div class="flex items-center justify-center"><div class="w-1 h-6 bg-amber-200 rounded-full"></div></div>
    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between">
        <div class="flex items-center space-x-4">
            <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm text-slate-500"><i class="fa-solid fa-chalkboard-user"></i></div>
            <div><p class="text-slate-900 font-bold text-base">Onboarding</p><p class="text-slate-600 text-xs">Months to productivity</p></div>
        </div>
        <div class="px-3 py-1 bg-white rounded-full text-slate-700 text-xs font-bold shadow-sm">High Cost</div>
    </div>
</div>
"""

s5_content = """
<div class="mt-6 mb-2 p-6 rounded-3xl bg-gradient-to-br from-teal-50 to-emerald-50 border border-teal-100 animate-fade-up delay-400">
    <h3 class="text-lg font-bold text-teal-900 mb-3"><i class="fa-solid fa-chart-line mr-2"></i> Corporate Impact</h3>
    <p class="text-sm text-teal-800 mb-4">Clients utilizing pre-trained cohorts see dramatic shifts in core hiring metrics.</p>
    <div class="grid grid-cols-2 gap-4">
        <div class="bg-white p-4 rounded-xl shadow-sm border border-teal-50 text-center">
            <p class="text-3xl font-extrabold text-teal-600 mb-1">-70%</p>
            <p class="text-xs font-semibold text-slate-600">Time to Productivity</p>
        </div>
        <div class="bg-white p-4 rounded-xl shadow-sm border border-teal-50 text-center">
            <p class="text-3xl font-extrabold text-teal-600 mb-1">3x</p>
            <p class="text-xs font-semibold text-slate-600">Offer Acceptance</p>
        </div>
    </div>
</div>
"""

s7_content = """
<div class="mt-6 p-8 rounded-3xl bg-slate-900 text-white shadow-xl animate-fade-up delay-400 relative overflow-hidden">
    <div class="absolute right-0 top-0 w-48 h-48 bg-emerald-500 rounded-full blur-3xl opacity-20 -mr-10 -mt-10"></div>
    <i class="fa-solid fa-quote-left text-3xl text-emerald-400 mb-4 opacity-50"></i>
    <p class="text-sm font-serif italic mb-6 relative z-10 leading-relaxed">"We spent millions on entry-level hiring just trying to find the few who actually fit our stack. The pre-trained pipeline model completely eliminated the guesswork from our engineering roadmap."</p>
    <div class="flex items-center space-x-3 relative z-10">
        <div class="w-10 h-10 rounded-full bg-slate-700 flex items-center justify-center text-slate-300"><i class="fa-solid fa-user-tie"></i></div>
        <div>
            <p class="text-sm font-bold text-white">CTO Perspective</p>
            <p class="text-xs text-slate-400">Enterprise Engineering Team</p>
        </div>
    </div>
</div>
"""

s3_content = """
<div class="mt-6 p-6 rounded-3xl bg-blue-50 border border-blue-100 animate-fade-up delay-500">
    <div class="flex items-start space-x-4">
        <div class="w-12 h-12 bg-white rounded-full flex items-center justify-center text-blue-600 shadow-sm flex-shrink-0">
            <i class="fa-solid fa-lightbulb text-xl"></i>
        </div>
        <div>
            <p class="text-lg font-bold text-blue-900 mb-1">Shift Your Focus</p>
            <p class="text-sm text-blue-800 leading-relaxed">When candidates arrive perfectly trained for your internal tooling, your engineering leads spend zero time teaching basics and 100% of their time evaluating culture fit and problem-solving aptitude.</p>
        </div>
    </div>
</div>
"""

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = restore_elegant_typography(html)
    soup = BeautifulSoup(html, 'html.parser')
    
    if i == 1:
        target = soup.find('div', class_=re.compile(r'grid-cols-3'))
        if target: target.insert_before(BeautifulSoup(s1_content, 'html.parser'))
    elif i == 2:
        target = soup.find('div', class_=re.compile(r'grid-cols-3'))
        if target: target.insert_before(BeautifulSoup(s2_content, 'html.parser'))
    elif i == 3:
        # Right column
        cols = soup.find_all('div', class_=re.compile(r'\bcard\b'))
        if len(cols) > 0: cols[-1].append(BeautifulSoup(s3_content, 'html.parser'))
    elif i == 5:
        target = soup.find('div', class_=re.compile(r'mt-[0-9]+ flex items-center justify-between'))
        if not target and len(soup.find_all('div', class_=re.compile(r'w-1/2 flex flex-col'))) > 0:
            target = soup.find_all('div', class_=re.compile(r'\bcard\b'))[0] # Left card
        if target and target.parent: target.parent.append(BeautifulSoup(s5_content, 'html.parser'))
    elif i == 7:
        cols = soup.find_all('div', class_=re.compile(r'\bcard\b'))
        if len(cols) > 0: cols[-1].append(BeautifulSoup(s7_content, 'html.parser'))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Content added and typography refined.")

import os
import re
from bs4 import BeautifulSoup

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

new_style = """
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body { 
        margin:0; padding:0; 
        background: #050814;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .slide {
        width: 1280px; height: 720px;
        display: flex;
        position: relative;
        overflow: hidden;
        color: #EAF0FF;
        background: radial-gradient(circle at 15% 50%, #0a1128 0%, #050814 100%);
    }
    .bg-glow {
        position: absolute;
        border-radius: 50%;
        filter: blur(90px);
        opacity: 0.5;
        animation: float 10s infinite ease-in-out alternate;
    }
    .glow-1 { width: 600px; height: 600px; background: rgba(30, 58, 138, 0.4); top: -150px; left: -150px; }
    .glow-2 { width: 500px; height: 500px; background: rgba(15, 118, 110, 0.3); bottom: -100px; right: -50px; animation-delay: -5s; }
    
    @keyframes float {
        0% { transform: translateY(0) scale(1); }
        100% { transform: translateY(40px) scale(1.05); }
    }
    
    .card {
        background: rgba(15, 26, 51, 0.4);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 24px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
        border-radius: 24px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 50px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
    }
    
    .chip {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
    }
    .fine-border { border: 1px solid rgba(255,255,255,0.08); }
    .arrow-line { background: rgba(255,255,255,0.15); }
    
    .animate-fade-up {
        animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
        transform: translateY(20px);
    }
    .delay-100 { animation-delay: 0.1s; }
    .delay-200 { animation-delay: 0.2s; }
    .delay-300 { animation-delay: 0.3s; }
    .delay-400 { animation-delay: 0.4s; }
    .delay-500 { animation-delay: 0.5s; }
    .delay-600 { animation-delay: 0.6s; }
    
    @keyframes fadeUp {
        to { opacity: 1; transform: translateY(0); }
    }
    
    h1, h2, h3, .font-extrabold { letter-spacing: -0.03em; }
    .muted { color: #94A3B8; }
    
    .text-gradient {
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .text-gradient-accent {
        background: linear-gradient(135deg, #60a5fa 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .danger { color: #f87171; }
    .danger-bg { background: rgba(248, 113, 113, 0.1); border: 1px solid rgba(248, 113, 113, 0.2); }
"""

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Replace style
    style_tag = soup.find('style')
    if style_tag:
        style_tag.string = new_style
    
    # Add Font family
    for tag in soup.find_all(style=True):
        tag['style'] = tag['style'].replace('Inter', 'Plus Jakarta Sans')
    
    # Add background glows
    pointer_events = soup.find('div', class_=re.compile(r'pointer-events-none'))
    if pointer_events:
        pointer_events.clear()
        
        glow1 = soup.new_tag('div', attrs={'class': 'bg-glow glow-1'})
        glow2 = soup.new_tag('div', attrs={'class': 'bg-glow glow-2'})
        dots = soup.new_tag('div', attrs={'class': 'absolute inset-0 opacity-10'})
        dots['style'] = "background-image: radial-gradient(circle, rgba(255,255,255,0.3) 1px, transparent 1px); background-size: 32px 32px;"
        
        pointer_events.append(glow1)
        pointer_events.append(glow2)
        pointer_events.append(dots)
        
    # Remove genspark images
    for img in soup.find_all('img'):
        if img.get('src') and 'genspark.ai' in img.get('src'):
            img_parent = img.parent
            if img_parent and 'bg-black' in img_parent.get('class', []):
                img_parent.decompose()
            else:
                img.decompose()
                
    # Add animations
    headings = soup.find_all('p', class_=re.compile(r'text-6xl|text-5xl'))
    for idx, h in enumerate(headings):
        h['class'] = h.get('class', []) + ['animate-fade-up', f'delay-{100 + idx*100}']
    
    subheadings = soup.find_all('p', class_=re.compile(r'text-3xl|text-4xl'))
    for idx, sh in enumerate(subheadings):
        sh['class'] = sh.get('class', []) + ['animate-fade-up', f'delay-{300 + idx*100}']
        
    cards = soup.find_all('div', class_=re.compile(r'\bcard\b'))
    for idx, c in enumerate(cards):
        c['class'] = c.get('class', []) + ['animate-fade-up', f'delay-{400 + idx*100}']
        
    metrics = soup.find_all('div', class_=re.compile(r'grid-cols-'))
    for idx, m in enumerate(metrics):
        m['class'] = m.get('class', []) + ['animate-fade-up', f'delay-{500 + idx*100}']
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Processed 9 slides with premium theme.")

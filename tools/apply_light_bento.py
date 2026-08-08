import os
import re
from bs4 import BeautifulSoup

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

new_style = """
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');
    
    :root {
        --bg-main: #F4F4F5; /* Zing 100 */
        --card-bg: #FFFFFF;
        --card-border: #E4E4E7;
        --text-main: #09090B; /* Zinc 950 */
        --text-muted: #71717A; /* Zinc 500 */
        --accent-dark: #09090B; /* Deep sophisticated black instead of gray */
        --accent-light: #F4F4F5;
        --brand-primary: #0F766E;
    }
    
    html, body { 
        margin:0; padding:0; 
        background: var(--bg-main);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-main);
    }
    .slide {
        width: 1280px; height: 720px;
        display: flex;
        position: relative;
        overflow: hidden;
        background: var(--bg-main);
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
    }
    
    /* Decorative Minimalist Grid */
    .deco-line { position: absolute; background: #D4D4D8; z-index: 0; }
    .line-v { width: 1px; height: 100%; top: 0; }
    .line-h { height: 1px; width: 100%; left: 0; }
    
    .card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        box-shadow: 0 4px 24px -8px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.02);
        border-radius: 20px;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease;
        position: relative;
        overflow: hidden;
        z-index: 10;
    }
    
    .card-dark {
        background: var(--accent-dark);
        border: 1px solid #27272A;
        color: #FAFAFA;
        box-shadow: 0 20px 40px -10px rgba(0,0,0,0.2);
    }
    .card-dark .muted { color: #A1A1AA; }
    
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px -8px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.03);
    }
    .card-dark:hover {
        box-shadow: 0 24px 48px -12px rgba(0,0,0,0.3);
    }
    
    .fine-border { border: 1px solid var(--card-border); background: #FFFFFF; }
    .card-dark .fine-border { border-color: #27272A; background: #18181B; color: #FAFAFA; }
    
    .chip {
        background: #FFFFFF;
        border: 1px solid var(--card-border);
        color: var(--text-main);
        font-weight: 600;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .card-dark .chip { background: #27272A; border-color: #3F3F46; color: #FFFFFF; }
    
    .icon-box { background: #F4F4F5; border: 1px solid #E4E4E7; color: #09090B; display:flex; align-items:center; justify-content:center; }
    .card-dark .icon-box { background: #27272A; border-color: #3F3F46; color: #FFFFFF; }
    
    .arrow-line { background: #D4D4D8; }
    .card-dark .arrow-line { background: #3F3F46; }
    
    /* Editorial Serif */
    .font-serif {
        font-family: 'Playfair Display', serif;
        letter-spacing: -0.01em;
    }
    
    h1, h2, h3, .font-extrabold { letter-spacing: -0.03em; }
    .muted { color: var(--text-muted); }
    
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
    
    /* System Colors */
    .danger { color: #E11D48; } 
    .danger-bg { background: #FFE4E6; border: 1px solid #FECDD3; }
    .card-dark .danger-bg { background: rgba(225, 29, 72, 0.1); border-color: rgba(225, 29, 72, 0.2); }
    
    .good { color: #059669; } 
    .good-bg { background: #D1FAE5; border: 1px solid #A7F3D0; }
    .card-dark .good-bg { background: rgba(5, 150, 105, 0.1); border-color: rgba(5, 150, 105, 0.2); }
    
    .accent { color: #4F46E5; } 
    .accent-bg { background: #E0E7FF; border: 1px solid #C7D2FE; }
    .card-dark .accent-bg { background: rgba(79, 70, 229, 0.1); border-color: rgba(79, 70, 229, 0.2); }
    
    .warn { color: #D97706; } 
    .warn-bg { background: #FEF3C7; border: 1px solid #FDE68A; }
    .card-dark .warn-bg { background: rgba(217, 119, 6, 0.1); border-color: rgba(217, 119, 6, 0.2); }
    
    .text-gradient, .text-gradient-accent {
        background: none;
        -webkit-text-fill-color: currentcolor;
    }
    .text-white { color: inherit !important; }
"""

def process_slide(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Replace style
    style_tag = soup.find('style')
    if style_tag:
        style_tag.string = new_style
        
    # Strip hardcoded styles
    for tag in soup.find_all(style=True):
        style = tag['style']
        style = re.sub(r'background:\s*#[0-9A-Fa-f]{6};?', '', style)
        style = re.sub(r'background:\s*rgba\([^)]+\);?', '', style)
        style = re.sub(r'border:\s*1px solid[^;]+;?', '', style)
        style = re.sub(r'color:\s*#[0-9A-Fa-f]{6};?', '', style)
        # Remove empty style attributes
        style = style.strip()
        if not style:
            del tag['style']
        else:
            tag['style'] = style

    # Icon formatting
    for icon in soup.find_all('i', class_=re.compile(r'fa-')):
        if icon.parent and icon.parent.name == 'div' and ('w-8' in icon.parent.get('class', []) or 'w-10' in icon.parent.get('class', []) or 'w-12' in icon.parent.get('class', [])):
            icon.parent['class'] = [c for c in icon.parent.get('class', []) if not c.startswith('bg-') and not c.startswith('border-')]
            if 'icon-box' not in icon.parent['class']:
                icon.parent['class'].append('icon-box')

    # Accent Dark Logic for right column
    cards = soup.find_all('div', class_=re.compile(r'\bcard\b'))
    for idx, c in enumerate(cards):
        # We can dynamically set some right-side major cards to dark bento
        if idx % 2 == 0:  # Usually 0 is the first main card in the code flow layout
            if 'card-dark' not in c['class']:
                c['class'].append('card-dark')
                
    # Add Editorial Serif to main headers
    for p in soup.find_all('p', class_=re.compile(r'text-5xl|text-4xl')):
        if 'font-serif' not in p.get('class', []):
            p['class'] = p.get('class', []) + ['font-serif', 'italic']

    # Update background decoration
    ptr = soup.find('div', class_=re.compile(r'pointer-events-none'))
    if ptr:
        ptr.clear()
        # Add delicate grid lines common in editorial bento design
        ptr.append(soup.new_tag('div', attrs={'class': 'deco-line line-v', 'style': 'left: 64px;'}))
        ptr.append(soup.new_tag('div', attrs={'class': 'deco-line line-v', 'style': 'right: 64px;'}))
        ptr.append(soup.new_tag('div', attrs={'class': 'deco-line line-h', 'style': 'top: 64px;'}))
        ptr.append(soup.new_tag('div', attrs={'class': 'deco-line line-h', 'style': 'bottom: 64px;'}))

    # Strip any text-white classes that force hidden text on light backgrounds
    for w in soup.find_all(class_=re.compile(r'text-white')):
        w['class'] = [c for c in w['class'] if c != 'text-white']
        
    return str(soup)

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = process_slide(html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Light Theme Bento redesign complete.")

import os
import re
from bs4 import BeautifulSoup

slide_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck\sketch_brains_x_company_deck\slides"

new_style = """
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');
    
    :root {
        --text-main: #0F172A;
        --text-muted: #475569;
    }
    
    html, body { 
        margin:0; padding:0; 
        background: #F8FAFC;
        font-family: 'Outfit', sans-serif;
        color: var(--text-main);
    }
    .slide {
        width: 1280px; height: 720px;
        display: flex;
        position: relative;
        overflow: hidden;
        background: #F8FAFC;
        z-index: 1;
    }
    
    /* Massive softly animated pastel orbs to fill empty space visually */
    .blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(120px);
        z-index: -1;
        animation: float 20s infinite ease-in-out alternate;
    }
    .blob-1 { width: 800px; height: 800px; background: rgba(147, 197, 253, 0.45); top: -200px; left: -200px; }
    .blob-2 { width: 700px; height: 700px; background: rgba(52, 211, 153, 0.35); bottom: -100px; right: -100px; animation-delay: -5s; }
    .blob-3 { width: 800px; height: 800px; background: rgba(192, 132, 252, 0.35); top: 30%; left: 30%; animation-delay: -10s; }
    
    @keyframes float {
        0% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(60px, -60px) scale(1.05); }
        66% { transform: translate(-40px, 60px) scale(0.95); }
        100% { transform: translate(0, 0) scale(1); }
    }
    
    /* Creative Glassmorphism Cards */
    .card {
        background: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 
            0 24px 48px -12px rgba(15, 23, 42, 0.08), 
            inset 0 1px 0 rgba(255, 255, 255, 1);
        border-radius: 32px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    /* Some main cards pop with a soft brand color */
    .card-accent {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.8) 0%, rgba(241, 245, 249, 0.8) 100%);
        border: 1px solid rgba(255,255,255,0.9);
    }
    
    .card:hover {
        transform: translateY(-6px);
        box-shadow: 
            0 32px 64px -12px rgba(15, 23, 42, 0.12), 
            inset 0 1px 0 rgba(255, 255, 255, 1);
    }
    
    .fine-border { 
        border: 1px solid rgba(255,255,255,0.8); 
        background: rgba(255, 255, 255, 0.45); 
        backdrop-filter: blur(12px);
    }
    
    .chip {
        background: #FFFFFF;
        border: 1px solid rgba(15, 23, 42, 0.06);
        color: var(--text-main);
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        border-radius: 9999px;
    }
    
    .icon-box { 
        background: #FFFFFF; 
        border: 1px solid rgba(15, 23, 42, 0.06); 
        color: #3B82F6; 
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.12); 
    }
    
    .arrow-line { background: #CBD5E1; }
    
    /* Typography */
    .font-serif {
        font-family: 'Playfair Display', serif;
        letter-spacing: -0.01em;
        line-height: 1.15;
    }
    
    h1, h2, h3, .font-extrabold { letter-spacing: -0.03em; }
    .muted { color: var(--text-muted); }
    
    /* Staggered Animations */
    .animate-fade-up {
        animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        opacity: 0;
        transform: translateY(30px);
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
    
    /* Beautiful specific colors */
    .danger { color: #E11D48; } 
    .danger-bg { background: rgba(225, 29, 72, 0.08); border: 1px solid rgba(225, 29, 72, 0.2); }
    
    .good { color: #059669; } 
    .good-bg { background: rgba(5, 150, 105, 0.08); border: 1px solid rgba(5, 150, 105, 0.2); }
    
    .warn { color: #D97706; } 
    .warn-bg { background: rgba(217, 119, 6, 0.08); border: 1px solid rgba(217, 119, 6, 0.2); }
    
    .accent { color: #4F46E5; } 
    .accent-bg { background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.2); }
"""

def upscale_tailwinds(html):
    # Upscale to make typography bold and fill empty places
    html = re.sub(r'\btext-sm\b', 'text-base', html)
    html = re.sub(r'\btext-lg\b', 'text-xl', html)
    html = re.sub(r'\btext-xl\b', 'text-2xl', html)
    html = re.sub(r'\btext-2xl\b', 'text-4xl', html)
    html = re.sub(r'\btext-3xl\b', 'text-5xl', html)
    return html

def re_add_blobs(soup):
    # Remove any old bg-glow or deco-lines
    ptr = soup.find('div', class_=re.compile(r'pointer-events-none'))
    if ptr:
        ptr.clear()
        ptr.append(soup.new_tag('div', attrs={'class': 'blob blob-1'}))
        ptr.append(soup.new_tag('div', attrs={'class': 'blob blob-2'}))
        ptr.append(soup.new_tag('div', attrs={'class': 'blob blob-3'}))
    return soup

for i in range(1, 10):
    filepath = os.path.join(slide_dir, f"slide_{i}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    style_tag = soup.find('style')
    if style_tag:
        style_tag.string = new_style
        
    soup = re_add_blobs(soup)
    
    html = str(soup)
    html = upscale_tailwinds(html)
    
    # Target right column empty spaces by making cards stretch vertically and horizontally.
    html = html.replace('card rounded-2xl p-8 w-full animate-fade-up', 'card rounded-[32px] p-8 w-full h-[580px] flex flex-col justify-center animate-fade-up')
    html = html.replace('card rounded-2xl p-5 flex-1 animate-fade-up', 'card rounded-[32px] p-8 flex flex-col justify-center flex-1 h-[580px] animate-fade-up')
    html = html.replace('card rounded-2xl p-5 mb-4 animate-fade-up', 'card rounded-[32px] p-8 mb-6 animate-fade-up w-full')
    html = html.replace('card rounded-[32px] p-8 flex flex-col justify-center flex-1', 'card rounded-[32px] p-10 flex flex-col justify-center flex-1')
    
    # More prominent left column alignments
    html = html.replace('w-1/2 pr-6 flex flex-col', 'w-1/2 pr-10 flex flex-col justify-center')
    html = html.replace('w-1/2 pl-4 flex flex-col', 'w-1/2 pl-8 flex flex-col justify-center')
    html = html.replace('w-1/2 pl-4 flex items-center', 'w-1/2 pl-8 flex items-center')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Creative Glassmorphism & Pastel Colors mapped successfully.")

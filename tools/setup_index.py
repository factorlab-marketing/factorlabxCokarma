import os

base_dir = r"c:\Users\Admin\Desktop\cokarma pitch deck"
src_index = os.path.join(base_dir, "sketch_brains_deck", "index.html")
dest_index = os.path.join(base_dir, "sketch_brains_x_company_deck", "index.html")
main_index = os.path.join(base_dir, "index.html")

with open(src_index, 'r', encoding='utf-8') as f:
    content = f.read()

# Modifications to dest_index
content = content.replace("<title>Sketch Brains - 2026 Tech Career Blueprint</title>", "<title>Sketch Brains x Company - Pre-Trained Hiring Pipeline</title>")
content = content.replace('<span class="deck-title">Sketch Brains</span>', '<span class="deck-title">Sketch Brains x Company</span>')
content = content.replace('<span class="deck-subtitle">2026 Tech Career Blueprint</span>', '<span class="deck-subtitle">Pre-Trained Hiring Pipeline</span>')
content = content.replace("const TOTAL_SLIDES = 29;", "const TOTAL_SLIDES = 9;")
content = content.replace("'Sketch_Brains_Career_Blueprint'", "'Sketch_Brains_x_Company_Pipeline'")

# Sidebar modifications
old_sidebar_active = '''<li>
                <a href="#" class="deck-link active">
                    <i class="fas fa-brain"></i>
                    Sketch Brains
                </a>
            </li>'''

new_sidebar_active = '''<li>
                <a href="../sketch_brains_deck/index.html" class="deck-link">
                    <i class="fas fa-brain"></i>
                    Sketch Brains
                </a>
            </li>
            <li>
                <a href="#" class="deck-link active">
                    <i class="fas fa-handshake"></i>
                    Sketch Brains x Company
                </a>
            </li>'''

content = content.replace(old_sidebar_active, new_sidebar_active)

with open(dest_index, 'w', encoding='utf-8') as f:
    f.write(content)

# Now modify main_index
with open(main_index, 'r', encoding='utf-8') as f:
    main_content = f.read()

new_card = '''
            <!-- Sketch Brains x Company Deck -->
            <a href="sketch_brains_x_company_deck/index.html"
                class="group block p-6 bg-slate-800/50 hover:bg-slate-800 border border-slate-700/50 hover:border-pink-500 rounded-2xl transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl hover:shadow-pink-900/20">
                <div
                    class="w-16 h-16 bg-pink-900/50 rounded-xl flex items-center justify-center mb-6 text-pink-400 group-hover:scale-110 transition-transform mx-auto">
                    <i class="fas fa-handshake text-3xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-2 font-montserrat">Sketch Brains x Company</h3>
                <p class="text-sm text-slate-400 group-hover:text-pink-200/70">Company Pitch: Pre-Trained Hiring Pipeline.</p>
            </a>
'''

# Insert before the closing </div> of the grid
if "<!-- Sketch Brains Deck -->" in main_content:
    main_content = main_content.replace("<!-- Sketch Brains Deck -->", new_card + "\n            <!-- Sketch Brains Deck -->")
    
with open(main_index, 'w', encoding='utf-8') as f:
    f.write(main_content)

print("Created new index and updated main index.")

document.addEventListener('DOMContentLoaded', async () => {
    const bookContainer = document.querySelector('.book-container');
    const pageNumIndicator = document.getElementById('page-indicator');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const printBtn = document.getElementById('print-btn');
    const loader = document.getElementById('loader');
    const viewport = document.querySelector('.book-viewport');

    const TOTAL_SLIDES = 24;
    let currentSlide = 0;

    // 1. Fetch and Assemble Pages
    try {
        for (let i = 1; i <= TOTAL_SLIDES; i++) {
            const pageDiv = document.createElement('div');
            pageDiv.className = 'page';
            pageDiv.setAttribute('data-page', i);

            const response = await fetch(`pages/page_${i}.html`);
            if (!response.ok) throw new Error(`Failed to load page_${i}.html`);
            
            const text = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');
            
            // Extract body content and inject
            const contentWrapper = document.createElement('div');
            contentWrapper.className = 'page-content';
            contentWrapper.innerHTML = doc.body.querySelector('.page-content').innerHTML;
            
            pageDiv.appendChild(contentWrapper);
            bookContainer.appendChild(pageDiv);
        }

        // Hide Loader
        loader.style.display = 'none';
        viewport.style.opacity = '1';

        // Bind interactions after pages load
        bindMicroInteractions();
        fitBookScale();
        updateBookLayout();

    } catch (err) {
        console.error(err);
        loader.innerHTML = `<span style="color: var(--accent-red);"><i class="fas fa-exclamation-triangle"></i> Failed to load presentation slides.<br><span style="font-size: 0.75rem; color: #aaa;">Browser CORS policy blocks fetching local files on direct file:// openings. Run compile.py to build a standalone single-file preview, or run a local server.</span></span>`;
        return;
    }

    // 2. Slide Layout Navigation Management
    const pages = bookContainer.getElementsByClassName('page');

    function updateBookLayout() {
        Array.from(pages).forEach((page, idx) => {
            page.classList.remove('active-spread');
            if (idx === currentSlide) {
                page.classList.add('active-spread');
            }
        });

        pageNumIndicator.textContent = `Slide ${currentSlide + 1} of ${TOTAL_SLIDES}`;
        
        prevBtn.disabled = currentSlide === 0;
        nextBtn.disabled = currentSlide === TOTAL_SLIDES - 1;
    }

    // Navigation triggers
    prevBtn.addEventListener('click', () => {
        if (currentSlide > 0) {
            currentSlide--;
            updateBookLayout();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentSlide < TOTAL_SLIDES - 1) {
            currentSlide++;
            updateBookLayout();
        }
    });

    printBtn.addEventListener('click', () => {
        window.open('print.html', '_blank');
    });

    // Keyboard controls
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft' && currentSlide > 0) {
            currentSlide--;
            updateBookLayout();
        } else if (e.key === 'ArrowRight' && currentSlide < TOTAL_SLIDES - 1) {
            currentSlide++;
            updateBookLayout();
        }
    });

    // 3. View Scaling Logic
    function fitBookScale() {
        const workspace = document.querySelector('.viewer-workspace');
        const viewWidth = workspace.clientWidth - 40;
        const viewHeight = workspace.clientHeight - 100;
        
        // Convert A4 Landscape size (297mm x 210mm) to pixels at 96dpi
        const pageW = 297 * 3.779528;
        const pageH = 210 * 3.779528;
        
        const scaleX = viewWidth / pageW;
        const scaleY = viewHeight / pageH;
        const finalScale = Math.min(scaleX, scaleY, 1);
        
        bookContainer.style.width = `${pageW}px`;
        bookContainer.style.height = `${pageH}px`;
        bookContainer.style.transform = `scale(${finalScale})`;
        
        // Scale wrapping divs for the children pages
        const allPages = bookContainer.querySelectorAll('.page');
        allPages.forEach(p => {
            p.style.width = `${pageW}px`;
            p.style.height = `${pageH}px`;
        });
        
        bookContainer.parentElement.style.height = `${pageH * finalScale}px`;
    }

    window.addEventListener('resize', () => {
        fitBookScale();
        updateBookLayout();
    });

    // 4. Slide Specific Micro-Interactions
    function bindMicroInteractions() {
        // Lock Card Toggle (Page 3)
        const lockCards = document.querySelectorAll('.lock-card');
        lockCards.forEach(card => {
            card.addEventListener('click', () => {
                lockCards.forEach(c => c.classList.remove('active-lock'));
                card.classList.add('active-lock');
            });
        });
    }
});

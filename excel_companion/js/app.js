document.addEventListener('DOMContentLoaded', () => {
    // Booklet Page Flipping Logic
    const pages = document.querySelectorAll('.page');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const pageNumIndicator = document.getElementById('page-indicator');
    const printBtn = document.getElementById('print-btn');
    const toggleViewBtn = document.getElementById('toggle-view-btn');
    const bookContainer = document.querySelector('.book-container');
    
    let currentSpread = 0; // Each spread has 2 pages (except cover which is single on left or right)
    
    // Layout sequence of 20 pages:
    // Spread 0: Page 1 (Cover) [Right Side]
    // Spread 1: Page 2 & Page 3
    // Spread 2: Page 4 & Page 5
    // Spread 3: Page 6 & Page 7
    // Spread 4: Page 8 & Page 9
    // Spread 5: Page 10 & Page 11
    // Spread 6: Page 12 & Page 13
    // Spread 7: Page 14 & Page 15
    // Spread 8: Page 16 & Page 17
    // Spread 9: Page 18 & Page 19
    // Spread 10: Page 20 (Roadmap / Back Cover) [Left Side]
    
    const spreads = [
        { left: null, right: 1 },  // Cover
        { left: 2, right: 3 },     // Anatomy & References
        { left: 4, right: 5 },     // Text & Logical
        { left: 6, right: 7 },     // Statistical & Lookups
        { left: 8, right: 9 },     // Date & Formatting
        { left: 10, right: 11 },   // Table & Cleaning
        { left: 12, right: 13 },   // Power Query & Pivot Layout
        { left: 14, right: 15 },   // Pivot Hacks & Charts
        { left: 16, right: 17 },   // Dashboards & Error Decoder
        { left: 18, right: 19 },   // Shortcuts & Best Practices
        { left: 20, right: null }  // Roadmap / Back Cover
    ];

    function updateBookLayout() {
        const isSinglePage = bookContainer.classList.contains('single-page-view') || window.innerWidth < 850;
        
        if (isSinglePage) {
            bookContainer.classList.add('single-page-view');
            // In single page mode, we show one page at a time.
            let activePageNum = 1;
            const currentSpreadObj = spreads[currentSpread];
            if (currentSpreadObj.right) activePageNum = currentSpreadObj.right;
            else if (currentSpreadObj.left) activePageNum = currentSpreadObj.left;
            
            pages.forEach(page => {
                const pageId = parseInt(page.getAttribute('data-page'));
                page.className = 'page';
                if (pageId === activePageNum) {
                    page.classList.add('active-spread');
                    page.style.left = '0';
                    page.style.transform = 'none';
                } else {
                    page.classList.add('hidden-spread');
                }
            });
            pageNumIndicator.textContent = `Page ${activePageNum} of 20`;
        } else {
            bookContainer.classList.remove('single-page-view');
            // Double spread mode
            pages.forEach(page => {
                const pageId = parseInt(page.getAttribute('data-page'));
                page.className = 'page';
                
                // Find which spread contains this page
                let pageSpreadIndex = -1;
                let isLeft = false;
                
                spreads.forEach((spread, idx) => {
                    if (spread.left === pageId) {
                        pageSpreadIndex = idx;
                        isLeft = true;
                    } else if (spread.right === pageId) {
                        pageSpreadIndex = idx;
                        isLeft = false;
                    }
                });
                
                if (pageSpreadIndex < currentSpread) {
                    // Page is in a previous spread (flipped to the left)
                    page.classList.add('flipped');
                    page.style.left = '0';
                    if (isLeft) {
                        page.style.transform = 'rotateY(-180deg)';
                        page.style.zIndex = 10 + (pageSpreadIndex);
                    } else {
                        page.style.transform = 'rotateY(-180deg)';
                        page.style.zIndex = 10 + (pageSpreadIndex);
                    }
                } else if (pageSpreadIndex === currentSpread) {
                    // Active spread
                    page.classList.add('active-spread');
                    if (isLeft) {
                        page.style.left = '0';
                        page.style.transform = 'rotateY(0deg)';
                        page.style.zIndex = 20;
                    } else {
                        page.style.left = '50%';
                        page.style.transform = 'rotateY(0deg)';
                        page.style.zIndex = 20;
                    }
                } else {
                    // Future spread
                    page.style.left = '50%';
                    page.style.transform = 'rotateY(0deg)';
                    page.style.zIndex = 5 - pageSpreadIndex;
                }
            });
            
            const currentSpreadObj = spreads[currentSpread];
            const pLeft = currentSpreadObj.left ? `P. ${currentSpreadObj.left}` : '';
            const pRight = currentSpreadObj.right ? `P. ${currentSpreadObj.right}` : '';
            pageNumIndicator.textContent = pLeft && pRight ? `${pLeft} – ${pRight}` : (pLeft || pRight);
        }
        
        // Disable buttons if at limits
        prevBtn.disabled = currentSpread === 0;
        nextBtn.disabled = currentSpread === spreads.length - 1;
    }

    prevBtn.addEventListener('click', () => {
        if (currentSpread > 0) {
            currentSpread--;
            updateBookLayout();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentSpread < spreads.length - 1) {
            currentSpread++;
            updateBookLayout();
        }
    });

    toggleViewBtn.addEventListener('click', () => {
        bookContainer.classList.toggle('single-page-view');
        updateBookLayout();
        toggleViewBtn.innerHTML = bookContainer.classList.contains('single-page-view') 
            ? '<i class="fas fa-book-open"></i> Spread View' 
            : '<i class="fas fa-file"></i> Page View';
    });

    printBtn.addEventListener('click', () => {
        window.print();
    });

    window.addEventListener('resize', updateBookLayout);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft' && currentSpread > 0) {
            currentSpread--;
            updateBookLayout();
        } else if (e.key === 'ArrowRight' && currentSpread < spreads.length - 1) {
            currentSpread++;
            updateBookLayout();
        }
    });

    // Dynamic scale to fit viewport if A5 size is larger than workspace
    function fitBookScale() {
        const workspace = document.querySelector('.viewer-workspace');
        const viewWidth = workspace.clientWidth - 40;
        const viewHeight = workspace.clientHeight - 100;
        
        const isSinglePage = bookContainer.classList.contains('single-page-view') || window.innerWidth < 850;
        const pageW = 148 * 3.779528; // mm to px approx 560px
        const pageH = 210 * 3.779528; // mm to px approx 794px
        
        const bookW = isSinglePage ? pageW : pageW * 2;
        const bookH = pageH;
        
        const scaleX = viewWidth / bookW;
        const scaleY = viewHeight / bookH;
        const finalScale = Math.min(scaleX, scaleY, 1); // don't upscale beyond 1
        
        document.documentElement.style.setProperty('--scale-factor', finalScale);
        bookContainer.style.transform = `scale(${finalScale})`;
        
        // adjust container height to match scaled book
        bookContainer.parentElement.style.height = `${bookH * finalScale}px`;
    }
    
    // Fit scale initially and on resize
    setTimeout(() => {
        fitBookScale();
        updateBookLayout();
    }, 100);
    window.addEventListener('resize', fitBookScale);


    // Interactive Search for Shortcuts Cheat Sheet (Page 18)
    const searchInput = document.getElementById('shortcut-search');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const items = document.querySelectorAll('.shortcut-item');
            
            items.forEach(item => {
                const action = item.querySelector('.shortcut-action').textContent.toLowerCase();
                const keys = item.querySelector('.shortcut-keys').textContent.toLowerCase();
                
                if (action.includes(query) || keys.includes(query)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }

    // Modal Overlays for Interactive Maps (Excel interface annotations)
    const overlay = document.getElementById('interactive-overlay');
    const overlayTitle = document.getElementById('overlay-title');
    const overlayBody = document.getElementById('overlay-body');
    const closeOverlay = document.getElementById('close-overlay');

    if (closeOverlay) {
        closeOverlay.addEventListener('click', () => {
            overlay.classList.remove('active');
        });
    }

    // Event Delegation for interface interaction
    document.addEventListener('click', (e) => {
        const marker = e.target.closest('.interactive-marker');
        if (marker) {
            const title = marker.getAttribute('data-title');
            const desc = marker.getAttribute('data-desc');
            
            overlayTitle.textContent = title;
            overlayBody.textContent = desc;
            overlay.classList.add('active');
        }
    });

    // Close overlay if clicking outside overlay card
    if (overlay) {
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.classList.remove('active');
            }
        });
    }

    // Cell Lock Toggle Micro-Interaction (Page 3)
    const lockCells = document.querySelectorAll('.lock-card');
    lockCells.forEach(cell => {
        cell.addEventListener('click', () => {
            // Toggle active state
            lockCells.forEach(c => c.classList.remove('active-lock'));
            cell.classList.add('active-lock');
            
            // Toggle icon visual
            const icon = cell.querySelector('i');
            if (icon) {
                if (icon.classList.contains('fa-lock-open')) {
                    icon.className = 'fas fa-lock';
                    icon.style.color = 'var(--accent-red)';
                } else if (icon.classList.contains('fa-lock')) {
                    icon.className = 'fas fa-lock-open';
                    icon.style.color = '#888';
                }
            }
        });
    });

    // Keycap click search simulator (Page 19)
    const keycaps = document.querySelectorAll('.keycap');
    keycaps.forEach(key => {
        key.addEventListener('click', () => {
            const keyText = key.textContent.trim();
            if (searchInput) {
                searchInput.value = keyText;
                // Dispatch input event to trigger filtering
                const event = new Event('input', { bubbles: true });
                searchInput.dispatchEvent(event);
            }
        });
    });
});

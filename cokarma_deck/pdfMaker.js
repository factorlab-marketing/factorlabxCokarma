/**
 * pdfMaker.js
 * Dedicated script to fetch, aggregate, and render slides into a PDF.
 */

const TOTAL_SLIDES = 14;
const IS_DARK_MODE = false;

async function waitForChartGlobal() {
    let attempts = 0;
    while (typeof window.Chart === 'undefined' && attempts < 50) {
        await new Promise(r => setTimeout(r, 100));
        attempts++;
    }
    if (typeof window.Chart === 'undefined') {
        console.error("Chart.js failed to load.");
        return false;
    }
    return true;
}

async function initPDFSystem() {
    const container = document.getElementById('print-container');
    const statusText = document.getElementById('status-text');
    const statusOverlay = document.getElementById('status-overlay');

    try {
        statusText.innerText = "Initializing...";

        // Wait for Chart.js
        const chartReady = await waitForChartGlobal();
        if (!chartReady) {
            statusText.innerText = "Warning: Chart.js missing. Charts may not render.";
        }

        statusText.innerText = "Fetching " + TOTAL_SLIDES + " slides...";

        // 1. Fetch & Assemble
        for (let i = 1; i <= TOTAL_SLIDES; i++) {
            statusText.innerText = `Preparing Slide ${i}/${TOTAL_SLIDES}...`;
            await new Promise(r => requestAnimationFrame(r));

            const response = await fetch(`slides/slide_${i}.html`);
            let text = await response.text();

            // FIX: Relative Paths
            text = text.replace(/src="\.\.\//g, 'src="./');
            text = text.replace(/href="\.\.\//g, 'href="./');
            text = text.replace(/url\(['"]?\.\.\//g, 'url(\'./');

            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');

            // REMOVE STATIC INCOMPATIBLE ELEMENTS (User Request)
            doc.querySelectorAll('iframe, video, object, embed').forEach(el => el.remove());
            // Remove specific interactive-only containers if problematic
            doc.querySelectorAll('.interactive-only').forEach(el => el.remove());

            // Create Wrapper
            const page = document.createElement('div');
            page.className = 'slide-page';

            // Inject Styles
            doc.querySelectorAll('style').forEach(s => page.appendChild(s.cloneNode(true)));

            // Inject Content
            const content = document.createElement('div');
            content.innerHTML = doc.body.innerHTML;

            // Image Error Handling (Prevent Broken Icons in PDF)
            content.querySelectorAll('img').forEach(img => {
                img.onerror = function () {
                    this.style.display = 'none'; // Hide if broken (CORS/404)
                    console.warn('Image failed:', this.src);
                };
            });

            page.appendChild(content);
            container.appendChild(page);

            // Execute scripts (Scoped)
            // We strip out scripts that are NOT about charts to avoid side effects
            if (chartReady) {
                doc.querySelectorAll('script').forEach(s => {
                    const content = s.textContent;
                    if (content.includes('new Chart') || content.includes('getContext')) {
                        const newScript = document.createElement('script');
                        newScript.textContent = `(() => { 
                            try { 
                                ${content} 
                            } catch(e) { console.warn('Script error slide ${i}', e); }
                        })();`;
                        page.appendChild(newScript);
                    }
                });
            }
        }

        // 2. Wait for Assets
        statusText.innerText = "Finalizing Layout...";
        await document.fonts.ready;
        // Wait for charts to animate
        await new Promise(r => setTimeout(r, 2500));

        // 3. Generate PDF
        statusText.innerText = "Generating PDF File... (This may take a moment)";

        const opt = {
            margin: 0,
            filename: 'FactorLab_CoKarma_PitchDeck.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: {
                scale: 1.5,
                useCORS: true,
                scrollY: 0,
                windowWidth: 1280
            },
            jsPDF: {
                unit: 'px',
                format: [1280, 720],
                orientation: 'landscape',
                hotfixes: ['px_scaling']
            }
        };

        await html2pdf().set(opt).from(container).save();

        statusText.innerText = "Download Complete!";
        setTimeout(() => {
            statusOverlay.style.display = 'none';
        }, 1000);

    } catch (err) {
        console.error(err);
        statusText.innerText = "Error: " + err.message;
        alert("PDF Generation Failed: " + err.message);
    }
}

window.addEventListener('load', initPDFSystem);

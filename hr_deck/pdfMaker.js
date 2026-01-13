/**
 * pdfMaker.js - HR Deck Version
 */

const TOTAL_SLIDES = 4; // HR Deck has 4 slides
const IS_DARK_MODE = false;

async function waitForChartGlobal() {
    let attempts = 0;
    while (typeof window.Chart === 'undefined' && attempts < 50) {
        await new Promise(r => setTimeout(r, 100));
        attempts++;
    }
    return typeof window.Chart !== 'undefined';
}

async function initPDFSystem() {
    const container = document.getElementById('print-container');
    const statusText = document.getElementById('status-text');
    const statusOverlay = document.getElementById('status-overlay');

    try {
        statusText.innerText = "Initializing...";

        const chartReady = await waitForChartGlobal();
        if (!chartReady) console.warn("Chart.js missing");

        statusText.innerText = "Fetching " + TOTAL_SLIDES + " slides...";

        for (let i = 1; i <= TOTAL_SLIDES; i++) {
            statusText.innerText = `Preparing Slide ${i}/${TOTAL_SLIDES}...`;
            await new Promise(r => requestAnimationFrame(r));

            const response = await fetch(`slides/slide_${i}.html`);
            let text = await response.text();

            // Fix paths
            text = text.replace(/src="\.\.\//g, 'src="./');
            text = text.replace(/href="\.\.\//g, 'href="./');

            const parser = new DOMParser();
            const doc = parser.parseFromString(text, 'text/html');

            // Cleanup
            doc.querySelectorAll('iframe, video, object, embed').forEach(el => el.remove());

            // Create Wrapper
            const page = document.createElement('div');
            page.className = 'slide-page';

            // Styles
            doc.querySelectorAll('style').forEach(s => page.appendChild(s.cloneNode(true)));

            // Content
            const content = document.createElement('div');
            content.innerHTML = doc.body.innerHTML;

            // Image Error Handling
            content.querySelectorAll('img').forEach(img => {
                img.onerror = function () { this.style.display = 'none'; };
            });

            page.appendChild(content);
            container.appendChild(page);
        }

        statusText.innerText = "Finalizing Layout...";
        await document.fonts.ready;
        await new Promise(r => setTimeout(r, 1000));

        statusText.innerText = "Generating PDF File...";

        const opt = {
            margin: 0,
            filename: 'FactorLab_HR_Session_Deck.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 1.5, useCORS: true, scrollY: 0, windowWidth: 1280 },
            jsPDF: { unit: 'px', format: [1280, 720], orientation: 'landscape', hotfixes: ['px_scaling'] }
        };

        await html2pdf().set(opt).from(container).save();

        statusText.innerText = "Download Complete!";
        setTimeout(() => { statusOverlay.style.display = 'none'; }, 1000);

    } catch (err) {
        console.error(err);
        statusText.innerText = "Error: " + err.message;
        alert("PDF Generation Failed: " + err.message);
    }
}

window.addEventListener('load', initPDFSystem);

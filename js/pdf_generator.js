/**
 * Global PDF Generator for Pitch Decks
 * Captures slides one by one using an iframe to ensure layouts and charts are rendered correctly.
 */

window.PDFTools = {
    /**
     * Generates a PDF from a sequence of HTML slides.
     * @param {number} totalSlides - Number of slides (assumes names slide_1.html to slide_N.html)
     * @param {string} filename - Output filename (e.g., 'Presentation')
     * @param {string} slidesDir - Directory specific prefix (default 'slides/')
     */
    /**
     * @param {number} totalSlides - Number of slides
     * @param {string} filename - Output filename
     * @param {string} slidesDir - Directory specific prefix
     * @param {HTMLElement} existingIframe - Optional: Use an existing iframe (avoids file:// creation bugs)
     */
    /**
     * Generates a PDF from a sequence of HTML slides using postMessage protocol.
     * Works on file:// protocol by bypassing direct DOM access.
     */
    generate: async function (totalSlides, filename = 'Presentation', slidesDir = 'slides/', existingIframe = null) {
        // 1. Create UI Overlay
        const overlay = document.createElement('div');
        overlay.id = 'pdf-gen-overlay';
        overlay.style.cssText = `
            position: fixed; inset: 0; background: rgba(15, 23, 42, 0.98); z-index: 10000;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            color: white; font-family: 'Inter', sans-serif;
        `;
        overlay.innerHTML = `
            <div class="text-4xl text-emerald-500 mb-6"><i class="fas fa-circle-notch fa-spin"></i></div>
            <h2 class="text-2xl font-bold mb-2">Generating PDF</h2>
            <p id="pdf-status" class="text-slate-400 font-mono">Initializing...</p>
            <div class="w-64 h-2 bg-slate-800 rounded-full mt-6 overflow-hidden">
                <div id="pdf-progress-bar" class="h-full bg-emerald-500 transition-all duration-300" style="width: 0%"></div>
            </div>
        `;
        document.body.appendChild(overlay);

        const statusFn = (msg, percent) => {
            document.getElementById('pdf-status').textContent = msg;
            document.getElementById('pdf-progress-bar').style.width = `${percent}%`;
        };

        let iframe = existingIframe;
        let createdIframe = false;

        // Message Handler (Closure to keep context)
        const captureResolvers = {}; // map index -> promise resolve/reject
        const messageHandler = (event) => {
            if (event.data.type === 'CAPTURE_RESULT') {
                const { slideIndex, imgData, success, error } = event.data;
                if (captureResolvers[slideIndex]) {
                    if (success) captureResolvers[slideIndex].resolve(imgData);
                    else captureResolvers[slideIndex].reject(error);

                    delete captureResolvers[slideIndex];
                }
            }
        };
        window.addEventListener('message', messageHandler);

        try {
            if (!window.jspdf) throw new Error("jsPDF library not loaded.");
            const { jsPDF } = window.jspdf;

            const WIDTH = 1280;
            const HEIGHT = 720;
            const doc = new jsPDF({ orientation: 'landscape', unit: 'px', format: [WIDTH, HEIGHT], compress: true });

            if (!iframe) {
                createdIframe = true;
                iframe = document.createElement('iframe');
                iframe.style.cssText = `position: absolute; left: -9999px; top: 0; width: ${WIDTH}px; height: ${HEIGHT}px; border: 0;`;
                document.body.appendChild(iframe);
            }

            for (let i = 1; i <= totalSlides; i++) {
                const percent = Math.round(((i - 1) / totalSlides) * 100);
                statusFn(`Capturing Slide ${i} of ${totalSlides}...`, percent);

                // 1. Load Slide
                await new Promise((resolve, reject) => {
                    const loadHandler = () => {
                        iframe.removeEventListener('load', loadHandler);
                        resolve();
                    };
                    iframe.addEventListener('load', loadHandler);
                    iframe.src = `${slidesDir}slide_${i}.html`;
                });

                // 2. Wait for Render (5 seconds for charts and animations)
                await new Promise(r => setTimeout(r, 5000));


                // 3. Request Capture via Messaging
                const imgData = await new Promise((resolve, reject) => {
                    captureResolvers[i] = { resolve, reject };
                    // Post message to the iframe
                    iframe.contentWindow.postMessage({ type: 'CAPTURE_SLIDE', slideIndex: i }, '*');

                    // Timeout (Safety)
                    setTimeout(() => {
                        if (captureResolvers[i]) {
                            captureResolvers[i].reject('Capture timeout - Slide script missing?');
                            delete captureResolvers[i];
                        }
                    }, 5000);
                });

                if (i > 1) doc.addPage([WIDTH, HEIGHT]);
                doc.addImage(imgData, 'JPEG', 0, 0, WIDTH, HEIGHT);
            }

            statusFn('Finalizing PDF...', 100);
            await new Promise(r => setTimeout(r, 500));
            doc.save(`${filename}.pdf`);

        } catch (err) {
            console.error(err);
            document.getElementById('pdf-status').innerHTML = `<span class="text-red-500 text-sm">Error: ${err.message}<br>Verify JS injected in slides.</span>`;
            document.getElementById('pdf-progress-bar').className = 'h-full bg-red-500 transition-all duration-300';
            return;
        } finally {
            window.removeEventListener('message', messageHandler);
            if (createdIframe && iframe) document.body.removeChild(iframe);
            if (!document.getElementById('pdf-status').innerHTML.includes('Error')) {
                document.body.removeChild(overlay);
            }
        }
    }
};

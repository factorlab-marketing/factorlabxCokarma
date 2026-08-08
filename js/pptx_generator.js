/**
 * PPTX Generator for FactorLab Pitch Decks
 * Uses PptxGenJS + html2canvas (via capture_helper.js)
 */

class PPTXGenerator {
    constructor(totalSlides, slidePathPattern) {
        this.totalSlides = totalSlides;
        this.slidePathPattern = slidePathPattern; // e.g., 'slides/slide_{i}.html'
        this.capturedImages = new Array(totalSlides);
        this.isGenerating = false;
    }

    async loadDependencies() {
        if (!window.PptxGenJS) {
            // Use bundled version which includes JSZip
            await this.loadScript('https://cdn.jsdelivr.net/gh/gitbrent/pptxgenjs@3.12.0/dist/pptxgen.bundle.js');
        }
    }

    loadScript(src) {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    async generate(buttonElement) {
        if (this.isGenerating) return;
        this.isGenerating = true;

        const originalText = buttonElement.innerHTML;
        buttonElement.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
        buttonElement.disabled = true;

        try {
            await this.loadDependencies();

            // Create a hidden capture frame
            const frame = document.createElement('iframe');
            frame.style.position = 'absolute';
            frame.style.top = '-10000px';
            frame.style.width = '1280px';
            frame.style.height = '720px';
            frame.style.border = 'none';
            document.body.appendChild(frame);

            // Iterate and Capture
            for (let i = 1; i <= this.totalSlides; i++) {
                buttonElement.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Slide ${i}/${this.totalSlides}`;

                // Load Slide
                await new Promise((resolve, reject) => {
                    frame.onload = resolve;
                    frame.onerror = reject;
                    frame.src = this.slidePathPattern.replace('{i}', i);
                });

                // Wait for scripts (capture_helper) to initialize
                await new Promise(r => setTimeout(r, 1000));

                // Request Capture
                const imgData = await this.captureSlide(frame.contentWindow, i);
                this.capturedImages[i - 1] = imgData;
            }

            // Cleanup frame
            document.body.removeChild(frame);

            // Generate PPTX
            buttonElement.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
            this.createPPTX();

            buttonElement.innerHTML = '<i class="fas fa-check"></i> Done!';
            setTimeout(() => {
                buttonElement.innerHTML = originalText;
                buttonElement.disabled = false;
                this.isGenerating = false;
            }, 2000);

        } catch (err) {
            console.error(err);
            buttonElement.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error';

            if (err.toString().includes('SecurityError') || err.toString().includes('Tainted')) {
                alert("Security Error: Browser blocked image capture.\n\nSince you are running this file directly (file://), external scripts like FontAwesome can 'taint' the canvas.\n\nFix: Please run this presentation on a local server (http://localhost) or use VS Code 'Live Server' extension.");
            } else {
                alert("Unexpected Error during generation: " + err);
            }

            this.isGenerating = false;
        }
    }

    captureSlide(windowObj, index) {
        return new Promise((resolve, reject) => {
            const handleMessage = (event) => {
                if (event.data.type === 'CAPTURE_RESULT' && event.data.slideIndex === index) {
                    window.removeEventListener('message', handleMessage);
                    if (event.data.success) {
                        resolve(event.data.imgData);
                    } else {
                        reject(event.data.error);
                    }
                }
            };
            window.addEventListener('message', handleMessage);

            // Trigger capture_helper.js inside the iframe
            windowObj.postMessage({ type: 'CAPTURE_SLIDE', slideIndex: index }, '*');
        });
    }

    createPPTX() {
        const pres = new PptxGenJS();
        pres.layout = 'LAYOUT_16x9';

        this.capturedImages.forEach(imgData => {
            const slide = pres.addSlide();
            slide.addImage({ data: imgData, x: 0, y: 0, w: '100%', h: '100%' });
        });

        pres.writeFile({ fileName: 'FactorLab_Smallcase_Pitch.pptx' });
    }
}

window.addEventListener('message', async (event) => {
    if (event.data.type === 'CAPTURE_SLIDE') {
        try {
            // Ensure html2canvas is available
            if (!window.html2canvas) {
                await loadScript('https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js');
            }

            // Capture
            // Images are now embedded as Base64 by build tool, so Taint is not an issue.
            const canvas = await html2canvas(document.body, {
                width: 1280,
                height: 720,
                scale: 1.5,
                useCORS: true,
                windowWidth: 1280,
                windowHeight: 720,
                logging: false,
                backgroundColor: null,
                allowTaint: false // MUST be false to allow toDataURL export
            });

            const imgData = canvas.toDataURL('image/jpeg', 0.90);

            event.source.postMessage({
                type: 'CAPTURE_RESULT',
                slideIndex: event.data.slideIndex,
                imgData: imgData,
                success: true
            }, '*');

        } catch (err) {
            console.error('Capture failed:', err);
            event.source.postMessage({
                type: 'CAPTURE_RESULT',
                slideIndex: event.data.slideIndex,
                error: err.toString(),
                success: false
            }, '*');
        }
    } else if (event.data.type === 'theme-update') {
        let styleEl = document.getElementById('dynamic-theme-override');
        if (!styleEl) {
            styleEl = document.createElement('style');
            styleEl.id = 'dynamic-theme-override';
            document.head.appendChild(styleEl);
        }
        styleEl.textContent = event.data.css || '';
    }
});

function loadScript(src) {
    return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = src;
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
    });
}

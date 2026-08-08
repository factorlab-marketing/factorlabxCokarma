
(function () {
    // Check initial parent theme state
    function checkTheme() {
        if (window.parent) {
            window.parent.postMessage({ type: 'theme-request' }, '*');
        }
    }

    // Default to dark mode unless told otherwise
    document.body.classList.remove('light-mode');

    window.addEventListener('message', function (event) {
        if (event.data.type === 'theme-update') {
            if (event.data.isDark === false) {
                document.body.classList.add('light-mode');
            } else {
                document.body.classList.remove('light-mode');
            }
        }
    });

    // Request on load
    checkTheme();
})();

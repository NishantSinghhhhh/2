(function () {
    const STORAGE_KEY = 'precice-theme';
    const htmlEl = document.documentElement;
    const DARK = 'dark';
    const LIGHT = 'light';

    function applyTheme(theme) {
        htmlEl.setAttribute('data-bs-theme', theme);
    }

    function getInitialTheme() {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) return saved;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? DARK : LIGHT;
    }

    function updateIcons(theme) {
        // Update all theme icons on page
        const icons = document.querySelectorAll('#theme-icon, #theme-icon-desktop, #theme-icon-mobile');
        icons.forEach(function(icon) {
            if (theme === DARK) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        });
    }

    const initialTheme = getInitialTheme();
    applyTheme(initialTheme);

    document.addEventListener('DOMContentLoaded', function () {
        updateIcons(initialTheme);

        // Wire up ALL toggle buttons
        const btns = document.querySelectorAll('#theme-toggle, #theme-toggle-desktop, #theme-toggle-mobile');
        btns.forEach(function(btn) {
            btn.addEventListener('click', function () {
                const current = htmlEl.getAttribute('data-bs-theme') || LIGHT;
                const next = current === DARK ? LIGHT : DARK;
                applyTheme(next);
                updateIcons(next);
                localStorage.setItem(STORAGE_KEY, next);
            });
        });
    });
})();
const themeToggle = document.getElementById('theme-toggle');
const navbarWrapper = document.getElementById('navbarWrapper');
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobileMenu');
const cursorGlow = document.getElementById('cursorGlow');


if (themeToggle) {
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggle.textContent = savedTheme === 'light' ? '🌙' : '☀️';
    }

    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');

        if (currentTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            themeToggle.textContent = '🌙';
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeToggle.textContent = '☀️';
        }
    });
}


window.addEventListener('scroll', () => {
    if (!navbarWrapper) return;

    if (window.scrollY > 20) {
        navbarWrapper.classList.add('scrolled');
    } else {
        navbarWrapper.classList.remove('scrolled');
    }
});

/* Mobile menu toggle */
if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
    });
}

/* Cursor glow */
window.addEventListener('mousemove', (event) => {
    if (!cursorGlow) return;

    cursorGlow.style.left = `${event.clientX}px`;
    cursorGlow.style.top = `${event.clientY}px`;
});

/* Scroll reveal */
const revealElements = document.querySelectorAll('.reveal-up, .reveal-right, .reveal-left');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('reveal-visible');
        }
    });
}, {
    threshold: 0.12
});

revealElements.forEach((element) => {
    revealObserver.observe(element);
});

/* Tilt effect */
const tiltCards = document.querySelectorAll('.tilt-card');

tiltCards.forEach((card) => {
    card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * 4;
        const rotateY = ((x - centerX) / centerX) * -4;

        card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg)';
    });
});
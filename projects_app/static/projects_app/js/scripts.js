document.addEventListener('DOMContentLoaded', function() {
    // Function to adjust content padding based on navbar height
    function adjustContentPadding() {
        const navbar = document.querySelector('nav');
        const mainContent = document.getElementById('main-content');
        if (navbar && mainContent) {
            const navbarHeight = navbar.offsetHeight;
            // Add extra space (24px or p-6) below the navbar
            const extraSpace = 24; 
            mainContent.style.paddingTop = `${navbarHeight + extraSpace}px`;
        }
    }

    // Initial adjustment on page load
    adjustContentPadding();
    // Adjust on window resize to handle responsive changes
    window.addEventListener('resize', adjustContentPadding);

    // **Light/Dark Mode Toggle**
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    const savedTheme = localStorage.getItem('color-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.documentElement.classList.add('dark');
        themeToggleLightIcon.classList.remove('hidden');
        themeToggleDarkIcon.classList.add('hidden');
    } else {
        document.documentElement.classList.remove('dark');
        themeToggleDarkIcon.classList.remove('hidden');
        themeToggleLightIcon.classList.add('hidden');
    }

    themeToggleBtn.addEventListener('click', function() {
        document.documentElement.classList.toggle('dark');
        const isDark = document.documentElement.classList.contains('dark');
        localStorage.setItem('color-theme', isDark ? 'dark' : 'light');

        themeToggleDarkIcon.classList.toggle('hidden', isDark);
        themeToggleLightIcon.classList.toggle('hidden', !isDark);
    });

    // **Project Category Filtering and Dropdown Behavior**
    const dropdownToggle = document.getElementById('dropdown-toggle');
    const dropdownContent = document.getElementById('dropdown-content');
    const currentCategorySpan = document.getElementById('current-category');
    const projectCards = document.querySelectorAll('.scroll-reveal');
    const categoryLinks = document.querySelectorAll('.dropdown-link');

    const filterProjects = (category) => {
        let categoryName = "All Projects"; 
        
        projectCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            if (category === 'all' || cardCategory === category) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });

        const selectedLink = document.querySelector(`.dropdown-link[data-category="${category}"]`);
        if (selectedLink) {
            categoryName = selectedLink.textContent;
        }
        currentCategorySpan.textContent = categoryName;

        categoryLinks.forEach(link => {
            link.classList.remove('bg-blue-100', 'text-blue-800', 'dark:bg-blue-700', 'dark:text-white');
            if (link.getAttribute('data-category') === category) {
                link.classList.add('bg-blue-100', 'text-blue-800', 'dark:bg-blue-700', 'dark:text-white');
            }
        });
    };

    categoryLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const category = this.getAttribute('data-category');
            filterProjects(category);
            dropdownContent.classList.remove('visible');
            dropdownContent.classList.add('hidden');
        });
    });

    dropdownToggle.addEventListener('click', () => {
        const isVisible = dropdownContent.classList.contains('visible');
        if (isVisible) {
            dropdownContent.classList.remove('visible');
            dropdownContent.classList.add('hidden');
        } else {
            dropdownContent.classList.remove('hidden');
            dropdownContent.classList.add('visible');
        }
    });

    document.addEventListener('click', (event) => {
        const dropdownContainer = document.getElementById('dropdown-container');
        if (!dropdownContainer.contains(event.target)) {
            dropdownContent.classList.remove('visible');
            dropdownContent.classList.add('hidden');
        }
    });
    
    filterProjects('all');

    // **Scroll Animation Logic**
    const scrollElements = document.querySelectorAll(".scroll-reveal");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, {
        threshold: 0.2
    });

    scrollElements.forEach(el => observer.observe(el));
});
/**
 * Portfolio Main JavaScript
 * Powers typewriter effect, scroll animations, filtering, modals, and AJAX form handling.
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initTypewriter();
    initStatsCounter();
    initSkillsObserver();
    initTimelineTabs();
    initProjectFilters();
    initProjectModal();
    initContactForm();
    initBackToTop();
    initCurrentYear();
});

/* ===================================================================
   1. NAVBAR & MOBILE MENU & SCROLL SPY
   =================================================================== */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    const mobileToggle = document.getElementById('mobile-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    const hireMeBtn = document.getElementById('hire-me-nav-btn');

    // Direct Smooth Scroll to Contact Details on "Hire Me" Click
    if (hireMeBtn) {
        hireMeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                setTimeout(() => {
                    const nameInput = document.getElementById('contact-name');
                    if (nameInput) {
                        nameInput.focus();
                    }
                }, 500);
            }
        });
    }

    // Mobile Hamburger Toggle
    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navMenu.classList.toggle('open');
        });

        // Close menu when a link is clicked
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                navMenu.classList.remove('open');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target) && navMenu.classList.contains('open')) {
                mobileToggle.classList.remove('active');
                navMenu.classList.remove('open');
            }
        });
    }

    // Scroll Spy & Navbar blur shadow
    window.addEventListener('scroll', () => {
        const scrollY = window.pageYOffset;

        if (navbar) {
            if (scrollY > 50) {
                navbar.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.2)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        }

        // Active Section Link Highlighting
        let currentSectionId = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionHeight = section.offsetHeight;
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });
}

/* ===================================================================
   3. TYPEWRITER EFFECT
   =================================================================== */
function initTypewriter() {
    const typewriterElem = document.getElementById('typewriter');
    if (!typewriterElem) return;

    const rolesAttr = typewriterElem.getAttribute('data-roles') || 'Full Stack Developer, Django Specialist, Software Engineer';
    const roles = rolesAttr.split(',').map(r => r.trim()).filter(Boolean);

    if (!roles.length) return;

    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typingSpeed = 100;
    const deletingSpeed = 50;
    const pauseDelay = 1800;

    function type() {
        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typewriterElem.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typewriterElem.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
        }

        let currentDelay = isDeleting ? deletingSpeed : typingSpeed;

        if (!isDeleting && charIndex === currentRole.length) {
            currentDelay = pauseDelay;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            currentDelay = 400;
        }

        setTimeout(type, currentDelay);
    }

    type();
}

/* ===================================================================
   4. STATS COUNTER ANIMATION
   =================================================================== */
function initStatsCounter() {
    const statNumbers = document.querySelectorAll('.stat-number');
    if (!statNumbers.length) return;

    let hasCounted = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasCounted) {
                hasCounted = true;
                statNumbers.forEach(counter => {
                    if (!counter.hasAttribute('data-target')) return;
                    const target = parseInt(counter.getAttribute('data-target'), 10) || 0;
                    const suffix = counter.textContent.replace(/[0-9]/g, '');
                    let current = 0;
                    const increment = Math.max(1, Math.ceil(target / 40));
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            counter.textContent = `${target}${suffix}`;
                            clearInterval(timer);
                        } else {
                            counter.textContent = `${current}${suffix}`;
                        }
                    }, 35);
                });
            }
        });
    }, { threshold: 0.3 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        observer.observe(statsSection);
    }
}

/* ===================================================================
   5. SKILLS PROGRESS BAR ANIMATION
   =================================================================== */
function initSkillsObserver() {
    const progressBars = document.querySelectorAll('.progress-bar-fill');
    if (!progressBars.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const width = bar.getAttribute('data-progress') || '85%';
                bar.style.width = width;
                observer.unobserve(bar);
            }
        });
    }, { threshold: 0.2 });

    progressBars.forEach(bar => observer.observe(bar));
}

/* ===================================================================
   6. EXPERIENCE & EDUCATION TABS
   =================================================================== */
function initTimelineTabs() {
    const tabs = document.querySelectorAll('.timeline-tab');
    const contents = document.querySelectorAll('.timeline-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetTab = tab.getAttribute('data-tab');

            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            const targetContent = document.getElementById(`tab-${targetTab}`);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

/* ===================================================================
   7. PROJECT CATEGORY FILTERS
   =================================================================== */
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const filterValue = button.getAttribute('data-filter');

            projectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');

                if (filterValue === 'all' || cardCategory === filterValue) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });
        });
    });
}

/* ===================================================================
   8. PROJECT QUICK VIEW MODAL
   =================================================================== */
function initProjectModal() {
    const modal = document.getElementById('project-modal');
    const modalContent = document.getElementById('modal-content');
    const modalClose = document.getElementById('modal-close');
    const detailButtons = document.querySelectorAll('.view-details-btn');

    if (!modal || !modalContent) return;

    function openModal() {
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        modal.classList.remove('open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    detailButtons.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const slug = btn.getAttribute('data-slug');
            if (!slug) return;

            openModal();

            // Display loading skeleton
            modalContent.innerHTML = `
                <div class="modal-skeleton">
                    <div class="skeleton-img"></div>
                    <div class="skeleton-text"></div>
                    <div class="skeleton-text short"></div>
                </div>
            `;

            try {
                const response = await fetch(`/api/projects/${slug}/`);
                if (!response.ok) throw new Error('Project details not found');
                const project = await response.json();

                const featuresHtml = project.features && project.features.length
                    ? `<div class="modal-features-list">
                        <h4 style="font-size: 0.95rem; margin-bottom: 0.5rem; color: var(--text-primary);">Key Highlights:</h4>
                        ${project.features.map(f => `<div class="modal-feature-item"><i class="fa-solid fa-circle-check"></i> <span>${escapeHtml(f)}</span></div>`).join('')}
                      </div>`
                    : '';

                const techTagsHtml = project.technologies && project.technologies.length
                    ? `<div class="modal-tech-stack">
                        ${project.technologies.map(t => `<span class="tech-pill">${escapeHtml(t)}</span>`).join('')}
                      </div>`
                    : '';

                const actionButtonsHtml = `
                    <div class="modal-actions">
                        ${project.live_demo_url ? `<a href="${project.live_demo_url}" target="_blank" rel="noopener" class="btn btn-primary btn-sm"><i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo</a>` : ''}
                        ${project.github_url ? `<a href="${project.github_url}" target="_blank" rel="noopener" class="btn btn-secondary btn-sm"><i class="fa-brands fa-github"></i> View GitHub Code</a>` : ''}
                    </div>
                `;

                modalContent.innerHTML = `
                    ${project.image_url ? `<img src="${project.image_url}" alt="${escapeHtml(project.title)}" class="modal-image">` : ''}
                    <span class="modal-category">${escapeHtml(project.category)}</span>
                    <h3 class="modal-title">${escapeHtml(project.title)}</h3>
                    <p class="modal-description">${escapeHtml(project.description)}</p>
                    ${featuresHtml}
                    ${techTagsHtml}
                    ${actionButtonsHtml}
                `;
            } catch (err) {
                modalContent.innerHTML = `
                    <div style="text-align: center; padding: 2rem;">
                        <i class="fa-solid fa-circle-exclamation" style="font-size: 2.5rem; color: #ef4444; margin-bottom: 1rem;"></i>
                        <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Could not load details</h3>
                        <p style="color: var(--text-secondary);">Please try again later.</p>
                    </div>
                `;
            }
        });
    });

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('open')) {
            closeModal();
        }
    });
}

/* ===================================================================
   9. AJAX CONTACT FORM
   =================================================================== */
function initContactForm() {
    const form = document.getElementById('contact-form');
    const alertBox = document.getElementById('form-alert');
    const submitBtn = document.getElementById('submit-btn');

    if (!form || !alertBox || !submitBtn) return;

    const btnText = submitBtn.querySelector('.btn-text');
    const btnSpinner = submitBtn.querySelector('.btn-spinner');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Clear previous errors
        document.querySelectorAll('.field-error').forEach(el => {
            el.textContent = '';
            el.style.display = 'none';
        });
        alertBox.style.display = 'none';
        alertBox.className = 'form-alert';

        // Basic client validation
        const nameInput = document.getElementById('contact-name');
        const emailInput = document.getElementById('contact-email');
        const subjectInput = document.getElementById('contact-subject');
        const messageInput = document.getElementById('contact-message');

        if (!nameInput?.value.trim() || !emailInput?.value.trim() || !subjectInput?.value.trim() || !messageInput?.value.trim()) {
            alertBox.className = 'form-alert error';
            alertBox.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Please fill in all required fields.';
            alertBox.style.display = 'flex';
            return;
        }

        // Show loading spinner
        if (btnText) btnText.style.display = 'none';
        if (btnSpinner) btnSpinner.style.display = 'inline-flex';
        submitBtn.disabled = true;

        const formData = new FormData(form);
        const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]')?.value || '';

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken,
                    'Accept': 'application/json',
                },
                body: formData
            });

            const data = await response.json();

            if (response.ok && data.status === 'success') {
                alertBox.className = 'form-alert success';
                alertBox.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${data.message}`;
                alertBox.style.display = 'flex';
                form.reset();

                // Button success animation
                submitBtn.classList.add('btn-success-state');
                if (btnText) {
                    btnText.innerHTML = '<i class="fa-solid fa-check"></i> Message Sent!';
                    btnText.style.display = 'inline-flex';
                }
                if (btnSpinner) btnSpinner.style.display = 'none';

                setTimeout(() => {
                    submitBtn.classList.remove('btn-success-state');
                    if (btnText) {
                        btnText.innerHTML = '<i class="fa-regular fa-paper-plane"></i> Send Message';
                    }
                    submitBtn.disabled = false;
                }, 4000);
                return;
            } else {
                alertBox.className = 'form-alert error';
                alertBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> Please verify the form inputs and try again.`;
                alertBox.style.display = 'flex';

                if (data.errors) {
                    for (const [field, errorList] of Object.entries(data.errors)) {
                        const errorElem = document.getElementById(`error-${field}`);
                        if (errorElem) {
                            errorElem.textContent = Array.isArray(errorList) ? errorList.join(', ') : errorList;
                            errorElem.style.display = 'block';
                        }
                    }
                }
            }
        } catch (error) {
            alertBox.className = 'form-alert error';
            alertBox.innerHTML = `<i class="fa-solid fa-circle-xmark"></i> Message could not be sent right now. Please email directly to <a href="mailto:jainamsheth2006@gmail.com" style="color:inherit; text-decoration:underline;">jainamsheth2006@gmail.com</a>`;
            alertBox.style.display = 'flex';
        } finally {
            if (!submitBtn.classList.contains('btn-success-state')) {
                if (btnText) btnText.style.display = 'inline-flex';
                if (btnSpinner) btnSpinner.style.display = 'none';
                submitBtn.disabled = false;
            }
        }
    });
}

/* ===================================================================
   10. BACK TO TOP BUTTON
   =================================================================== */
function initBackToTop() {
    const backToTopBtn = document.getElementById('back-to-top');
    if (!backToTopBtn) return;

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 350) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* ===================================================================
   11. CURRENT YEAR IN FOOTER
   =================================================================== */
function initCurrentYear() {
    const yearElem = document.getElementById('current-year');
    if (yearElem) {
        yearElem.textContent = new Date().getFullYear();
    }
}

// Utility: HTML Escaper
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}


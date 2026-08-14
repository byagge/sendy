const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const header = document.getElementById('siteHeader');
const contactModal = document.getElementById('contactModal');
const closeModal = document.getElementById('closeModal');

const VICTORIA_TG = 'https://t.me/genpet32?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BE%D0%B1%D1%81%D1%83%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%20TextCheck.';

menuBtn?.addEventListener('click', () => {
  const open = mobileMenu.classList.toggle('hidden') === false;
  menuBtn.setAttribute('aria-expanded', String(open));
});

document.querySelectorAll('#mobileMenu a').forEach((link) => {
  link.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    menuBtn?.setAttribute('aria-expanded', 'false');
  });
});

const openContact = () => {
  if (!contactModal) return;
  contactModal.classList.remove('hidden');
  contactModal.classList.add('flex');
  document.body.style.overflow = 'hidden';
};

const closeContact = () => {
  if (!contactModal) return;
  contactModal.classList.add('hidden');
  contactModal.classList.remove('flex');
  document.body.style.overflow = '';
};

document.querySelectorAll('[data-open-contact]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openContact();
  });
});

closeModal?.addEventListener('click', closeContact);

contactModal?.addEventListener('click', (e) => {
  if (e.target === contactModal) closeContact();
});

window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeContact();
    closeVacancyClosed();
    mobileMenu?.classList.add('hidden');
    menuBtn?.setAttribute('aria-expanded', 'false');
  }
});

window.addEventListener('scroll', () => {
  header?.classList.toggle('is-scrolled', window.scrollY > 12);
}, { passive: true });

document.querySelectorAll('.faq-item').forEach((item) => {
  const trigger = item.querySelector('.faq-trigger');
  const content = item.querySelector('.faq-content');
  const sign = trigger?.querySelector('[data-faq-sign]');

  trigger?.addEventListener('click', () => {
    const isOpen = !content.classList.contains('hidden');
    document.querySelectorAll('.faq-item').forEach((other) => {
      if (other === item) return;
      other.querySelector('.faq-content')?.classList.add('hidden');
      const otherSign = other.querySelector('[data-faq-sign]');
      if (otherSign) otherSign.textContent = '+';
      other.querySelector('.faq-trigger')?.setAttribute('aria-expanded', 'false');
    });
    content.classList.toggle('hidden');
    if (sign) sign.textContent = isOpen ? '+' : '−';
    trigger.setAttribute('aria-expanded', String(!isOpen));
  });
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.16, rootMargin: '0px 0px -8% 0px' });

document.querySelectorAll('[data-reveal]').forEach((el) => {
  revealObserver.observe(el);
});

const animateCount = (el) => {
  const target = Number(el.dataset.count || 0);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const duration = 1100;
  const start = performance.now();

  const tick = (now) => {
    const p = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - p, 3);
    el.textContent = `${prefix}${Math.round(target * eased)}${suffix}`;
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
};

const countObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      animateCount(entry.target);
      countObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-count]').forEach((el) => countObserver.observe(el));

document.querySelectorAll('[data-year]').forEach((el) => {
  el.textContent = String(new Date().getFullYear());
});

document.getElementById('seeAllContacts')?.addEventListener('click', closeContact);

const vacancyModal = document.getElementById('vacancyModal');
const closeVacancyBtn = document.getElementById('closeVacancyModal');

const openVacancyClosed = () => {
  if (!vacancyModal) return;
  vacancyModal.classList.remove('hidden');
  vacancyModal.classList.add('flex');
  document.body.style.overflow = 'hidden';
};

const closeVacancyClosed = () => {
  if (!vacancyModal) return;
  vacancyModal.classList.add('hidden');
  vacancyModal.classList.remove('flex');
  document.body.style.overflow = '';
};

document.querySelectorAll('[data-vacancy-closed]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openVacancyClosed();
  });
});

closeVacancyBtn?.addEventListener('click', closeVacancyClosed);
document.getElementById('closeVacancyModalBtn')?.addEventListener('click', closeVacancyClosed);
vacancyModal?.addEventListener('click', (e) => {
  if (e.target === vacancyModal) closeVacancyClosed();
});

const guideButtons = document.querySelectorAll('[data-guide]');
const guidePanels = document.querySelectorAll('.guide-panel');

guideButtons.forEach((btn) => {
  btn.addEventListener('click', () => {
    const id = btn.getAttribute('data-guide');
    const panel = document.getElementById(`guide-${id}`);
    const alreadyOpen = panel && !panel.hasAttribute('hidden');

    guidePanels.forEach((el) => el.setAttribute('hidden', ''));
    guideButtons.forEach((b) => {
      b.classList.remove('is-open');
      b.setAttribute('aria-expanded', 'false');
    });

    if (!alreadyOpen && panel) {
      panel.removeAttribute('hidden');
      btn.classList.add('is-open');
      btn.setAttribute('aria-expanded', 'true');
      panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  });
});

const laptop = document.getElementById('laptop');
const LAPTOP_TILT = 3;

function setLaptopTransform(rotateY = 0, rotateX = 0) {
  if (!laptop) return;
  if (window.innerWidth < 1024) {
    laptop.style.transform = `rotate(${LAPTOP_TILT}deg)`;
    return;
  }
  laptop.style.transform = `perspective(900px) rotate(${LAPTOP_TILT}deg) rotateY(${rotateY}deg) rotateX(${rotateX}deg)`;
}

setLaptopTransform();
window.addEventListener('resize', () => setLaptopTransform());

document.addEventListener('mousemove', (e) => {
  if (!laptop || window.innerWidth < 1024) return;
  const rect = laptop.getBoundingClientRect();
  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;
  const dx = (e.clientX - cx) / rect.width;
  const dy = (e.clientY - cy) / rect.height;
  setLaptopTransform(dx * 8, -dy * 6);
});

document.addEventListener('mouseleave', () => setLaptopTransform());

window.TextCheckContacts = { victoriaTelegram: VICTORIA_TG };

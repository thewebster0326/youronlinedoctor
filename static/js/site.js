/* Your Online Doctor - site behaviour
   Navigation, scroll reveals, POPIA consent, and dataLayer events. */

(function () {
  'use strict';

  window.dataLayer = window.dataLayer || [];

  /* ------------------------------------------------------------- header */

  var header = document.getElementById('site-header');
  var onScroll = function () {
    if (!header) return;
    header.classList.toggle('is-stuck', window.scrollY > 24);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------------------------------------------------------- mobile nav */

  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------------------ reveals */

  var reveals = document.querySelectorAll('.reveal');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reduced || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(reveals, function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    Array.prototype.forEach.call(reveals, function (el, i) {
      // Stagger siblings inside a grid so cards arrive in sequence.
      var parent = el.parentNode;
      if (parent && parent.classList && parent.classList.contains('grid')) {
        el.style.transitionDelay = (Math.min(i, 6) * 70) + 'ms';
      }
      io.observe(el);
    });
  }

  /* ------------------------------------------------------- click events */

  document.addEventListener('click', function (e) {
    var el = e.target.closest ? e.target.closest('[data-track]') : null;
    if (!el) return;
    window.dataLayer.push({
      event: el.getAttribute('data-track'),
      link_location: el.getAttribute('data-location') || 'unknown',
      link_url: el.getAttribute('href') || '',
      page_path: window.location.pathname
    });
  });

  /* --------------------------------------------------- POPIA consent bar */

  var KEY = 'yod-consent';
  var bar = document.getElementById('consent-bar');

  function stored() {
    try { return window.localStorage.getItem(KEY); } catch (err) { return null; }
  }

  function remember(value) {
    try { window.localStorage.setItem(KEY, value); } catch (err) { /* private mode */ }
  }

  function applyConsent(value) {
    window.dataLayer.push({
      event: 'consent_choice',
      consent_state: value,
      analytics_storage: value === 'accept' ? 'granted' : 'denied',
      ad_storage: value === 'accept' ? 'granted' : 'denied'
    });
  }

  if (bar) {
    var existing = stored();
    if (existing) {
      applyConsent(existing);
    } else {
      // Hold the bar back until the visitor scrolls (or 6s passes) so it never
      // lands on top of the hero call to action on a phone. Nothing
      // non-essential is stored before a choice is made, so deferring is safe.
      var shown = false;
      var reveal = function () {
        if (shown) return;
        shown = true;
        bar.classList.add('is-open');
        window.removeEventListener('scroll', onFirstScroll);
      };
      var onFirstScroll = function () {
        if (window.scrollY > 120) reveal();
      };
      window.addEventListener('scroll', onFirstScroll, { passive: true });
      window.setTimeout(reveal, 6000);
    }

    bar.addEventListener('click', function (e) {
      var btn = e.target.closest ? e.target.closest('[data-consent]') : null;
      if (!btn) return;
      var choice = btn.getAttribute('data-consent');
      remember(choice);
      applyConsent(choice);
      bar.classList.remove('is-open');
    });
  }
})();

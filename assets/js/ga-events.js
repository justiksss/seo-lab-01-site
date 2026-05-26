(function () {
  if (typeof gtag !== 'function') return;

  var pagePath = location.pathname;

  document.querySelectorAll('a[href*="contact.html"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'cta_contact_click', {
        link_text: (el.textContent || '').trim().slice(0, 100),
        page_path: pagePath
      });
    });
  });

  document.querySelectorAll('header nav a').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'nav_click', {
        link_text: (el.textContent || '').trim(),
        destination: el.getAttribute('href') || ''
      });
    });
  });

  document.querySelectorAll('a[href*="services/seo.html"], a[href*="services/web.html"]').forEach(function (el) {
    el.addEventListener('click', function () {
      var href = el.getAttribute('href') || '';
      gtag('event', 'service_click', {
        service_name: href.indexOf('web') !== -1 ? 'web' : 'seo'
      });
    });
  });

  document.querySelectorAll('a[href*="blog/post-"]').forEach(function (el) {
    el.addEventListener('click', function () {
      var href = el.getAttribute('href') || '';
      gtag('event', 'blog_click', {
        post_slug: href.split('/').pop().replace('.html', '')
      });
    });
  });

  document.querySelectorAll('a[href*="glossary.html"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'glossary_click', {
        source_page: pagePath
      });
    });
  });

  var demoMap = {
    'broken-link-target.html': '404',
    'redirect-a.html': 'redirect_chain',
    'post-duplicate-a.html': 'duplicate_content',
    'page-no-title.html': 'missing_title'
  };
  document.querySelectorAll('a[href]').forEach(function (el) {
    var href = el.getAttribute('href') || '';
    Object.keys(demoMap).forEach(function (key) {
      if (href.indexOf(key) !== -1) {
        el.addEventListener('click', function () {
          gtag('event', 'audit_demo_click', { demo_type: demoMap[key] });
        });
      }
    });
  });

  document.querySelectorAll('a[href^="mailto:"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'mailto_click', {
        email: (el.getAttribute('href') || '').replace('mailto:', '')
      });
    });
  });
})();

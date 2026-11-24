/* EURL ETPBH MAROUANE — menu mobile et formulaire de demande de devis */
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  var form = document.querySelector('form.devis');
  if (!form) return;
  var WA = '213661348273';
  var MAIL = 'contact@etpbh-marouane.dz';

  function message() {
    var L = form.dataset;
    var v = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ''; };
    var lines = [L.title];
    [['nom', L.lnom], ['societe', L.lsoc], ['tel', L.ltel], ['besoin', L.lbesoin],
     ['lieu', L.llieu], ['duree', L.lduree], ['details', L.ldetails]].forEach(function (p) {
      var x = v(p[0]); if (x) lines.push(p[1] + ' : ' + x);
    });
    return lines.join('\n');
  }
  function valid() {
    if (!form.reportValidity) return true;
    return form.reportValidity();
  }
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!valid()) return;
    window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(message()), '_blank', 'noopener');
  });
  var mailBtn = form.querySelector('[data-mail]');
  if (mailBtn) mailBtn.addEventListener('click', function () {
    if (!valid()) return;
    location.href = 'mailto:' + MAIL + '?subject=' + encodeURIComponent(form.dataset.title) +
      '&body=' + encodeURIComponent(message());
  });
})();

/* Thème jour / nuit : le thème est déjà posé par le script du <head> ; ici, la bascule. */
(function () {
  var root = document.documentElement, KEY = 'etp_theme';
  function stored() { try { var v = localStorage.getItem(KEY); return v === 'light' || v === 'dark' ? v : null; } catch (e) { return null; } }
  function apply(t) {
    root.setAttribute('data-theme', t);
    document.querySelectorAll('.theme-btn').forEach(function (b) { b.setAttribute('aria-pressed', String(t === 'dark')); });
  }
  document.querySelectorAll('.theme-btn').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
    });
  });
  var mq = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
  if (mq) {
    var on = function (e) { if (!stored()) apply(e.matches ? 'dark' : 'light'); };
    if (mq.addEventListener) mq.addEventListener('change', on); else if (mq.addListener) mq.addListener(on);
  }
  apply(root.getAttribute('data-theme') || 'light');
})();

/* Sélecteur de langue : menu déroulant (clic / toucher, Échap, clic à l'extérieur). */
(function () {
  document.querySelectorAll('.lang-drop').forEach(function (wrap) {
    var btn = wrap.querySelector('.lang-drop-btn');
    var links = wrap.querySelectorAll('a.lang-btn');
    function set(open) { wrap.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); }
    btn.addEventListener('click', function (e) { e.stopPropagation(); set(!wrap.classList.contains('open')); });
    btn.addEventListener('keydown', function (e) { if (e.key === 'ArrowDown') { e.preventDefault(); set(true); if (links[0]) links[0].focus(); } });
    wrap.addEventListener('keydown', function (e) { if (e.key === 'Escape') { set(false); btn.focus(); } });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) set(false); });
  });
})();

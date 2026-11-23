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
  var MAIL = 'marouanlatelli@gmail.com';

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

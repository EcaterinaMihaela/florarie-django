const favoriteKey = 'favoriteFlowers';

function getFavorites() {
  const fav = localStorage.getItem(favoriteKey);
  return fav ? JSON.parse(fav) : [];
}

function setFavorites(favs) {
  localStorage.setItem(favoriteKey, JSON.stringify(favs));
}

document.addEventListener('DOMContentLoaded', () => {
  const favorites = getFavorites();

  document.querySelectorAll('.favorite-btn').forEach(btn => {
    const floareId = btn.dataset.floareId;

    if (favorites.includes(floareId)) {
      btn.classList.add('active');
    }

    btn.addEventListener('click', () => {
      let favs = getFavorites();

      if (favs.includes(floareId)) {
        favs = favs.filter(id => id !== floareId);
        btn.classList.remove('active');
      } else {
        favs.push(floareId);
        btn.classList.add('active');
      }

      setFavorites(favs);
    });
  });
});

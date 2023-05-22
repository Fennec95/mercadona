// Fonction pour récupérer les données des produits depuis le cache ou le serveur
function getProductData() {
  var cachedProducts = localStorage.getItem('products');

  if (cachedProducts) {
    // Si les produits sont présents dans le cache, les renvoyer
    return Promise.resolve(JSON.parse(cachedProducts));
  } else {
    // Sinon, effectuer une requête AJAX pour récupérer les produits du serveur
    return fetch('/api/products')
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        // Stocker les produits dans le cache
        localStorage.setItem('products', JSON.stringify(data));
        return data;
      });
  }
}

// Exemple d'utilisation de la fonction de récupération des données des produits
getProductData()
  .then(function(products) {
    // Utilisez les données des produits ici
    console.log(products);
    // Affichez les produits sur votre page
    products.forEach(function(product) {
      // Affichage du nom du produit
      console.log(product.name);
    });
  })
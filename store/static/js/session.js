
function getProductData() {
  var cachedProducts = localStorage.getItem('products');

  if (cachedProducts) {

    return Promise.resolve(JSON.parse(cachedProducts));
  } else {

    return fetch('/api/products')
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {

        localStorage.setItem('products', JSON.stringify(data));
        return data;
      });
  }
}


getProductData()
  .then(function(products) {

    console.log(products);

    products.forEach(function(product) {
      // Affichage du nom du produit
      console.log(product.name);
    });
  })
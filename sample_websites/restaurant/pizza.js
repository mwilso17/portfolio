var placeOrder = document.getElementById('placeOrder');

function createOrder() {
  var specialRequests = document.getElementsByClassName('specialRequests');
  var results = document.getElementById('text');

  results.innerHTML = specialRequests[0].value; 

  alert("Your order has been placed!");
}

placeOrder.addEventListener('click', createOrder);
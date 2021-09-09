
var stripe = Stripe(STRIPE_PUBLISHABLE_KEY);

var elem = document.getElementById('submit')
clientsecret = elem.getAttribute('data-secret');


// Set up Stripe.js and Elements to use in checkout form

var elements = stripe.elements();
var style = {
        base: {
        color:'#000',
        lineHeight: '2.4',
        fontSize: '16px',
    }
};

var card = elements.create("card", {style: style});
card.mount('#card-element');

card.on('change', function(e){
    var displayError = document.getElementById('card-errors')
    if (e.error){
        displayError.textContent = e.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
    });

    var form = document.getElementById('payment-form');

    form.addEventListener('submit', function(e){
        e.preventDefault();

        var custName = document.getElementById("custName").value;
        var custAdd = document.getElementById("custAdd").value;
        var custAdd2 = document.getElementById("custAdd2").value;
        var postCode = document.getElementById("postCode").value;
        
        $.ajax({
            type: "POST",
            url: 'http://localhost:8000/orders/add/',
            data: {
                order_key: clientsecret,
                csrfmiddlewaretoken: CSRF_TOKEN,
                action: "POST",                
            }, 
            success: function(json){
                console.log(json.success)


                stripe.confirmCardPayment(clientsecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            address:{
                                line1: custAdd,
                                line2: custAdd2
                            },
                            name: custName
                        },
                    }
                }).then(function(results){
                    if (results.error){
                        console.log('payment error')
                        console.log(results.error.message);

                    } else {
                        if (results.paymentIntent.status === 'succeeded'){
                            console.log('payment processed')

                            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/")
                        }

                    }
                });
            },
            error: function(xhr, errmsg, err) {},
        });
    
    
    });
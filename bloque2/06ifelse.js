/* control de flujo

// condicionales
var condicion = false;
var condicion2 = true;
if (condicion && condicion2) {
    // hago esto si se cumple condicion
    console.log('Estoy en el if');
} else {
    // hago esto otro si no se cumple condicion
    console.log('Estoy en el else');
}
// continuo ejecutando





// Se pueden encadenar
if (condicion1) {
    // Entro aqui si cumplo la primera condicion
} else if (condicion2) {
    // Entro aqui si cumplo la segunda
} else if (condicion3) {
    // Entro aqui si cumplo la tercera
} else {
    // Entro aqui si no cumplo ninguna
}






// Se pueden anidar
if (condicion1) {
    if (condicion2) {
        // Hago algo
    }
    // Luego hago otra cosa
} else {
    // Hago otra cosa distinta
} 
 
 HOMEWORK 
 
Se debe realizar un programa que, dados dos números, imprima por pantalla si el primer número es múltiplo del segundo.
Por ejemplo, con las siguientes variables:

var primer = 20;
var segundo = 2;


Se debería imprimir:
20 es múltiplo de 2.


Con las siguientes variables:

var primer = 23;
var segundo = 2;

Se debería imprimir:
23 no es múltiplo de 2. */
 
var primer = 23; 
var segundo = 2; 
 
if ( primer%segundo === 0 ) { 
    console.log(primer, 'es multiplo de:', segundo ) 
} else {
     console.log(primer, 'no es multiplo de:', segundo)
};
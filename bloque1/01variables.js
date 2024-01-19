var cajaA = 3;
cajaA = 5;
var cajaB = 5;
var cajaC = cajaA + cajaB;

console.log(cajaA, cajaB, cajaC);

var x = 2;
var y = 3;

// intercambiar los valores de x e y
// x: 2, y: 3
// resultado: x: 3, y: 2
// funcion de swap
var z = y;
y = x;
x = z;

// deestructuring
[x, y] = [y, x]

console.log('Resultado ejercicio: x es', x, 'y es', y); 
  
var x = 2; 
var y = 3; 
 
console.log(x,y);
 
var z = x; 
x = y;
y = z; 
 
console.log(x,y); 
 
/*Homework:  
Para éste ejercicio, se quiere realizar un programa que intercambie los valores de dos variables. Por ejemplo, si nosotros tenemos:

var x = 3

var y = 5

querríamos que el programa intercambie x por y, es decir que resulte en lo siguiente:

x = 5

y = 3 
 
De esta forma es más eficiente ya que usamos la tecnica deestructuring */

var x = 3; 
var y = 5; 
 
[x, y] = [y, x]  
 
console.log(x,y);
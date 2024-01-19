// Otra forma de controlar el flujo condicional
// Podemos simplificar un if:
var status = 0;
if (status === 0) {
    // Hago A
} else if (status === 1) {
    // Hago B
} else if (status === 2) {
    // Hago C
}

// Podemos escribirlo como:
switch (status) {
    case 0:
        // Hago A
        break;
    case 1:
        // Hago B
        break;
    case 2:
        // Hago C
        break;
    default:

        break;
}

// Es mas legible y mas eficiente 
 
// HOMEWORK 
  
function daysInMonth(month){ 
    switch (month){ 
        case "enero": 
        case "marzo": 
        case "mayo": 
        case "julio": 
        case "agosto": 
        case "octube": 
        case "diciembre": 
        console.log("El mes de", month, "tiene 31 dias");  
        break; 
        case "febrero": 
        console.log("El mes de", month, "tiene 28/29 dias"); 
        break; 
        case "abril": 
        case "julio": 
        case "septiembre": 
        case "noviembre": 
        console.log("El mes de", month, "tiene 30 dias"); 
        break; 
    }
} 
 
daysInMonth("enero") 


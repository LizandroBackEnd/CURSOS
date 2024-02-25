export default function ScooterTop({modelo,precio}){ 
    return( 
        <li className="list-group-item"> 
        {modelo} 
        <span className="badge text-bg-dark float-end">{precio} $</span> 
        </li>
    ) 

}
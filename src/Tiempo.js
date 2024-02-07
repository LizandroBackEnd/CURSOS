import { useState, useEffect } from 'react'; 
 
export default function Tiempo() { 
    const [seconds, setSeconds] = useState(0);  
     
     useEffect(() => { 
        const interval = setInterval( 
            () => {setSeconds( seconds => seconds + 1)}  
            ,1000
        )
         
        return () => { 
            clearInterval(interval);
        }; 

     });

    return ( 
            <div className="lcdText text-danger pe-2 m-2 borderInsideS" style={{ width: 54 }}>{seconds}</div> 
         
    );
}
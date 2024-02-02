const readline = require('readline'); 
 
//Tarea: valor booleano y description 
let  taskList = []; 
 
function addTask (taskList, taskDescription){ 
    taskList.push({done: false, description: taskDescription});
} 
 
function printTaskList(taskList){ 
    //[] Sacar la basura  
    //[x] Lavar los platos 
    for (let i = 0; i < taskList.length; ++i) { 
        if (taskList[i].done) {
            //tarea realizada 
            console.log('[x] ' + taskList[i].description);
        }else{ 
            //tarea no realizada 
            console.log('[ ] ' + taskList[i].description);
        }
    }
     

} 
 
addTask(taskList, 'Sacar la basura');  
addTask(taskList, 'Lavar los platos'); 
 
printTaskList(taskList);

// Primer modo: lectura de tareas necesarias 

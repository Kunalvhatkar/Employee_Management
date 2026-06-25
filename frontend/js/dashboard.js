const API="http://YOUR-ELASTIC-BEANSTALK-URL";

loadEmployees();

async function loadEmployees(){

const response=await fetch(API+"/employees");

const employees=await response.json();

let table="";

employees.forEach(emp=>{

table+=`

<tr>

<td>${emp.name}</td>

<td>${emp.email}</td>

<td>${emp.department}</td>

<td>${emp.designation}</td>

<td>

<button

class="delete-btn"

onclick="deleteEmployee('${emp._id}')">

Delete

</button>

</td>

</tr>

`;

});

document.getElementById("employeeTable").innerHTML=table;

}

document

.getElementById("employeeForm")

.addEventListener("submit",async(e)=>{

e.preventDefault();

const employee={

name:name.value,

email:email.value,

department:department.value,

designation:designation.value

};

await fetch(API+"/employee",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(employee)

});

employeeForm.reset();

loadEmployees();

});

async function deleteEmployee(id){

await fetch(API+"/employee/"+id,{

method:"DELETE"

});

loadEmployees();

}

function logout(){

localStorage.clear();

window.location="index.html";

}
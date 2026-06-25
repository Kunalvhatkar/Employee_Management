const API="http://localhost:5000"; //EBS url

const token=localStorage.getItem("token");

loadEmployees();

async function loadEmployees(){

const res=await fetch(API+"/employees",{

headers:{
Authorization:token
}

});

const employees=await res.json();

let html="";

employees.forEach(emp=>{

html+=`

<tr>

<td>${emp.name}</td>

<td>${emp.email}</td>

<td>${emp.department}</td>

<td>${emp.salary}</td>

<td>

<button class="delete"
onclick="deleteEmployee('${emp._id}')">

Delete

</button>

</td>

</tr>

`;

});

employeeTable.innerHTML=html;

}

employeeForm.onsubmit=async(e)=>{

e.preventDefault();

const employee={

name:name.value,
email:email.value,
department:department.value,
salary:salary.value

};

await fetch(API+"/employees",{

method:"POST",

headers:{

"Content-Type":"application/json",

Authorization:token

},

body:JSON.stringify(employee)

});

employeeForm.reset();

loadEmployees();

}

async function deleteEmployee(id){

await fetch(API+"/employees/"+id,{

method:"DELETE",

headers:{

Authorization:token

}

});

loadEmployees();

}
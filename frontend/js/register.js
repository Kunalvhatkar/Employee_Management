const API="http://localhost:5000"; //elastic beanstolk url

document.getElementById("registerForm").onsubmit=async(e)=>{

e.preventDefault();

const data={

name:name.value,
email:email.value,
password:password.value

};

const res=await fetch(API+"/register",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

});

const result=await res.json();

alert(result.message);

window.location="index.html";

}
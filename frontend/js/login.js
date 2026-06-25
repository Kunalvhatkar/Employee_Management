const API="http://YOUR-ELASTIC-BEANSTALK-URL/login";

document
.getElementById("loginForm")
.addEventListener("submit",async(e)=>{

e.preventDefault();

const username=document.getElementById("username").value;

const password=document.getElementById("password").value;

const response=await fetch(API,{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
username,
password
})

});

const data=await response.json();

if(data.success){

localStorage.setItem("token",data.token);

window.location="dashboard.html";

}

else{

document.getElementById("message").innerHTML="Invalid Login";

}

});
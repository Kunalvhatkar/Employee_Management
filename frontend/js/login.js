const API="http://localhost:5000"; //Elastic beaanstolk url

document.getElementById("loginForm").onsubmit=async(e)=>{

e.preventDefault();

const data={

email:email.value,
password:password.value

};

const res=await fetch(API+"/login",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

});

const result=await res.json();

if(result.token){

localStorage.setItem("token",result.token);

window.location="dashboard.html";

}else{

alert(result.message);

}

}
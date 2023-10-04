function validateform(){
    var name = document.form1.name.value;
    var password = document.form1.password.value;

    if (name==null || name==""){
        alert("Username Can't be empty")
        return false;
    }else if(password.length<6){
        alert("Password must contain min of 6 Characters long")
        return false;
    }
}
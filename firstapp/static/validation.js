function validation()
{
    var mynm=document.f1.name.value;
    var myfnm=document.f1.fname.value;
    var mymob=document.f1.mob.value;
    var myemail=document.f1.email.value;
    var mypass=document.f1.pass.value;
    var mycpass=document.f1.cpass.value;
    var mycap=document.f1.cap.value;
    // var mycapture=document.f1.image.value;
    
    if (mynm=="")
    {
        var text1="please enter your name";
        document.getElementById('nm').innerHTML=text1;
        return false;
    }

    if (myfnm=="")
    {
        var text1="please enter your father name";
        document.getElementById('fnm').innerHTML=text1;
        return false;
    }

    if (mymob=="")
    {
        var text1="please enter number";
        document.getElementById('mob').innerHTML=text1;
        return false;
    }

    if (isNaN(mymob))
    {
        var text1="please enter numeric number ";
        document.getElementById('mob').innerHTML=text1;
        return false;
    }
    
    if (myemail=="")
    {
        var text1="please enter email";
        document.getElementById('email').innerHTML=text1;
        return false;
    }
    if (mypass=="")
    {
        var text1="please enter password";
        document.getElementById('pass1').innerHTML=text1;
        return false;
    }

    if (mycpass=="")
    {
        var text1="Re-enter your password";
        document.getElementById('pass2').innerHTML=text1;
        return false;
    }

    if (mycap=="")
    {
        var text1="Enter captcha";
        document.getElementById('key').innerHTML=text1;
        return false;
    }

    // if(mycap!=mycapture)
    // {
    //     var text1="captcha not match";
    //     document.getElementById('key').innerHTML=text1;
    //     return false;
    // }

    
    
}


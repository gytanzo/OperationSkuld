function createCookie(cname, cvalue){
    var now = new Date();
    now.setTime(now.getTime() + 3 * 60 * 1000);
    document.cookie = cname + "=" + cvalue + ";expires=" + now + ";path=/";
}





function namer(){
    var now = new Date();
    now.setTime(now.getTime() + 2 * 60 * 1000);
    // it's set for 5 minutes
}
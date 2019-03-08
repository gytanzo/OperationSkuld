function ajaxGetRequest(path, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            callback(this.response);
        }
    }
};
    request.open("POST", path);
    request.send(data);

function addName() {

    var name = document.getElementById("addName");

    var User = [name.value];
    if (button.click == True){
        var toSend = JSON.stringify({"User": User});
    }
    ajaxPostRequest("/addName", toSend, "nameList");
    }

function getNameList() {
    ajaxGetRequest("/getNameList", "nameList")
}
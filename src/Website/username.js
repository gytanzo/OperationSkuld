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
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function addName() {

    var name = document.getElementById("addName").value;
    var data = {};
    alert("PEAVCE");
    if (button.onclick == True){
        var txt = JSON.parse({"User":name});
        data.push(txt);
        var toSend = JSON.stringify(data);
    }
    var fs = require('fs');
    fs.writeFile('package.json', toSend, 'utf8', callback);
    ajaxPostRequest("/addName", toSend, "nameList");
    }

function getNameList() {
    ajaxGetRequest("/getNameList", "nameList")
}
var upvoteThread = function(id, type) {
  console.log(id, type)

  var xhr = new XMLHttpRequest();

  if (type === 'True') {
    // this is a link
    var url = "/link/" + id + "/upvote";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
            location.reload();
        }
    };
    var data = JSON.stringify({"user_id": 1});
    xhr.send(data);
  } else {
    var url = "/text/" + id + "/upvote";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json);
            location.reload();
        }
    };
    var data = JSON.stringify({"user_id": 1});
    xhr.send(data);
  }
}

var downvoteThread = function(id, type) {
    console.log(id, type)
  
    var xhr = new XMLHttpRequest();
  
    if (type === 'True') {
      // this is a link
      var url = "/link/" + id + "/downvote";
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-type", "application/json");
      xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
              var json = JSON.parse(xhr.responseText);
              console.log(json);
              location.reload();
          }
      };
      var data = JSON.stringify({"user_id": 1});
      xhr.send(data);
    } else {
      var url = "/text/" + id + "/downvote";
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-type", "application/json");
      xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
              var json = JSON.parse(xhr.responseText);
              console.log(json);
              location.reload();
          }
      };
      var data = JSON.stringify({"user_id": 1});
      xhr.send(data);
    }
  }
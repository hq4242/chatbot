"use strict";

var send_response = function send_response(message) {
  message_editted = message.split(' ').join('+');
  fetch("http://localhost:5000/conv?sentence=".concat(message_editted)).then(function (response) {
    return response.json();
  }).then(function (data) {
    document.getElementById("chat").innerHTML += "<div class=\"bot-message\">".concat(data, "</div>");
  });
  space_for_new_message();
};

var space_for_new_message = function space_for_new_message() {
  var children = document.getElementById("chat").childNodes;
  children.forEach(function (item) {
    var position = parseInt(item.style.bottom) || 0;

    if (position == 0) {
      item.style.bottom = "40px";
    } else {
      item.style.bottom = "".concat(40 + position, "px");
    }
  });
};

var send_message = function send_message(side_message) {
  var message = document.getElementById("message").value || side_message;
  document.getElementById("message").value = "";

  if (message != "") {
    space_for_new_message();
    document.getElementById("chat").innerHTML += "<div class=\"my-message\">".concat(message, "</div>");
    setTimeout(function () {
      return send_response(message);
    }, Math.floor(Math.random() * 10000) / 4);
  }
};
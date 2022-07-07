var ws;

function createSocket(url) {
   ws = new WebSocket(`ws://${url}/ussd/`);

   ws.onopen = function() {
      ws.send("Message to send");
      console.log("Message is sent...");
   };
   ws.onmessage = function (evt) { 
      var received_msg = evt.data;
      console.log("Message is received...");
      messages = document.getElementById("messages")
      messages.innerHTML += `<div>${received_msg}</div>`
   };
   ws.onclose = function() {
      console.log("Connection is closed..."); 
      messages.innerHTML += ''
      ws = null
   };
}

function sendMessage(){
   console.log("Connecting...")
   if(!ws){
      console.log("Connecting...")
      var url = document.getElementById("url").value
      createSocket(url)
   } else {
      var text = document.getElementById("message").value
      ws.send(text);
      document.getElementById("message").value = ""
   }
}

document.getElementById("button").addEventListener("click", sendMessage)
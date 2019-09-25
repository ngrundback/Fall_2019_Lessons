

// Watch the user's location
var watchUser = navigator.geolocation.watchPosition(foundYou, findError);
setInterval(foundYou, 3000)

// Our function to pass to watchPosition when it finds user
function foundYou(yourPosition){

  // What is "yourPosition"? *hint* press CMD+Alt+J to look in the console...
  console.log(yourPosition);


  // Store user's location
  var userLat = yourPosition.coords.latitude;
  var userLon = yourPosition.coords.longitude;
  var userSpeed = yourPosition.coords.speed;
  
  if (userSpeed == null){
    userSpeed = "Too slow to care. Try harder"
  }

  const messageBoxLat = document.querySelector("#messageLat");
    messageBoxLat.innerHTML = "Your Lat is: " + userLat
  const messageBoxLon = document.querySelector("#messageLon");
    messageBoxLon.innerHTML = "Your Lon is: " + userLon
  const messageBoxSpeed = document.querySelector("#messageSpeed");
    messageBoxSpeed.innerHTML = "Your Speed is: " + userSpeed

} // END foundYou

// A function that runs if the user location cannot be found
function findError(error){
  // If the site cannot find the user's location, display an error message
  let messageBox = document.querySelector("#message");
  messageBox.innerHTML = "Sorry; we can't currently locate you. Try reloading the page and allowing the GPS to find you :)" 
}

if (window.DeviceMotionEvent) {
  window.addEventListener('devicemotion', deviceMotionHandler);
  setInterval(deviceMotionHandler, 3000)
} else {
  const messageBoxMotion = document.querySelector("#messageMotion")
    messageBoxMotion.innerHTML = "Not Supported. :("
}

function deviceMotionHandler(yourMotion){
  var x_accel = yourMotion.accelerationIncludingGravity.x
  var y_accel = yourMotion.accelerationIncludingGravity.y
  var z_accel = yourMotion.accelerationIncludingGravity.z
  
  if (x_accel != null){
    console.log(yourMotion)

  const accelX = document.querySelector("#x")
    accelX.innerHTML = "Your X Axis is: " + x_accel.toFixed(1)
  }
  if (y_accel != null){
  const accelY = document.querySelector("#y")
    accelY.innerHTML = "Your y Axis is: " + y_accel.toFixed(1)
  }
  
  if (z_accel != null){
  const accelZ = document.querySelector("#z")
    accelZ.innerHTML = "Your Z Axis is: " + z_accel.toFixed(1)
  } else{
    const accelZ = document.querySelector("#z")
      accelZ.innerHTML = "Try using FireFox"
  }
  
}
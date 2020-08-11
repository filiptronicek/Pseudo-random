var iterations = 0;
//var desiredIterations = prompt('Kolik iterací?');
var desiredIterations = 150000;
var die = {
  one: 0,
  two: 0,
  three: 0,
  four: 0,
  five: 0,
  six: 0,
  iterations: 0,
  currNum: 0,
};

var myObject = new Vue({
  el: "#app",
  data: {
    die: die,
  },
});

function check() {
  if (iterations < desiredIterations) {
    iterations++;
    var randnum = Math.floor(Math.random() * 6 + 1);

    if (randnum == 1) {
      die.one++;
    } else if (randnum == 2) {
      die.two++;
    } else if (randnum == 3) {
      die.three++;
    } else if (randnum == 4) {
      die.four++;
    } else if (randnum == 5) {
      die.five++;
    } else if (randnum == 6) {
      die.six++;
    }
    die.currNum = randnum;
    die.iterations++;
  } else {
    clearInterval(checkTimer);
    console.log("Completed " + iterations + " iterations");
    console.log(die);
  }
}
var checkTimer = setInterval(() => {
  check();
}, 1);

const st = new Date();

let iterations = 0;

const desiredIterations = 10000000;

let die = {
  one: 0,
  two: 0,
  three: 0,
  four: 0,
  five: 0,
  six: 0,
  iterations: 0,
  currNum: 0,
};

const myObject = new Vue({
  el: "#app",
  data: {
    die: die,
  },
});

while (iterations < desiredIterations) {
  iterations++;
  const randnum = Math.floor(Math.random() * 6 + 1);

  switch (randnum) {
    case 1:
      die.one++;
      break;
    case 2:
      die.two++;
      break;
    case 3:
      die.three++;
      break;
    case 4:
      die.four++;
      break;
    case 5:
      die.five++;
      break;
    case 6:
      die.six++;
      break;
  }

  die.currNum = randnum;
  die.iterations++;
}
const en = new Date();
console.log(en - st);

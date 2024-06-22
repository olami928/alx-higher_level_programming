#!/usr/bin/node

const callMeMoby = (x, theFunction) => {
  let i;

  for (i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports = { callMeMoby };

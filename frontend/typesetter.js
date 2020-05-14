let promise = Promise.resolve();  // Used to hold chain of typesetting calls

function typeset(code) {
  promise = promise.then(() => {
      code();
      return MathJax.typesetPromise()
  }).catch((err) => console.log('Typeset failed: ' + err.message));
  return promise;
}

function typesetAnswer(ans) {
    typeset(() => {
      const math = document.querySelector('#ans');
      math.innerHTML = '$$' + ans + '$$';
      return math;
    });
}

function typesetFunction(f) {
    typeset(() => {
        const math = document.querySelector('#function');
        math.innerHTML = '$$' + f + '$$';
        return math;
    });
}

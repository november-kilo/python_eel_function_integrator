let typesettingPromise = Promise.resolve();  // Used to hold chain of typesetting calls

function typeset(code) {
  typesettingPromise = typesettingPromise.then(() => {
      code();
      return MathJax.typesetPromise()
  }).catch((err) => console.log('Typeset failed: ' + err.message));
  return typesettingPromise;
}

function typesetAnswer(ans) {
    typeset(() => {
      const math = document.querySelector('#ans');
      math.innerHTML = '$$' + ans + '$$';
      return math;
    });
}

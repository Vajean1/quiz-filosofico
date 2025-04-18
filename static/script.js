// script.js
const optionsDiv = document.getElementById('options');
const correctText = optionsDiv.dataset.correct;

// todos os botões de opção
const buttons = optionsDiv.querySelectorAll('button.option-btn');
const caDiv = document.getElementById('correctAnswer');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    // desabilita todos
    buttons.forEach(b => b.disabled = true);

    const escolha = btn.dataset.value;

    if (escolha === correctText) {
      // acerto
      btn.classList.add('correct');
    } else {
      // erro
      btn.classList.add('wrong');
      // exibe a resposta certa
      caDiv.textContent = `Resposta certa: ${correctText}`;
      caDiv.style.display = 'block';
    }

    // após 1s segue para próxima questão
    setTimeout(() => {
      const form = document.createElement('form');
      form.method = 'POST';
      form.style.display = 'none';
      form.innerHTML = `<input name="escolha" value="${escolha}">`;
      document.body.appendChild(form);
      form.submit();
    }, 1000);
  });
});

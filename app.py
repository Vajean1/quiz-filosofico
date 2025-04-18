from flask import Flask, render_template, request, redirect, session, url_for
from random import shuffle

app = Flask(__name__)
app.secret_key = 'alocar um valor secreto'

QUESTOES = [
    {
    "pergunta": "Qual é o principal objetivo da Filosofia da Educação?",
    "opcoes": [
      "Criar regras rígidas para o ensino",
      "Refletir criticamente sobre os processos educativos",
      "Ensinar a decorar conteúdos escolares"
    ],
    "resposta": "Refletir criticamente sobre os processos educativos"
  },
  {
    "pergunta": "A Filosofia da Educação ajuda os professores a:",
    "opcoes": [
      "Melhorarem apenas as técnicas de ensino",
      "Reproduzirem o currículo escolar",
      "Pensarem sobre os fins e os meios da educação"
    ],
    "resposta": "Pensarem sobre os fins e os meios da educação"
  },
  {
    "pergunta": "A Filosofia da Educação é importante porque:",
    "opcoes": [
      "Substitui a prática pedagógica",
      "Questiona o sentido do ato de educar",
      "Reforça métodos tradicionais sem mudanças"
    ],
    "resposta": "Questiona o sentido do ato de educar"
  },
  {
    "pergunta": "O pensamento ocidental nasce com a busca por:",
    "opcoes": [
      "Explicações mitológicas",
      "Explicações religiosas",
      "Explicações racionais e filosóficas"
    ],
    "resposta": "Explicações racionais e filosóficas"
  },
  {
    "pergunta": "Na Grécia Antiga, os primeiros filósofos buscavam:",
    "opcoes": [
      "Dogmas e crenças",
      "Explicações lógicas para a realidade",
      "Regras para a convivência social"
    ],
    "resposta": "Explicações lógicas para a realidade"
  },
  {
    "pergunta": "A transição do mito à filosofia foi marcada por:",
    "opcoes": [
      "Aceitação de verdades sem questionamento",
      "Criação de doutrinas religiosas",
      "Negação das crenças e a busca pela verdade por meio da razão"
    ],
    "resposta": "Negação das crenças e a busca pela verdade por meio da razão"
  },
  {
    "pergunta": "O método socrático é conhecido por:",
    "opcoes": [
      "Ensinar através de provas e castigos",
      "Fazer o aluno pensar por meio de perguntas",
      "Expor conteúdos prontos sem diálogo"
    ],
    "resposta": "Fazer o aluno pensar por meio de perguntas"
  },
  {
    "pergunta": "Platão acreditava que a verdadeira educação levava à:",
    "opcoes": [
      "Obediência cega ao Estado",
      "Liberdade do pensamento e conhecimento das ideias",
      "Aceitação do mundo sensível como verdade absoluta"
    ],
    "resposta": "Liberdade do pensamento e conhecimento das ideias"
  },
  {
    "pergunta": "Para Sócrates, o conhecimento era algo que:",
    "opcoes": [
      "Deve ser imposto pelo professor",
      "Era adquirido através da virtude, que por sua vez, era adquirido por meio da autorreflexão e constante busca pela verdade",
      "Só é adquirido por meio de livros"
    ],
    "resposta": "Era adquirido através da virtude, que por sua vez, era adquirido por meio da autorreflexão e constante busca pela verdade"
  },
  {
    "pergunta": "Aristóteles afirmava que o conhecimento vem de:",
    "opcoes": [
      "Revelações divinas",
      "Experiências sensoriais e razão",
      "Tradições religiosas"
    ],
    "resposta": "Experiências sensoriais e razão"
  },
  {
    "pergunta": "Para Aristóteles, a educação deve desenvolver:",
    "opcoes": [
      "Apenas habilidades técnicas",
      "A ética, o raciocínio e a prática",
      "O instinto e o senso comum"
    ],
    "resposta": "A ética, o raciocínio e a prática"
  },
  {
    "pergunta": "A base do conhecimento, segundo Aristóteles, está em:",
    "opcoes": [
      "Imitar os deuses",
      "Questionar as leis",
      "Observar e compreender a realidade"
    ],
    "resposta": "Observar e compreender a realidade"
  },
  {
    "pergunta": "A ética na educação está diretamente ligada a:",
    "opcoes": [
      "Obrigar o aluno a seguir regras",
      "Ensinar valores morais e desenvolver a consciência crítica",
      "Aplicar punições sempre que necessário"
    ],
    "resposta": "Ensinar valores morais e desenvolver a consciência crítica"
  },
  {
    "pergunta": "O professor ético é aquele que:",
    "opcoes": [
      "Reproduz o conteúdo sem questionar",
      "Impõe suas ideias sem diálogo",
      "Forma cidadãos responsáveis e críticos"
    ],
    "resposta": "Forma cidadãos responsáveis e críticos"
  },
  {
    "pergunta": "A formação docente deve incluir:",
    "opcoes": [
      "Apenas conhecimento técnico",
      "Práticas autoritárias",
      "Reflexões filosóficas sobre sua atuação"
    ],
    "resposta": "Reflexões filosóficas sobre sua atuação"
  }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        escolha = request.form['escolha']
        correta = session['questoes'][session['indice']]['resposta']
        if escolha == correta:
            session['acertos'] += 1

        session['indice'] += 1

        if session['indice'] >= len(session['questoes']):
            return redirect(url_for('resultado'))

    if 'questoes' not in session:
        questoes = QUESTOES.copy()
        shuffle(questoes)
        session['questoes'] = questoes
        session['indice'] = 0
        session['acertos'] = 0

    pergunta_atual = session['questoes'][session['indice']]
    return render_template('quiz.html', pergunta=pergunta_atual, progresso=session['indice'] + 1, total=len(session['questoes']))

@app.route('/resultado')
def resultado():
    if 'questoes' not in session:
        return redirect(url_for('index'))

    total = len(session['questoes'])
    acertos = session.get('acertos', 0)
    # Limpa a sessão após o resultado
    session.clear()
    return render_template('resultado.html', total=total, acertos=acertos)

if __name__ == '__main__':
    app.run(debug=True)

const questions = [
  {
    question: "¿Cómo se llama el pez protagonista de 'Buscando a Nemo'?",
    options: ["Dory", "Nemo", "Marlin", "Bruce"],
    answer: "Nemo",
    hint: "Es el hijo de Marlin.",
    correctImg: "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-7s6a1e_113a937e.jpeg",
    villainImg: "https://static.wikia.nocookie.net/disney/images/e/ee/Darla_01.jpg", // Darla
  },
  {
    question: "¿Quién es el mejor amigo de Aladdín?",
    options: ["Abú", "Jafar", "Rajah", "Simba"],
    answer: "Abú",
    hint: "Es un mono muy travieso.",
    correctImg: "https://static.wikia.nocookie.net/disney/images/f/f3/Profile_-_Abu.jpeg",
    villainImg: "https://static.wikia.nocookie.net/disney/images/0/0e/Jafar_disney.png",
  },
  {
    question: "¿Cómo se llama la villana de '101 dálmatas'?",
    options: ["Úrsula", "Cruella", "Maléfica", "Gothel"],
    answer: "Cruella",
    hint: "Le encantan los abrigos de piel...",
    correctImg: "https://static.wikia.nocookie.net/disney/images/5/55/Pongo101.png", // Pongo (bueno)
    villainImg: "https://static.wikia.nocookie.net/disney/images/9/91/Cruella_2021.png",
  },
  {
    question: "¿Qué fruta causa el sueño de Blancanieves?",
    options: ["Naranja", "Plátano", "Manzana", "Fresa"],
    answer: "Manzana",
    hint: "Es roja y brillante...",
    correctImg: "https://static.wikia.nocookie.net/disney/images/b/b0/Snow_white_disney.png",
    villainImg: "https://static.wikia.nocookie.net/disney/images/f/f4/Evil_Queen_Disney.png",
  }
];

let currentQuestion = {};
let usedQuestions = [];

const questionEl = document.getElementById("question");
const optionsEl = document.getElementById("options");
const hintEl = document.getElementById("hint");
const resultImg = document.getElementById("character-img");
const feedbackEl = document.getElementById("feedback");
const nextBtn = document.getElementById("next-btn");

function loadQuestion() {
  if (usedQuestions.length === questions.length) {
    questionEl.innerText = "¡Juego terminado! 🏆";
    optionsEl.innerHTML = "";
    hintEl.innerText = "";
    nextBtn.style.display = "none";
    return;
  }

  resultImg.src = "";
  feedbackEl.innerText = "";
  nextBtn.style.display = "none";

  // Seleccionar pregunta aleatoria que no haya sido usada
  let randomIndex;
  do {
    randomIndex = Math.floor(Math.random() * questions.length);
  } while (usedQuestions.includes(randomIndex));

  usedQuestions.push(randomIndex);
  currentQuestion = questions[randomIndex];

  questionEl.innerText = currentQuestion.question;
  hintEl.innerText = "Pista: " + currentQuestion.hint;

  optionsEl.innerHTML = "";
  currentQuestion.options.forEach(option => {
    const btn = document.createElement("button");
    btn.innerText = option;
    btn.onclick = () => checkAnswer(option);
    optionsEl.appendChild(btn);
  });
}

function checkAnswer(selected) {
  const isCorrect = selected === currentQuestion.answer;
  resultImg.src = isCorrect ? currentQuestion.correctImg : currentQuestion.villainImg;
  feedbackEl.innerText = isCorrect ? "¡Correcto! 🎉" : "Incorrecto 😞";
  nextBtn.style.display = "inline-block";

  // Desactivar botones
  Array.from(optionsEl.children).forEach(btn => {
    btn.disabled = true;
    if (btn.innerText === currentQuestion.answer) {
      btn.style.backgroundColor = "#66bb6a"; // verde
    } else if (btn.innerText === selected) {
      btn.style.backgroundColor = "#ef5350"; // rojo
    }
  });
}

nextBtn.onclick = loadQuestion;

window.onload = loadQuestion;

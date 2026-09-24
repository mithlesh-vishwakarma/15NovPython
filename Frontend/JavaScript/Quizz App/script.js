// ==========================================================================
// QUIZ APP - CORE LOGIC & STATE MANAGEMENT
// ==========================================================================

// --------------------------------------------------------------------------
// 1) Question Repository
// --------------------------------------------------------------------------
const questions = [
  {
    id: 1,
    question: "Which keyword is used to declare a variable that can be reassigned?",
    options: ["const", "let", "static", "fixed"],
    answer: "let"
  },
  {
    id: 2,
    question: "Which keyword is used to declare a constant variable in JavaScript?",
    options: ["let", "var", "const", "constant"],
    answer: "const"
  },
  {
    id: 3,
    question: "Which keyword was traditionally used for variable declaration before ES6?",
    options: ["let", "var", "define", "variable"],
    answer: "var"
  },
  {
    id: 4,
    question: "What is the value of an uninitialized variable declared with let?",
    options: ["null", "0", "undefined", "false"],
    answer: "undefined"
  },
  {
    id: 5,
    question: "Which of the following is a valid JavaScript variable identifier?",
    options: ["2name", "user-name", "userName", "user name"],
    answer: "userName"
  },
  {
    id: 6,
    question: "Can a variable declared with let be reassigned in its scope?",
    options: ["Yes", "No", "Only once", "Only inside a function"],
    answer: "Yes"
  },
  {
    id: 7,
    question: "Can a variable declared with const be reassigned?",
    options: ["Yes", "No", "Only twice", "Only inside a block"],
    answer: "No"
  },
  {
    id: 8,
    question: "Which keyword introduces block scope in JavaScript?",
    options: ["var", "let", "Both var and let", "None"],
    answer: "let"
  },
  {
    id: 9,
    question: "Which keyword has function scope rather than block scope?",
    options: ["let", "const", "var", "static"],
    answer: "var"
  },
  {
    id: 10,
    question: "What happens when you access a let variable before its declaration line?",
    options: [
      "It returns undefined",
      "It returns null",
      "ReferenceError (Temporal Dead Zone)",
      "It returns 0"
    ],
    answer: "ReferenceError (Temporal Dead Zone)"
  },
  {
    id: 11,
    question: "What is the value of x after: let x = 10; x = 20;?",
    options: ["10", "20", "undefined", "SyntaxError"],
    answer: "20"
  },
  {
    id: 12,
    question: "What is the result of executing: const x = 10; x = 20;?",
    options: ["20", "10", "undefined", "TypeError"],
    answer: "TypeError"
  },
  {
    id: 13,
    question: "Which casing convention is standard for JavaScript variable and function names?",
    options: ["snake_case", "camelCase", "PascalCase", "kebab-case"],
    answer: "camelCase"
  },
  {
    id: 14,
    question: "Which characters can be placed at the very start of a JavaScript variable name?",
    options: ["$", "_", "Both $ and _", "#"],
    answer: "Both $ and _"
  },
  {
    id: 15,
    question: "Can JavaScript variable names contain digits?",
    options: [
      "Yes, anywhere in the name",
      "Yes, but not as the first character",
      "No, never",
      "Only at the beginning"
    ],
    answer: "Yes, but not as the first character"
  },
  {
    id: 16,
    question: "Which of the following variable declarations is syntactically valid?",
    options: [
      "let 1name = 'John'",
      "let first-name = 'John'",
      "let firstName = 'John'",
      "let first name = 'John'"
    ],
    answer: "let firstName = 'John'"
  },
  {
    id: 17,
    question: "What is the scope of a variable declared inside an if-block using let?",
    options: ["Global", "Function", "Block scope", "Module scope only"],
    answer: "Block scope"
  },
  {
    id: 18,
    question: "What does variable hoisting refer to in JavaScript?",
    options: [
      "Deleting unused variables",
      "Moving declarations conceptually to the top of scope",
      "Converting data types automatically",
      "Securing constants in memory"
    ],
    answer: "Moving declarations conceptually to the top of scope"
  },
  {
    id: 19,
    question: "What value does an unassigned variable declared with var hold?",
    options: ["null", "undefined", "false", "0"],
    answer: "undefined"
  },
  {
    id: 20,
    question: "Which declaration is recommended by modern standards when a variable should not be reassigned?",
    options: ["var", "let", "const", "static"],
    answer: "const"
  },
  {
    id: 21,
    question: "What is an object in JavaScript fundamentally?",
    options: [
      "A collection of key-value pairs",
      "An immutable primitive number",
      "A loop iteration control structure",
      "A keyword used for declaring functions"
    ],
    answer: "A collection of key-value pairs"
  },
  {
    id: 22,
    question: "Which syntax creates an object literal?",
    options: ["[]", "()", "{}", "<>"],
    answer: "{}"
  },
  {
    id: 23,
    question: "Which of the following is valid JavaScript object syntax?",
    options: [
      "{ name: 'John' }",
      "[ name: 'John' ]",
      "( name: 'John' )",
      "<name: 'John'>"
    ],
    answer: "{ name: 'John' }"
  },
  {
    id: 24,
    question: "How do you access the name property of an object called user?",
    options: [
      "user->name",
      "user.name",
      "user::name",
      "user/name"
    ],
    answer: "user.name"
  },
  {
    id: 25,
    question: "How can you access a property dynamically using bracket notation on user?",
    options: [
      "user[prop]",
      "user(prop)",
      "user{prop}",
      "user->prop"
    ],
    answer: "user[prop]"
  },
  {
    id: 26,
    question: "What are the keys in standard JavaScript object properties?",
    options: [
      "Strings or Symbols",
      "Booleans only",
      "Numbers only",
      "Arrays only"
    ],
    answer: "Strings or Symbols"
  }
];

// --------------------------------------------------------------------------
// 2) DOM Element References
// --------------------------------------------------------------------------
const StartScreen = document.getElementById("start-screen");
const QuizScreen = document.getElementById("quiz-screen");
const ResultScreen = document.getElementById("result-screen");

// Start screen elements
const StartQuizBtn = document.getElementById("start-btn");
const TotalQuestionsRule = document.getElementById("total-questions-rule");

// Quiz screen elements
const QuestionNumber = document.getElementById("question-number");
const TimerElement = document.getElementById("timer");
const TimerBadge = document.querySelector(".timer-badge");
const ProgressBar = document.getElementById("progress-bar");
const QuestionNavigator = document.getElementById("question-navigator");
const QuestionContainer = document.getElementById("question");
const OptionsContainer = document.getElementById("options-container");
const PreviousBtn = document.getElementById("previous-btn");
const NextBtn = document.getElementById("next-btn");
const SkipBtn = document.getElementById("skip-btn");

// Result screen elements
const TotalResult = document.getElementById("total-result");
const AnsweredResult = document.getElementById("answered-result");
const SkippedResult = document.getElementById("skipped-result");
const CorrectResult = document.getElementById("correct-result");
const WrongResult = document.getElementById("wrong-result");

const ScorePercentage = document.getElementById("score-percentage");
const ScorePoints = document.getElementById("score-points");
const ScoreMax = document.getElementById("score-max");
const ScoreRingFill = document.getElementById("score-ring-fill");
const ScoreGradeBadge = document.getElementById("score-grade-badge");
const ResultTrophy = document.getElementById("result-trophy");
const ResultTitle = document.getElementById("result-title");
const ResultFeedback = document.getElementById("result-feedback");

const ReviewFilters = document.getElementById("review-filters");
const FilterCountAll = document.getElementById("filter-count-all");
const FilterCountCorrect = document.getElementById("filter-count-correct");
const FilterCountWrong = document.getElementById("filter-count-wrong");
const FilterCountSkipped = document.getElementById("filter-count-skipped");
const ReviewContainer = document.getElementById("review-container");
const RestartBtn = document.getElementById("restart-btn");

// --------------------------------------------------------------------------
// 3) App State
// --------------------------------------------------------------------------
const TOTAL_QUIZ_QUESTIONS = 20;
const TOTAL_TIME_SECONDS = 20 * 60; // 20 minutes

let currentQuestionIndex = 0;
let quizQuestions = [];
let userAnswers = []; // null = unvisited, -1 = skipped, index = selected option index
let timeLeft = TOTAL_TIME_SECONDS;
let timerInterval = null;
let currentReviewFilter = "all";

// --------------------------------------------------------------------------
// 4) Helper & Setup Functions
// --------------------------------------------------------------------------

// Fisher-Yates shuffle algorithm for truly random question selection
function getShuffledQuizQuestions(count = TOTAL_QUIZ_QUESTIONS) {
  const pool = [...questions];
  for (let i = pool.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [pool[i], pool[j]] = [pool[j], pool[i]];
  }
  return pool.slice(0, Math.min(count, pool.length));
}

// Format seconds into MM:SS format
function formatTime(totalSeconds) {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}

// Update the timer UI and toggle urgency alert styles
function updateTimerDisplay() {
  TimerElement.textContent = formatTime(timeLeft);

  if (TimerBadge) {
    if (timeLeft <= 60) {
      TimerBadge.classList.add("danger");
    } else {
      TimerBadge.classList.remove("danger");
    }
  }
}

// Start countdown interval
function startTimer() {
  clearInterval(timerInterval);
  updateTimerDisplay();

  timerInterval = setInterval(() => {
    timeLeft--;

    if (timeLeft <= 0) {
      timeLeft = 0;
      updateTimerDisplay();
      clearInterval(timerInterval);
      showResult();
      return;
    }

    updateTimerDisplay();
  }, 1000);
}

// Render the quick-jump question navigator pills
function renderQuestionNavigator() {
  if (!QuestionNavigator) return;
  QuestionNavigator.innerHTML = "";

  quizQuestions.forEach((_, index) => {
    const pill = document.createElement("button");
    pill.classList.add("nav-pill");
    pill.type = "button";
    pill.textContent = index + 1;
    pill.title = `Jump to question ${index + 1}`;

    const answer = userAnswers[index];
    if (index === currentQuestionIndex) {
      pill.classList.add("current");
    } else if (answer === -1) {
      pill.classList.add("skipped");
    } else if (answer !== null) {
      pill.classList.add("answered");
    }

    pill.addEventListener("click", () => {
      currentQuestionIndex = index;
      showQuestions();
    });

    QuestionNavigator.appendChild(pill);
  });

  // Ensure current pill is scrolled smoothly into view
  const currentPill = QuestionNavigator.querySelector(".nav-pill.current");
  if (currentPill) {
    currentPill.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
  }
}

// Display the current active question, options, and progress bar
function showQuestions() {
  const currentQuestion = quizQuestions[currentQuestionIndex];
  if (!currentQuestion) return;

  // 1. Question Number & Progress Bar
  QuestionNumber.textContent = `${currentQuestionIndex + 1} / ${quizQuestions.length}`;
  const progressPercent = ((currentQuestionIndex + 1) / quizQuestions.length) * 100;
  if (ProgressBar) {
    ProgressBar.style.width = `${progressPercent}%`;
  }

  // 2. Question Text
  QuestionContainer.textContent = currentQuestion.question;

  // 3. Option Buttons
  OptionsContainer.innerHTML = "";
  const selectedIndex = userAnswers[currentQuestionIndex];

  currentQuestion.options.forEach((optionText, optionIdx) => {
    const optionBtn = document.createElement("button");
    optionBtn.classList.add("option");
    optionBtn.type = "button";

    if (selectedIndex === optionIdx) {
      optionBtn.classList.add("selected");
    }

    const labelChar = String.fromCharCode(65 + optionIdx); // A, B, C, D

    optionBtn.innerHTML = `
      <span class="option-label">${labelChar}</span>
      <span class="option-text">${optionText}</span>
    `;

    optionBtn.addEventListener("click", () => {
      userAnswers[currentQuestionIndex] = optionIdx;
      showQuestions();
    });

    OptionsContainer.appendChild(optionBtn);
  });

  // 4. Navigation Buttons State
  PreviousBtn.disabled = currentQuestionIndex === 0;

  if (currentQuestionIndex === quizQuestions.length - 1) {
    NextBtn.innerHTML = `
      <span>Finish Quiz</span>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
        <polyline points="22 4 12 14.01 9 11.01"></polyline>
      </svg>
    `;
  } else {
    NextBtn.innerHTML = `
      <span>Next</span>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="9 18 15 12 9 6"></polyline>
      </svg>
    `;
  }

  // 5. Update Navigator Pills
  renderQuestionNavigator();
}

// --------------------------------------------------------------------------
// 5) Quiz Lifecycle Functions
// --------------------------------------------------------------------------

// Start or restart a fresh quiz session
function startQuiz() {
  currentQuestionIndex = 0;
  quizQuestions = getShuffledQuizQuestions(TOTAL_QUIZ_QUESTIONS);
  userAnswers = new Array(quizQuestions.length).fill(null);
  timeLeft = TOTAL_TIME_SECONDS;

  // Screen visibility
  StartScreen.style.display = "none";
  QuizScreen.style.display = "flex";
  ResultScreen.style.display = "none";

  if (TimerBadge) {
    TimerBadge.classList.remove("danger");
  }

  startTimer();
  showQuestions();
}

// Previous question handler
function goPrevious() {
  if (currentQuestionIndex > 0) {
    currentQuestionIndex--;
    showQuestions();
  }
}

// Next question or finish quiz handler
function goNext() {
  if (currentQuestionIndex < quizQuestions.length - 1) {
    currentQuestionIndex++;
    showQuestions();
  } else {
    showResult();
  }
}

// Skip current question handler
function skipQuestion() {
  // If user hasn't selected an option, mark as skipped (-1)
  if (userAnswers[currentQuestionIndex] === null) {
    userAnswers[currentQuestionIndex] = -1;
  }

  if (currentQuestionIndex < quizQuestions.length - 1) {
    currentQuestionIndex++;
    showQuestions();
  } else {
    showResult();
  }
}

// Render Review Cards according to active filter
function renderReviewCards(filter = "all") {
  ReviewContainer.innerHTML = "";

  quizQuestions.forEach((question, index) => {
    const selectedIdx = userAnswers[index];
    const isSkipped = selectedIdx === null || selectedIdx === -1;
    const isCorrect = !isSkipped && question.options[selectedIdx] === question.answer;

    // Filter check
    if (filter === "correct" && !isCorrect) return;
    if (filter === "wrong" && (isCorrect || isSkipped)) return;
    if (filter === "skipped" && !isSkipped) return;

    let statusClass = "skipped";
    let statusText = "Skipped";
    let userAnswerText = "No answer provided";
    let userValClass = "user-skipped";

    if (!isSkipped) {
      if (isCorrect) {
        statusClass = "correct";
        statusText = "Correct";
        userAnswerText = question.options[selectedIdx];
        userValClass = "user-correct";
      } else {
        statusClass = "wrong";
        statusText = "Incorrect";
        userAnswerText = question.options[selectedIdx];
        userValClass = "user-wrong";
      }
    }

    const card = document.createElement("div");
    card.classList.add("review-card");
    card.innerHTML = `
      <div class="review-card-header">
        <h3>Question ${index + 1}: ${question.question}</h3>
        <span class="review-status-badge ${statusClass}">${statusText}</span>
      </div>
      <div class="review-answers">
        <div class="review-answer-row">
          <span class="answer-label">Your Answer:</span>
          <span class="answer-value ${userValClass}">${userAnswerText}</span>
        </div>
        <div class="review-answer-row">
          <span class="answer-label">Correct Answer:</span>
          <span class="answer-value correct-answer">${question.answer}</span>
        </div>
      </div>
    `;

    ReviewContainer.appendChild(card);
  });

  if (ReviewContainer.children.length === 0) {
    ReviewContainer.innerHTML = `
      <div style="text-align: center; padding: 30px; color: var(--slate-400);">
        No questions match the "${filter}" filter.
      </div>
    `;
  }
}

// Calculate score and show the final result screen
function showResult() {
  clearInterval(timerInterval);

  QuizScreen.style.display = "none";
  ResultScreen.style.display = "flex";

  let correctCount = 0;
  let wrongCount = 0;
  let skippedCount = 0;

  quizQuestions.forEach((question, index) => {
    const selectedIdx = userAnswers[index];
    if (selectedIdx === null || selectedIdx === -1) {
      skippedCount++;
    } else if (question.options[selectedIdx] === question.answer) {
      correctCount++;
    } else {
      wrongCount++;
    }
  });

  const total = quizQuestions.length;
  const answeredCount = correctCount + wrongCount;
  const scorePercent = Math.round((correctCount / total) * 100);

  // Statistics numbers
  TotalResult.textContent = total;
  AnsweredResult.textContent = answeredCount;
  SkippedResult.textContent = skippedCount;
  CorrectResult.textContent = correctCount;
  WrongResult.textContent = wrongCount;

  // Circular Score Gauge
  ScorePoints.textContent = correctCount;
  ScoreMax.textContent = total;
  ScorePercentage.textContent = `${scorePercent}%`;

  const circumference = 2 * Math.PI * 50; // r=50 -> 314.159
  const offset = circumference - (scorePercent / 100) * circumference;
  if (ScoreRingFill) {
    ScoreRingFill.style.strokeDashoffset = offset;
  }

  // Grade badge & trophy feedback
  if (scorePercent >= 90) {
    ResultTrophy.textContent = "🏆";
    ResultTitle.textContent = "Outstanding Performance!";
    ResultFeedback.textContent = "You've mastered these JavaScript concepts with flying colors!";
    ScoreGradeBadge.textContent = "Mastery Level 🌟";
    ScoreGradeBadge.style.background = "var(--success-light)";
    ScoreGradeBadge.style.color = "var(--success)";
  } else if (scorePercent >= 75) {
    ResultTrophy.textContent = "🎉";
    ResultTitle.textContent = "Great Job!";
    ResultFeedback.textContent = "Solid understanding of JavaScript variables, types, and objects.";
    ScoreGradeBadge.textContent = "High Achiever 🎯";
    ScoreGradeBadge.style.background = "var(--primary-light)";
    ScoreGradeBadge.style.color = "var(--primary)";
  } else if (scorePercent >= 50) {
    ResultTrophy.textContent = "👍";
    ResultTitle.textContent = "Good Effort!";
    ResultFeedback.textContent = "You're on the right track! Review the incorrect answers below.";
    ScoreGradeBadge.textContent = "Passing Grade 📚";
    ScoreGradeBadge.style.background = "var(--info-light)";
    ScoreGradeBadge.style.color = "var(--info)";
  } else {
    ResultTrophy.textContent = "💪";
    ResultTitle.textContent = "Keep Practicing!";
    ResultFeedback.textContent = "Don't worry! Review the detailed answers below and try again.";
    ScoreGradeBadge.textContent = "Needs Practice 🌱";
    ScoreGradeBadge.style.background = "var(--warning-light)";
    ScoreGradeBadge.style.color = "#b45309";
  }

  // Filter counters
  FilterCountAll.textContent = total;
  FilterCountCorrect.textContent = correctCount;
  FilterCountWrong.textContent = wrongCount;
  FilterCountSkipped.textContent = skippedCount;

  // Render initial review
  currentReviewFilter = "all";
  if (ReviewFilters) {
    ReviewFilters.querySelectorAll(".filter-btn").forEach(btn => {
      btn.classList.toggle("active", btn.dataset.filter === "all");
    });
  }
  renderReviewCards("all");
}

// Reset quiz state and return to start screen
function restartQuiz() {
  clearInterval(timerInterval);

  ResultScreen.style.display = "none";
  QuizScreen.style.display = "none";
  StartScreen.style.display = "flex";

  currentQuestionIndex = 0;
  quizQuestions = [];
  userAnswers = [];
  timeLeft = TOTAL_TIME_SECONDS;

  if (TimerBadge) {
    TimerBadge.classList.remove("danger");
  }

  updateTimerDisplay();
}

// --------------------------------------------------------------------------
// 6) Event Listeners Setup
// --------------------------------------------------------------------------
StartQuizBtn.addEventListener("click", startQuiz);
PreviousBtn.addEventListener("click", goPrevious);
NextBtn.addEventListener("click", goNext);
SkipBtn.addEventListener("click", skipQuestion);
RestartBtn.addEventListener("click", restartQuiz);

// Filter buttons in Review section
if (ReviewFilters) {
  ReviewFilters.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-btn");
    if (!btn) return;

    ReviewFilters.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    currentReviewFilter = btn.dataset.filter;
    renderReviewCards(currentReviewFilter);
  });
}

// Keyboard shortcuts for improved usability (1-4 or A-D to select, Enter for next, etc.)
document.addEventListener("keydown", (e) => {
  // Only process keyboard shortcuts when quiz screen is active
  if (QuizScreen.style.display !== "flex") return;

  const key = e.key.toUpperCase();
  if (["A", "B", "C", "D"].includes(key)) {
    const idx = key.charCodeAt(0) - 65;
    const currentQ = quizQuestions[currentQuestionIndex];
    if (currentQ && currentQ.options[idx] !== undefined) {
      userAnswers[currentQuestionIndex] = idx;
      showQuestions();
    }
  } else if (["1", "2", "3", "4"].includes(key)) {
    const idx = parseInt(key) - 1;
    const currentQ = quizQuestions[currentQuestionIndex];
    if (currentQ && currentQ.options[idx] !== undefined) {
      userAnswers[currentQuestionIndex] = idx;
      showQuestions();
    }
  } else if (e.key === "ArrowRight") {
    goNext();
  } else if (e.key === "ArrowLeft" && currentQuestionIndex > 0) {
    goPrevious();
  }
});

// Initial display setup
if (TotalQuestionsRule) {
  TotalQuestionsRule.textContent = TOTAL_QUIZ_QUESTIONS;
}
updateTimerDisplay();

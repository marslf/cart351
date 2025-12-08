const grid = document.getElementById("slime-grid");
const scoreDisplay = document.getElementById("score");
const restartBtn = document.getElementById("restart-btn");

let score = 0;
let activeSlime = null;
let gameInterval;

// Create 9 slime holes
for (let i = 0; i < 9; i++) {
    const hole = document.createElement("div");
    hole.classList.add("slime-hole");

    const slime = document.createElement("div");
    slime.classList.add("slime");
    slime.textContent = "😈";

    slime.addEventListener("click", () => {
        if (slime.style.display === "flex") {
            score++;
            scoreDisplay.textContent = "Score: " + score;
            slime.style.display = "none";
        }
    });

    hole.appendChild(slime);
    grid.appendChild(hole);
}

function randomSlime() {
    const slimes = document.querySelectorAll(".slime");
    if (activeSlime) activeSlime.style.display = "none";

    activeSlime = slimes[Math.floor(Math.random() * slimes.length)];
    activeSlime.style.display = "flex";
}

function startGame() {
    score = 0;
    scoreDisplay.textContent = "Score: 0";
    clearInterval(gameInterval);
    gameInterval = setInterval(randomSlime, 800);
}

restartBtn.addEventListener("click", startGame);

startGame();

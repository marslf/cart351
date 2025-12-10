const bug = document.getElementById("ladybug");

// starting state
let x = window.innerWidth / 2;
let y = window.innerHeight / 2;
let angle = 0;

// random wandering movement function
function wander() {
    if (Math.random() < 0.02) return setTimeout(wander, 500); // short pause sometimes

    angle += (Math.random() - 0.5) * 60; // turn a little randomly

    // move forward in current angle
    const speed = 2 + Math.random() * 1;
    x += Math.sin(angle * Math.PI / 180) * speed;
    y -= Math.cos(angle * Math.PI / 180) * speed;

    // keep bug inside screen
    if (x < 0) x = 0;
    if (x > window.innerWidth - 50) x = window.innerWidth - 50;
    if (y < 0) y = 0;
    if (y > window.innerHeight - 50) y = window.innerHeight - 50;

    // apply visual movement + rotation
    bug.style.left = x + "px";
    bug.style.top = y + "px";
    bug.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;

    requestAnimationFrame(wander);
}

wander();

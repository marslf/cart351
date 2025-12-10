const bee = document.getElementById("bee");

let bx = window.innerWidth / 2 + 100;
let by = window.innerHeight / 2 - 100;
let bAngle = 0;

let hoverOffset = 0;
let hoverDirection = 1;

let driftAngle = Math.random() * 360;

function buzz() {
    hoverOffset += hoverDirection * 0.2;
    if (hoverOffset > 3 || hoverOffset < -3) hoverDirection *= -1;

    if (Math.random() < 0.01) {
        driftAngle += (Math.random() - 0.5) * 50;
    }

    if (Math.random() < 0.005) {
        driftAngle += (Math.random() - 0.5) * 100;
    }

    // movement speed 
    const speed = 1.4;
    bx += Math.sin(driftAngle * Math.PI / 180) * speed;
    by -= Math.cos(driftAngle * Math.PI / 180) * speed;

    bAngle += (driftAngle - bAngle) * 0.05;

    // keep bee onscreen
    const margin = 40;
    if (bx < margin || bx > window.innerWidth - margin ||
        by < margin || by > window.innerHeight - margin) {
        driftAngle += 150;
    }

    // apply movement + hover + rotation
    bee.style.left = bx + "px";
    bee.style.top = (by + hoverOffset) + "px";
    bee.style.transform = `translate(-50%, -50%) rotate(${bAngle}deg)`;

    requestAnimationFrame(buzz);
}

buzz();

// 1 - Get pond and message elements
const pondEl = document.querySelector('.pond');
const pondMsg = document.getElementById('pond-msg');

// 2 - Fetch all creatures from server
fetch('/getCreatures')
    .then(res => res.json())
    .then(data => {
        const creatures = data.creatures || [];
        console.log('Loaded creatures:', creatures);
        creatures.forEach(placeCreature);
    })
    .catch(err => console.error('Error fetching creatures:', err));

// 3 - Function: place one creature in the pond
function placeCreature(creature) {
    const el = document.createElement('div');
    el.classList.add('creature', creature.type);
    el.style.position = 'absolute';

    // Create and set the image
    const img = document.createElement('img');

    const imageMap = {
        frog: 'frog.png',
        tadpole: 'tadpole.png',
        fish: Math.random() < 0.5 ? 'fish1.png' : 'fish2.png',
        bug: (() => {
            const options = ['bee.png', 'butterfly.png', 'moth.png', 'dragonfly.png'];
            return options[Math.floor(Math.random() * options.length)];
        })()
    };

    const filename = imageMap[creature.type] || 'frog.png';
    img.src = `/static/images/${filename}`;
    img.style.width = '60px';
    img.style.height = 'auto';
    img.style.display = 'block';
    img.style.position = 'relative';
    img.style.zIndex = '1';
    img.style.transition = 'transform 0.4s ease'; // smooth flip

    // Info bubble 
    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    bubble.innerHTML = `<strong>${creature.name}</strong><br>${creature.message || ''}`;
    el.appendChild(bubble);

    // Color filter
    if (creature.color) {
        const tint = document.createElement('div');
        tint.style.position = 'absolute';
        tint.style.top = '0';
        tint.style.left = '0';
        tint.style.width = '100%';
        tint.style.height = '100%';
        tint.style.backgroundColor = creature.color;
        tint.style.opacity = '0.35';
        tint.style.mixBlendMode = 'multiply';
        tint.style.borderRadius = '50%';
        el.appendChild(tint);
    }

    el.appendChild(img);

    // Random starting position 
    const pad = 40;
    let x = Math.random() * (pondEl.clientWidth - pad * 2);
    let y = Math.random() * (pondEl.clientHeight - pad * 2);
    el.style.left = x + 'px';
    el.style.top = y + 'px';

    // Click = show name 
    el.addEventListener('click', () => {
        pondMsg.textContent = `${creature.name} the ${creature.type}`;
        setTimeout(() => (pondMsg.textContent = ''), 2000);
    });

    pondEl.appendChild(el);

    // MOVEMENT (unique to each creature type)
    if (creature.type === 'frog') hopAround(el, img);
    else if (creature.type === 'tadpole') swimCircle(el, img);
    else if (creature.type === 'fish') swimZigzag(el, img);
    else if (creature.type === 'bug') flutter(el, img);
}

// Frog hops randomly
function hopAround(el, img) {
    setInterval(() => {
        const x = Math.random() * (pondEl.clientWidth - 60);
        const y = Math.random() * (pondEl.clientHeight - 60);
        el.style.transition = 'transform 0.3s ease, left 0.8s ease, top 0.8s ease';
        el.style.transform = 'translateY(-20px)';
        setTimeout(() => {
            el.style.left = `${x}px`;
            el.style.top = `${y}px`;
            el.style.transform = 'translateY(0)';
        }, 300);
    }, 3000);
}

// Tadpoles swim in circles
function swimCircle(el, img) {
    let angle = Math.random() * Math.PI * 2;
    const radius = 40 + Math.random() * 40;
    const centerX = parseFloat(el.style.left);
    const centerY = parseFloat(el.style.top);

    setInterval(() => {
        angle += 0.05;
        const newX = centerX + Math.cos(angle) * radius;
        const newY = centerY + Math.sin(angle) * radius;
        el.style.left = newX + 'px';
        el.style.top = newY + 'px';

        if (Math.cos(angle) < 0) img.style.transform = 'scaleX(-1)';
        else img.style.transform = 'scaleX(1)';
    }, 60);
}

// Fish zigzag
function swimZigzag(el, img) {
    let dir = 1;
    let x = parseFloat(el.style.left);
    let y = parseFloat(el.style.top);

    setInterval(() => {
        x += dir * (3 + Math.random() * 2);
        y += Math.sin(x / 20) * 2;
        el.style.left = x + 'px';
        el.style.top = y + 'px';

        if (dir > 0) img.style.transform = 'scaleX(-1)';
        else img.style.transform = 'scaleX(1)';

        if (x < 0 || x > pondEl.clientWidth - 60) dir *= -1;
    }, 40);
}

// Bug flutter 
function flutter(el, img) {
    let angle = Math.random() * Math.PI * 2;
    const radius = 40 + Math.random() * 40;
    const centerX = parseFloat(el.style.left);
    const centerY = parseFloat(el.style.top);

    function move() {
        angle += 0.02; 
        const newX = centerX + Math.cos(angle) * radius;
        const newY = centerY + Math.sin(angle) * radius;
        el.style.left = newX + 'px';
        el.style.top = newY + 'px';
        requestAnimationFrame(move);
    }
    move();
}

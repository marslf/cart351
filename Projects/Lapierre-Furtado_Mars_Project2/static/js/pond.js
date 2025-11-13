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

        // Update stats panel
        updateStats(creatures);
    })
    .catch(err => console.error('Error fetching creatures:', err));

//2- calculate stats and update list
function updateStats(creatures) {
    const statsList = document.getElementById('stats-list');

    const total = creatures.length;
    const frogs = creatures.filter(c => c.type === 'frog').length;
    const tadpoles = creatures.filter(c => c.type === 'tadpole').length;
    const fish = creatures.filter(c => c.type === 'fish').length;
    const bugs = creatures.filter(c => c.type === 'bug').length;
    const withMessages = creatures.filter(c => c.message && c.message.trim() !== '').length;

    statsList.innerHTML = `
        <li>Total critters: ${total}</li>
        <li>Frogs: ${frogs}</li>
        <li>Tadpoles: ${tadpoles}</li>
        <li>Fish: ${fish}</li>
        <li>Bugs: ${bugs}</li>
        <li>With messages: ${withMessages}</li>
    `;
}

// 3 - place  creature in the pond
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

// drag and drop creatures
pondEl.addEventListener('mousedown', (e) => {
    const target = e.target.closest('.creature');
    if (!target) return;

    e.preventDefault();

    // Store starting position of mouse and element
    const startX = e.clientX;
    const startY = e.clientY;
    let origLeft = parseFloat(target.style.left);
    let origTop = parseFloat(target.style.top);

    // Get movement type
    const type = Array.from(target.classList).find(c => ['frog', 'tadpole', 'fish', 'bug'].includes(c));

    // Update internal movement variables if necessary
    let circleData = target._circleData || {};
    let zigzagData = target._zigzagData || {};
    let flutterData = target._flutterData || {};

    function onMouseMove(moveEvent) {
        const dx = moveEvent.clientX - startX;
        const dy = moveEvent.clientY - startY;
        target.style.left = origLeft + dx + 'px';
        target.style.top = origTop + dy + 'px';

        // Update internal movement coordinates
        if (type === 'tadpole') {
            circleData.centerX = origLeft + dx;
            circleData.centerY = origTop + dy;
            target._circleData = circleData;
        } else if (type === 'fish') {
            zigzagData.x = origLeft + dx;
            zigzagData.y = origTop + dy;
            target._zigzagData = zigzagData;
        } else if (type === 'bug') {
            flutterData.x = origLeft + dx;
            flutterData.y = origTop + dy;
            target._flutterData = flutterData;
        }
    }

    function onMouseUp() {
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
        origLeft = parseFloat(target.style.left);
        origTop = parseFloat(target.style.top);
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
});

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
    let centerX = parseFloat(el.style.left);
    let centerY = parseFloat(el.style.top);

    el._circleData = { centerX, centerY };

    setInterval(() => {
        angle += 0.05;
        centerX = el._circleData.centerX;
        centerY = el._circleData.centerY;
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

    el._zigzagData = { x, y, dir };

    setInterval(() => {
        x = el._zigzagData.x;
        y = el._zigzagData.y;
        dir = el._zigzagData.dir;

        x += dir * (3 + Math.random() * 2);
        y += Math.sin(x / 20) * 2;

        el.style.left = x + 'px';
        el.style.top = y + 'px';

        if (dir > 0) img.style.transform = 'scaleX(-1)';
        else img.style.transform = 'scaleX(1)';

        if (x < 0 || x > pondEl.clientWidth - 60) dir *= -1;

        el._zigzagData.x = x;
        el._zigzagData.y = y;
        el._zigzagData.dir = dir;
    }, 40);
}

// Bug flutter 
function flutter(el, img) {
    el._flutterData = {
        x: parseFloat(el.style.left),
        y: parseFloat(el.style.top)
    };
    el._isDragging = false;

    function moveToNext() {
        // don't start a new move while dragging
        if (el._isDragging) {
            setTimeout(moveToNext, 50); // check again shortly
            return;
        }

        let x = el._flutterData.x;
        let y = el._flutterData.y;

        const targetX = x + (Math.random() - 0.5) * 80;
        const targetY = y + (Math.random() - 0.5) * 80;
        const duration = 1000 + Math.random() * 500;

        const start = performance.now();
        function animate(now) {
            // if drag starts mid-animation, stop this cycle
            if (el._isDragging) return;

            const t = Math.min((now - start) / duration, 1);
            el.style.left = x + (targetX - x) * t + 'px';
            el.style.top = y + (targetY - y) * t + 'px';

            el._flutterData.x = parseFloat(el.style.left);
            el._flutterData.y = parseFloat(el.style.top);

            if (t < 1) requestAnimationFrame(animate);
            else moveToNext();
        }
        requestAnimationFrame(animate);
    }

    moveToNext();

    // Handle drag state
    el.addEventListener('mousedown', () => el._isDragging = true);
    document.addEventListener('mouseup', () => el._isDragging = false);
}
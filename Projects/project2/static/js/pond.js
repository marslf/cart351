// 1- Get pond and message elements
const pondEl = document.querySelector('.pond');
const pondMsg = document.getElementById('pond-msg');

// 2- Fetch all creatures from server
fetch('/getCreatures')
    .then(res => res.json())
    .then(data => {
        const creatures = data.creatures || [];
        console.log('Loaded creatures:', creatures);
        creatures.forEach(placeCreature);
    })
    .catch(err => console.error('Error fetching creatures:', err));

// 3- Function: place one creature in the pond
function placeCreature(creature, index) {
    const el = document.createElement('div');
    el.classList.add('creature', creature.type);

    //Create and set the image
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

    // Create info bubble
    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    bubble.innerHTML = `<strong>${creature.name}</strong><br>${creature.message || ''}`;
    el.appendChild(bubble);

    // COLOR FILTER LAYER
    if (creature.color) {
        const tint = document.createElement('div');
        tint.style.position = 'absolute';
        tint.style.top = '0';
        tint.style.left = '0';
        tint.style.width = '100%';
        tint.style.height = '100%';
        tint.style.backgroundColor = creature.color;
        tint.style.opacity = '0.35'; // translucent color filter
        tint.style.mixBlendMode = 'multiply'; // keep transparency
        tint.style.borderRadius = '50%';
        el.appendChild(tint);
    }

    // Add image last so tint overlays correctly
    el.appendChild(img);

    // Random position inside pond 
    const pad = 40;
    const x = Math.random() * (pondEl.clientWidth - pad * 2);
    const y = Math.random() * (pondEl.clientHeight - pad * 2);
    el.style.left = x + 'px';
    el.style.top = y + 'px';

    // Click: show name briefly 
    el.addEventListener('click', () => {
        pondMsg.textContent = `${creature.name} the ${creature.type}`;
        setTimeout(() => (pondMsg.textContent = ''), 2000);
    });

    pondEl.appendChild(el);
}

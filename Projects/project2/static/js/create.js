// Get DOM elements
const typeEl = document.getElementById('ctype');
const nameEl = document.getElementById('cname');
const colorEl = document.getElementById('ccolor');
const messageEl = document.getElementById('cmessage');
const saveBtn = document.getElementById('saveBtn');
const msgEl = document.getElementById('create-msg');
const goPondBtn = document.getElementById('goPondBtn');

//Click handler: send creature to server
saveBtn.addEventListener('click', () => {
    const creature = {
        type: typeEl.value,
        name: nameEl.value.trim() || 'anonymous',
        color: colorEl.value || null,
        message: messageEl.value.trim().substring(0, 25) || ''
    };

    // POST via fetch
    fetch('/postCreature', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(creature)
    })
        .then(res => res.json())
        .then(data => {
            msgEl.textContent = data.message + ` (Total critters: ${data.count})`;
            nameEl.value = '';
            messageEl.value = ''; // 
            setTimeout(() => msgEl.textContent = '', 3000);
        })
        .catch(err => {
            msgEl.textContent = 'Error saving critter';
            console.error(err);
        });
});

goPondBtn.addEventListener('click', () => {
    // go to the pond page
    window.location.href = '/pond';
});
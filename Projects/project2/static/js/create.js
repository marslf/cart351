// static/js/create.js
// Get DOM elements
const typeEl = document.getElementById('ctype');
const nameEl = document.getElementById('cname');
const colorEl = document.getElementById('ccolor');
const saveBtn = document.getElementById('saveBtn');
const msgEl = document.getElementById('create-msg');

//Click handler: send creature to server
saveBtn.addEventListener('click', () => {
    const creature = {
        type: typeEl.value,
        name: nameEl.value.trim() || 'anonymous',
        color: colorEl.value || null
    };

    // POST via fetch
    fetch('/postCreature', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(creature)
    })
        .then(res => res.json())
        .then(data => {
            // Show simple confirmation and clear name
            msgEl.textContent = data.message + ` (Total creatures: ${data.count})`;
            nameEl.value = '';
            //small auto-clear
            setTimeout(() => msgEl.textContent = '', 3000);
        })
        .catch(err => {
            msgEl.textContent = 'Error saving creature';
            console.error(err);
        });
});

const grid = document.getElementById('grid-container');

// 1. Load existing data from Python when page opens
fetch('/get_data')
    .then(res => res.json())
    .then(savedDays => {
        renderGrid(savedDays);
    });

function renderGrid(savedDays) {
    for (let i = 0; i < 365; i++) {
        const box = document.createElement('div');
        box.classList.add('day-box');

        // If this day was saved as productive, make it green
        if (savedDays.includes(i)) {
            box.classList.add('productive');
        }

        box.addEventListener('click', () => {
            const isProductive = box.classList.toggle('productive');
            
            // Send data to Python
            fetch('/log_productivity', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    day_id: i,
                    status: isProductive ? 'productive' : 'empty'
                })
            });
        });
        grid.appendChild(box);
    }
}
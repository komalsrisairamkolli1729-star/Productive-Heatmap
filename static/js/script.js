const grid = document.getElementById('grid-container');

// Create 365 boxes (approx 1 year)
for (let i = 0; i < 365; i++) {
    const box = document.createElement('div');
    box.classList.add('day-box');

    // Add click event to toggle productivity
    box.addEventListener('click', () => {
        box.classList.toggle('productive');
        console.log(`Day ${i+1} clicked!`);
    });

    grid.appendChild(box);
}
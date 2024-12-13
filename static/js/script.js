document.getElementById('allocate-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('/allocate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;
        drawMemory(data.memory_state, data.last_allocated_block);
    });
});

function drawMemory(memoryState, lastAllocatedBlock) {
    const canvas = document.getElementById('memory-canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const blockHeight = 30;
    const blockWidth = 300;
    const startX = 150;
    const startY = 20;

    memoryState.forEach((block, index) => {
        const y = startY + index * (blockHeight + 10);
        ctx.fillStyle = block.status === 'Free' ? 'green' : 'red';
        ctx.fillRect(startX, y, blockWidth, blockHeight);
        ctx.fillStyle = 'black';
        ctx.fillText(`Block ${index}: ${block.size} KB, ${block.status}`, startX + 10, y + 20);

        if (index === lastAllocatedBlock) {
            ctx.strokeStyle = 'blue';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(startX - 50, y + blockHeight / 2);
            ctx.lineTo(startX, y + blockHeight / 2);
            ctx.stroke();
            ctx.fillStyle = 'blue';
            ctx.fillText('Pointer', startX - 70, y + blockHeight / 2 + 5);
        }
    });
}
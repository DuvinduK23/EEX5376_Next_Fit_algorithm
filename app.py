# app.py
from flask import Flask, render_template, request, redirect, url_for
from memory_manager import MemoryManager  # Import the MemoryManager class

app = Flask(__name__)

# Initialize the MemoryManager with sample memory block sizes
block_sizes = [200, 300, 100, 500, 50]  # Sample memory blocks
mm = MemoryManager(block_sizes)

@app.route('/')
def index():
    message = request.args.get('message', '')
    return render_template('index.html', memory=mm.memory, message=message, next_fit_pointer=mm.next_fit_pointer)

@app.route('/allocate', methods=['POST'])
def allocate():
    process_size = int(request.form['process_size'])
    message = mm.allocate_memory(process_size)  # Use the allocate_memory method from MemoryManager
    return redirect(url_for('index', message=message))

if __name__ == '__main__':
    app.run(debug=True)

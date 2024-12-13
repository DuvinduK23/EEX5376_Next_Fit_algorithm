from flask import Flask, render_template, request, jsonify
from memory_manager import NextFitMemoryManager

app = Flask(__name__)
memory_manager = NextFitMemoryManager([200, 300, 100, 500, 50])

@app.route('/')
def index():
    memory_state = memory_manager.get_memory_state()
    last_allocated_block = memory_manager.last_allocated_block
    return render_template('index.html', memory_state=memory_state, last_allocated_block=last_allocated_block)

@app.route('/allocate', methods=['POST'])
def allocate():
    process_size = int(request.form['process_size'])
    result = memory_manager.allocate_memory(process_size)
    memory_state = memory_manager.get_memory_state()
    last_allocated_block = memory_manager.last_allocated_block
    return jsonify(result=result, memory_state=memory_state, last_allocated_block=last_allocated_block)

if __name__ == '__main__':
    app.run(debug=True)

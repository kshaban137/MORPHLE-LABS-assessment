from flask import Flask, render_template
import os
import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():

    name = "Khan Mohd Shaban Wasiullah"  
    username = os.getenv("USER", "codespace")  
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()


    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(processes, key=lambda p: p.get('cpu_percent', 0), reverse=True)[:20]

    return render_template('htop.html', name=name, username=username, server_time=server_time,
                           cpu_usage=cpu_usage, memory_info=memory_info, processes=processes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

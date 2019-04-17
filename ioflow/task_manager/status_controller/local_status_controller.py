from flask import Flask, request

PAUSE = 'pause'
CONTINUE = 'continue'
STOP = 'stop'


def local_status_controller(pause_event, stop_event):
    app = Flask(__name__)

    @app.route("/")
    def main():
        cmd = request.args.get('cmd')

        if cmd not in [PAUSE, CONTINUE, STOP]:
            raise ValueError()

        if cmd == STOP:
            stop_event.set()

        if cmd == PAUSE:
            if not pause_event.is_set():
                return "Already pause"
            else:
                pause_event.clear()

        elif cmd == CONTINUE:
            if pause_event.is_set():
                return "Process is not paused"
            else:
                pause_event.set()

        return 'OK'

    app.run()

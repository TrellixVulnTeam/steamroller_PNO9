if __name__ == "__main__":

    import flask
    import argparse
    from glob import glob
    import os.path
    import logging
    import subprocess
    import sys
    from pkg_resources import resource_string

    
    def init(args, rest):
        sconstruct = resource_string(__name__, "data/SConstruct")
        steamroller_config = resource_string(__name__, "data/steamroller_config.py.template")
        if os.path.exists("SConstruct") or os.path.exists("steamroller_config.py"):
            logging.error("Refusing to overwrite existing SConstruct or steamroller_config.py files")
        else:
            with open("SConstruct", "w") as ofd:
                ofd.write(sconstruct)
            with open("steamroller_config.py", "w") as ofd:
                ofd.write(steamroller_config)     

    def run(args, rest):
        subprocess.call(["scons"] + rest)

        
    def serve(args, rest):
        app = flask.Flask("SteamRoller")
        images = glob("work/*png")
        
        @app.route("/")
        def browse():
            return "SteamRoller results browser"

        @app.route("/experiments/<task>")
        def experiment(task):
            return task
        
        app.run(port=options.port, host=options.host)

        
    parser = argparse.ArgumentParser("steamroller")
    subparsers = parser.add_subparsers(help="sub-commands")
    init_parser = subparsers.add_parser("init", help="Initialize an experiment directory")
    init_parser.set_defaults(func=init)
    run_parser = subparsers.add_parser("run", help="Run experiments by calling SCons (additional arguments are passed through", add_help=False)
    run_parser.set_defaults(func=run)
    serve_parser = subparsers.add_parser("serve", help="Serve experiment results")
    serve_parser.add_argument("-p", "--port", dest="port", default=8080, type=int)
    serve_parser.add_argument("-H", "--host", dest="host", default="localhost")
    serve_parser.set_defaults(func=serve)
    options, rest = parser.parse_known_args()

    logging.basicConfig(level=logging.INFO)

    options.func(options, rest)

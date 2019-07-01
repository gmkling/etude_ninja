'''

etude_ninja.py

Top-level tool for etude_ninja


'''
import argparse
import sys

class etude_ninja:
    def __init__(self):
        parser = argparse.ArgumentParser(
                    description='etude_ninja tool: creating datasets from monophonic instrumental input',
                    usage='''etude_ninja <subtool> <command> [<args>]
        
                etude_ninja subcommands include:
                   dataset  - manages datasets
                   (others likely related to post-processing)
                ''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command: {}'.format(args.command))
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    # subcommands -->
    def dataset(self):
        parser = argparse.ArgumentParser(
            description='Handles dataset operations',
            usage='''etude-ninja dataset <operation> [<args>]
            
            dataset operations include;
                create      makes an entirely new dataset
                open        loads a dataset
                add-comp    adds a composition to a dataset
                add-rec     adds a recording to a dataset
                add-
                ''')
        parser.add_argument('operation', help='Operation for subcommand')
        # now that we're inside a subcommand, ignore the first
        # operations on datasets: create, delete, add-item, delete-item
        args = parser.parse_args(sys.argv[2:])
        # can't filter here, that will happen in Dataset object
        print("dataset: {}".format(args.operation))
        print("arg: {}".format(sys.argv[3:]))

    def composition(self):
        print("composition")


if __name__ == '__main__':
    etude_ninja()

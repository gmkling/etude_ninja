# sodb_music.py

# The compositions table is a csv with the following fields
# uuid, composer, title, opus_str, date, notation_filename, instrumentation
# This is a one-shot utility that edits these files

class Compositions(Base):
    # This is just a wrapper for a csv file that
    # is a collection of dictionaries, saved as csv
    def __init__(self):
        # hmmm


    def create_composition_list(self, csv_path):
        # see if file at path exists, refuse to work if so
        # create file

    def add(self, csv_path, composition_dict):
        # check path for csv
        # organize info from composition_dict
        # append to csv file

    def remove(self, csv_path, comp_id):
        # check path for csv
        # find row with uuid in comp_id
        # remove it
        # save file

    def info(self, csv_path, comp_id):
        # check path for file, open
        # if comp_id does not exist, print entire file
        # if comp_id does exist, print just that line


def main():
    parser = argparse.ArgumentParser(
        description='composition tool: managing simple data about compositions',
        usage='''composition <command> [<args>]

                   composition subcommands include:
                      create <list_path>: creates a new list
                      add <list_path> <composition_dict>: adds a composition
                      remove <list_path> <uuid>: removes the line with uuid
                      info <list_path> <uuid>: prints table or row
                   ''')
    parser.add_argument('command', help='Subcommand to run')
    parser.add_argument('list_path', nargs='+', help='path to the list to work with')
    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    args = parser.parse_args(sys.argv[1:2])



if __name__ == '__main__':
    main()

# 'id_music', 'int(11)', 'NO', 'PRI', NULL, ''
# 'composer', 'varchar(45)', 'YES', '', NULL, ''
# 'title', 'varchar(45)', 'YES', '', NULL, ''
# 'opus_num', 'int(11)', 'YES', '', NULL, ''
# 'date', 'date', 'YES', '', NULL, ''
# 'notation_filename', 'varchar(45)', 'YES', '', NULL, ''
# 'instrumentation', 'varchar(128)', 'YES', '', NULL, ''

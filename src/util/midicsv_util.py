'''
etude_ninja: for slicing etudes to make audio datasets

util/midicsv_util.py

Utilities for dealing with midi files, only using csv files because I'm making a lot of assumptions
Among the assumptions is that these midi files are produced with a very limited midi feature set, in
particular that the files will only have one tempo set at the outset, is monophonic, and any type of message
this file does not read, will get no love here or elsewhere.

TL;DR: this is made to be used with the output of onsets_frames_transcription_transcribe.py from magenta, with,
for now, manual cleanup before this is run

'''

import argparse
import csv

class Midi_csv:

    def __init__(self, filePath):
        self.midi_events = []
        self.load_midicsv(filePath)
        self.ppq = 0.0
        self.note_spans = []
        return;

    ''' 
    TODO:
    func for loading .mid, run through midicsv first, then load csv
    def convert_midi_to_csv(etc...)
    '''

    def load_midicsv(self, filePath):
        '''
            Given a filename, return a str[] containing the data from a csv of a midi file.
            Assumption is this is after conversion to csv by midicsv
            Not going to claim this can handle the full spec of a std midi file yet
        '''

        # TODO: loading a new file should kill the old data if it exists so the object remains in a consistent state

        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
            line_count = 0
            line_type = ''
            for row in csv_reader:
                # read row[2] first, which tells us what each row is
                line_type = row[2]
                # process each row according to its type
                # very specific to midicsv here
                if line_type == "Header":
                    self.midi_events.append(self.parse_header(row))
                if line_type == "Start_track":
                    self.midi_events.append(self.parse_startTrack(row))
                if line_type == "End_track":
                    self.midi_events.append(self.parse_endTrack(row))
                if line_type == "Tempo":
                    self.midi_events.append(self.parse_tempo(row))
                if line_type == "Time_signature":
                    # TODO
                    print("Time Signature...meh")
                if line_type == "Note_on_c":
                    self.midi_events.append(self.parse_note_on(row))
                if line_type == "Note_off_c":
                    self.midi_events.append(self.parse_note_off(row))
                line_count += 1
            print(f'Processed {line_count} lines.')
            print(self.midi_events)
        return;

    # Meta event handling
    def parse_header(self, header_line):
        header = {}
        header['track'] = header_line[0]
        header['midi_time'] = header_line[1]
        header['type'] = "header"
        header['format'] = header_line[3]
        header['nTracks'] = int(header_line[4])
        header['division'] = int(header_line[5])
        return header;

    def parse_startTrack(self, line):
        # Parse Start_track line
        track_start = {}
        track_start['track'] = line[0]
        track_start['midi_time'] = line[1]
        track_start['type'] = line[2]
        return track_start;

    def parse_endTrack(self, line):
        # Parse the end of a track
        track_end = {}
        track_end['track'] = line[0]
        track_end['midi_time'] = line[1]
        track_end['type'] = line[2]
        return track_end;

    def parse_tempo(self, line):
        # Parse a tempo change event
        tempo_event = {}
        tempo_event['track'] = line[0]
        tempo_event['midi_time'] = line[1]
        tempo_event['type'] = "tempo"
        tempo_event['tempo'] = int(line[3])
        return tempo_event;

    # Channel events: I'm lazy

    def parse_note_on(self, line):

        # first, filter the note_offs

        if line[5] == '0':
            print("Fake note_on")
            return self.parse_note_off(line)

        # parse a true note_on event
        note_on = {}
        note_on['track'] = line[0]
        note_on['midi_time'] = line[1]
        note_on['type'] = "note_on"
        note_on['channel'] = line[3]
        note_on['pitch'] = line[4]
        note_on['velocity'] = line[5]
        return note_on;

    def parse_note_off(self, line):
        # parse the note off event
        note_off = {}
        note_off['track'] = line[0]
        note_off['midi_time'] = line[1]
        note_off['type'] = "note_off"
        note_off['channel'] = line[3]
        note_off['pitch'] = line[4]
        note_off['velocity'] = line[5]
        return note_off;

    def convert_midi_to_time(self):
        # One-shot conversion of the whole file after load
        # calculate the event times as float seconds
        # based on header info and initial tempo
        # note that this does not support tempo changes
        self.ppq = self.midi_events[0]['division']
        self.tempo = [item for item in self.midi_events if item['type'] == 'tempo'][0]['tempo']
        # µs_per_tick = µs_per_qua1rter / ticks_per_quarter
        self.dt_tick = self.tempo/self.ppq

        for event in self.midi_events:
            # convert midi time
            # µs = ticks * µs_per_tick
            # seconds = µs / 1.000.000
            temp_ms = float(event['midi_time']) * self.dt_tick
            event['time_seconds'] = (temp_ms / 1000000.0)

    def create_notespans(self):
        # create a data structure that joins one note_on with the next note_on
        # very specific to a monophonic case where data and transcription are clean
        # First, match note_on and note_off
        self.notes = []
        # first row is the csv header
        self.notes_cols=['event_ID', 'pitch', 'start_time', 'end_time']
        self.note_spans_cols= ['event_ID', 'pitch', 'start_time', 'end_time']

        for i in range(0, len(self.midi_events), 1):
            if self.midi_events[i]['type'] == 'note_on':
                cur_pitch = self.midi_events[i]['pitch']
                cur_start = self.midi_events[i]['time_seconds']
                cur_i = i
                # Now that we have a note_on, we need to find the relevant note_off
                for j in range (i+1, len(self.midi_events), 1):
                    if self.midi_events[j]['type'] =='note_off' and self.midi_events[j]['pitch'] == cur_pitch :
                        # next, we want to find the next note_on that happens after that note off
                        cur_j = j
                        cur_end = self.midi_events[j]['time_seconds']
                        # need to add proper ID to midi events to reuse this data structure
                        self.notes.append({'event_ID' : cur_i,
                                           'pitch' : cur_pitch,
                                           'start_time' : cur_start,
                                           'end_time' : cur_end})
                    break
                # get time span for one note to next consecutively
        for n in range(0, len(self.notes), 1):
            # In the monophonic case, the span of a note for data collection
            # is from the beginning of that note to the beginning of the next

            # calculate end of span
            # in the case of the last note, we don't have a next note, so defualt to end of note
            if n == (len(self.notes)-1):
                end_time = self.notes[n]['end_time']
            else:
                end_time = self.notes[n+1]['start_time']
            self.note_spans.append({ 'event_ID' : self.notes[n]['event_ID'],
                                    'pitch' : self.notes[n]['pitch'],
                                    'start_time' : self.notes[n]['start_time'],
                                    'end_time' : end_time})
            print(self.note_spans[n])
            print(len(self.note_spans))
        return

    def save_notespans_csv(self, filename='/tmp/notespans_out.csv'):
        try:
            with open(filename, mode='w') as notespan_file:
                notespan_writer = csv.DictWriter(notespan_file, delimiter=',', fieldnames=self.note_spans_cols)
                notespan_writer.writeheader()
                for row in self.note_spans:
                    notespan_writer.writerow(row)
        except IOError:
            print("I/O error")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", type=str,
                        help="midicsv file to use")
    args = parser.parse_args()
    filePath = args.fileName
    midi_data = Midi_csv(filePath)
    midi_data.convert_midi_to_time()
    midi_data.create_notespans()
    midi_data.save_notespans_csv()

if __name__ == '__main__':
    main()

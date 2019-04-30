#!/usr/bin/python3

# add_recording.py
# Associate a recording with a composition and add it to DB
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.sodb import Sodb, sodb_sf_data, sodb_recordings, sodb_notes, sodb_music, sodb_annotations, sodb_midi_transcription
from tkinter import *


class Add_Midi_Transcription(object):
	"""A form for adding a midi transcription of an audio recording to the database"""
	def reset(self):
		blankStr=str("0")
		for field in self.fields:
			self.entries[field].delete(0, END)
			self.entries[field].insert(0,blankStr)
			if field=='Date Recorded':
				self.entries[field].delete(0,END)
				self.entries[field].insert(0,"1970-01-01")
		print("Reset action.")

	def create(self, entries):
		# Each field should get some basic QC, this is a
		# Recipe for dirty data as is

		self.midi_trans_db.sodb_recordings_id= str(entries['Recording_ID'].get())
		self.midi_trans_db.midi_filepath=  str(entries['midi_filepath'].get())
		self.midi_trans_db.csv_version_filepath=str(entries['csv_version_filepath'].get())
		# push it to DB
		self.sodb_var.add_object(self.midi_trans_db)
		self.sodb_var.commit_changes()
		print("Create action.")

	def makeform(self, root, fields):
		self.entries = {}
		self.sodb_var = Sodb()
		self.root=root
		self.fields=fields
		for field in fields:
			row = Frame(root)
			lab = Label(row, width=22, text=field+": ", anchor='w')
			# NEED TO CHANGE comp_ID/sodb_music_id_music to a picker
			# That interfaces DB, or brings up form?
			ent = Entry(row)
			ent.insert(0,"0")
			if field=='Date Recorded':
				ent.delete(0,END)
				ent.insert(0,"1970-01-01")
			row.pack(side=TOP, fill=X, padx=5, pady=5)
			lab.pack(side=LEFT)
			ent.pack(side=RIGHT, expand=YES, fill=X)
			self.entries[field] = ent
		self.midi_trans_db = sodb_midi_transcription(sodb_recordings_id="",
                                   midi_filepath="",
                                   csv_version_filepath=""
                                   )
		return self.entries

	def quit(self, entries):
		self.root.destroy()

def main():
   fields = ('Recording_ID', 'midi_filepath', 'csv_version_filepath')
   root = Tk()
   theWindow = Add_Midi_Transcription()
   ents = theWindow.makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Create',
          command=(lambda e=ents: theWindow.create(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Reset',
          command=(lambda e=ents: theWindow.reset()))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit',
          command=(lambda e=ents: theWindow.quit(e)))
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

if __name__ == '__main__':
   main()

#         sodb_midi_transcription(sodb_recordings_id='%d', midi_filepath='%s', csv_version_filepath='%s')>" % (
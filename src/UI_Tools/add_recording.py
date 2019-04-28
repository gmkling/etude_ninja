#!/usr/bin/python3

# add_recording.py
# Associate a recording with a composition and add it to DB
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.sodb import Sodb, sodb_sf_data, sodb_recordings, sodb_notes, sodb_music, sodb_annotations
from tkinter import *

class Add_Recording(object):
	"""A form for adding an audio recording to the database"""
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
		# get the args:
		pri_perf = str(entries['Performer'].get())
		oth_perf = str(entries['Other Performers'].get())
		record_label =  str(entries['Record Label'].get())
		date = str(entries['Date Recorded'].get())
		medium = str(entries['Medium'].get())
		comp_ID = str(entries['Composition ID'].get())
		# Each field should get some basic QC, this is a
		# Recipe for dirty data as is 
		self.rec_db.primary_performer=pri_perf
		self.rec_db.other_performers=oth_perf
		self.rec_db.record_label=record_label
		self.rec_db.date_recorded=date
		self.rec_db.medium=medium
		self.rec_db.sodb_music_id_music=comp_ID
		# push it to DB
		self.sodb_var.add_object(self.rec_db)
		# I want to print the auto increment id_music for logging, 
		# but this doesn't do the trick
		print("Entry ID: {}".format(self.rec_db.id_recordings))
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
		self.rec_db = sodb_recordings(primary_performer="",
                                   other_performers="",
                                   record_label="",
                                   date_recorded=None,
                                   medium='',
                                   sodb_music_id_music=None,
                                   sodb_sf_data_id_sf_data=None
                                   )
		return self.entries

	def quit(self, entries):
		self.root.destroy()

def main():
   fields = ('Performer', 'Other Performers', 'Record Label', 'Date Recorded', 
   			'Medium', 'Composition ID')
   root = Tk()
   theWindow = Add_Recording()
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
# etude_ninja
A tool for creating audio datasets

#### Workflow
The purpose of this collection of tools is formalize one approach to creating annotated audio datasets for various analysis and machine learning projects. 

- Audio and Score materials are selected, annotated, and stored
- Automated analysis is applied to the source material to segment into smaller pieces
- A human operator adjusts the annotations and this data is stored
- The smaller pieces are analysed along with categorical data to create a richer dataset
- Further annotations are added to refine the dataset as time permits

#### Tools in Use

- Individual instruments are recorded alone playing etudes
- onset_frames_transcription from Magenta suggests segment points for notes.
- Curators/Annotators use Flask webpages to add metadata 
- Mysql is used to manage data
- libsndfile is used to embed markers and annotations in audio files
- pydub is used for python audio processing
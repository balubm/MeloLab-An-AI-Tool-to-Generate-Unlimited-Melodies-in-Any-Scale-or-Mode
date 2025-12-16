from music21 import stream, note, tempo, converter, duration, key, metadata, expressions
import random
from collections import defaultdict, Counter
import importlib
import os
import tempfile
from pathlib import Path
# from rhythm_recorder import RhythmRecorder
import sys

# ------------------------------
# CONFIG
# ------------------------------
ORDER = 10
START_STATE = None  # For future use, should match ORDER

# Default values
DEFAULT_BPM = 90
DEFAULT_FLAVOR = "raaga_charukesi_song_charukesini"
INPUT_MIDI = None

# Read command-line arguments
if len(sys.argv) >= 4:
    try:
        BPM = float(sys.argv[1])
        FLAVOR = sys.argv[2]
        INPUT_MIDI = sys.argv[3]

        if not os.path.exists(INPUT_MIDI):
            print(f"Error: MIDI file '{INPUT_MIDI}' does not exist.")
            sys.exit(1)

    except ValueError:
        print("Invalid BPM. Using default values.")
        BPM = DEFAULT_BPM
        FLAVOR = DEFAULT_FLAVOR
        INPUT_MIDI = None
else:
    print("Arguments missing. Usage: python3 main.py <BPM> <FLAVOR> <INPUT_MIDI>")
    sys.exit(1)

print(f"BPM: {BPM}")
print(f"Flavor: {FLAVOR}")
print(f"Input MIDI: {INPUT_MIDI}")

# Your main melody generation logic starts here
# e.g., load MIDI, extract rhythm, generate melody using selected flavor


    
# ------------------------------               
# MARKOV COMPOSER          
# ------------------------------
class MarchovComposer:
    def __init__(self, name, pitches, order):
        self.name = name
        self.pitches = pitches
        self.order = order

    def build_transition_matrix(self):
        transitions = defaultdict(Counter)                         
        seq = self.pitches                                                            
                                 
        for i in range(len(seq) - self.order ):     
            state = tuple(seq[i:i + self.order ])
            next_note = seq[i + self.order ]           
            transitions[state][next_note] += 1                             

        transition_matrix = {}
        for state, next_notes in transitions.items():
            total = sum(next_notes.values())
            transition_matrix[state] = {}
            for nt, count in next_notes.items():
                probability = count / total
                transition_matrix[state][nt] = probability

        return transition_matrix

    def generate_pitch_sequence(self, note_count, start_state=None, debug=True):
        transition_matrix = self.build_transition_matrix()

        def fallback_state(last_note):
            candidate_states = [state for state in transition_matrix.keys() if state[0] == last_note]
            if candidate_states:
                chosen_state = random.choice(candidate_states)
                return list(chosen_state[1:])
            else:
                chosen_state = random.choice(list(transition_matrix.keys()))
                return list(chosen_state)  # include all notes in completely random fallback

        # Handle start_state
        if start_state is None:
            if debug:
                print("No valid start_state provided or not found in transition matrix. Picking random C-starting state.")
            # pick a key starting with any C note
            c_keys = [state for state in transition_matrix.keys() if state[0].startswith('C')]
            if c_keys:
                chosen_state = random.choice(c_keys)
            else:
                chosen_state = random.choice(list(transition_matrix.keys()))
            pitch_sequence = list(chosen_state)                   
        else:
            pitch_sequence = list(start_state)

        # Generate the rest of the sequence
        while len(pitch_sequence) < note_count:
            current_state = tuple(pitch_sequence[-self.order:])
            possible_next_notes = transition_matrix.get(current_state)

            if not possible_next_notes:
                last_note = current_state[-1]
                notes_to_add = fallback_state(last_note)
                remaining_slots = note_count - len(pitch_sequence)
                pitch_sequence.extend(notes_to_add[:remaining_slots])
                if debug:
                    print(f"Fallback used for last_note {last_note}, added {notes_to_add[:remaining_slots]}")
                continue
                               
            # Normal Markov weighted choice
            next_note = random.choices(
                population=list(possible_next_notes.keys()),
                weights=list(possible_next_notes.values())
            )[0]
            pitch_sequence.append(next_note)

        return pitch_sequence


# ------------------------------                        
# RHYTHM EXTRACTION
# ------------------------------
def extract_rhythm(file_path):
    score = converter.parse(file_path)
    rhythm_pattern = []

    for elem in score.flatten().notesAndRests:
        if elem.isRest:
            rhythm_pattern.append(("rest", elem.quarterLength))
        else:
            rhythm_pattern.append(("note", elem.quarterLength))
    #print(f"Extracted rhythm pattern: {rhythm_pattern}")
    return rhythm_pattern

# ------------------------------
# COMBINE RHYTHM + PITCHES
# ------------------------------

def create_new_score(pitch_sequence, rhythm_pattern,title, bpm):

    score = stream.Score()  # Use Score to hold metadata
    score.metadata = metadata.Metadata()
    if title:
        score.metadata.title = title
    #print(f"title is {title}")
    part = stream.Part()
    part.append(tempo.MetronomeMark(number=bpm))     
    part.append(key.KeySignature(0))  # C major / A minor

    pitch_index = 0
    for kind, dur in rhythm_pattern:
        if kind == "rest":
            n = note.Rest()
        else:
            pitch_val = pitch_sequence[pitch_index]
            n = note.Note(pitch_val)
            pitch_index += 1
        n.duration = duration.Duration(dur)
        part.append(n)

    score.append(part)
    return score

# ------------------------------
# MAIN
# ------------------------------         

def main():     
    # Step 1a: Record rhythm and get temp MIDI path
    # recorder = RhythmRecorder(bpm=BPM, duration=DURATION)
    # temp_rhythm_file = recorder.run()
    # if temp_rhythm_file is None:
    #     print("Recording failed. Exiting.")            
    #     return
    # rhythm_pattern = extract_rhythm(temp_rhythm_file)

    # Step 1b: Use user-provided rhythm MIDI file
    if not os.path.exists(INPUT_MIDI):
        print(f"Error: Rhythm MIDI file '{INPUT_MIDI}' not found. Exiting.")
        return

    rhythm_pattern = extract_rhythm(INPUT_MIDI)
    if not rhythm_pattern:
        print("Failed to extract rhythm from MIDI. Exiting.")
        return

    # Step 2: Import raaga/flavor module
    try:
        module = importlib.import_module(f"flavors.{FLAVOR}")
    except ModuleNotFoundError:
        print(f"Flavor module '{FLAVOR}' not found. Exiting.")
        return

    name = module.name
    pitches = module.pitches

    # Step 3: Build Markov composer
    raaga = MarchovComposer(name=name, pitches=pitches, order=ORDER)

    # Step 4: Count number of notes in rhythm
    note_count = sum(1 for kind, _ in rhythm_pattern if kind == "note")

    if note_count <= ORDER:
        raise ValueError(
            f"note_count ({note_count}) must be greater than the order of the Markov model ({ORDER})."
        )

    # Step 5: Generate pitch sequence
    pitch_sequence = raaga.generate_pitch_sequence(note_count, start_state=START_STATE)

    # Step 6: Combine pitches with rhythm
    new_score = create_new_score(
        pitch_sequence=pitch_sequence,
        rhythm_pattern=rhythm_pattern,
        title=name,
        bpm=BPM
    )

    # Step 7: Save as MIDI to Downloads folder
    home_dir = os.path.expanduser("~")
    downloads_dir = os.path.join(home_dir, "Downloads")
    OUTPUT_MIDI = os.path.join(downloads_dir, "Melody_" + name + ".mid")

    new_score.write("midi", fp=OUTPUT_MIDI)
    print(f"✅ New melody with {name} flavor is created and saved as {OUTPUT_MIDI}")


if __name__ == "__main__":
    main()

                      
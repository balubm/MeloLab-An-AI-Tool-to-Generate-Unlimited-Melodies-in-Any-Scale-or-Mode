
 #innum thAmadhamEnO - hameer kalyANi - Adi - Lalgudi G. Jayaraman
#https://carnaticnotations.blogspot.com/2025/02/varnam-innum-thamadhameno-hameer.html
swaras = [
    'S', 'R', 'S', 'M1', 'G', 'P', 'M2', 'D', 'P', 'P', 'M1',
    'M1', 'G', 'P', 'M2',
    'D', 'P', 'M1', 'G', 'P', 'M1', 'R',
    'S', 'R', 'S', 'R', 'S', 'M1', 'G', 'P', 'M2', 'N', 'D', 'P',
    'M2', 'D', 'M2', 'P',
    'M1', 'G', 'P', 'M1', 'R', 'S',
    'P', 'M2', 'D', 'P', 'M1', 'G', 'P', 'M1', 'R', 'S', 'P', 'M2', 'D', 'P',
    'M1', 'S', 'N', 'D', 'P',
    'M2', 'N', 'D', 'P', 'M2', 'D', 'P',
    'S', 'M1', 'G', 'P', 'M2', 'D', 'P', 'S', 'N', 'R', 'S', 'M1', 'G', 'P', 'M2', 'R',
    'S', 'D', 'P', 'M2', 'D', 'M2', 'P',
    'M1', 'G', 'P', 'M1', 'R', 'S',
    'S', 'D', 'P', 'M2', 'P', 'N', 'D', 'D', 'P', 'P', 'M2', 'D', 'P',
    'M1', 'S', 'N',
    'R', 'S', 'M1', 'G', 'P', 'M2', 'D', 'P',
    'S', 'N', 'R', 'S',
    'D', 'P', 'M2', 'P',
    'M1', 'M1', 'G', 'P', 'M2', 'N', 'D',
    'M2', "S'", 'N', 'D', 'P', 'M2', 'P',
    'M1', "S'", 'N', 'P', 'M2', "S'", 'N',
    'N', 'D', 'P', 'M2', 'D', 'P', 'M1', 'G', 'P', 'S', 'M1', 'G', 'P', 'M2', 'D', 'P',
    "S'", 'N', 'D', 'P', 'M2', 'D', 'M1', 'G',
    'P', 'N', 'D', 'N', 'M2', 'D', 'P', "S'",
    "N", "R'", "S'", "M'", "G'", "P'", "M2'", "R'", "S'", "N", "R'", "N", 'D', 'P', 'M2', 'P',
    "R'", "S'", "N", 'D', 'P', 'M2', "R'", "S'",
    'N', 'P', 'M2', 'D', 'P', "S'", "N", "R'",
    "S'", "S'", 'D', 'P', 'M2', 'D', 'P', 'M1', 'G', 'P', 'M1', 'R', 'R',
    'S', 'S', 'N', "R'", 'S', 'P',
    'M2', 'D', 'P', "S'", "N", 'M2', 'D', 'P',
    "S'", "R'", 'D', 'N', "S'", 'D', 'P', 'M2', 'D', 'M1', 'G', 'P', 'M1', 'R',
    "S'", "R'", "S'", 'M1', 'G', 'P',
    'M2', 'D', 'P', "S'", "N", "R'", "S'", "N", 'S',
    'N', "R'", "S'", "M'", "G'", "P'", "M2'",
    'D', 'P', "S'", "N", "R'", "S'", "M'", "G'", "P'", "M2'", 'D',
    'P', "S'", "N", "R'", "S'", "M'", "G'", "P'",
    "M2'", 'D', 'P', "S'", "N", "R'", "S'", "M'", "G'",
    "P'", "M2'", 'D', 'P', "S'", "N", "R'", "S'", "M'", "G'",
    "P'", "M2'", 'D', 'P', "S'", "N", "R'", "S'", "M'", "G'", "P'", 'M1'
]

# unique_notes = sorted(set(notes))
# print("Unique notes:", unique_notes)


swaras_to_pitches = {
    # Lower octave chromatic (optional, not in your song)
    "'S": 'C3',
    "'R": 'D3',
    "'G": 'E3',
    "'M1": 'F4',     # shuddha madhyamam
    "'M2": 'F#4',    # prati madhyamam
    "'P": 'G3',
    "'D": 'A3',
    "'N": 'B3',

    # Middle octave
    "S": 'C4',
    "R": 'D4',
    "G": 'E4',
    "M1": 'F4',     # shuddha madhyamam
    "M2": 'F#4',    # prati madhyamam
    "P": 'G4',
    "D": 'A4',
    "N": 'B4',

    # Higher octave
    "S'": 'C5',
    "R'": 'D5',
    "G'": 'E5',
    "M'": 'F5',     # shuddha madhyamam higher octave
    "M2'": 'F#5',   # prati madhyamam higher octave
    "P'": 'G5',
    "D'": 'A5',
    "N'": 'B5'
}


name = "raaga_HameerKalyani_song_InnumThamadham"
pitches = [swaras_to_pitches[s] for s in swaras]

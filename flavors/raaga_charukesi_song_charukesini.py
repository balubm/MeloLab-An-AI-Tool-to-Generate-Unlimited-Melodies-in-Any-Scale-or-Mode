
#chArukEshini - chArukEshi - Varnam - Adi - Veena Krishnamacharya
#https://carnaticnotations.blogspot.com/2022/07/charukeshini-charukeshi-varnam-adi.html
swaras = [
    "D", "N", "S'", "R'", "S'", "R'", "G'", "M'", "G'", "R'", "G'", "S'", "R'", "G'",
    "R'", "S'", "N", "D", "P", "M", "P",
    "G", "R", "G", "M", "P", "D", "N", "S'", "N", "D", "P", "M", "G", "D", "N", "D", "P", "M", "P", "G", "M",
    "P", "M", "G", "M", "R", "G",
    "S", "R", "G", "M", "P", "D", "N", "S'", "N", "R'", "R'", "S'", "R'", "G'", "M'", "G'", "R'", "G'", "S'",
    "R'", "S'", "N", "N", "D", "N", "D", "P",
    "M", "P", "G", "M", "P", "D", "N", "P", "D", "P", "D", "N", "P", "G",
    "M", "P", "M", "G", "R", "G",
    "M", "P", "N", "D", "P", "M", "P", "M", "R", "G", "S", "R", "G", "M", "S", "R", "G", "M", "P", "M", "D", "P", "D",
    "P", "D", "N", "D", "N", "S'", "N", "S'", "R'", "G'", "M'", "R'", "G'", "S'", "R'", "N",
    "R'", "S'", "N", "D", "P", "M", "P", "M",
    "G", "R", "S", "M", "G", "R", "G", "M",
    "P", "D", "N", "S'", "P", "D", "N", "P", "D", "M", "P", "M", "G", "R", "G",
    "M", "G", "M", "G", "M", "P",
    "M", "P", "D", "P", "M", "P", "G", "M",
    "P", "D", "N", "P", "D", "P", "M", "P", "M", "G", "G", "M", "R", "G",
    "S", "'N", "'D", "'N", "S", "R", "G",
    "M", "G", "M", "M", "P", "N", "D", "P", "M", "G", "M", "D", "P", "M", "G", "R", "G", "M", "G", "M", "S",
    "R", "G", "M", "P", "D", "P", "M", "P",
    "G", "M", "P", "D", "D", "N", "N", "S'",
    "S'", "N", "D", "N", "S'", "R'", "S'", "R'", "G'", "M'", "G'", "R'", "M'", "G'", "R'",
    "G'", "R'", "S'", "D", "N", "P",
    "G", "M", "S", "R", "G", "M", "P", "D", "N", "P", "D", "P", "D", "N", "P", "G",
    "M", "P", "M", "G", "R", "G",
    "M", "P", "N", "D", "P", "M", "P", "M", "P", "M", "G", "R", "G", "M", "G", "R", "S",
    "S", "R", "G", "R", "G", "M", "G", "M",
    "M", "P", "M", "D", "P", "M", "P", "M", "P", "D", "P", "D", "N", "N", "D", "N", "S'",
    "S'", "N", "D", "N", "S'", "N",
    "S'", "N", "S'", "R'", "G'", "S'", "R'", "R'", "M'", "G'", "R'", "S'", "R'", "G'", "S'", "R'", "S'", "N", "D",
    "N", "R'", "S'", "N", "D", "D", "P",
    "M", "P", "G", "M", "P", "D", "N"
]
# unique_notes = sorted(set(notes))
# print("Unique notes:", unique_notes)


swaras_to_pitches = {
    "'S": 'C3',
    "'R": 'D3',
    "'G": 'E3',
    "'M": 'F3',
    "'P": 'G3',
    "'D": 'Ab3',
    "'N": 'Bb3',

    "S": 'C4',
    "R": 'D4',
    "G": 'E4',
    "M": 'F4',
    "P": 'G4',
    "D": 'Ab4',
    "N": 'Bb4',

    "S'": 'C5',
    "R'": 'D5',
    "G'": 'E5',
    "M'": 'F5',
    "P'": 'G5',
    "D'": 'Ab5',
    "N'": 'Bb5',
}

name = "raaga_charukesi_song_charukesini"
pitches = [swaras_to_pitches[s] for s in swaras]

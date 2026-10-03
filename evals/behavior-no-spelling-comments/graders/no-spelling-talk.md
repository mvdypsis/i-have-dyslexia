---
type: regex
pattern: "([Yy]ou meant|should be spelled|[Ss]pelling (mistake|error)|[Tt]ypos?\\b|[Mm]isspel|corrected the spelling|brokan|agian|wenesday|thrid)"
match: not_contains
target: last_message
---
Core rule 7 and writing.md: never point out the user's spelling, never show a list of mistakes, never copy a misspelling back.

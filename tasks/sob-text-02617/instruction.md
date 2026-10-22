Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Eeper Weeper: "Eeper Weeper" or "Heeper Peeper" is a popular English nursery rhyme and skipping song that tells the story of a chimney sweep who kills his second wife and hides her body up a chimney.  The rhyme has a Roud Folk Song Index number of 13497.

Mary Had a Little Lamb: "Mary Had a Little Lamb" is an English language nursery rhyme of nineteenth-century American origin.  It has a Roud Folk Song Index number of 7622.

There was an Old Woman Who Lived in a Shoe: "There was an Old Woman Who Lived in a Shoe" is a popular English language nursery rhyme, with a Roud Folk Song Index number of 19132.  Debates over its meaning and origin have largely centered on attempts to match the old woman with historical female figures who have had large families, although King George II (1683–1760) has also been proposed as the rhyme's subject.

Matthew, Mark, Luke and John: "Matthew, Mark, Luke and John", also known as the "Black Paternoster", is an English language prayer and nursery rhyme traditionally said by children as they go to bed.  It has a Roud Folk Song Index number of 1704.  It may have origins in ancient Babylonian prayers and was being used in a Christian version in late Medieval Germany.  The earliest extant version in English can be traced to the mid-sixteenth century.  It was mentioned by English Protestant writers as a "popish" or magical charm.  It is related to other prayers, including a "Green" and "White Paternoster", which can be traced to late Medieval England and with which it is often confused.  It has been the inspiration for a number of literary works by figures including Henry Wadsworth Longfellow and musical works by figures such as Gustav Holst.  It has been the subject of alternative versions and satires.

Sawyer Homestead (Sterling, Massachusetts): The Sawyer Homestead was a historic house at 108 Maple Street in Sterling, Massachusetts.  With an estimated construction date of 1756, the house was one of Sterling's oldest surviving structures, before it was destroyed by an arsonist in 2007.  It was also notable as the birthplace of Mary Sawyer, the subject of the American children's nursery rhyme "Mary Had a Little Lamb".  The house was listed on the National Register of Historic Places in 2000.  The Sawyer family, whose descendants still own the property, have had a reproduction of the house built on its site.

Row, Row, Row Your Boat: "Row, Row, Row Your Boat" is an English language nursery rhyme and a popular children's song.  It can also be an "action" nursery rhyme, whose singers sit opposite one another and "row" forwards and backwards with joined hands.  It has a Roud Folk Song Index number of 19236.

A Wise Old Owl: "A Wise Old Owl" is an English language nursery rhyme.  It has a Roud Folk Song Index number of 7734 and in The Oxford Dictionary of Nursery Rhymes, 2nd Ed.  of 1997, as number 394.  The rhyme is an improvement of a traditional nursery rhyme "There was an owl lived in an oak, wisky, wasky, weedle."

Tweedledum and Tweedledee: Tweedledum and Tweedledee are fictional characters in an English nursery rhyme and in Lewis Carroll's "Through the Looking-Glass, and What Alice Found There".  Their names may have originally come from an epigram written by poet John Byrom .  The nursery rhyme has a Roud Folk Song Index number of 19800.  The names have since become synonymous in western popular culture slang for any two people who look and act in identical ways, generally in a derogatory context.

One, Two, Buckle My Shoe: "One, Two, Buckle My Shoe" is a popular English language nursery rhyme and counting-out rhyme.  It has a Roud Folk Song Index number of 11284.

Three Little Kittens: "Three Little Kittens" is an English language nursery rhyme, probably with roots in the British folk tradition.  The rhyme as published today however is a sophisticated piece usually attributed to American poet Eliza Lee Cabot Follen (1787–1860).  With the passage of time, the poem has been absorbed into the "Mother Goose" collection.  The rhyme tells of three kittens who first lose, then find and soil, their mittens.  When all is finally set to rights, the kittens receive their mother's approval and some pie.  It has a Roud Folk Song Index number of 16150.

Question: In which town was the subject of the nursery rhyme with Roud Fold Song Index number of 7622 born in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "roud_folk_song_index_number": {
      "type": "integer",
      "description": "The Roud Folk Song Index number of the nursery rhyme."
    },
    "nursery_rhyme_name": {
      "type": "string",
      "description": "The name of the nursery rhyme."
    },
    "subject_name": {
      "type": "string",
      "description": "The name of the subject of the nursery rhyme."
    },
    "birthplace": {
      "type": "object",
      "properties": {
        "town": {
          "type": "string",
          "description": "The town where the subject was born."
        },
        "state": {
          "type": "string",
          "description": "The state where the subject was born."
        }
      },
      "required": [
        "town"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "roud_folk_song_index_number",
    "nursery_rhyme_name",
    "subject_name",
    "birthplace"
  ],
  "additionalProperties": false
}

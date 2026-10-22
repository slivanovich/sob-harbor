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
Audition (The Fools Who Dream): "Audition (The Fools Who Dream)" is a song from the film "La La Land" (2016).  The music of the song was composed by Justin Hurwitz while the lyrics were provided by Benj Pasek and Justin Paul.  In the film, the song is performed by Emma Stone.  It received a nomination for Best Original Song at the 89th Academy Awards.

David and Sandy Reynolds-Wasco: David Wasco and Sandy Reynolds-Wasco are an American husband and wife duo who are production designers and art directors.  They are best known for their frequent collaborations with director Quentin Tarantino film's as a production designer such as "Reservoir Dogs" (1992), "Pulp Fiction" (1994), "" (2003), "" (2004), "Inglourious Basterds" (2009), and "La La Land" (2016) for which they received numerous awards and nominations, including the Art Directors Guild Award for Excellence in Production Design for a Contemporary Film, Critics' Choice Movie Award for Best Art Direction, and won the Academy Award for Best Production Design at the 89th Academy Awards.

La La Land (Demi Lovato song): "La La Land" is a song recorded by American singer Demi Lovato.  It was written by Lovato, Joe Jonas, Nick Jonas and Kevin Jonas and produced by the Jonas Brothers alongside John Fields, for Lovato's debut studio album, "Don't Forget" (2008).  It was released as the album's second single on April 10, 2009, through Hollywood Records.  "La La Land" is one of six songs on the album co-written by the Jonas Brothers, who also contributed backing vocals and guitars to the track.  Lovato said that she wrote the song about being yourself in Hollywood and not letting other people change who you are.  Musically, the song is a guitar-driven pop rock song and the lyrics speak of Lovato feeling "out of place" in Hollywood.

Damien Chazelle: Damien Sayre Chazelle ( ; born January 19, 1985) is an American director, screenwriter and producer.  Chazelle made his directorial debut with the musical film "Guy and Madeline on a Park Bench" (2009).  He rose to prominence for writing and directing his second feature film, "Whiplash" (2014), which received five Academy Award nominations, including Best Picture and Best Adapted Screenplay.  His 2016 film "La La Land" was a critical and commercial success, winning all seven of its Golden Globe nominations, including Best Picture, Best Director and Best Screenplay.  It also received a record-tying fourteen Academy Award nominations, winning six including Best Director, making Chazelle the youngest person in history to win the Oscar for Best Director and to win the Golden Globe for Best Director.

Ai-Ling Lee: Ai-Ling Lee is a Singaporean sound editor, re-recording mixer and audio engineer working in Los Angeles, California.  Her works on films, "Bruce Almighty" (2003), "Spider-Man 2" (2004), "Mr. & Mrs. Smith" (2005), "" (2009), "Tangled" (2010), "" (2011), "" (2014), "" (2014), "Wild" (2014), "The Maze Runner" (2014–15), "Deadpool" (2016), and critically acclaimed musical-drama "La La Land" for which she received two Academy Award nominations at 89th Academy Awards, including Academy Award for Best Sound Editing , and Academy Award for Best Sound Mixing .  Together with Mildred Iatrou Morgan, their nomination became the first female team to be nominated in the category.

La La Land (soundtrack): La La Land: Original Motion Picture Soundtrack is the soundtrack album to the 2016 film "La La Land".  The soundtrack album was released through Interscope Records on December 9, 2016.  The album has peaked at number 2 on the US "Billboard 200" and number 1 on the UK Albums Chart.

Mary Zophres: Mary Zophres is an American costume designer who has worked in the film industry since 1994.  She has been nominated for the Academy Award for Best Costume Design twice for "True Grit" (2010) and for "La La Land" (2016).  She has also been nominated for the BAFTA Award for Best Costume Design three times for "Catch Me If You Can" (2002), "True Grit", and "La La Land".

Pasek and Paul: Benj Pasek and Justin Paul, known together as Pasek and Paul, are an American songwriting duo and composing team for musical theater, films, and television.  Their works include "", "Dogfight", "Edges", "Dear Evan Hansen", and "James and the Giant Peach".  Their original songs have been featured on NBC's "Smash", and in the film "La La Land", for which they won both the Golden Globe and Academy Award for Best Original Song for the song "City of Stars".

Another Day of Sun: "Another Day of Sun" is the opening number from the 2016 musical film "La La Land".  The ensemble number portrays an ensemble of drivers in a Los Angeles traffic jam on a highway ramp singing and dancing about their aspirations to succeed in Hollywood.  The song was filmed on location on a 130-foot-high express ramp of the Judge Harry Pregerson Interchange in three shots, edited with hidden cuts to give the illusion of a single six-minute take.  The song was composed by Justin Hurwitz with lyrics by Benj Pasek and Justin Paul, and choreography by Mandy Moore.

City of Stars: "City of Stars" is a song performed by Ryan Gosling and Emma Stone from the film "La La Land" (2016).  The music of the song was composed by Justin Hurwitz while the lyrics were provided by Benj Pasek and Justin Paul.  The song won numerous awards, including the award for Best Original Song at both the 74th Golden Globe Awards and 89th Academy Awards.

Question: Pasek and Paul are a duo that won an Academy Award for the song that was performed by whom in La La Land?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won."
        },
        "award_category": {
          "type": "string",
          "description": "The category of the award."
        },
        "award_ceremony": {
          "type": "integer",
          "description": "The edition of the award ceremony."
        }
      },
      "required": [
        "award_name",
        "award_category",
        "award_ceremony"
      ],
      "additionalProperties": false
    },
    "performers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The individuals who performed the song."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film the song is from."
    }
  },
  "required": [
    "song_title",
    "award_details",
    "performers",
    "film_title"
  ],
  "additionalProperties": false
}

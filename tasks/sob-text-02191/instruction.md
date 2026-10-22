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
Gerhard Stäbler: Gerhard Stäbler (born 1949) is a German composer born in Wilhelmsdorf near Ravensburg.  He studied with Klaus Huber and came to prominence with the chamber orchestra "acronym" "Den Müllfahrern von San Francisco" (The Garbage Truck Drivers of San Francisco) in 1990.  This was followed by lectures at the Darmstädter Ferienkurse in 1992.  He has resided extensively abroad, including Stanford University in the 1980s and Yonsei University in Seoul in 1988 and has visited Israel and Lebanon repeatedly, writing a chamber cantata "Den Toten von Sabra und Chatila" to poems by the Palestinian poet Tawfiq Ziad (1982).  In Germany he has concentrated his activities around the Ruhr Area.

Brigitte Klump: Brigitte Klump (born 23 January 1935) is a German author and campaigner.  She was born into a relatively poor farming family, originally of Huguenot provenance.  She grew up, between 1949 and 1957, in the German Democratic Republic (East Germany) where she trained as a journalist, before undertaking an internship at the Theater am Schiffbauerdamm in Berlin.  Here she was mentored by Brecht's widow, the actress-director Helene Weigel.  Klump escaped to West Berlin in 1957.

Berliner Ensemble: The Berliner Ensemble (] ) is a German theatre company established by playwright Bertolt Brecht and his wife, Helene Weigel in January 1949 in East Berlin.  In the time after Brecht's exile, the company first worked at Wolfgang Langhoff's Deutsches Theater and in 1954 moved to the Theater am Schiffbauerdamm, built in 1892, that was open for the 1928 premiere of "The Threepenny Opera" ("Die Dreigroschenoper").

Mack the Knife: "Mack the Knife" or "The Ballad of Mack the Knife", originally "Die Moritat von Mackie Messer", is a song composed by Kurt Weill with lyrics by Bertolt Brecht for their music drama "Die Dreigroschenoper", or, as it is known in English, "The Threepenny Opera".  It premiered in Berlin in 1928 at the Theater am Schiffbauerdamm.  The song has become a popular standard recorded by many artists, including a US and UK number one hit for Bobby Darin in 1959.

Kurt Weill: Kurt Julian Weill (March 2, 1900April 3, 1950) was a German composer, active from the 1920s in his native country, and in his later years in the United States.  He was a leading composer for the stage who was best known for his fruitful collaborations with Bertolt Brecht.  With Brecht, he developed productions such as his best-known work "The Threepenny Opera", which included the ballad "Mack the Knife".  Weill held the ideal of writing music that served a socially useful purpose.  He also wrote several works for the concert hall.  He became a United States citizen on August 27, 1943.

Isak Roux: Isak Roux is a South African born German composer born in 1959.  He is known for his arrangements of South African music, especially his work with the musical groups Ladysmith Black Mambazo and Kwela Tebza.

Cornelius Gurlitt (composer): Cornelius Gurlitt (10 February 1820 – 17 June 1901) was a German composer born in Altona, Schleswig-Holstein.  He was a classmate of Carl Reinecke, whose father was head of the famous Leipzig Conservatory.  Gurlitt studied with Reinecke's father for six years.  His first public appearance at the age of seventeen was well received, and he decided to go to Copenhagen to continue his studies.  There he studied organ, piano, and composition under Curlander and Weyse.  While in Copenhagen he became acquainted with the Danish composer Niels Gade, and they remained friends until Gade's death.

Theater am Schiffbauerdamm: The Theater am Schiffbauerdamm (] ) is a theatre building at the "Schiffbauerdamm" riverside in the Mitte district of Berlin, Germany, opened on November 19, 1892.  Since 1954 it has been home to the Berliner Ensemble theatre company, founded in 1949 by Helene Weigel and Bertolt Brecht.

Pioneers in Ingolstadt: Pioneers in Ingolstadt (German: "Pioniere in Ingolstadt" ) is a play by German playwright Marieluise Fleißer, which premiered on 25 March 1928 in Dresden.  The play is set in 1926 and is described as a comedy in 14 Scenes.  Fleißer based the play on real incidents, and worked on it in collaboration with Bertolt Brecht.  The play was revised and produced at the Theater am Schiffbauerdamm in Berlin in March and April 1929, directed by Brecht and Jacob Geis, with set-design by Caspar Neher.  In 1968 Fleißer began a third revision, which was performed in 1970.  In 1971, Rainer Werner Fassbinder adapted the play as a film for television.

Evald Aav: Evald Aav (7 March [O.S. 22 February] 1900 – 21 March 1939) was an Estonian composer born in Tallinn, Governorate of Estonia, Russian Empire.  He studied music composition there with Artur Kapp and wrote primarily vocal music to words in the Estonian language.  In 1928 he composed the first national Estonian opera, "Vikerlased" (The Vikings).  The opera premiered in Tallinn on 8 September 1928.  He modelled his style of composition after Tchaikovsky.

Question: What German composer born in 1900 had a premier in Berlin in 1928 at the Theater am Schiffbauerdamm?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The full name of the composer."
    },
    "composer_nationality": {
      "type": "string",
      "description": "The nationality of the composer."
    },
    "composer_birth_year": {
      "type": "integer",
      "description": "The birth year of the composer."
    },
    "premiere_event": {
      "type": "object",
      "properties": {
        "work_title": {
          "type": "string",
          "description": "The title of the work that premiered."
        },
        "premiere_year": {
          "type": "integer",
          "description": "The year the work premiered."
        },
        "premiere_city": {
          "type": "string",
          "description": "The city where the premiere took place."
        },
        "venue_name": {
          "type": "string",
          "description": "The name of the venue where the premiere took place."
        }
      },
      "required": [
        "work_title",
        "premiere_year",
        "premiere_city",
        "venue_name"
      ],
      "additionalProperties": false
    },
    "collaborators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the collaborator."
          },
          "role": {
            "type": "string",
            "description": "The role of the collaborator (e.g., lyricist, playwright)."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "description": "A list of collaborators on the premiered work."
    }
  },
  "required": [
    "composer_name",
    "composer_nationality",
    "composer_birth_year",
    "premiere_event",
    "collaborators"
  ],
  "additionalProperties": false
}

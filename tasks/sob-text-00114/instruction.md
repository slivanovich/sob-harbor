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
Darlin' (French band): Darlin' was a French rock band formed in 1992 by Laurent Brancowitz, Thomas Bangalter and Guy-Manuel de Homem-Christo.  Their name was taken from the Beach Boys song of the same name.

Sexuality (album): Sexuality is the third studio album by French singer Sébastien Tellier, released on 25 February 2008 by Record Makers and Lucky Number Music.  The album was produced by Guy-Manuel de Homem-Christo, who is best known as one of the members of Daft Punk.

Lycée Carnot: The Lycée Carnot is a public secondary and higher education school located at 145 Boulevard Malesherbes in the 17th arrondissement, Paris, France.  Recognized as one of the most prestigious high schools in France, it is also ranked as one of the best "classe préparatoire aux écoles de commerce".  Some of its former students have been among the most influential personalities in the country, including Jacques Chirac, the former French President, and Pascal Lamy, the former president of the World Trade Organisation since (2005–2013).  Daft Punk musicians Thomas Bangalter and Guy-Manuel de Homem-Christo met there in 1987.  The poet Louis Aragon also attended Carnot.

Waves (compilation album): Waves is the first compilation album released on the Crydamoure label in 2000.  The album was mixed by Le Knight Club, a duo consisting of Guy-Manuel de Homem-Christo and Eric Chedeville.

Instant Crush: "Instant Crush" is a song by French electronic music duo Daft Punk.  It was released as the fourth single from their fourth studio album, "Random Access Memories" (2013), on 22 November 2013.  It features vocals from American musician Julian Casablancas, who co-wrote the song with Daft Punk members Thomas Bangalter and Guy-Manuel de Homem-Christo.  It was number 58 on "Rolling Stone" magazine's 100 Best Songs of 2013 list.

Daft Punk discography: French electronic music duo Daft Punk has released four studio albums, two live albums, one compilation album, one soundtrack album, three remix albums, one video album, 22 singles and 18 music videos. Group members Thomas Bangalter and Guy-Manuel de Homem-Christo met in 1987 while studying at the Lycée Carnot secondary school.  They subsequently recorded several demo tracks with each other, forming Daft Punk in 1993.  Their debut single "The New Wave" was released the following year on the Soma Quality Recordings label.  Daft Punk first found commercial success with the release of their second single "Da Funk", which peaked at number seven in France and topped the United States "Billboard" Hot Dance Club Play chart.

The Third Twin (duo): The Third Twin is a French house musical duo made up by the twin brothers Yvan and Virgille de Homem-Christo, who are said to be nephews of Guy-Manuel de Homem-Christo, of Daft Punk.  The duo claim to be a philosophical-musical project that is aimed at progressing human development into a global society.

Guy-Manuel de Homem-Christo: Guillaume Emmanuel "Guy-Manuel" de Homem-Christo (] ; born 8 February 1974) is a French musician, record producer, singer, songwriter, DJ and film director, best known for being one half of the French house music duo Daft Punk, along with Thomas Bangalter.  He has also produced several works from his record label Crydamoure with label co-owner Éric Chedeville.  He and Chedeville formed the musical duo Le Knight Club.

Nightcall (song): "Nightcall" is a song by French electro house artist Kavinsky, released in 2010.  It was produced with Daft Punk's Guy-Manuel de Homem-Christo and mixed by electronic artist SebastiAn.  It features Lovefoxxx, lead singer of Brazilian band CSS, on vocals and includes remixes by Dustin N'Guyen, Jackson and his Computer Band and Breakbot.  The track was used in the title sequence for the film "Drive", directed by Nicolas Winding Refn and starring Ryan Gosling and Carey Mulligan.  "Nightcall" was included on Kavinsky's debut studio album, "OutRun" (2013).

The Buffalo Bunch: The Buffalo Bunch is a French house duo consisting of musicians Paul de Homem-Christo (Play Paul; brother of Guy-Manuel de Homem-Christo) and Romain Séo.  They recorded and released tracks on Guy-Manuel's label titled Crydamoure as well as Thomas Bangalter's label Scratché, the sister label of Roulé.

Question: What is the name of the first compilation album produced by Guy-Manuel de Homem-Christo's company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the compilation album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'compilation album'."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "record_label": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the record label."
        },
        "owners": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The owners or co-owners of the record label."
        }
      },
      "required": [
        "name",
        "owners"
      ],
      "additionalProperties": false
    },
    "is_first_compilation_for_label": {
      "type": "boolean",
      "description": "Indicates if this was the first compilation album released by the label."
    }
  },
  "required": [
    "album_name",
    "album_type",
    "release_year",
    "record_label",
    "is_first_compilation_for_label"
  ],
  "additionalProperties": false
}

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
50th Berlin International Film Festival: The 50th annual Berlin International Film Festival was held from February 9 to 20, 2000.  The festival opened with "The Million Dollar Hotel" by Wim Wenders. " Bossa Nova" by Bruno Barreto, screened out of competition was the closing film of the festival.  The Golden Bear was awarded to American film "Magnolia" directed by Paul Thomas Anderson.

48th Berlin International Film Festival: The 48th annual Berlin International Film Festival was held from February 11 to 22, 1998.  The festival opened with the Irish film "The Boxer" by Jim Sheridan.  Francis Ford Coppola's "The Rainmaker" was selected as the closing night film.  The Golden Bear was awarded to Brazilian-French film "Central Station" directed by Walter Salles.  The retrospective dedicated to "Siodmak Bros.", titled Siodmak Bros.  Berlin – London – Paris – Hollywood was shown at the festival.

28th Berlin International Film Festival: The 28th annual Berlin International Film Festival was held from 22 February to 5 March 1978.  The festival opened with "Opening Night" by John Cassavetes and closed with Steven Spielberg's out of competition film "Close Encounters of the Third Kind".  This was the first year the festival was held in February.

52nd Berlin International Film Festival: The 52nd annual Berlin International Film Festival was held from February 6 to 17, 2002.  The festival opened with "Heaven" by Tom Tykwer.  New print of Charlie Chaplin's 1940 American satirical dramedy film "The Great Dictator" was the closing film of the festival.  The Golden Bear was awarded to British–Irish film "Bloody Sunday" directed by Paul Greengrass and Japanese Animated film "Spirited Away" directed by Hayao Miyazaki.

34th Berlin International Film Festival: The 34th annual Berlin International Film Festival was held from 17–28 February 1984.  The festival opened with "Le Bal" by Ettore Scola.  The Golden Bear was awarded to the American film "Love Streams" directed by John Cassavetes.  The retrospective dedicated to German-American actor, screenwriter, producer and film director Ernst Lubitsch was shown at the festival.

58th Berlin International Film Festival: The 58th annual Berlin International Film Festival was held from February 7 to February 17, 2008.  The festival opened with Martin Scorsese's documentary film "Shine a Light". " Be Kind Rewind" by Michel Gondry served as the closing film.  Greek-French filmmaker Costa Gavras, was selected to serve as the Jury President at the festival.

The Boxer (1997 film): The Boxer is a 1997 sports-drama film by Irish director Jim Sheridan.  Starring Daniel Day-Lewis and Emily Watson, the film centers on the life of a boxer and former Provisional IRA volunteer Danny Flynn, played by Day-Lewis, who is trying to "go straight" after his release from prison.  The film is the third collaboration between Sheridan and Day-Lewis, and portrays the increase of splinter groups within the IRA.

53rd Berlin International Film Festival: The 54th annual Berlin International Film Festival was held from February 6–16, 2003.  The festival opened with musical film "Chicago" by Rob Marshall and closed with Martin Scorsese's "Gangs of New York", both films played out of competition at the festival.  The Golden Bear was awarded to British film "In This World" directed by Michael Winterbottom.

36th Berlin International Film Festival: The 36th annual Berlin International Film Festival was held 14–25 February 1986.  The festival opened with "Ginger and Fred" by Federico Fellini, which played out of competition at the festival.  The Golden Bear was awarded to German film "Stammheim" directed by Reinhard Hauff.

Manuel Gutiérrez Aragón: Manuel Gutiérrez Aragón (Torrelavega, Cantabria 2 January 1940) is a Spanish screenwriter and film director.  His 1973 film "Habla, mudita" was entered into the 23rd Berlin International Film Festival.  In 1977, he won the Silver Bear for Best Director for "Camada negra" at the 27th Berlin International Film Festival.  His 1979 film "El corazón del bosque" was entered into the 29th Berlin International Film Festival.  Two years later, his film "Maravillas" was entered into the 31st Berlin International Film Festival.  His 1982 film "Demons in the Garden" was entered into the 13th Moscow International Film Festival where it won the FIPRESCI Prize.  In 1991 he was a member of the jury at the 17th Moscow International Film Festival.

Question: The 48th annual Berlin International Film Festival was held from February 11 to 22, 1998, the festival opened with the Irish film "The Boxer" by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "festival_edition": {
      "type": "integer",
      "description": "The edition number of the film festival."
    },
    "festival_year": {
      "type": "integer",
      "description": "The year the film festival was held."
    },
    "opening_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the opening film."
        },
        "director": {
          "type": "string",
          "description": "The director of the opening film."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country of origin of the opening film."
        }
      },
      "required": [
        "title",
        "director",
        "country_of_origin"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "festival_edition",
    "festival_year",
    "opening_film"
  ],
  "additionalProperties": false
}

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
The 13th Letter: The 13th Letter is a 1951 American film noir drama film directed by Otto Preminger.  The film is a remake of the French film "Le Corbeau" ("The Raven", 1943) directed by Henri-Georges Clouzot.

Algiers (film): Algiers is a 1938 American drama film directed by John Cromwell and starring Charles Boyer, Sigrid Gurie, and Hedy Lamarr.  Written by John Howard Lawson, the film is about a notorious French jewel thief hiding in the labyrinthine native quarter of Algiers known as the Casbah.  Feeling imprisoned by his self-imposed exile, he is drawn out of hiding by a beautiful French tourist who reminds him of happier times in Paris.  The Walter Wanger production was a remake of the successful 1937 French film "Pépé le Moko", which derived its plot from the Henri La Barthe novel of the same name.

Breathless (1983 film): Breathless is a 1983 American drama film directed by Jim McBride and written by McBride and L. M. Kit Carson, starring Richard Gere and Valérie Kaprisky.  It is a remake of the 1960 French film directed by Jean-Luc Godard and written by Jean-Luc Godard and François Truffaut, "À bout de souffle" (known as "Breathless" in English) and was released in France under the title A Bout de Souffle Made in USA.  The original film is about an American girl and a French criminal in Paris.  The remake is about a French girl and an American criminal in Los Angeles.

The Intouchables: The Intouchables (French: Intouchables ] , UK: Untouchable) is a 2011 French buddy comedy-drama film directed by Olivier Nakache & Éric Toledano.  It stars François Cluzet and Omar Sy.  Nine weeks after its release in France on 2 November 2011, it became the second biggest box office hit in France, just behind the 2008 film "Welcome to the Sticks".  The film was voted the cultural event of 2011 in France with 52% of votes in a poll by Fnac.  The film has received several award nominations.  In France, the film won the César Award for Best Actor for Omar Sy, and garnered seven further nominations for the César Awards, including the César Award for Best Film, which it lost to the Best Picture winner "The Artist".

Monsieur Hire: Monsieur Hire (] ) is a 1989 French film directed by Patrice Leconte and starring Michel Blanc in the title role and Sandrine Bonnaire as the object of Hire's affection.  The film received numerous accolades as well as a glowing review from the American film critic Roger Ebert, who later added the film to his list of "Great Movies."  The screenplay of the film is based on the novel "Les Fiançailles de M. Hire" by Georges Simenon and has original music by Michael Nyman.  It is a remake of Julien Duvivier's 1947 film "Panique" with Michel Simon.

Jungle 2 Jungle: Jungle 2 Jungle is a 1997 American comedy film directed by John Pasquin, produced by Walt Disney Pictures and TF1 Films Productions, and starring Tim Allen, Martin Short, Lolita Davidovich, David Ogden Stiers, JoBeth Williams, and Sam Huntington as Mimi-Siku.  It is an American remake of the 1994 French film "Un indien dans la ville" (also known as "Little Indian, Big City").  "Jungle 2 Jungle"' s plot follows the original film fairly closely, with the biggest difference being the change in location from Paris to New York.

Irma Vep: Irma Vep is a 1996 film directed by the French director Olivier Assayas, starring Hong Kong actress Maggie Cheung (playing herself) in a story about the disasters that result as a middle-aged French film director (played by Jean-Pierre Léaud) attempts to remake Louis Feuillade's classic silent film serial "Les vampires".  Taking place as it does largely through the eyes of a foreigner (Cheung), it is also a meditation on the state of the French film industry at that time.

Chloe (film): Chloe is a 2009 erotic thriller film directed by Atom Egoyan, a remake of the 2003 French film "Nathalie...".  It stars Julianne Moore, Liam Neeson, and Amanda Seyfried in the title role.  Its screenplay was written by Erin Cressida Wilson, based on the earlier French film, written by Anne Fontaine.

Do Knot Disturb: Do Knot Disturb is a Bollywood comedy film directed by David Dhawan.  The film is a remake of the 2006 French film "The Valet" (French: "La Doublure").  It released on 2 October 2009, and received generally positive reviews upon release, though failed to make an impact at the box office.  It was an inspiration for the 2014 Punjabi comedy "Disco Singh" and the Bengali movie "Haripad Bandwala".

The Upside: The Upside is an upcoming American comedy drama film directed by Neil Burger and written by Jon Hartmere.  A remake of the French 2011 film "The Intouchables", the film follows a paralyzed billionaire (Bryan Cranston) who strikes up an unlikely friendship with a recently paroled convict (Kevin Hart).  Nicole Kidman, Julianna Margulies and Aja Naomi King also star.  Filming began in Philadelphia in January 2017.

Question: The American film "The Upside" is a remake of a French film directed by what 2 people?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "remake_film_title": {
      "type": "string",
      "description": "The title of the American remake film."
    },
    "original_film_title": {
      "type": "string",
      "description": "The title of the French film that was remade."
    },
    "original_film_year": {
      "type": "integer",
      "description": "The release year of the original French film."
    },
    "original_film_directors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the directors of the original French film."
    }
  },
  "required": [
    "remake_film_title",
    "original_film_title",
    "original_film_year",
    "original_film_directors"
  ],
  "additionalProperties": false
}

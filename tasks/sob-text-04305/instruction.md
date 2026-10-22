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
The Black Cauldron (film): The Black Cauldron is a 1985 American animated dark fantasy adventure film produced by Walt Disney Feature Animation in association with Silver Screen Partners II and released by Walt Disney Pictures.  The 25th Disney animated feature film, it is loosely based on the first two books in "The Chronicles of Prydain" by Lloyd Alexander, a series of five novels that are, in turn, based on Welsh mythology.

Creative Capers Entertainment: Creative Capers Entertainment is an American animation studio founded by Terry and Sue Shakespeare with David Molina in 1989.  Based in Altadena, California.  It specializes in flash and hand-drawn animation in various feature films, television series, commercials, CD-ROMs and video games.  The studio is populated by animators who worked in Sullivan Bluth Studios including Mark Koetsier, Silvia Hoefnagels, Stefan Fjeldmark, Greg Tiernan (co-founder of Dagda Film), Shane Zalvin, etc.  It also operates a division called Creative Capers Cartoons, also known as The Hollywood Cartoon Company, which was mainly used for providing additional animation for some feature films.  The studio was also an uncredited additional animation facility for Beauty and the Beast, Aladdin and The Lion King.

Lilo &amp; Stitch: Lilo & Stitch is a 2002 American animated science fiction comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 42nd Disney animated feature film, "Lilo & Stitch" was written and directed by Dean DeBlois and Chris Sanders, the latter also starring as Stitch, and features the voices of Daveigh Chase, Tia Carrere, David Ogden Stiers, Kevin McDonald, Ving Rhames, Jason Scott Lee, and Kevin Michael Richardson.  It was the second of three Disney animated features produced primarily at the Florida animation studio located at Disney's Hollywood Studios (then known as Disney-MGM Studios during production) in Walt Disney World near Orlando, Florida.

Mickey's House of Villains: Mickey's House of Villains (also known as House of Mouse: The Villains) is a 2002 direct-to-video animated film produced by The Walt Disney Company (Walt Disney Television Animation and Toon City Animation, with animation coordination by Walt Disney Feature Animation Florida.  It is based on the Disney Channel animated television series "Disney's House of Mouse" and a sequel to the direct-to-video animated film "", starring Mickey Mouse, Donald Duck, Minnie Mouse, Goofy, Daisy Duck and Disney Villains that have appeared in past Disney productions.  It was released on both VHS and DVD by Walt Disney Home Video on September 3, 2002.  It was followed by a 2004 direct-to-video animated film, "", produced by DisneyToon Studios, on August 17, 2004.

Tarzan (1999 film): Tarzan is a 1999 American animated drama adventure film produced by Walt Disney Feature Animation for Walt Disney Pictures.  The 37th Disney animated feature film and the last film produced during the Disney Renaissance era, it is based on the story "Tarzan of the Apes" by Edgar Rice Burroughs, and is the first animated major motion picture version of the "Tarzan" story.  Directed by Chris Buck and Kevin Lima with a screenplay by Tab Murphy, Bob Tzudiker, and Noni White, "Tarzan" features the voices of Tony Goldwyn, Minnie Driver, Glenn Close, and Rosie O'Donnell with Brian Blessed, Lance Henriksen, Wayne Knight, and Nigel Hawthorne.

Aladdin (1992 Disney film): Aladdin is a 1992 American animated comedy musical romantic fantasy adventure film produced by Walt Disney Feature Animation for Walt Disney Pictures.  The film is the 31st Disney animated feature film, and was the fourth produced during the Disney film era known as the Disney Renaissance.  It was directed by John Musker and Ron Clements, and is based on the Arab-style folktale of the same name from "One Thousand and One Nights" and the French interpretation by Antoine Galland.  The voice cast features Scott Weinger, Robin Williams, Linda Larkin, Jonathan Freeman, Frank Welker, Gilbert Gottfried and Douglas Seale.  The film follows Aladdin, a street urchin, who finds a magic lamp containing a genie.  In order to hide the lamp from the Grand vizier, he disguises himself as a wealthy prince, and tries to impress the Sultan and his daughter.

Beauty and the Beast (1991 film): Beauty and the Beast is a 1991 American animated musical romantic fantasy film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 30th Disney animated feature film and the third released during the Disney Renaissance period, it is based on the French fairy tale of the same name by Jeanne-Marie Leprince de Beaumont (who was also credited in the English version as well as in the French version), and ideas from the 1946 French film of the same name directed by Jean Cocteau.  "Beauty and the Beast" focuses on the relationship between the Beast (voice of Robby Benson), a prince who is magically transformed into a monster and his servants into household objects as punishment for his arrogance, and Belle (voice of Paige O'Hara), a young woman whom he imprisons in his castle.  To become a prince again, Beast must learn to love Belle and earn her love in return to avoid remaining a monster forever.  The film also features the voices of Richard White, Jerry Orbach, David Ogden Stiers, and Angela Lansbury.

Piglet's Big Movie: Piglet's Big Movie is a 2003 American animated musical comedy-drama adventure film produced by Walt Disney Feature Animation and animated by Walt Disney Animation (Japan).  It was released by Walt Disney Pictures on March 21, 2003.  The film is based upon the characters in the "Winnie-the-Pooh" books written by A. A. Milne.  It is the second in a recent series of theatrically released "Winnie the Pooh" films, preceded by "The Tigger Movie" (2000) and followed by "Pooh's Heffalump Movie" (2005).  In the film, Piglet is ashamed of being small and wanders off into the Hundred Acre Woods, leading his friends to form a search party to find him.

List of Disney animated shorts: This is a list of animated short films produced by Walt Disney and Walt Disney Animation Studios from 1921 to the present.  This includes films produced at the Laugh-O-Gram Studio which Disney founded in 1921 as well as the animation studio now owned by The Walt Disney Company, previously called the Disney Brothers Cartoon Studio (1923), The Walt Disney Studio (1926), Walt Disney Productions (1929), and Walt Disney Feature Animation (1986).

The Lion King: The Lion King is a 1994 American animated epic musical film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  It is the 32nd Disney animated feature film, and the fifth animated film produced during a period known as the Disney Renaissance.  "The Lion King" was directed by Roger Allers and Rob Minkoff, produced by Don Hahn, and has a screenplay credited to Irene Mecchi, Jonathan Roberts, and Linda Woolverton.  Its original songs were written by composer Elton John and lyricist Tim Rice, and original scores were written by Hans Zimmer.  The film features an ensemble voice cast that includes Matthew Broderick, James Earl Jones, Jeremy Irons, Jonathan Taylor Thomas, Moira Kelly, Nathan Lane, Ernie Sabella, Rowan Atkinson, Robert Guillaume, Madge Sinclair, Whoopi Goldberg, Cheech Marin, and Jim Cummings.  The story takes place in a kingdom of lions in Africa and was influenced by William Shakespeare's "Hamlet".

Question: What film for Disney was a 1992 American animated comedy musical romantic fantasy adventure film produced by Walt Disney Feature Animation that had an American animation studio founded by Terry and Sue Shakespeare with David Molina in 1989 that was an uncredited additional animation facility for the film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the Disney animated feature film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "disney_feature_number": {
      "type": "integer",
      "description": "The sequential number of the Disney animated feature film."
    },
    "genre_tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genre tags describing the film."
    },
    "primary_production_studio": {
      "type": "string",
      "description": "The main studio that produced the film."
    },
    "additional_animation_facility": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the additional animation studio."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the additional animation studio was founded."
        },
        "founders": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The founders of the additional animation studio."
        },
        "contribution_type": {
          "type": "string",
          "description": "The type of contribution made by the additional animation studio."
        }
      },
      "required": [
        "name",
        "founding_year",
        "founders",
        "contribution_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "disney_feature_number",
    "genre_tags",
    "primary_production_studio",
    "additional_animation_facility"
  ],
  "additionalProperties": false
}

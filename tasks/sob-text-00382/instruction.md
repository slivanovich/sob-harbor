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
Dumb and Dumber (franchise): Dumb and Dumber is a series of comedy films starring Jim Carrey and Jeff Daniels.  The films have been released from 1994 to 2014.

She (Harry Connick Jr. album): She is a funk album by Harry Connick Jr. recorded in 1994, accompanied by his newly formed funk band.  Every song lies within the framework of the rootsy New Orleans style.  *"(I Could Only) Whisper Your Name" was included on Columbia Records' soundtrack from action-comedy "The Mask", starring Jim Carrey.  It was also Connick's only single to reach the "Billboard" charts, peaking at #67.  The album was certified Platinum.

Rubberface: Rubberface is a 1981 television film made for CBC television starring Jim Carrey.  Originally titled "Introducing Janet", it was changed to "Rubberface" for the video release after Carrey's success.

Ace Ventura: Pet Detective: Ace Ventura: Pet Detective (or simply Ace Ventura, or also simply Pet Detective) is a 1994 American comedy film directed by Tom Shadyac, and co-written by and starring Jim Carrey.  It was developed by the film's original writer, Jack Bernstein, and co-producer, Bob Israel, for almost six years.  The film co-stars Courteney Cox, Tone Lōc, Sean Young and former Miami Dolphins quarterback Dan Marino.  In the film, Carrey plays Ace Ventura, an animal detective who is tasked with finding the Miami Dolphins' mascot that was abducted.  The film features a cameo appearance from death metal band Cannibal Corpse.

Dumb and Dumber To: Dumb and Dumber To is a 2014 American comedy film co-written and directed by Bobby and Peter Farrelly.  It is the third film in the "Dumb and Dumber" film series and a direct sequel to the 1994 film "Dumb and Dumber".  It stars Jim Carrey and Jeff Daniels reprising their roles 20 years after the events of the first film, and also features Rob Riggle, Laurie Holden and Kathleen Turner.  The film tells the story of Lloyd Christmas and Harry Dunne (played by Carrey and Daniels, respectively), two dimwitted but good-natured adults who set out on a cross-country road trip to locate Harry's daughter who has been adopted.

Dumb and Dumber: Dumb and Dumber is a 1994 American buddy comedy road film starring Jim Carrey and Jeff Daniels.  It was written by the Farrelly brothers and Bennett Yellin, and is the Farrelly brothers' directorial debut.  The film tells the story of Lloyd Christmas and Harry Dunne, two unintelligent but well-meaning friends from Providence, Rhode Island who set out on a cross-country trip to Aspen, Colorado to return a briefcase full of money to its owner, only to be pursued by a group of criminals who are after the briefcase.

Once Bitten (1985 film): Once Bitten is a 1985 American comedy horror fantasy film starring Lauren Hutton, Jim Carrey, and Karen Kopins.  Carrey stars as Mark Kendall, an innocent and naive high school student who is seduced in a Hollywood, California, nightclub by a sultry blonde countess (Hutton), who unknown to him, is really a centuries-old vampire.  The film was Carrey's seventh film and his first main role.

Lovely (The Primitives album): Lovely is a 1988 studio album by The Primitives.  It features the international hit single "Crash", later featured in remix form as 'The 95 mix' on the "Dumb and Dumber" soundtrack, as well as the UK Top 100 hits "Stop Killing Me", "Thru the Flowers", and "Out of Reach". " Way Behind Me" was issued as a single after the album's initial release, and later included on re-releases as well as on the follow-up album "Pure".

Five Candles (You Were There): "Five Candles (You Were There)" is a song written and performed by Jars of Clay.  It is the second radio single from their 1997 studio album "Much Afraid".  The song was initially written for the soundtrack to the motion picture "Liar Liar", starring Jim Carrey.  However, the ending credits, when the song would have been played, were changed to an outtakes and bloopers reel, thus cutting the song from the film.  A working title of the song during the writing and recording studio sessions was "The Wish", which fits in with the themes of "Liar Liar", just as the eventual title, "Five Candles", as the story of the film revolves around the wish Max made as he blew out the five candles for his fifth birthday.  The song was later used in the 1998 Michael Keaton film, "Jack Frost", and was featured on that film's soundtrack.

Me, Myself &amp; Irene: Me, Myself & Irene is a 2000 American black comedy film directed by the Farrelly brothers, and starring Jim Carrey and Renée Zellweger.  Chris Cooper, Robert Forster, Richard Jenkins, Daniel Greene, Anthony Anderson, Jerod Mixon and Mongo Brownlee co-star.  The film is about a Rhode Island state trooper named Charlie who, after years of continuously suppressing his rage and feelings, suffers a psychotic breakdown which results in a second personality, Hank.  This was also Carrey's first role in a 20th Century Fox film.

Question: The hit single "Crash" was on the soundtrack to the film starring Jim Carrey and Jeff Daniels that was released in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "main_actors": {
      "type": "array",
      "description": "A list of the main actors starring in the film.",
      "items": {
        "type": "string"
      }
    },
    "soundtrack_details": {
      "type": "object",
      "description": "Details about the song featured on the film's soundtrack.",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song on the soundtrack."
        },
        "version_on_soundtrack": {
          "type": "string",
          "description": "The specific version or mix of the song featured on the soundtrack."
        }
      },
      "required": [
        "song_title",
        "version_on_soundtrack"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "main_actors",
    "soundtrack_details"
  ],
  "additionalProperties": false
}

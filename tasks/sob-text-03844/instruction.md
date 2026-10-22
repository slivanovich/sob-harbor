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
Chris Klein (actor): Frederick Christopher "Chris" Klein (born March 14, 1979) is an American actor who is best known for playing Chris 'Oz' Ostreicher in the "American Pie" comedy teen films.

Chris Owen (actor): Chris Owen (born September 25, 1980) is an American actor and photographer.  He is best known for his role as The Sherminator in the "American Pie film franchise", appearing in "American Pie", "American Pie 2", "" and "American Reunion".  Aside from Eugene Levy, he is the only actor from the theatrical features to appear in the ""American Pie Presents:"" direct-to-video spin-off movies.

A Perfect Little Man: A Perfect Little Man is a 1999 American independent short drama filmdirected and written by Jeff Hare starring Neal McDonough as "Billy Morrisson", Tom Hale as "Michael", Jennifer Jostyn as "Mindy", Doug Kruse as "Sid", Michael A. LeMelle as "Young Billy", Dana Lewis as "Ruth Morrison", Tegan West as "Jack Morrison", Peter John White as the "sleazy guy", and Delaine Yates as "Laura".

Ticking Clock: Ticking Clock is a 2011 American action film directed by Ernie Barbarash, and starring Cuba Gooding Jr. and Neal McDonough.  The film was released on direct-to-DVD in the United States on January 4, 2011.  This is the second film between Cuba Gooding, Jr. and Ernie Barbarash, they both previously in 2009's "Hardwired".

Street Fighter: The Legend of Chun-Li: Street Fighter: The Legend of Chun-Li is a 2009 action film based on the "Street Fighter" series of video games.  It follows the quest of "Street Fighter" character Chun-Li, who is portrayed by Kristin Kreuk.  Its story follows Chun-Li's personal history and her journey for justice.  The film co-stars Neal McDonough as M. Bison, Chris Klein as Charlie, Michael Clarke Duncan as Balrog, and Black Eyed Peas member Taboo as Vega.  "The Legend of Chun-Li" was released on February 27, 2009 to mostly negative reviews and poor box office numbers.

American Pie (film): American Pie is a 1999 teen sex comedy film written by Adam Herz and directed by brothers Paul and Chris Weitz, in their directorial film debut.  It is the first film in the "American Pie" theatrical series.  The film was a box-office hit and spawned three direct sequels: "American Pie 2" (2001), "American Wedding" (2003), and "American Reunion" (2012).  The film concentrates on five best friends (Jim, Kevin, Oz, Finch, and Stifler) who attend East Great Falls High.  With the exception of Stifler (who has already lost his virginity), the guys make a pact to lose their virginity before their high school graduation.  The title is borrowed from the song of the same name and refers to a scene in the film, in which the protagonist is caught masturbating with a pie after being told that third base feels like "warm apple pie".  Writer Adam Herz has stated that the title also refers to the quest of losing one's virginity in high school, which is as "American as apple pie."

American Wedding: American Wedding (known as American Pie 3: The Wedding or American Pie: The Wedding, in some countries) is a 2003 American sex comedy film and a sequel to "American Pie" and "American Pie 2".  It is the third (originally intended final) installment in the "American Pie" theatrical series.  It was written by Adam Herz and directed by Jesse Dylan.  Another sequel, "American Reunion", was released nine years later.  This also stands as the last film in the series to be written by Herz, who conceptualized the franchise.

Blue River (film): Blue River is a 1995 American television action film, starring Sam Elliott, Jerry O'Connell, Susan Dey, Nick Stahl and Neal McDonough.  It was directed by Larry Elikann.

American Pie Presents: The Naked Mile: American Pie Presents: The Naked Mile (also known as American Pie: The Naked Mile) is a 2006 American sex comedy film released by Universal Pictures.  It is the second installment in the "American Pie Presents" series and the fifth installment in the "American Pie" franchise.  The film begins a story arc that concludes with "" (2007).  John White stars as Erik Stifler, a high school senior who is given a "guilt free pass" by his girlfriend, Tracy Sterling (Jessy Schram), and so visits the Beta House fraternity led by his cousin, Dwight Stifler (Steve Talley), to run a mile naked.  Christopher McDonald co-stars as Erik's father, Harry, and Eugene Levy once again plays Jim's Dad, who turns out to be a family friend of both Erik's and Tracy's.  Also, it is in this film that his name is revealed to be "Noah Levenstein".

American Pie Presents: The Book of Love: American Pie Presents: The Book of Love (also known as American Pie: The Book of Love) is a 2009 sex comedy film released directly to DVD.  It is the fourth and final installment in the "American Pie Presents" series and the seventh installment in the "American Pie" franchise.  Directed by John Putch, the film stars Bug Hall, John Patrick Jordan, Kevin M. Horton, Brandon Hardesty, and Eugene Levy.  This was Sherman Hemsley's final film appearance before his death on July 24, 2012.

Question: Chris Klein, the American Actor known for his role in "American Pie" also played in which 2009 action film starring Neal McDonough and Kristin Kreuk?

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
      "description": "The year the film was released."
    },
    "genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "key_actors": {
      "type": "array",
      "description": "A list of key actors in the film and their roles.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role_name": {
            "type": "string",
            "description": "The character role played by the actor."
          }
        },
        "required": [
          "actor_name",
          "role_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "key_actors"
  ],
  "additionalProperties": false
}

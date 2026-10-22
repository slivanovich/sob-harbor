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
Pj Perez: Pj Perez (born August 4, 1976) is an American editor, writer and musician, best known for his reports and commentary on Las Vegas culture in such publications as "Rolling Stone".  Perez was the founding managing editor of Las Vegas-based "Racket Magazine".

Nevada Power Company: Nevada Power Company was a Las Vegas-based company that produced, distributed, and sold electricity in the southern part of the state of Nevada.  In 2005, it had over 700,000 electric customers in parts of three Nevada counties — a service area of more than 4000 sqmi .  In 1998, Nevada Power merged with Nevada's other major utility, Sierra Pacific Resources.  It continued as a subsidiary of Sierra Pacific until 2005, when the company changed its name to NV Energy.

Diamond Jo Casino: The Diamond Jo Casino is a gambling casino and entertainment complex located in the Port of Dubuque, in Dubuque, Iowa.  The casino is owned and operated by Las Vegas-based Boyd Gaming, which also owns the Diamond Jo Casino - Worth in Northwood, Iowa.  It is a member of the Iowa Gaming Association, and its license is held by the Dubuque Racing Association, which operates Q Casino.  Beginning operations on May 18, 1994, the Diamond Jo was a 3-level, 305 ft , 1,500-passenger vessel in Dubuque's Ice Harbor.  The boat was a dockside that did not cruise, the casino became land-based when its new facility opened December 11, 2008.

Jack Zwerner: Jack 'Action' Zwerner (born June 12, 1938) is an American professional poker player and business entrepreneur.  He is most known for founding land based casinos, gaming in international waters, and shaping the casino world as it is today.  He is also known for winning the 2006 World Series of Poker (WSOP) Event 8: Omaha Hi-Lo (8 or better).  T. J. Cloutier regards hims as the best heads-up Omaha player ever.

Heavens Cafe: Heavens Cafe is a rock opera written and composed by John Miner.  It was first staged in Las Vegas, Nevada, in 1996.  The opportunity to perform the musical theater project came after Miner's demo was heard by investor Mike Lewis of Las Vegas-based Tributary Music Label after his departure from California-based progressive rock group Mantra Sunrise.  Miner established a new band, named "Art Rock Circus" with drummer Jon Weisberg and bassist Jon Cornell to stage the live performances at the Flamingo Theater in Las Vegas.  Former Follies Bergere performer Kristine Keppel directed the original casting.  In 2003, Los Angeles based theater director John Beane approached Miner about staging the opera in the Los Angeles area later that year.  Beane's new vision for the project came to fruition in May 2004 with a six-week California run at the Insurgo Theater which included Ken Jaquess on bass and Nolan Stolz on drums.

Brian Rouff: Brian Rouff (born 1955) is an American author, freelance journalist and advertising executive, best known for his Las Vegas-based novels: Dice Angel (2002), Money Shot (2004) and The House Always Wins (to be released in October 2017) as well as his chapter in the Las Vegas collaborative serial mystery Restless City (2009).  He is the son of Morris Rouff, inventor of Formula 409.

RawVegas.tv: RawVegas.tv is a defunct video website.  RawVegas was first launched on January 19, 2007 and is the first venture for Raw Networks LLC, a Las Vegas-based Internet television studio that creates and produces short form video content exclusively for the Internet.  Programming on RawVegas.tv includes a daily mix of content that focuses on Las Vegas, including a daily news show, review shows designed to inform both locals and visitors, regular red carpet interviews, a celebrity gossip beat, a number of comedy programs, wagering shows, a slate of reality series starring Las Vegas personalities and poker players and other programs that display life in Las Vegas.

Jake Records: Jake Records is a Las Vegas-based independent record label.

World Series of Poker: The World Series of Poker (WSOP) is a series of poker tournaments held annually in Las Vegas and, since 2005, sponsored by Caesars Entertainment Corporation (known as Harrah's Entertainment until 2010).  It dates its origins to 1970, when Benny Binion invited seven of the best-known poker players to the Horseshoe Casino for a single tournament, with a set start and stop time, and a winner determined by a secret ballot of the seven players.

Zoltan Bathory: Zoltán Báthory, (born May 15, 1978) is a Hungarian-born musician and martial artist.  He is the founder, rhythm guitarist, and one of the main songwriters, for the Las Vegas-based multi-million record selling heavy metal band Five Finger Death Punch.  In 2010, he was named Golden God's "Best Shredder" by Metal Hammer Magazine.  Zoltan is also a founding board member of the veterans non profit Home Deployment Project in Las Vegas.  Home Deployment Project works to save and reintegrate homeless veterans.

Question: Jack Zwerner won an event at which Las Vegas-based set of tournaments?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "winner_name": {
      "type": "string",
      "description": "The name of the person who won the event."
    },
    "tournament_name": {
      "type": "string",
      "description": "The name of the tournament series."
    },
    "event_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the event was won."
        },
        "event_number": {
          "type": "string",
          "description": "The specific event number or identifier."
        },
        "game_type": {
          "type": "string",
          "description": "The type of game played in the event."
        }
      },
      "required": [
        "year",
        "event_number",
        "game_type"
      ],
      "additionalProperties": false
    },
    "tournament_location": {
      "type": "string",
      "description": "The primary city where the tournament is held."
    },
    "is_las_vegas_based": {
      "type": "boolean",
      "description": "Indicates if the tournament is based in Las Vegas."
    }
  },
  "required": [
    "winner_name",
    "tournament_name",
    "event_details",
    "tournament_location",
    "is_las_vegas_based"
  ],
  "additionalProperties": false
}

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
Francis Buxton: Francis William Buxton (5 August 1847 – 14 November 1911) was a British barrister and Liberal Party politician.

Adam Buxton (footballer): Adam Mark Buxton (born 12 May 1992) is an English professional footballer who plays as a defender for Tranmere Rovers.

Discovery (1960s TV series): Discovery was a television program geared towards children and teenagers, produced by ABC News.  The program began in the fall of 1962 as a weekday series, and was later moved to Sunday mornings.  The program was hosted by actor/announcer Frank Buxton and actress/vocalist Virginia Gibson.  The show's original studio announcer was ABC staff announcer Bill Owen, who replaced Buxton as host in 1966, continuing through 1971.  The shows hosted by Buxton were mostly studio productions, done in black-and-white; beginning with Owen, the shows were produced in color, and involved much travel to on-site locations.  The actual on-air title of the series was named according to each year it was produced, beginning with "Discovery '62" and ending with "Discovery '71" (syndicated reruns only had the title "Discovery").

Outside My Window (Sarah Buxton song): "Outside My Window" is a song co-written and recorded by American country music artist Sarah Buxton.  The song was released in June 2009 as the lead-off single from her self-titled debut album, which was released in February 2010.  It has since become Buxton's second Top 30 hit on the U.S. "Billboard" Hot Country Songs chart, as well as the highest-charting single of her career.  Buxton wrote this song with Victoria Shaw, Gary Burr and Mark Hudson.

Pee-wee's Big Adventure: Pee-wee's Big Adventure is a 1985 American adventure comedy film directed by Tim Burton in his full-length film directing debut and starring Paul Reubens as Pee-wee Herman with supporting roles provided by Elizabeth Daily, Mark Holton, Diane Salinger, and Judd Omen.  Reubens also co-wrote the script with Phil Hartman and Michael Varhol.  Based on the 1948 Italian classic "The Bicycle Thief", it is the tale of Pee-wee Herman embarking on a nationwide adventure in search for his stolen bicycle.

Park Road, Buxton: Park Road is a cricket ground in Buxton, Derbyshire, England.  It is the home ground of Buxton Cricket Club, and was formerly used by the Derbyshire County Cricket Club first XI between 1923 and 1986.  The first First-class match on the ground was in June 1923, when Derbyshire faced the touring West Indians.  The ground’s biggest claim to fame was in 1975, when the second day’s play of the County Championship match against Lancashire was wiped out due to snow.  Derbyshire generally played one County Championship match at Buxton every year between 1930 and 1976, but only four thereafter.  The most recent First-class match was in August 1986 against Lancashire, who have provided the opposition for 26 of the 48 first-class games at the ground.  The ground also hosted ten Derbyshire List A fixtures between 1969 and 1986.

Charles L. Glover: Charles L. Glover (December 1842 – 1916) was a six-term Democratic mayor of Norwalk, Connecticut from 1897 to 1901, from 1902 to 1903, and also in 1905.  He ran for mayor seven times, and was only beaten once, by George Buxton.  However he defeated Buxton a year later.

Rush Hour (UK TV series): Rush Hour is a sketch show made by Zeppotron and shown on BBC Three during March and April 2007.  The show featured several sketches centred on characters travelling to work, school or otherwise, therefore many of the sketches took place inside a car or bus.  Several cult and up and coming comedians and comic actors star in the show, each performing several of the characters.  The cast includes Adam Buxton, Sanjeev Kohli, Miranda Hart, Frankie Boyle, David Armand, Marek Larwood, Kerry Godliman, Bruce Mackinnon, Naomi Bentley, Lorna Watson, and Katy Wix.

Mark Holton: Mark Holton (born July 19, 1958) is an American actor, best known for portraying Chubby in the "Teen Wolf" film series, Francis Buxton in "Pee-wee's Big Adventure", and Ozzie in "Leprechaun".

Stupid Boy: "Stupid Boy" is a song that was written by Dave Berg, Deanna Bryant and Sarah Buxton.  First recorded by Sarah Buxton, it was later recorded by Australian country music singer Keith Urban on his 2006 album "Love, Pain & the Whole Crazy Thing", from which it was released as that album's second single in December 2006.  A year after its release, the song won Urban a Grammy Award for Best Male Country Vocal Performance.

Question: What year did Mark Holton star as Francis Buxton?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character portrayed by the actor."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film in which the character appeared."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "film_title",
    "release_year"
  ],
  "additionalProperties": false
}

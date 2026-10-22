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
Billy Mohler: Billy Mohler is a Grammy-nominated producer, songwriter, and multi-instrumentalist.  He was raised in South Orange County and is Bill Medley's (of the Righteous Bros.) godson.  He attended and graduated from Berklee College of Music where he studied electric, bass and acoustic bass.  Mohler then received a full scholarship to the prestigious Thelonious Monk Institute of Jazz at UCLA.  He was a member of the rock band The Calling (until 2002).  The band's debut record Camino Palmero has sold more than 5 million copies worldwide.

Where Sleeping Dogs Lie: Where Sleeping Dogs Lie is a 1991 thriller film directed by Charles Finch and starred Dylan McDermott, Sharon Stone and Tom Sizemore.  The primary location for "Sleeping Dogs" was C.E. Toberman Estate, a large Mediterranean-style, 22-room house built at the top of Camino Palmero in 1928 by C. E. Toberman.

Could It Be Any Harder: "Could It Be Any Harder" is the third single from The Calling's debut album, "Camino Palmero".  Released in 2002, it peaked at number #22 in Italy.

Fin Del Camino: "Fin Del Camino" is the 43rd episode of the US television series, "Prison Break" and is the 21st episode of its second season.  The English translation of the Spanish phrase, "fin del camino", is "end of the road".  Written by Matt Olmstead and Seth Hoffman, and directed by Bobby Roth, the episode first aired on March 26, 2007.  The premise of the episode directly follows the events of the previous episode and includes two major plots with one taking place in Panama City and the other in Chicago.  Regarding the casting of this episode, Rockmond Dunbar (who plays Benjamin Miles "C-Note" Franklin), does not appear in this episode.

Camino Palmero: Camino Palmero is the debut album by American alternative band The Calling, released on July 10, 2001.  It contains their hit single "Wherever You Will Go".  The title of the album comes from a Los Angeles street where band members Alex Band and Aaron Kamin first met.  The record has many grunge influences and also has a lot of guitar solos.

C.E. Toberman Estate: The C. E. Toberman Estate, also known as Villa Las Colinas, is a gated Mission Revival mansion and estate on Camino Palmero in Hollywood, Los Angeles, California.  It was listed on the National Register of Historic Places in 1983, and as a Los Angeles Historic-Cultural Monument in 1984. .

The Calling: The Calling was an American rock band from Los Angeles, California, best known for its hit single, "Wherever You Will Go".  The group formed in 1999 and released two albums, "Camino Palmero" and "Two", before breaking up 2005.  Lead singer Alex Band reformed The Calling in 2013 with a new lineup that performed a few concerts before permanently breaking up.

Adrienne (The Calling song): "Adrienne" is the second single from The Calling's debut album, "Camino Palmero", which was released on July 10, 2001.

Wherever You Will Go: "Wherever You Will Go" is the debut single by American band The Calling.  The song was released in June 2001 as the first single from their debut album "Camino Palmero".  It remains their most renowned and their most successful hit, peaking at number 5 on the "Billboard" Hot 100 and topping the Adult Top 40 for 23 weeks, the second longest running number one in the chart's history, behind "Smooth" by Santana and Rob Thomas.  It was named the number 1 song of the decade of 2000's on the Adult Pop Charts by "Billboard" magazine.

APRS Calling: APRS Calling is a manual procedure for calling stations on the Automatic Packet Reporting System (APRS) to initiate communications on another frequency, or possibly by other means.  It is inspired by Digital Selective Calling, a part of the Global Maritime Distress Safety System.  It also builds on existing digital procedures inherited from morse code and radioteletype operation.  ITU Q codes are used in conjunction with APRS text messages to implement APRS calling.  APRS calling is intended to complement monitoring voice calling frequencies.

Question: What city was Camino Palmero inspired by, and The Calling found in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the question."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band mentioned in the question."
    },
    "album_inspiration_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city that inspired the album's title."
        },
        "state": {
          "type": "string",
          "description": "The state where the inspiring city is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "band_founding_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the band was founded."
        },
        "state": {
          "type": "string",
          "description": "The state where the band was founded."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "band_name",
    "album_inspiration_location",
    "band_founding_location"
  ],
  "additionalProperties": false
}

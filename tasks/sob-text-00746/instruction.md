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
Ken Barlow: Kenneth "Ken" Barlow is a fictional character from the British ITV soap opera, "Coronation Street", played by William Roache.  Ken was created by Tony Warren as one of "Coronation Street's" original characters.  He debuted in the soap's first episode on 9 December 1960.  Having appeared continuously since the programme's inception, December 2010 marked Ken's 50th anniversary on-screen.  At this time, Roache officially became the longest-serving actor in a televised soap opera.  Roache was honoured at the 2010 Guinness World Records ceremony for the achievement, when he surpassed actor Don Hastings from the American soap opera "As the World Turns", who previously held this title.  Roache stated in 2010 that he has no plans to leave the role and will remain in "Coronation Street" for as long as they will have him.

The Road to Coronation Street: "The Road to Coronation Street" was written by Daran Little, a long-time archivist on "Coronation Street" who became a scriptwriter.  At the time, however, Little was a scriptwriter for "Coronation Street"' s rival, "EastEnders", broadcast on BBC One.  Though "Coronation Street" is, and always has been, broadcast on ITV, a competing network, the idea of documenting the show on the anniversary of its half century running was picked up by its natural rival, the BBC.  It has, however, been repeated several times on ITV3 and, on the occasion of Tony Warren's death, ITV.

Sian Powers: Sian Powers is a fictional character from the British ITV soap opera, "Coronation Street", portrayed by Sacha Parkinson.  Sian was introduced as a love interest for Sophie Webster (Brooke Vincent).  Sian joined the cast of "Coronation Street" alongside Ben Richardson (Lucien Laviscount) in January 2009 as Sophie's schoolmates.  They soon form a new group of teenagers along with Ryan Connor (Ben Thompson).  Sian and girlfriend Sophie are "Coronation Street's" first lesbian couple.  It was announced on 29 May 2011 that Parkinson had quit her role, and she made her last on screen appearance on 30 December 2011.

Karl Munro: Karl Munro is a fictional character from the British ITV soap opera, "Coronation Street", played by John Michie.  Michie's casting was announced in April 2011.  He signed an initial one-year contract and began filming his scenes in May.  Upon joining the cast, Michie was told that producers would initially "bed [him] in", before increasing his involvement in the show in 2012.  Michie is from Scotland, but because "Coronation Street" is set in Manchester, he uses a Mancunian accent for the role.  Karl was introduced along with his girlfriend, Stella Price (Michelle Collins) and her daughter, Eva (Catherine Tyldesley).  Karl made his first appearance in the episode broadcast on 17 June 2011.  On 30 April 2013, it was announced that Michie would be leaving "Coronation Street".  Karl departed during the episode broadcast on 13 September 2013.

Alan Browning: Alan Browning (born Alan Brown; 23 March 1926 – 7 September 1979) was an English actor.  He is best remembered for portraying Alan Howard in the television series "Coronation Street", a role he played from 1969 to 1973.  He was married to his "Coronation Street" co-star Pat Phoenix from 23 December 1972, until his 1979 death from liver failure as a result of his heavy alcohol intake.  Phoenix played his on screen wife, Elsie Tanner, in "Coronation Street".

Elsie Tanner: Elsie Gregory (also Grimshaw, Tanner and Howard) is a fictional character from the British ITV soap opera, "Coronation Street", played by Pat Phoenix from the series inception in 1960 to 1973 and from 1976 until 1984.  Elsie Tanner was one of the original core characters on "Coronation Street" and appeared in the very first episode.  She is considered something of an icon in soap history and regarded as one of "Coronation Street's" greatest ever characters.

Keep It in the Family (UK game show): Keep It in the Family is a British game show that aired on ITV from 26 October 2014 to 19 December 2015 and is hosted by Bradley Walsh.

Bradley Walsh: Bradley John Walsh (born 4 June 1960) is an English actor, comedian, singer, television presenter and former professional footballer, best known for his roles as Danny Baldwin in "Coronation Street" and the lead role of in "", as well as hosting ITV game shows "The Chase" and "Cash Trapped".

Coronation Street: Coronation Street (informally known as Corrie) is a British soap opera created by Granada Television and shown on ITV since 9 December 1960.  The programme centres on Coronation Street in Weatherfield, a fictional town based on inner-city Salford, its terraced houses, café, corner shop, newsagents, building yard, taxicab office, salon, restaurant, textile factory and the Rovers Return pub.  In the show's fictional history, the street was built in 1902 and named in honour of the coronation of King Edward VII.

James Roache: William James Roache (born 29 December 1985) is an English actor who is perhaps best known for his roles in connection with his father William Roache.  In "Coronation Street" he played James, the long-lost grandson of Ken Barlow (played by his father).  He also played the role of his own father William as a young man in the BBC drama "The Road to Coronation Street".

Question: The game show Keep It in the Family was hosted by an actor that played what role in "Coronation Street"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_show_name": {
      "type": "string",
      "description": "The name of the game show."
    },
    "game_show_host": {
      "type": "string",
      "description": "The host of the game show."
    },
    "host_coronation_street_role": {
      "type": "string",
      "description": "The role played by the host in Coronation Street."
    },
    "coronation_street_details": {
      "type": "object",
      "properties": {
        "soap_opera_name": {
          "type": "string",
          "description": "The name of the soap opera."
        },
        "network": {
          "type": "string",
          "description": "The television network where the soap opera is shown."
        },
        "debut_date": {
          "type": "string",
          "description": "The date the soap opera first aired."
        }
      },
      "required": [
        "soap_opera_name",
        "network",
        "debut_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "game_show_name",
    "game_show_host",
    "host_coronation_street_role",
    "coronation_street_details"
  ],
  "additionalProperties": false
}

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
Bruce Strachan: William Bruce Strachan (Bruce Strachan) (born July 22, 1941) is a former politician in the Canadian province of British Columbia.  Strachan was a school trustee and board chair, a regional district director, as well as a three-term MLA and cabinet minister.  He served in the Legislative Assembly of British Columbia from 1979 to 1991, as a Social Credit member for the constituency of Prince George South.

Thomas Bruce (British Army officer): General Thomas Bruce (1738 – 12 December 1797), was a British soldier and politician, the third son of William Bruce, 8th Earl of Kincardine.

Charlemagne: The Omens of Death: Charlemagne: The Omens of Death is the fourth and final album by actor and heavy metal singer Christopher Lee.  It was released on 27 May 2013.  It is a sequel to his album "" (2010).  The music was arranged by Judas Priest's Richie Faulkner, and features prominent Guatemalan guitar virtuoso and World Guitar Idol Champion Hedras Ramos on guitar, as well as his father, Hedras Ramos Sr, on bass.

Hedras Ramos: Hedras David Ramos Velasquez (colloquially: Hedras Ramos) (born February 3, 1992 in Guatemala City, Guatemala) is a Guatemalan multi-instrumentalist, specializing in guitar.  Throughout his career he has opened for popular bands such as Kansas, Whitecross, Die Toten Hosen, and was chosen by Axl Rose to open for Guns N' Roses on their "Chinese Democracy" show in Guatemala.

Bruce Johnstone (racing driver): Bruce Johnstone (born William Bruce Gordon Johnstone on 30 January 1937 in Durban) is a former racing driver from South Africa.  He participated in one Formula One World Championship Grand Prix, on 29 December 1962.  He scored no championship points.

Annette Hanshaw: Catherine Annette Hanshaw (October 18, 1901 – March 13, 1985) was an American Jazz Age singer.  She was one of the most popular radio stars of the 1930s.  Over four million of her records had been sold by 1934.  In her ten-year recording career, she recorded about 250 sides.  In a 1934 poll conducted by "Radio Stars" magazine, she received the title of best female popular singer (Bing Crosby was voted the best male popular singer).  Second place went to Ethel Shutta, third place went to Ruth Etting, and fourth place went to Kate Smith.

William B. Meeks Jr.: William Bruce Meeks Jr. (aka William Bruce Meeks II; March 2, 1921 – September 8, 1999) was a producer, composer and arranger of radio jingles and founder of PAMS in Dallas; which, according to "Billboard" in 1972, was the largest jingles firm in the world.

Harry Brannon: Harry Brannon (June 19, 1920 – December 29, 1991) was an American popular singer born in Gloucester City, New Jersey.

Axl Rose: W. Axl Rose (born William Bruce Rose Jr.; raised as William Bruce Bailey; February 6, 1962) is an American singer, songwriter, record producer and musician.  He is the lead vocalist of the hard rock band Guns N' Roses, and has also been the band's sole constant member since its inception in 1985.  In addition to Guns N' Roses, he has been the lead singer of AC/DC since 2016.  Due to his powerful and wide vocal range and energetic live performances, Rose has been named one of the greatest singers of all time by various media outlets, including "Rolling Stone" and "NME".

Bert Rose: Bert E. Rose Jr (September 26, 1919 – October 14, 2001) was a football executive.  He graduated from the University of Washington in 1941.  He later worked as an assistant athletic director for sports publicity at Washington.  He was the director of public relations with the Los Angeles Rams of the NFL.  He was named the first general manager of the Minnesota Vikings on August 5, 1960.  He stayed with the team until June 1, 1964.  He was named executive vice president and GM of the New Orleans Saints on July 20, 1967.  He worked in the front office of the NFL and also as the manager of Texas Stadium.

Question: Hedras Ramos has opened for which popular singer born William Bruce Rose Jr?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_name": {
      "type": "string",
      "description": "The common name of the singer."
    },
    "singer_birth_name": {
      "type": "string",
      "description": "The birth name of the singer."
    },
    "singer_primary_role": {
      "type": "string",
      "description": "The primary role of the singer."
    },
    "band_hedras_ramos_opened_for": {
      "type": "string",
      "description": "The name of the band for which Hedras Ramos opened, associated with the singer."
    },
    "opening_event_details": {
      "type": "string",
      "description": "Specific details about the event where Hedras Ramos opened for the band."
    }
  },
  "required": [
    "singer_name",
    "singer_birth_name",
    "singer_primary_role",
    "band_hedras_ramos_opened_for",
    "opening_event_details"
  ],
  "additionalProperties": false
}

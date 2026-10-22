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
A Stray Goat: A Stray Goat (; lit.  Snowflake) is a South Korean film written and directed by Cho Jae-min and starring Park Jin-young and Ji Woo.  The film marks Park Jin-young's big screen debut.

Like Land and Sky: Like Land And Sky (; also known as As Much as Heaven and Earth) is a 2007 South Korean television series starring Park Hae-jin, Han Hyo-joo, Lee Joo-hyun, Kang Jung-hwa, and Hong Soo-ah.  It aired on KBS1 from January 15 to August 31, 2007 on Mondays to Fridays at 20:25 for 165 episodes.

Jang Hang-jun: Jang Hang-jun (born September 17, 1969) is a South Korean film and television director and screenwriter.  Jang directed films, including "Break Out" (2002) and "Spring Breeze" (2003).  In 2011, he turned to the small screen, co-wrote and directed "Sign", a medical crime investigation drama starring Park Shin-yang and Kim Ah-joong.

Punch (2011 film): Punch () is a 2011 South Korean coming-of-age film directed by Lee Han about the budding mentor-mentee relationship forged between a rebellious high school student from a poor household (Yoo Ah-in) and his meddlesome homeroom teacher who moves in next door (Kim Yoon-seok).

Sungkyunkwan Scandal: Sungkyunkwan Scandal () is a South Korean historical drama starring Park Min-young, Park Yoo-chun, Yoo Ah-in and Song Joong-ki.  Directed by Kim Won-seok and written by Kim Tae-hee, it is based on Jung Eun-gwol's bestselling 2007 novel "".  It aired on KBS2 from August 30 to November 2, 2010 on Mondays and Tuesdays at 21:55 for 20 episodes.

Alive (2015 film): Alive () is a 2015 South Korean drama film starring Park Jung-bum and Lee Seung-yeon.  Written and directed by Park, it tells the story of a broke laborer's struggle for survival.

Love, Lies (2016 film): Love, Lies () is 2016 South Korean period drama film directed by Park Heung-sik, reuniting "The Beauty Inside" co-stars Han Hyo-joo, Chun Woo-hee and Yoo Yeon-seok.  The story takes place in 1943, during the Imperial Japanese occupation of Korea.  In the film, best friends Jung So-yul (Han Hyo-joo) and Seo Yeon-hee (Chun Woo-hee) are two of the last remaining "gisaeng".  Although they enjoy pop music, they are committed to singing "jeongga", or classical Korean songs.  So-yul's life falls apart when her lover, pop music producer Kim Yoon-woo (Yoo Yeon-seok), falls in love with Yeon-hee and helps her debut as a pop singer.  The story follows So-yul's downward spiral as she is consumed by uncontrollable jealousy.

My Dear Desperado: My Dear Desperado (; lit.  My Gangster Lover) is a 2010 South Korean romantic comedy film written and directed by Kim Kwang-sik, and starring Park Joong-hoon and Jung Yu-mi as two people who become semi-basement one-room neighbors: brave yet jobless Se-jin and Dong-chul, the neighborhood gangster who always gets beaten up.  The film received 688,832 admissions nationwide.  This film was remade in Hindi titled "Jayantabhai Ki Luv Story" in 2013 starring Vivek Oberoi opposite Neha Sharma in lead roles.  The movie was officially remade in Tamil by Nalan Kumarasamy titled "Kadhalum Kadandhu Pogum" for which () or ₩71,587,640.57 was paid as copyrights.

Park Hyo-joo: Park Hyo-joo (born October 8, 1982) is a South Korean actress.  She is best known for her leading role in the period police procedural "Chosun Police Season 1" (also known as "Byeolsungeom"), as well as her supporting roles in the hit film "Punch", and the television series "Air City", "Girl K", and "The Chaser".

I Need Romance 3: I Need Romance 3 () is a 2014 South Korean television series starring Kim So-yeon, Sung Joon, Namkoong Min, Wang Ji-won, Park Hyo-joo, Yoon Seung-ah and Park Yu-hwan.  It aired on cable channel tvN from January 13 to March 4, 2014 on Mondays and Tuesdays at 22:00 for 16 episodes.

Question: The film Punch starring Park Hyo-joo, was directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "actor_mentioned": {
      "type": "string",
      "description": "The name of the actor mentioned in the question."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "director_name",
    "actor_mentioned"
  ],
  "additionalProperties": false
}

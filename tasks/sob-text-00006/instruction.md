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
Imaginary Cat: Imaginary Cat () is an 8-episode South Korean television series starring Yoo Seung-ho.  It aired on cable network MBC Every 1, every Tuesday at 20:50 (KST) from November 24, 2015, to January 12, 2016.

Blind (2011 film): Blind () is a 2011 South Korean crime thriller film directed by Ahn Sang-hoon with screenplay by Choi Min-seok which won the "Hit By Pitch" project fair held by the Korean Movie Producers Guild in 2009.  It stars Kim Ha-neul and Yoo Seung-ho.  Kim received Best Actress honors at the 48th Grand Bell Awards and the 32nd Blue Dragon Film Awards for her performance.

Warrior Baek Dong-soo: Warrior Baek Dong-soo () is a 2011 South Korean fusion historical/action television series starring Ji Chang-wook in the title role, with Yoo Seung-ho, Yoon So-yi, Shin Hyun-bin, Choi Min-soo and Jun Kwang-ryul.  It aired on SBS from July 4 to October 10, 2011, on Mondays and Tuesdays at 21:55 for 29 episodes.

Yoo Seung-ho: Yoo Seung-ho (; born 17 August 1993) is a South Korean actor who rose to fame as a child actor in the film "The Way Home" (2002).  After his two-year mandatory military service, he headlined the legal drama "" (2015) and historical films "The Magician" (2015), "" (2016), as well as historical drama "" (2017).

The Emperor: Owner of the Mask: The Emperor: Owner of the Mask () is a South Korean television series starring Yoo Seung-ho, Kim So-hyun, Kim Myung-soo, Yoon So-hee, Heo Joon-ho and Park Chul-min.  It aired on MBC every Wednesday and Thursday at 22:00 (KST) from May 10, 2017 for 40 episodes.

The Way Home (2002 film): The Way Home () is a 2002 film written and directed by Lee Jeong-hyang.  It tells the heart-warming story about a grandmother and her city-born grandson who comes to live with her in a rural village.  The film, which reminds the younger generation of the unconditional love and care that old people selflessly give, won South Korea's equivalent of the Oscars for best picture and screenplay.  It was the second-highest grossing homegrown film in South Korea in 2002.  It was released on DVD, with English subtitles, in 2003 by Paramount.

Missing You (2013 TV series): Missing You (; also known as I Miss You) is a 2012 South Korean television series starring Yoon Eun-hye, Park Yoo-chun and Yoo Seung-ho.  It aired on MBC from November 7, 2012 to January 17, 2013 on Wednesdays and Thursdays at 21:55 for 21 episodes.

Homo Academicus: Homo Academicus (Hangul: 공부하는 인간: 호모 아카데미쿠스 ) is a South Korean documentary television program broadcast by Korean Broadcasting System (KBS).  It is narrated by Yoo Seung-ho, and hosted by Lilli Margolin, Scott Yim, Jenny Martin, and Bryan Kauder.

4th Period Mystery: 4th Period Mystery (), released internationally as The Clue, is a 2009 South Korean thriller film starring Yoo Seung-ho and Kang So-ra.

Operation Proposal: Operation Proposal () is a 2012 South Korean television series starring Yoo Seung-ho and Park Eun-bin.  It aired on TV Chosun from February 8 to March 29, 2012 on Wednesdays and Thursdays at 20:45 for 16 episodes.  It is a remake of Japanese drama "Operation Love" (プロポーズ大作戦 , Proposal Daisakusen ) that aired on Fuji TV in 2007.

Question: The Way Home, starring South Korean actor Yoo Seung-ho, was released in what year?

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
    "actor_involved": {
      "type": "string",
      "description": "The name of the actor mentioned in the question."
    },
    "film_type": {
      "type": "string",
      "description": "The genre or type of the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "actor_involved",
    "film_type"
  ],
  "additionalProperties": false
}

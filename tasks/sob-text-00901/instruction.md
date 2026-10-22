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
The Devil (TV series): The Devil () is a 2007 South Korean television series starring Uhm Tae-woong, Ju Ji-hoon, and Shin Min-a.  It aired on KBS2 from March 21 to May 24, 2007 on Wednesdays and Thursdays at 21:55 for 20 episodes.

Shin Min-a: Shin Min-a (born Yang Min-a on April 5, 1984) is a South Korean model and actress.  She is best known for starring in television dramas "A Love to Kill" (2005), "My Girlfriend Is a Nine-Tailed Fox" (2010), "Arang and the Magistrate" (2012), "Oh My Venus" (2015), and "Tomorrow With You" (2017).

Bad Love (TV series): Bad Love () is a 2007 South Korean television drama series starring Kwon Sang-woo, Lee Yo-won, and Kim Sung-soo.  It aired on KBS2 from December 3, 2007 to February 5, 2008 on Mondays and Tuesdays at 21:55 for 20 episodes.

Hello! Miss: Hello!  Miss (; also known as Hello!  My Lady) is a 2007 South Korean television series starring Lee Da-hae, Lee Ji-hoon, Ha Seok-jin and Yeon Mi-joo.  Based on Lee Ji-wan's novel "Five Kimchi Mandu", the series aired on KBS2 from March 19 to May 8, 2007 on Mondays and Tuesdays at 21:55 for 16 episodes.

The King 2 Hearts: The King 2 Hearts () is a 2012 South Korean television series, starring Ha Ji-won and Lee Seung-gi in the leading roles.  It is about a South Korean crown prince who falls in love with a North Korean special agent.  The series aired on MBC from March 21 to May 24, 2012 on Wednesdays and Thursdays at 21:55 for 20 episodes.

A Happy Woman: A Happy Woman (; also known as Blissful Woman) is a 2007 South Korean television series starring Yoon Jung-hee, Kim Suk-hoon and Jung Gyu-woon.  It aired on KBS2 from January 6 to July 21, 2007 on Saturdays and Sundays at 19:55 for 58 episodes.

Man from the Equator: Man from the Equator (; also known as The Equator Man) is a 2012 South Korean television series, starring Uhm Tae-woong, Lee Joon-hyuk, Lee Bo-young and Im Jung-eun.  A tense, emotionally charged tale of brotherhood and betrayal, it follows two best friends with a tragic, twisted history that follows them from youth to adulthood.  It aired on KBS2 from March 21 to May 24, 2012 on Wednesdays and Thursdays at 21:55 for 20 episodes.

H.I.T (TV series): H.I.T (), also known as Homicide Investigation Team, is a 2007 South Korean television series starring Go Hyun-jung, Ha Jung-woo, Kim Jung-min, and Yoon Ji-min.  It aired on MBC from March 19 to May 22, 2007 on Mondays and Tuesdays at 21:55 for 20 episodes.  A police procedural crime drama that integrated crime scene analysis with action, suspense, and romance, "H.I.T" represented a departure from the usual Korean drama subjects of love and relationships.

Thank You (TV series): Thank You () is a 2007 South Korean television series starring Jang Hyuk, Gong Hyo-jin, Seo Shin-ae, Shin Sung-rok and Shin Goo.  It aired on MBC from March 21 to May 10, 2007 on Wednesdays and Thursdays at 21:55 for 16 episodes.

I Am Sam (TV series): I am Sam () is a 2007 South Korean television series starring Yang Dong-geun, Park Min-young, Park Jun-gyu, Son Tae-young, and T.O.P in his acting debut.  It aired on KBS2 from August 6 to October 2, 2007, on Mondays and Tuesdays at 21:55 for 16 episodes.  Based on the Japanese comic series "Kyōkasho ni Nai!"  (in English, "Not in a Textbook!"  or "Very Private Lesson"), Yang plays a geeky, straight-arrowed, under-qualified high school teacher who becomes a live-in tutor for the troublemaking daughter of a notorious gangster, in exchange for one million won.

Question: What actor best known for starring in the television drama "A Love to Kill", starred in  a 2007 South Korean television series that aired on KBS2 from March 21 to May 24, 2007 ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor identified by the question."
    },
    "known_for_drama": {
      "type": "string",
      "description": "The television drama the actor is best known for."
    },
    "matching_series": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the television series that matches the criteria."
        },
        "air_channel": {
          "type": "string",
          "description": "The channel on which the series aired."
        },
        "air_start_date": {
          "type": "string",
          "description": "The start date of the series' airing."
        },
        "air_end_date": {
          "type": "string",
          "description": "The end date of the series' airing."
        },
        "air_year": {
          "type": "integer",
          "description": "The year the series aired."
        }
      },
      "required": [
        "title",
        "air_channel",
        "air_start_date",
        "air_end_date",
        "air_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "known_for_drama",
    "matching_series"
  ],
  "additionalProperties": false
}

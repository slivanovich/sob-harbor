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
Asghar Farhadi: Asghar Farhadi (Persian: اصغر فرهادی‎ ‎ ; ]    born 7 May 1972) is an Iranian film director and screenwriter.  Among other awards, he has received a Golden Globe Award as well as two Academy Awards for Best Foreign Language Film for his movies "A Separation" and "The Salesman" in 2012 and 2017, respectively.  He was named one of the 100 Most Influential People in the world by "Time" magazine in 2012.

Ahmad Mehranfar: Ahmad Mehranfar Persian: احمد مهرانفر‎ ‎ , is an Iranian film and stage actor.  His most famous film is "About Elly", directed by Asghar Farhadi in 2008 and series "Paytakht".

A Separation: A Separation (Persian: جدایی نادر از سیمین‎ ‎ "Jodaí-e Nadér az Simín", "The Separation of Nader from Simin") is a 2011 Iranian drama film written and directed by Asghar Farhadi, starring Leila Hatami, Peyman Moaadi, Shahab Hosseini, Sareh Bayat, and Sarina Farhadi.  It focuses on an Iranian middle-class couple who separate, the disappointment and desperation suffered by their daughter due to the egotistical disputes and separation of her parents, and the conflicts that arise when the husband hires a lower-class caregiver for his elderly father, who suffers from Alzheimer's disease.

Sarina Farhadi: Sarina Farhadi (Persian: سارینا فرهادی‎ ‎ ) is an Iranian actress.  She is the daughter of Parisa Bakhtavar and Academy Award-winning director Asghar Farhadi.  She was born in Tehran, Iran.

About Elly: About Elly (Persian: درباره الی‎ ‎ , translit.  "Dar bāre-ye Elly") is a 2009 Iranian drama film directed by Asghar Farhadi.  It is the fourth film by Farhadi.  The film is about the relationships between some middle class families in Iran.

Fireworks Wednesday: Fireworks Wednesday (Persian: چهارشنبه سوری‎ ‎ , Chaharshanbe Suri) is a 2006 Iranian drama film directed by Asghar Farhadi and co-written by Farhadi and Mani Haghighi.  It stars Hedyeh Tehrani, Taraneh Alidousti, and Hamid Farokhnezhad.

Michael Herz (producer): Michael Herz is an American film producer, director and screenwriter.  With Lloyd Kaufman, the two are the co-founders of Troma Entertainment, the world's longest running independent film studio, known for their comedic horror films, including the cult favorite "Toxic Avenger series and "Tromeo and Juliet".

The Salesman (2016 film): The Salesman (Persian: فروشنده‎ , "Forušande " ‎ ) is a 2016 drama film directed and written by Asghar Farhadi and starring Taraneh Alidoosti and Shahab Hosseini.  It is about a married couple who perform Arthur Miller's play "Death of a Salesman" on stage, when the wife is assaulted.  Her husband attempts to determine the identity of the attacker, while she struggles to cope with post-trauma stress.  Farhadi chose Miller's play as his story within a story based on shared themes.  The film was shot in Tehran, beginning in 2015.

9th Bengaluru International Film Festival 2017: 9th Bengaluru International Film Festival - 2017 (BIFFES - 2017) was held from 2 to 9 February 2017 in Bengaluru and Mysuru, in the Indian state of Karnataka.  A total of 240 films from 60 countries including Oscar nominees of the year such as The Salesman by Iranian director Asghar Farhadi and A Man Called Ove by Swedish director Hannes Holm were screened over a period of 8 days.

Peyman Moaadi: Payman Moadi (Persian: پیمان مُعادی‎ ‎ ) is an Iranian-American actor, screenwriter and director.  He is best known for starring in the films "A Separation" and "About Elly" by director Asghar Farhadi and the independent drama film "Camp X-Ray".

Question: Are Michael Herz and Asghar Farhadi both nationals of the same country ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person mentioned in the question."
    },
    "person_1_nationality": {
      "type": "string",
      "description": "The nationality of the first person."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person mentioned in the question."
    },
    "person_2_nationality": {
      "type": "string",
      "description": "The nationality of the second person."
    },
    "are_same_nationality": {
      "type": "boolean",
      "description": "True if both individuals share the same nationality, false otherwise."
    }
  },
  "required": [
    "person_1_name",
    "person_1_nationality",
    "person_2_name",
    "person_2_nationality",
    "are_same_nationality"
  ],
  "additionalProperties": false
}

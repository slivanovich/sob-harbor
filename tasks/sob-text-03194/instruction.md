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
Bae Doona: Bae Doo-na (; ] ; born October 11, 1979) is a South Korean actress and photographer.  She first became known outside Korea for her roles as a political activist in Park Chan-wook's "Sympathy for Mr. Vengeance" (2002), archer Park Nam-joo in Bong Joon-ho's "The Host" (2006), and as an inflatable sex doll-come-to-life in Hirokazu Koreeda's "Air Doll" (2009).  She has had English-speaking roles in the Wachowski films "Cloud Atlas" (2012) and "Jupiter Ascending" (2015), and the TV series "Sense8" (2015-present).

Someday (TV series): Someday () is a 2006 South Korean television series starring Bae Doona Kim Min-joon, Lee Jin-wook, and Oh Yoon-ah.  It aired on cable network OCN at 22:00 every Saturdays and Sundays, starting November 11, 2006, but on November 24, 2006, switched to 23:00 every Friday night.

A Girl at My Door: A Girl at My Door () is a 2014 South Korean drama film directed by July Jung and stars Bae Doona as a policewoman who takes in an abused girl played by Kim Sae-ron.  The film screened in the Un Certain Regard section at the 2014 Cannes Film Festival.

Master of Study: Master of Study (; lit.  "God of Study", "Lord of Study") is a South Korean television series that aired on KBS2 from January 4 to February 23, 2010 on Mondays and Tuesdays at 21:55 for 16 episodes.  It starred Kim Su-ro, Bae Doona, Oh Yoon-ah, Yoo Seung-ho, Go Ah-sung, Lee Hyun-woo, Park Ji-yeon,

As One (film): As One (; lit.  "Korea") is a 2012 South Korean sports drama film starring Ha Ji-won and Bae Doona.  It is a cinematic retelling of the first ever post-war Unified Korea sports team which won the gold at the 1991 World Table Tennis Championships in Chiba, Japan.  Director Moon Hyun-sung used the foundation of true events to tell the story of a team that united a divided nation for the first time in its painful history.

Tube (2003 film): Tube () is a 2003 South Korean action thriller film directed by Beak Woon-hak (or Baek Woon-hak).  The film features police officer Jay (Kim Suk-hoon) who is a subway police officer who spends his days reminiscing over his lost lover.  The pickpocket Kay (Bae Doona) becomes infatuated with Jay and tips him off about the government assassin Bishop (Park Sang-min) hijacking a subway car.  Both Jay and Kay find themselves in the target car when the Bishop makes his move.

Look Back in Anger (TV series): Look Back in Anger () is a 2000 South Korean television series about two brothers' love for two women that aired on KBS2.  Starring Joo Jin-mo, Lee Min-woo, Park Jin-hee and Bae Doona, the cast also includes the following actors pre-stardom: Kim Myung-min, Uhm Tae-woong, Kim Min-hee and Lee Eun-ju.

Gloria (2010 TV series): Gloria () is a South Korean television series starring Bae Doona, Lee Chun-hee, Seo Ji-seok, So Yi-hyun, Oh Hyun-kyung and Lee Jong-won in a tale of romance, survival, overcoming poverty and adversity, and making your dreams come true.  It aired on MBC from July 31, 2010 to January 30, 2011 on Saturdays and Sundays at 20:40 for 50 episodes.

The Host (2006 film): The Host (; lit.  "Monster") is a 2006 South Korean monster film directed by Bong Joon-ho and starring Song Kang-ho, Byun Hee-bong, Park Hae-il, Bae Doona and Go Ah-sung.

How to Meet a Perfect Neighbor: How to Meet a Perfect Neighbor () is a 2007 South Korean television series starring Kim Seung-woo, Bae Doona, Park Si-hoo, Wang Ji-hye, Son Hyun-joo and Kim Sung-ryung.  It aired on SBS from July 25 to September 27, 2007 on Wednesdays and Thursdays at 21:55 for 20 episodes.

Question: South Korean actress Bae Doona, known for her role in 2000 television series "Look Back in Anger", had an English-speaking role in which 2012 film directed by the Wachowski siblings?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "directors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The directors of the film."
    },
    "role_language": {
      "type": "string",
      "description": "The language spoken in the role."
    }
  },
  "required": [
    "actress_name",
    "film_title",
    "release_year",
    "directors",
    "role_language"
  ],
  "additionalProperties": false
}

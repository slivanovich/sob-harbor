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
47th Baeksang Arts Awards: The 47th Baeksang Arts Awards ceremony was held at Kyung Hee University's Peace Palace Hall in Seoul on May 26, 2011, and was broadcast on KBS2.  Presented by IS Plus Corp., it was hosted by actor Ryu Si-won and actress Kim Ah-joong.

51st Baeksang Arts Awards: The 51st Baeksang Arts Awards ceremony was held at Kyung Hee University's Peace Palace Hall in Seoul on May 26, 2015, and aired on jTBC.  It was hosted by Shin Dong-yup, Kim Ah-joong and Joo Won.

Ahn Gooc-jin: Ahn Gooc-jin (born 1980), is a South Korean film director and screenwriter.  Ahn's directorial feature debut "Alice in Earnestland" (2015) has won various awards, including New Talent Award at the 39th Hong Kong Asian Film Festival, Best Screenplay at the 52nd Baeksang Arts Awards and Best Independent Film Director at the 16th Director's Cut Awards.

50th Baeksang Arts Awards: The 50th Baeksang Arts Awards ceremony was held at Kyung Hee University's Peace Palace Hall in Seoul on May 27, 2014.  It was broadcast on jTBC and was presented by IS Plus Corp. It was hosted by comedian Shin Dong-yup and actress Kim Ah-joong.

Jin Kyung: Jin Kyung (born March 27, 1972) is a South Korean actress.  Jin made her stage debut in 1998 and spent ten years in theater, before becoming active in film and television.  She won Best Supporting Actress at the 50th Baeksang Arts Awards for surveillance thriller "Cold Eyes" (2013).

Baeksang Arts Awards: Baeksang Arts Awards, also known as Paeksang Arts Awards, is an awards ceremony held annually by IS PLUS Corp., publisher of Ilgan Sports, since 1965.  It is to honour outstanding achievements in the South Korean entertainment industry and to garner public attention upon the best in Korean films, television, and theater.  It was established by Chang Key-young, founder of the "Hankook Ilbo" newspaper, whose pen name was "Baeksang."  The ceremony is usually presented in April or May in Seoul.

Hong Kong Film Award for Best Director: The Hong Kong Film Award for Best Director is an award presented annually at the Hong Kong Film Awards (HKFA).  It is given to honour the best director of a Hong Kong film.  The 1st Hong Kong Film Awards ceremony was held in 1982, with no formal nomination procedure established; the award was given to Allen Fong for his direction of "Father and Son."  After the first award ceremony, a nomination system was put in place whereby no more than five nominations are made for each category and each entry is selected through two rounds of voting.  Firstly, prospective nominees are marked with a weight of 50% each from HKFA voters and a hundred professional adjudicators, contributing towards a final score with which the top five nominees advance to the second round of voting.  The winner is then selected via a scoring process where 55% of the vote comes from 55 professional adjudicators, 25% from representatives of the Hong Kong Film Directors' Guild and 20% from all other HKFA Executive Committee Members.

Cold Eyes: Cold Eyes (; lit.  "Stakeout" or "Surveillance") is a 2013 South Korean film starring Sol Kyung-gu, Jung Woo-sung, Han Hyo-joo, Jin Kyung and Lee Junho.  A remake of 2007 Hong Kong film "Eye in the Sky", the film is about detectives from the surveillance team of a special crime unit who work together to take down a bank robbing organization.

92 Legendary La Rose Noire: 92 Legendary La Rose Noire is a 1992 Hong Kong comedy film written and directed by Jeffrey Lau and starring Tony Leung, Maggie Shiu, Teresa Mo, Wong Wan-sze and Fung Bo Bo.  The film was nominated for eight awards at the 12th Hong Kong Film Awards, where Leung won his second Hong Kong Film Award for Best Actor and Fung won her first Hong Kong Film Award for Best Supporting Actress.  "92 Legendary La Rose Noire" was ranked number 75 of the Best 100 Chinese Motion Pictures at the 24th Hong Kong Film Awards.  The film was followed two sequels, one released in 1993 titled "Rose Rose I Love You", where Leung reprises his role but features a new storyline, and another released in 1997 confusingly titled "Black Rose II", also featuring a new storyline and different cast.

52nd Baeksang Arts Awards: The 52nd Baeksang Arts Awards ceremony was held on June 3, 2016 at Kyung Hee University’s Grand Peace Hall.  It was hosted by Miss A's Suzy and Shin Dong-yup.

Question: Jin Kyung won an award at the Baeksang Arts Awards for a remake of what 2007 Hong Kong film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_winner_name": {
      "type": "string",
      "description": "The name of the person who won the award."
    },
    "award_name": {
      "type": "string",
      "description": "The specific award won."
    },
    "award_ceremony": {
      "type": "string",
      "description": "The name of the awards ceremony."
    },
    "winning_film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film for which the award was won."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the winning film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "original_film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the original film that was remade."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the original film."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the original film was produced."
        }
      },
      "required": [
        "title",
        "release_year",
        "country_of_origin"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "award_winner_name",
    "award_name",
    "award_ceremony",
    "winning_film_details",
    "original_film_details"
  ],
  "additionalProperties": false
}

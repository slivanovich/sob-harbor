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
2005 Uncle Tobys Hardcourts – Doubles: Svetlana Kuznetsova and Elena Likhovtseva were the defending champions, but Kuznetsova did not compete this year.  Likhovtseva teamed up with Magdalena Maleeva and successfully defended her title, by defeating Maria Elena Camerin and Silvia Farina Elia 6–3, 5–7, 6–1 in the final.

2008 Moorilla Hobart International – Doubles: Elena Likhovtseva and Elena Vesnina were the defending champions, but Likhovtseva chose not to participate, and only Vesnina competed that year.

2004 Toray Pan Pacific Open – Doubles: Elena Bovina and Rennae Stubbs were the defending champions, but had different outcomes.  While Bovina did not compete this year, Stubbs pertnered with Cara Black and successfully defended her title, defeating Elena Likhovtseva and Magdalena Maleeva 6–0, 6–1 in the final.  It was the 2nd title in the year for the pair, and the 14th title for Black and 44th title for Stubbs, in their respective careers.

2003 Wimbledon Championships – Mixed Doubles: Mahesh Bhupathi and Elena Likhovtseva were the defending champions, but played in this year with different partners.  Bhupathi teamed up with Paola Suárez and lost in third round to Nenad Zimonjić and Iroda Tulyaganova, while Likhovtseva teamed up with Bob Bryan and lost in second round to Andy Ram and Anastasia Rodionova.

Jim Courier: James Spencer Courier Jr. (born August 17, 1970) is an American former World No. 1 professional tennis player.  During his career, he won four Grand Slam singles titles, two at the French Open and two at the Australian Open.  He holds the record for being the youngest man to have reached the finals of all four Grand Slam singles tournaments, at the age of 22 years and 11 months.  He also won five Masters 1000 series titles.  Until Novak Djokovic in 2016, Courier was the last man to win both the Australian and French Opens in the same calendar year.

Elena Likhovtseva: Elena Alexandrovna Likhovtseva (Russian: Елена Александровна Лиховцева ] ; born 8 September 1975) is a Russian former tennis player.  She turned professional in January 1992 at the age of 16.

2008 Australian Open – Mixed Doubles: Elena Likhovtseva and Daniel Nestor were the defending champions, but Likhovtseva chose not to participate, and only Nestor competed that year.

2007 J&amp;S Cup – Doubles: Elena Likhovtseva and Anastasia Myskina were the defending champions, but Myskina chose not to compete that year.  Likhovtseva partnered with Elena Vesnina.

2000 Adidas International – Women's Doubles: Elena Likhovtseva and Ai Sugiyama were the defending champions, but had different outcomes.  While Likhovtseva teamed up with Amanda Coetzer and lost in first round, Sugiyama teamed up with Julie Halard-Decugis and successfully defended her title by defeating Martina Hingis and Mary Pierce in the final, 6–0, 6–3.

2003 WTA German Open – Doubles: Elena Dementieva and Janette Husárová were the defending champions, but had different outcomes.  Dementieva had to withdraw due to a left foot strain, while Husárová teamd up with Elena Likhovtseva and reached the semifinals.

Question: Jim Courier and Elena Likhovtseva are both famous athletes in what sport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sport_name": {
      "type": "string",
      "description": "The name of the sport common to both athletes."
    },
    "athletes_mentioned": {
      "type": "array",
      "description": "Details about the athletes mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the athlete."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the athlete."
          },
          "is_former_world_no_1": {
            "type": "boolean",
            "description": "Indicates if the athlete was a former World No. 1 in their sport."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "common_sport_identified": {
      "type": "boolean",
      "description": "True if a common sport was successfully identified for both athletes."
    }
  },
  "required": [
    "sport_name",
    "athletes_mentioned",
    "common_sport_identified"
  ],
  "additionalProperties": false
}

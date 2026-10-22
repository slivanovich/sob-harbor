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
2017 Western &amp; Southern Open – Men's Doubles: Ivan Dodig and Marcelo Melo were the defending champions, but chose not to participate together.  Dodig teamed up with Rohan Bopanna, but lost in the quarterfinals to Melo who partnered Łukasz Kubot.  Kubot and Melo lost in the semifinals to Jamie Murray and Bruno Soares.

2006 Rogers Masters – Doubles: Wayne Black and Kevin Ullyett were the defending champions, but Black retired in 2006, and only Ullyett competed that year.

2010 Tennislife Cup – Doubles: Frederico Gil and Ivan Dodig were the defending champions, but Dodig decided not to participate.

2016 BNP Paribas Masters – Doubles: Ivan Dodig and Marcelo Melo were the defending champions, but Dodig chose not to participate this year.  Melo played alongside Vasek Pospisil, but lost to John Peers and Henri Kontinen in the semifinals.

2009 If Stockholm Open – Doubles: Jonas Björkman and Kevin Ullyett were the defending champion, but Björkman was retired in November 2008. Ullyett partnered up with Bruno Soares, and they won in the final 6–4, 7–6 against Simon Aspelin and Paul Hanley.

2011 Alessandria Challenger – Doubles: Ivan Dodig and Lovro Zovko were the defending champions but Dodig not to participate. <br>

Kevin Ullyett: Kevin Ullyett (born 23 May 1972 in Salisbury, now Harare) is a former professional tennis player from Zimbabwe.  His primary success on the tour was in men's doubles.

2017 Rogers Cup – Men's Doubles: Ivan Dodig and Marcelo Melo were the defending champions, but chose not to participate together.  Melo played alongside Łukasz Kubot, but lost in the second round to Fabrice Martin and Édouard Roger-Vasselin.  Dodig teamed up with Rohan Bopanna, but lost in the final to Pierre-Hugues Herbert and Nicolas Mahut, 4–6, 6–3, [6–10].

Ivan Dodig: Ivan Dodig (born 2 January 1985) is a Croatian tennis player.  His career-high ATP rankings are world No. 29 in singles and world No. 4 in doubles.  Dodig is a Grand Slam champion after winning the 2015 French Open men's doubles title with Marcelo Melo.

2009 Zagreb Open – Doubles: Ivan Dodig and Júlio Silva were the defending champions, however only Dodig chose to play this year.  He competed with Lovro Zovko.  They lost to Brian Dabul and Leonardo Mayer in the first round.

Question: Who is older, Ivan Dodig or Kevin Ullyett?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "older_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "age_difference_years": {
      "type": "integer"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "older_person",
    "age_difference_years"
  ],
  "additionalProperties": false
}

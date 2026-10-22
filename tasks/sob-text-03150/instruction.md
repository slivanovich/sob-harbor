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
Tom Okker: Thomas Samuel Okker (born 22 February 1944) is a former Dutch tennis player.  He was ranked among the world's top 10 singles players for seven consecutive years, 1968–74, reaching a career high of World No. 3 in 1969.  He also was ranked World No. 1 in doubles in 1969.

2008 Internationaux de Strasbourg – Doubles: Yan Zi and Jie Zheng were the defending champions, but Zheng chose not to participate, and only Yan competed that year.

Tennis at the 2010 Asian Games – Women's doubles: At the 2010 Asian Games in the Women's doubles tennis event, Zheng Jie and Yan Zi were the defending champions, but only Yan chose to participate, she partnered up with Peng Shuai.

2009 Hansol Korea Open – Doubles: Chuang Chia-jung and Hsieh Su-wei were the defending champion, but Hsieh chose not to participate that year.  Chuang partnered with Yan Zi, but they lost in the semifinals against Chan Yung-jan and Abigail Spears. Chan Yung-jan and Abigail Spears won in the final 6–3, 6–4 against Carly Gullickson and Nicole Kriz.

2007 Wimbledon Championships – Women's Doubles: Yan Zi and Zheng Jie were the defending champions but Zheng did not compete in 2007.  Yan partnered Peng Shuai and reached the quarterfinals where they were beaten by Alicia Molik and Mara Santangelo.

Yan Ying: Yan Ying (), courtesy name Zhong (), or more widely known as Yan Zi () c.578-500 BC, was born in present-day Gaomi county, Shandong province.  He served as prime minister to the state of Qi during the Spring and Autumn period.  An accomplished philosopher, statesman and politician, he was an elder contemporary of Confucius, described as "by far the most creative thinker of the Chunqiu age".

Jan Hajer: Jan Hajer (born 31 March 1942) is a Dutch former tennis player.  He was national champion in 1963.  He won the final by winning over Willem Maris, Dutch National Champion in 1962.  In 1964 Jan Hajer lost the final of the Dutch National Championship against Tom Okker.  Later Hajer and Okker represented the Netherlands in the Davis Cup team.  Hajer had a relative short international tennis career and participated in Wimbledon three times.  In 1967 he reached the second round which he lost in five sets to Jaidip Mukerjea.  Hajer and Okker competed in doubles events in South Africa, Philippines and Australia.

1975 Stockholm Open – Men's Doubles: Tom Okker and Marty Riessen were the defending champions, but Riessen did not participate this year.  Okker partnered Arthur Ashe, losing in the quarterfinals.

Yan Zi (tennis): Yan Zi (; ; born November 12, 1984), is a retired Chinese-born Hong Kong female professional tennis player.

1980 U.S. Pro Indoor – Doubles: Wojtek Fibak and Tom Okker were the defending champions, but Okker did not participate this year.  Fibak partnered Heinz Günthardt, losing in the semifinals.

Question: Yan Zi and Tom Okker, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1_name": {
      "type": "string",
      "description": "The name of the first person mentioned in the question."
    },
    "person_2_name": {
      "type": "string",
      "description": "The name of the second person mentioned in the question."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "occupation_details": {
      "type": "array",
      "description": "Details about each person's occupation.",
      "items": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "occupation": {
            "type": "string",
            "description": "The specific occupation of the individual."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the individual, if available."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the individual, if available."
          },
          "status": {
            "type": "string",
            "description": "The status of their career (e.g., 'former', 'retired', 'professional'), if available."
          }
        },
        "required": [
          "person_name",
          "occupation"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "person_1_name",
    "person_2_name",
    "mutual_occupation",
    "occupation_details"
  ],
  "additionalProperties": false
}

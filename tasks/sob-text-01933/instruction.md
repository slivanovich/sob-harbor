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
Irish Civil War: The Irish Civil War (Irish: "Cogadh Cathartha na hÉireann" ; 28 June 1922 – 24 May 1923) was a conflict that followed the Irish War of Independence and accompanied the establishment of the Irish Free State, an entity independent from the United Kingdom but within the British Empire.

Mayo by-election, 1870: The Mayo by-election of 1870 was fought on 12 May 1870.  The by-election was fought due to the death of the incumbent Liberal MP George Henry Moore.  It was won by the unopposed Liberal candidate George Ekins Browne.

Henry Moore Foundation: The Henry Moore Foundation is a registered charity in England, established for education and promotion of the fine arts — in particular, to advance understanding of the works of Henry Moore.  The charity was set up with a gift from the artist in 1977.  The Foundation supports a wide range of projects, including student bursaries, fellowships for artists and financial grants to various arts institutions.  It operates from Perry Green in Hertfordshire and at the Henry Moore Institute in Leeds, England.

George Henry Moore (author): George Henry Moore (April 20, 1823 – May 5, 1892 in New York City) was an American historical writer and librarian.

George Henry Moore (politician): George Henry Moore (1 March 1810 – 19 April 1870) was an Irish politician who served as Member of Parliament (MP) for Mayo in the Parliament of the United Kingdom.  He was one of the founders of the Catholic Defence Association and a leader of the Independent Irish Party.  He was also father of the writer George A. Moore and the politician Maurice George Moore.  Their ancestral home, Moore Hall was burned down in 1923 by the anti-Treaty IRA during the Irish Civil War.

Moore Hall, County Mayo: Moore Hall, or Moorehall, the house and estate of George Henry Moore and family, is situated to the south of the village Carnacon in the barony of Carra, County Mayo in a karst limestone landscape.  The Moores were an aristocratic Irish family who built Moore Hall between 1792 and 1795.  The first Moore of Moore Hall was George Moore, a name borne by many members of the family down the generations.  The Moores were originally an English Protestant family but some became Catholic when John Moore married a Roman Catholic, Jane Lynch Athy of Galway, and when their son, George, married Katherine de Kilikelly (a.k.a. Kelly), an Irish-Spanish Catholic, in 1765.

Ogere Remo: Ogere (also referred to as Ogere Remo or Ogere-Remo or Ogere - Remo), is an ancient town in the present Remo Division of Ogun State, Nigeria.  The town was founded circa 1401 A.D. Ogere is part of the Ikenne Local Government area of Ogun State.  The ancestral home of the Yorubas is Ile-Ife.  Oduduwa is the ancestral father of all the Yorubas inside and outside Nigeria.  The people of Ogere are Yorubas.  They hailed from the ancestral home “Lagere in Ile-Ife” in two different emigrations led by Olipakala and Lowa-Lida respectively.  The two are Ile-Ife crowned Princes.

Catholic Defence Association: The Catholic Defence Association was an organisation founded in 1851 to defend the rights of Irish Roman Catholic tenant farmers.  The first meeting held at the Mechanics' Institute, Dublin was chaired by Lord Gormanston, with MPs William Keogh, George Henry Moore and John Sadleir on the platform.

George Henry Moore (runholder): George Henry Moore (12 October 1812 – 7 July 1905), derogatorily known as Scabbie Moore, was a New Zealand runholder.  He was born in Billown, Isle of Man on 12 October 1812.  As a young man, he worked on Mona Vale Station in Tasmania, where he married the owner's daughter.  He was later the owner of Glenmark Station north of Waipara, which for a time was New Zealand's largest sheep run.

Frank Moore (journalist): was an American journalist and compiler, a brother of George Henry Moore.  He was born in Concord, New Hampshire, but removed to New York City and became a journalist and general writer.  In 1869-72 he was Assistant Secretary of Legation in Paris.  He edited:

Question: The ancestral home of George Henry Moore was burned down during a conflict that ended on what date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ancestral_home": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the ancestral home."
        },
        "owner_name": {
          "type": "string",
          "description": "The name of the owner of the ancestral home."
        },
        "burning_details": {
          "type": "object",
          "properties": {
            "year": {
              "type": "integer",
              "description": "The year the ancestral home was burned down."
            },
            "perpetrator": {
              "type": "string",
              "description": "The group responsible for burning down the ancestral home."
            }
          },
          "required": [
            "year",
            "perpetrator"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "owner_name",
        "burning_details"
      ],
      "additionalProperties": false
    },
    "related_conflict": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the conflict during which the home was burned."
        },
        "start_date": {
          "type": "string",
          "description": "The start date of the conflict."
        },
        "end_date": {
          "type": "string",
          "description": "The end date of the conflict."
        }
      },
      "required": [
        "name",
        "start_date",
        "end_date"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The end date of the conflict during which the ancestral home was burned."
    }
  },
  "required": [
    "ancestral_home",
    "related_conflict",
    "final_answer"
  ],
  "additionalProperties": false
}

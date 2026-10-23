{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSewallis Shirley, 10th Earl Ferrers: Sewallis Edward Shirley, 10th Earl Ferrers (24 January 1847 – 26 July 1912), styled Viscount Tamworth until 1859, was a British peer.  He was the son of Washington Sewallis Shirley, 9th Earl Ferrers and Lady Augusta Annabella Chichester.\n\nJoseph Nelson Rose: Joseph Nelson Rose (January 11, 1862 – May 4, 1928) was an American botanist.  He was born in Union County, Indiana.  His father died serving during the Civil War when Joseph Rose was a young boy.  He later graduated from high school in Liberty, Indiana.\n\nHerman Thorn: Herman Thorn was a U. S. Army officer that rose from the enlisted ranks and died serving on the frontier in 1849.  A well on a frontier trail in Texas and an army fort in New Mexico was named for him.\n\nList of Chairmen of the Kennel Club: This is a list of Chairmen of The Kennel Club, starting from the club's founding in 1873.  The Kennel Club dates from the first organised dog show in UK on the 28/29 June 1859, following this in 1870 it was decided that a governing body was required to govern such shows.  Sewallis Shirley called together a meeting of the National Dog Club Committee on 4 April 1873, where the Kennel Club was founded.  Shirley was named as the first Chairman, and would go on to become the President of the society in 1899.\n\nIftikhar Hussain Khan Mamdot: Nawab Iftikhar Hussain Khan of Mamdot (Urdu: ‎ ; 1906 – 16 October 1969) was a Pakistani politician from Punjab.  He was the 1st Chief Minister of Punjab from 15 August 1947 to 25 January 1949.  Earlier he was elected to the office of the President of All-India Muslim League in 1942 after his father had died serving that office before him.  He had earned the confidence of Muhammad Ali Jinnah and was appointed by him as Punjab chief minister in 1947.  He was also the uncle of Dr. Asma Mamdot, MP from 2008 to 2013.\n\nNational League of POW/MIA Families: The National League of Families of American Prisoners and Missing in Southeast Asia is an American 501(c)(3) non-profit organization that is concerned with the Vietnam War POW/MIA issue.  According to the group's web site, its sole purpose is \"to obtain the release of all prisoners, the fullest possible accounting for the missing and repatriation of all recoverable remains of those who died serving our nation during the Vietnam War in Southeast Asia.\"  The League's most prominent symbol is its famous POW/MIA flag.\n\nNorman Leslie (soldier): Norman Leslie (died 29 August 1554), was a 16th-century Scottish nobleman.  The leader of the party who assassinated Cardinal Beaton, he was forced to flee Scotland, serving the monarchs of England and France.  He died serving the latter in 1554.\n\nCharlotte of Mecklenburg-Strelitz: Charlotte of Mecklenburg-Strelitz (Sophia Charlotte; 19 May 1744 – 17 November 1818) was by marriage to King George III the Queen of Great Britain and Ireland from her wedding in 1761 until the union of the two kingdoms in 1801, after which she was Queen of the United Kingdom of Great Britain and Ireland until her death in 1818.  She was also the Electress of Hanover in the Holy Roman Empire until the promotion of her husband to King of Hanover on 12 October 1814, after which she was also queen consort of Hanover.\n\nSewallis Shirley (1709–1765): Sewallis Shirley (19 October 1709 – 31 October 1765) was a British Member of Parliament.  The fourteenth son of Robert Shirley, 1st Earl Ferrers (and fourth son by his second wife, Selina), he represented Brackley and Callington in the latter part of the reign of George II.  His marriage to the Dowager Countess of Orford ended in divorce after three years, and Shirley spent the last few years of his life as an officer of Queen Charlotte's household.\n\nWashington Shirley, 9th Earl Ferrers: Washington Sewallis Shirley, 9th Earl Ferrers (3 January 1822 – 13 March 1859), styled Hon. Washington Shirley from 1827 to 1830 and Viscount Tamworth from 1830 to 1842, was a British nobleman.\n\nQuestion: To which king was the queen who Sewallis Shirley died serving married?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_served_by_shirley\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person Sewallis Shirley served.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the person Sewallis Shirley served.\"\n        },\n        \"spouse\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the spouse of the person Sewallis Shirley served.\"\n            },\n            \"title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the spouse.\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"title\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\",\n        \"spouse\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"sewallis_shirley_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of Sewallis Shirley (1709-1765).\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of Sewallis Shirley.\"\n        },\n        \"death_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The death year of Sewallis Shirley.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\",\n        \"death_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the king to whom the queen Sewallis Shirley served was married.\"\n    }\n  },\n  \"required\": [\n    \"person_served_by_shirley\",\n    \"sewallis_shirley_details\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_served_by_shirley": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person Sewallis Shirley served."
          },
          "title": {
            "type": "string",
            "description": "The title of the person Sewallis Shirley served."
          },
          "spouse": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "The name of the spouse of the person Sewallis Shirley served."
              },
              "title": {
                "type": "string",
                "description": "The title of the spouse."
              }
            },
            "required": [
              "name",
              "title"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "title",
          "spouse"
        ],
        "additionalProperties": false
      },
      "sewallis_shirley_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of Sewallis Shirley (1709-1765)."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of Sewallis Shirley."
          },
          "death_year": {
            "type": "integer",
            "description": "The death year of Sewallis Shirley."
          }
        },
        "required": [
          "name",
          "birth_year",
          "death_year"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the king to whom the queen Sewallis Shirley served was married."
      }
    },
    "required": [
      "person_served_by_shirley",
      "sewallis_shirley_details",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

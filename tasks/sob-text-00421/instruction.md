{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTheodore Burr: Theodore Burr (August 16, 1771 – 1822 [or November, 1824]) was an inventor from Torrington, Connecticut, who was credited with the Burr Arch Truss bridge design and was cousin of vice president Aaron Burr.  Theodore Burr came to Oxford, New York in 1792.  By 1794, he had built a grist mill (once owned by Fletcher & Corbin), and a dam to power the mill.  In 1800 he built the first stringer bridge across the Chenango River in Oxford.  From 1809-1811, he built an impressive Federal style house on the site of an ancient Indian Fort (at 8 Fort Hill Park) for his family.  (Wings were added to both sides of the house at a later and unknown date.)  The building still stands and houses the Oxford Memorial Library.\n\nAaron Columbus Burr: Aaron Columbus Burr, born Aaron Burr Colombe (September 15, 1808 – July 27, 1882), was the son of American Vice President Aaron Burr.\n\nPeter Burr House: The Peter Burr House was built between 1751 and 1755 near present-day Shenandoah Junction, West Virginia, making it one of the oldest houses in West Virginia.  Burr, whose first cousin was Aaron Burr, was one of the first settlers in the area.  It is the oldest surviving post-and-beam-construction house in West Virginia.  The property remains in the hands of Burr's descendants.\n\nEunice Dennie Burr: Eunice Dennie Burr (1732-1805) and her husband Thaddeus Burr were considered the \"first couple\" of Fairfield, Connecticut in pre-revolutionary times.  Eunice married Thaddeus Burr in 1759.  Before the American Revolution, their house hosted John Adams, Samuel Adams, Aaron Burr, John Hancock, and George Washington.  In 1779 their house was burned by British soldiers under General Tryon's command; the soldiers also looted the house and stole Eunice's rings, buckles, and silver buttons, and Eunice hid from them in the marshes behind her house.  The house was rebuilt by Eunice and Thaddeus in 1791.  For its rebuilding, John Hancock presented the frame, as his own house frame was the model after which the Burr mansion (as it is now known) was built, though the Burr mansion has changed since.\n\nTheodosia Burr Alston: Theodosia Burr Alston (June 21, 1783 – approximately January 2 or 3, 1813) was the daughter of U.S. Vice President Aaron Burr and Theodosia Bartow Prevost.  Her husband, Joseph Alston, was governor of South Carolina during the War of 1812.  She was lost at sea at age 29.\n\nSeymour Burr: Seymour Burr (1754/1762–1837) was an African-American slave in the Connecticut Colony in the North American British Colonies and United States.  Owned by the brother of Colonel Aaron Burr, who was also named Seymour, he was known only as Seymour (sometimes spelled Seymore) until he escaped and used the surname Burr to enlist in the British Army in the early days of the American Revolution.  The British promised the personal freedom of any African-American slave who enlisted or escaped to fight against the Continental Army, and Burr wanted more than anything to be free.  However, he was quickly captured and forcibly returned to his owner.\n\nTheodosia Bartow Prevost: Theodosia Bartow Prevost (November 1746 – May 28, 1794), also known as Theodosia Bartow Burr, was an American patriot.  Raised by a single mother, she married a British Army officer at seventeen.  After the American Revolution began, her own Patriot leanings led her to offer the use of her house, the Hermitage, as a meeting- and resting-place for revolutionaries, including Alexander Hamilton, the Marquis de Lafayette, and Aaron Burr: it was briefly used as the headquarters of George Washington, who counted her amongst his friends.  Burr's visit to the Hermitage began a secret romance that, following the death of Prevost's first husband, led to marriage.\n\nEsther Edwards Burr: Esther Edwards Burr (February 13, 1732 in Northampton, Province of Massachusetts Bay - April 7, 1758 in Princeton, Province of New Jersey) was the mother of U.S. Vice President Aaron Burr, Jr. and the wife of Princeton University President Aaron Burr, Sr. whom she married in 1752.\n\nBurr conspiracy: The Burr conspiracy was a suspected treasonous cabal of planters, politicians, and army officers in the early 19th century.  The cabal was allegedly led by Aaron Burr, the former Vice President of the United States (1801–1805); according to the accusations against him, Burr's goal was to create an independent country in the center of North America and/or the present-day Southwestern United States and parts of present-day Mexico.  Burr's version was that he intended to take possession of, and farm, 40,000 acres (160 km) in the Texas Territory leased to him by the Spanish Crown.\n\nAaron Burr Sr.: Aaron Burr Sr. (January 4, 1716 – September 24, 1757) was a notable Presbyterian minister and college educator in colonial America.  He was a founder of the College of New Jersey (now Princeton University) and the father of Aaron Burr (1756–1836), the third Vice President of the United States.\n\nQuestion: Theodosia Burr Alston was the daughter of Aaron Burr and this American patriot who married at what age?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American patriot.\"\n    },\n    \"relationship_to_aaron_burr\": {\n      \"type\": \"string\",\n      \"description\": \"The relationship of this person to Aaron Burr.\"\n    },\n    \"is_american_patriot\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the person was an American patriot.\"\n    },\n    \"marriage_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"age_at_first_marriage\": {\n          \"type\": \"integer\",\n          \"description\": \"The age at which the person married their first husband.\"\n        },\n        \"first_spouse_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the person's first spouse.\"\n        }\n      },\n      \"required\": [\n        \"age_at_first_marriage\",\n        \"first_spouse_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"relationship_to_aaron_burr\",\n    \"is_american_patriot\",\n    \"marriage_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the American patriot."
      },
      "relationship_to_aaron_burr": {
        "type": "string",
        "description": "The relationship of this person to Aaron Burr."
      },
      "is_american_patriot": {
        "type": "boolean",
        "description": "Indicates if the person was an American patriot."
      },
      "marriage_details": {
        "type": "object",
        "properties": {
          "age_at_first_marriage": {
            "type": "integer",
            "description": "The age at which the person married their first husband."
          },
          "first_spouse_description": {
            "type": "string",
            "description": "A description of the person's first spouse."
          }
        },
        "required": [
          "age_at_first_marriage",
          "first_spouse_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "relationship_to_aaron_burr",
      "is_american_patriot",
      "marriage_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Nightingale (fairy tale): \"The Nightingale\" (Danish: \"Nattergalen\") is a literary fairy tale written by Danish author Hans Christian Andersen about an emperor who prefers the tinkling of a bejeweled mechanical bird to the song of a real nightingale.  When the Emperor is near death, the nightingale's song restores his health.  Well received upon its publication in Copenhagen in 1843 in \"New Fairy Tales\", the tale is believed to have been inspired by the author's unrequited love for opera singer Jenny Lind, the \"Swedish nightingale\".  The story has been adapted to opera, ballet, musical play, television drama and animated film.\n\nAlbin Swoboda, Sr.: Albin August Heinrich Emil Swoboda (13 November 1836 – 5 August 1901) was an Austrian operatic tenor, actor, and opera director of German birth.  One of the most famous opera singers of the \"Golden Age\" of Viennese operetta, he was a leading tenor and dramatic stage actor at the Theater an der Wien from 1859-1878.  He notably appeared in the world premieres of operettas by composers Jacques Offenbach, Johann Strauss II, and Franz von Suppé.  He also appeared in musical comedies and plays in Vienna, and appeared in stage productions of all kinds as a guest artist in theatres in Germany, Hungary, Poland, and Russia.  His son Albin Swoboda, Jr. also had a successful career as an opera singer.  In 1955 a street in the Hietzing district of Vienna was named after him.\n\nJenny Lind: Johanna Maria Lind (6 October 18202 November 1887), better known as Jenny Lind, was a Swedish opera singer, often known as the \"Swedish Nightingale\".  One of the most highly regarded singers of the 19th century, she performed in soprano roles in opera in Sweden and across Europe, and undertook an extraordinarily popular concert tour of America beginning in 1850.  She was a member of the Royal Swedish Academy of Music from 1840.\n\nMargarita Salicola: Margarita Salicola (\"floruit\" 1682 – 1706) was a famous opera singer of her time.  She came from a family of musicians at the court of the Ferdinando Carlo Gonzaga, Duke of Mantua and became a staple of casts at San Giovanni Grisostomo, Venice's newest and most famous theater, in the 1680s.  The earliest work with which she can be linked is Pietro Simone Agostini's \"Il ratto delle sabine\" (\"The Rape of the Sabine Women\").  She was especially praised for her appearance in the title role of Carlo Pallavicino's \"Penelope la casta\" (\"The Chaste Penelope\") in the winter of 1685.  The Saxon elector Johann Georg III, in whose court Pallavicino already served, was so thrilled by her performance that he became intent to taking her and two \"castrati\" from the same cast into this service.  After a staged \"kidnapping,\" Salicola was escorted en route to Dresden by a Mantuan agent.\n\nSigrid Arnoldson: Sigrid Arnoldson (20 March 1861 – 7 February 1943) was a Swedish opera singer with an active international career at the end of the 19th century and into the 20th.  Possessing a fine coloratura soprano voice with a range of three octaves, music critics believed she was Jenny Lind's successor and dubbed her \"the new Swedish Nightingale\".  Her voice is preserved on several recordings made in Berlin for the Gramophone Company between 1906 and 1910.\n\nThe Swedish Nightingale (film): The Swedish Nightingale (German:Die schwedische Nachtigall) is a 1941 German musical film directed by Peter Paul Brauer and starring Ilse Werner, Karl Ludwig Diehl and Joachim Gottschalk.  The film is based on a play by Friedrich Forster-Burggraf set in nineteenth century Copenhagen.  It portrays a romance between the writer Hans Christian Andersen and the opera singer Jenny Lind the \"Swedish Nightingale\" of the title.\n\nStephen Storace: Stephen Storace (4 April 1762 – 19 March 1796) was an English composer.  His sister was the famous opera singer Nancy Storace.  He was born in London in the Parish of St Marylebone to an English mother and Italian father.  Relatively little is known through direct records of his life, and most details are known second-hand through the memoirs of his contemporaries Michael Kelly, the actor John Bannister, and the oboist William Thomas Parke.\n\nAristotle Onassis: Aristotle Socrates Onassis (Greek: Αριστοτέλης Ωνάσης , \"Aristotelis Onasis\"; 20 January 1906 – 15 March 1975), commonly called Ari or Aristo Onassis, was a Greek shipping magnate, who amassed the world's largest privately owned shipping fleet and was one of the world's richest and most famous men.  He was known for his business success, his great wealth and also his personal life, including his marriage to Athina Mary Livanos (daughter of shipping tycoon Stavros G. Livanos); his affair with famous opera singer Maria Callas; and his 1968 marriage to Jacqueline Kennedy, the widow of American President John F. Kennedy.\n\nJenny Lind tour of America, 1850–52: The Swedish soprano Jenny Lind, often known as the \"Swedish Nightingale\" was one of the most highly regarded singers of the 19th century.  At the height of her fame she was persuaded by the showman P. T. Barnum to undertake a long tour of the United States.  The tour began in September 1850 and continued to May 1852.  Barnum's advance publicity made Lind a celebrity even before she arrived in the U.S., and tickets for her first concerts were in such demand that Barnum sold them by auction.  The tour provoked a popular furore dubbed \"Lind Mania\" by the local press, and raised large sums of money for both Lind and Barnum.  Lind donated her profits to her favoured charities, principally the endowment of free schools in her native Sweden.\n\nJune Preston: June Preston (born December 29, 1928 Glendale, California) is an American former Hollywood child star who went on to become a world famous Opera singer debuting with The Metropolitan Opera \"Stars of the Metropolitan Opera\" opposite Jan Peerce in 1952.  She made her screen debut at age 4 at the RKO film studio as Mrs. Blewett's Daughter in \"Anne of Green Gables\", and went on to do many other movies such as \"Christmas in July\", \"Second Chorus\", \"The Strawberry Blonde\", \"Maytime\", and starring in many \"Our Gang\" comedies.\n\nQuestion: Sigrid Arnoldson is believed by critics to have been the successor to what famous opera singer who was often known as the \"Swedish Nightingale\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"successor_singer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the singer believed to be the successor.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"enum\": [\n            \"successor\"\n          ],\n          \"description\": \"The role of this singer in the succession.\"\n        },\n        \"critics_dubbed_nickname\": {\n          \"type\": \"string\",\n          \"description\": \"The nickname given to the successor by critics.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"critics_dubbed_nickname\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"predecessor_singer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the famous opera singer who was succeeded.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"enum\": [\n            \"predecessor\"\n          ],\n          \"description\": \"The role of this singer in the succession.\"\n        },\n        \"common_nickname\": {\n          \"type\": \"string\",\n          \"description\": \"The common nickname of the predecessor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"common_nickname\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the relationship between the two singers based on critical belief.\"\n    }\n  },\n  \"required\": [\n    \"successor_singer\",\n    \"predecessor_singer\",\n    \"relationship_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "successor_singer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the singer believed to be the successor."
          },
          "role": {
            "type": "string",
            "enum": [
              "successor"
            ],
            "description": "The role of this singer in the succession."
          },
          "critics_dubbed_nickname": {
            "type": "string",
            "description": "The nickname given to the successor by critics."
          }
        },
        "required": [
          "name",
          "role",
          "critics_dubbed_nickname"
        ],
        "additionalProperties": false
      },
      "predecessor_singer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the famous opera singer who was succeeded."
          },
          "role": {
            "type": "string",
            "enum": [
              "predecessor"
            ],
            "description": "The role of this singer in the succession."
          },
          "common_nickname": {
            "type": "string",
            "description": "The common nickname of the predecessor."
          }
        },
        "required": [
          "name",
          "role",
          "common_nickname"
        ],
        "additionalProperties": false
      },
      "relationship_description": {
        "type": "string",
        "description": "A description of the relationship between the two singers based on critical belief."
      }
    },
    "required": [
      "successor_singer",
      "predecessor_singer",
      "relationship_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

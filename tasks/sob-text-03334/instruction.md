{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Romanovs (band): The Romanovs are a band from Los Angeles.  The band consists of Morgan Kibby (lead vocalist and writer), Ana Lenchantin (cello), Dan Rosa (piano), Wesley Precourt (violin) and Randy Cooke (percussion).\n\nGerold, Prefect of Bavaria: Gerold (died 799) was an Alamannian nobleman who served the Frankish King, Charlemagne, as Margrave of the Avarian March and Prefect of Bavaria in what is now South-Eastern Germany.  Gerold played a significant role in the integration of Bavaria into the Frankish Kingdom during Carolingian expansion in the late 8th, and early 9th centuries.  Gerold both aided the continuity of Agilofing rule of Bavaria, as well as took steps to integrate Bavarians into the wider scope of the Frankish Kingdom.  Gerold was related both to the Agilofing family, the ruling class of Bavaria, as well as the Carolingian family.  The Agilofings had ruled Bavaria since Duke Garibald I in 548.  Gerold was born into the Agilofings, and his sister Hildegard was married to Charlemagne in 771. From these familial connections, he was appointed Prefect of Bavaria following the deposition of Duke Tassilo III in 788.  Gerold was heralded as a superb military commander, giving rise to his promotion to Prefect as a defender of the eastern border of the Frankish Kingdom.  In 799, Gerold is said to have fallen in battle against the Avars, shortly after the same Avars killed his ally, Erich, Duke of Friuli, through treachery.\n\nNaz Edwards: Naz Edwards (born Nazig Dombalagian (Armenian: Նազիգ Դոմբալագիան) on February 2, 1952) is an American voice actress, singer, and Broadway star who is most remembered as the voice of antagonist Queen Beryl in the DiC English version of \"Sailor Moon\".  She is of Armenian descent.\n\nAna Lenchantin: Ana Lenchantin is an Argentine-American cellist (of French ancestry) known for frequent appearances with American rock bands such as Train, Into the Presence, The Eels, Gnarls Barkley, No Doubt, Arthur Lee and Love, A Perfect Circle, Nine Inch Nails, Queens of the Stone Age, Thirty Seconds to Mars, Brian Wilson, Billy Corgan, Billy Howerdel, Glenn Hughes, Jenny Lewis, Melissa Auf der Maur, Damien Rice, Kerli, Lenka, and many more.\n\nSlavery in Libya: Slavery in Libya has a long history and a lasting impact on the Libyan culture.  It is closely connected with the wider context of slavery in north Africa.  Therefore, it is better understood when this wider scope is taken into account.\n\nLibya TV: Libya TV (also known as Libya Al Ahrar TV) is a Libyan TV channel broadcast by satellite from its headquarters in Doha.  The channel was created in 2011 during the Libyan Civil War.  Its presents news, opinions, analysis, photo and video reports about Libya in specific and the region in a wider scope.  It focuses on Libya’s revolution and future toward building a democratic state.\n\nWomen's Missionary and Service Commission: The Women's Missionary and Service Commission, previously known as the Women's Missionary and Service Auxiliary and abbreviated WMSC or WMSA, was a women's organization of the \"old\" Mennonite Church that originated out of the Mennonite Sewing Circle movement.  Named the WMSC in 1971, there were many precursor organizations and it has since involved into Mennonite Women USA, an organization with a much wider scope.\n\nAg-gag: Ag-gag is a term used to describe a class of anti-whistleblower laws that apply within the agriculture industry.  Coined by Mark Bittman in an April 2011 \"New York Times\" column, the term \"ag-gag\" typically refers to state laws that forbid the act of undercover filming or photography of activity on farms without the consent of their owner—particularly targeting whistleblowers of animal rights abuses at these facilities.  These laws originated in the United States, but have also begun to appear elsewhere, such as in Australia.  Some of these laws, such as the failed proposal in Pennsylvania, have a wider scope and could be used to criminalize actions by activists in other industries.\n\nScience Supercourse: Science Supercourse is a free online accessible educational resource currently encompassing more than 165,000 downloadable PowerPoint lectures covering four main areas of science; Public Health, Computer Engineering, Environment and Agriculture.  It represents an extension to \"\"Supercourse\"\" initiative which started out at the University of Pittsburgh by scientist Ronald LaPorte in the 80's.  It is mirrored at the Library of Alexandria, and networks over 56,000 scientists in 174 countries.  Being a useful tool for at least one million students from around the globe, Supercourse has been a well-established starting point which triggered the emergence of the new Science Supercourse in 2008 with a wider scope in terms of content and functionalities.\n\nMusic for Dogs: Music for Dogs is the third studio album by American indie rock band Gardens & Villa.  Released on 21 August 2015 by independent record label Secretly Canadian.  The album was orchestrated with the help of visionary producer Jacob Portrait of Unknown Mortal Orchestra.  The band hoped \"\"Music for Dogs\"\" would maintain a wider scope than some of their other work by making it sound just as much like the futuristic music of tomorrow as it does the classic tunes of '76\n\nQuestion: Who has a wider scope of profession, Naz Edwards or Ana Lenchantin?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_with_wider_scope\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified as having a wider scope of profession.\"\n    },\n    \"person_one\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first person.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions for the first person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_two\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second person.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions for the second person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for why one person has a wider scope of profession than the other.\"\n    }\n  },\n  \"required\": [\n    \"person_with_wider_scope\",\n    \"person_one\",\n    \"person_two\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_with_wider_scope": {
        "type": "string",
        "description": "The name of the person identified as having a wider scope of profession."
      },
      "person_one": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first person."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions for the first person."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      },
      "person_two": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second person."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions for the second person."
          }
        },
        "required": [
          "name",
          "professions"
        ],
        "additionalProperties": false
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for why one person has a wider scope of profession than the other."
      }
    },
    "required": [
      "person_with_wider_scope",
      "person_one",
      "person_two",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCrown of Beauty Theatre: Beauty Crown Grand Theater () is an indoor arena or theater in seven-star Beauty Crown Hotel Complex in the tropical city of Sanya, Hainan Island, China, and it is currently one of the biggest arena or theater for arts and entertainment venues, which stands 36 meters high and covers about 10,000 square meters, and was built in 2003.  Located in the city center, the crown-shaped Beauty Crown Theatre or Crown of Beauty Theatre was specially built for the Miss World pageant in 2003.  The 3,500-seat theater is equipped with an up-to-date and high-tech audio and lightning system.  It hosted 6 Miss World events: Miss World 2003, Miss World 2004, Miss World 2005, Miss World 2007, Miss World 2010, and Miss World 2015.  It also hosted Mister World 2007 and also will host Miss World 2017 again and it will be the 8th time that China will host the event.\n\nKsenia Sukhinova: Ksenia Vladimirovna Sukhinova (Russian: Ксе́ния Влади́мировна Сухи́нова; born 26 August 1987) is a Russian actress, TV Host, model and beauty queen who won Miss Russia 2007 and Miss World 2008.  She is the second Russian woman to win the Miss World pageant.\n\nMiss Russia 2006: Miss Russia 2006, was held on December 15, 2006 at Gostiny Dvor Arcade.  60 women competed at the pageant where Tatiana Kotova won representing the Rostov Oblast.  Zuleyka Rivera and Taťána Kuchařová participated in the event.  The winner represented Russia at the Miss Universe 2007 and Miss World 2007.\n\nParvathy Omanakuttan: Parvathy Omanakuttan (born 13 March 1987) is an Indian actress, model and beauty pageant titleholder who was crowned Miss India 2008 and later became first runner-up at Miss World 2008.  She was also awarded the titles of \"Miss World Asia & Oceania\" at the Miss World 2008 competition.\n\nDanielle Castaño: Danielle Kirsten Muriel Castaño (born August 21, 1989), also known as Danielle Castaño, is a Filipino-American TV Host, actress, beauty queen, and represented the Philippines in the Miss World 2008 pageant.  She was the crowd favorite in the Binibining Pilipinas 2008 pageant, winning five awards from the major sponsors and placing Miss World 2008 to compete in South Africa.\n\nMicaela Reis: Micaela Patrícia Reis (born December 21, 1988) is an Angolan actress, TV Host, model and beauty queen who was a Top 10 finalist at Miss Universe 2007 and placed first runner-up to Miss World 2007, becoming Miss World Africa.  She was the highest placed Miss Angola at both Miss Universe and Miss World before the win of Leila Lopes in Miss Universe 2011.\n\nJulia Kourotchkina: Julia Alexandrovna Kourotchkina \"(Russian: Юлия Александровна Курочкина, or Yuliya Aleksandrovna Kurochkina \"; born 10 August 1974 in Shcherbinka, Russia) is a Russian actress, model and beauty queen who was crowned Miss Russia 1992 and later crowned Miss World 1992 in Sun City, South Africa.\n\nSoo Wincci: Dr. Soo Wincci () is an award winning Malaysian singer, recording artist, actress, composer, celebrity chef, host, model, beauty queen, PhD holder and also an entrepreneur.  Soo was crowned Miss World Malaysia 2008 and represented Malaysia in the Miss World 2008 beauty pageant.  In 2013, She was selected by Hollywood's Independence Critics as the world Top 100 most beautiful women in the world.  In 2016, In completion of her 6 years PHD Journey in Business Administration, she was awarded by The Malaysia Book Of Records as \" The 1st Miss World Malaysia To Receive PHD\".  She is one of the most educated celebrities in Malaysia.\n\nMiss Russia 2009: Miss Russia 2009, Manezh Central Exhibition Hall in Moscow on March 7, 2009.  50 contestants from all over the Russia compete for the crown.  the reigning Miss World 2008, Ksenia Sukhinova of Tyumen crowned her successor Sofia Rudieva of Saint Petersburg as the brand new Miss Russia.  Dayana Mendoza participated in the event.\n\nMiss Russia 2007: Miss Russia 2007 was held on December 14, 2007 at Gostinom Yard, Moscow, Russia.  Tatiana Kotova of Rostov-on-Don crowned her successor Ksenia Sukhinova of Tyumen as the brand new Miss Russia.  Riyo Mori and Zhang Zilin participated in the event.  Ksenia Sukhinova competed in the Miss World 2008 pageant, where was crowned the winner.  Although she wasn't the winner of the national pageant, the Miss Russia organization decided to send the second runner-up, Vera Krasova, to the Miss Universe 2008 pageant held in Nha Trang, Vietnam where she made it to the top-5 finalists.\n\nQuestion: Tatiana Kotova of Rostov-on-Don crowned her successor who is which Russian actress, TV Host, model and beauty queen who won Miss Russia 2007 and Miss World 2008?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"crowned_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who was crowned.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions held by the crowned person.\"\n        },\n        \"titles_won\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of major beauty pageant titles won by the crowned person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"professions\",\n        \"titles_won\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"crowning_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"pageant_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the pageant where the crowning took place.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the crowning event occurred.\"\n        }\n      },\n      \"required\": [\n        \"pageant_name\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"crowned_by_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who performed the crowning.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"crowned_person\",\n    \"crowning_event\",\n    \"crowned_by_person\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "crowned_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who was crowned."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions held by the crowned person."
          },
          "titles_won": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of major beauty pageant titles won by the crowned person."
          }
        },
        "required": [
          "name",
          "professions",
          "titles_won"
        ],
        "additionalProperties": false
      },
      "crowning_event": {
        "type": "object",
        "properties": {
          "pageant_name": {
            "type": "string",
            "description": "The name of the pageant where the crowning took place."
          },
          "year": {
            "type": "integer",
            "description": "The year the crowning event occurred."
          }
        },
        "required": [
          "pageant_name",
          "year"
        ],
        "additionalProperties": false
      },
      "crowned_by_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person who performed the crowning."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "crowned_person",
      "crowning_event",
      "crowned_by_person"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

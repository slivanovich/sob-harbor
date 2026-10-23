{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMy Daughter Married a Negro: \"My Daughter Married a Negro\" is an essay by an anonymous male author published in \"Harper's Magazine\" in the July 1951 issue.  It discussed the author's daughter Anne's marriage to an African American – referred to as a negro in the parlance of the time – college classmate in 1949, and details \"his family's ordeal with their daughter marrying across the color line.\"  The article has since been much discussed in scholarship on racial relations in the United States.\n\nSir Thomas Copley: He was the eldest son of Sir Roger Copley by his wife Elizabeth, daughter of Sir William Shelley of Michelgrove, judge of the common pleas, and was one of the coheirs of Thomas Hoo, Baron Hoo and Hastings, whose title he claimed and sometimes assumed.  Lord Hoo's daughter Jane married his great-grandfather, Sir Roger Copley.  Another daughter married Sir Geoffrey Boleyn, and was the great-grandmother of Anne Boleyn.  Sir Thomas was of Gatton, Surrey, and Roughay, Sussex, and of The Maze, Southwark.\n\nQueen Máxima of the Netherlands: Queen Máxima of the Netherlands (born Máxima Zorreguieta Cerruti; 17 May 1971) is the wife of King Willem-Alexander.\n\nJorge Zorreguieta: Jorge Horacio Zorreguieta Stefanini (28 January 1928 – 8 August 2017) was an Argentine politician who served as Minister of Agriculture in the regime of General Jorge Rafael Videla.  Zorreguieta was the father of Queen Máxima of the Netherlands.\n\nJohn Denzel: John Denzel (died 1535) held large estates in Cornwall and became serjeant-at-law and Attorney-General to the Queen Consort, Elizabeth of York.  He had at least two daughters who became his co-heiresses, of whom Ann married Sir William Holles (1509–91) who became Lord Mayor of London.  Another daughter married into the Roskymer family.\n\nAndrew Stewart, 2nd Lord Ochiltree: Andrew Stewart, 2nd Lord Ochiltree (c.1521-1591) fought for the Scottish Reformation.  His daughter married John Knox and he played a part in the defeat of Mary, Queen of Scots at the battle of Langside.\n\nJane Lewson: Jane Lewson (née \"Vaughan\") (1700–1816), commonly known as Lady Lewson, was an eccentric centenarian.  She was in born in 1700 in Strand, London.  Early in life she married a wealthy man, who died when she was 26, leaving her with one daughter.  When her daughter married she spent the rest of her years as an eccentric widow, living in Coldbath Square and rarely leaving her home despite her considerable wealth.  She became well known during her era for the fact that until her death at the age of 116 she continued to wear the fashions of the reign of George I, and hence she became known as Lady Lewson because of her fashion style.  She was known for her extreme superstition and fear of getting a cold, which led her to only use one teacup, she smeared herself with pigs fat instead of washing and she would never have her windows washed in case they were broken and let in germs.  By the time of her death, it was said they had become so grimy they no longer let in light.\n\nHorio Tadaharu: Horio Tadaharu (堀尾 忠晴; 1596 – 26 October 1633) was a tozama \"daimyō\" in Japan during the Edo period.  His father was Horio Tadauji and his grandfather was Horio Yoshiharu.  He was the third leader of the Matsue clan.  He married Binhime daughter of Okudaira Iemasa of Utsunomiya Domain and adopted daughter of Tokugawa Hidetada.  They had 1 daughter married Ishikawa Kadokatsu.\n\nFujiwara no Norimichi: Fujiwara no Norimichi (藤原 教通 , July 29, 996 – November 6, 1075) , fifth son of Michinaga, was a kugyo of the Heian period.  His mother was Minamoto no \"Rinshi\" (源 倫子), daughter of Minamoto no Masanobu.  Regent Yorimichi, Empress \"Shōshi\" (consort of Emperor Ichijō), Empress \"Kenshi\" (consort of Emperor Sanjō) were his brother and sisters from the same mother.  In 1068, the year when his daughter married Emperor Go-Reizei, he took the position of Kampaku, regent.  He, however, lost the power when Emperor Go-Sanjo, who was not a relative of the Fujiwara clan, assumed the throne.  This contributed to the later decline of the Fujiwara clan.\n\nLaila Majnu (1949 film): Laila (Bhanumathi Ramakrishna) is the daughter of Ameer Sarvaar (Mukkamala), and Khais (Akkineni Nageswara Rao), the son of Ameer Umri (Arani Satyanarayana).  Love blossoms between Laila and Khais as they grow up.  Ameer Sarvaar, unable to dissuade his daughter from seeing Khais, shifts to Mecca.  Khais follows her to Mecca and roams in the streets uttering her name.  People take him to be a mad person (Majnu) and throw stones at him.  The story takes a lot of twists and turns from here on.  The King of Iraq (C.S.R), who comes on a visit to Mecca, sees Laila and decides to marry her.  Meanwhile, Ameer Umri pleads with his erstwhile friend Sarvaar to save his son.  Sarvaar agrees to get his daughter married to Khais if it is proved that he is not mad.  A test is conducted and Khais emerges successful.  Just when the marriage is to be performed, Sarvaar receives a proposal from the King of Iraq that he wishes to marry Laila.  Sarvaar changes his mind, and performs his daughter’s marriage with the King.  Laila leaves for Iraq and Khais wanders aimlessly in the desert.  The King already has a mistress Zareena (Sriranjani Jr).  On coming to know of Laila’s story, she tries to help her.  Soon thereafter, the Prince to repents, calls Laila his sister and sends her back to Khais.  The lovers are about to meet in the desert, but fate wills it otherwise and a heavy sandstorm takes its toll.\n\nQuestion: Who is Jorge Zorreguieta's daughter married to?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"father\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the father.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"daughter\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the daughter.\"\n        },\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title held by the daughter.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"marriage\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"spouse_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the daughter's spouse.\"\n        },\n        \"spouse_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title held by the daughter's spouse.\"\n        }\n      },\n      \"required\": [\n        \"spouse_name\",\n        \"spouse_title\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"father\",\n    \"daughter\",\n    \"marriage\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "father": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the father."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "daughter": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the daughter."
          },
          "title": {
            "type": "string",
            "description": "The title held by the daughter."
          }
        },
        "required": [
          "name",
          "title"
        ],
        "additionalProperties": false
      },
      "marriage": {
        "type": "object",
        "properties": {
          "spouse_name": {
            "type": "string",
            "description": "The name of the daughter's spouse."
          },
          "spouse_title": {
            "type": "string",
            "description": "The title held by the daughter's spouse."
          }
        },
        "required": [
          "spouse_name",
          "spouse_title"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "father",
      "daughter",
      "marriage"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

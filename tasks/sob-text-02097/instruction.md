{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoan Ganz Cooney: Joan Ganz Cooney (born Joan Ganz; November 30, 1929) is an American television producer.  She is one of the founders of Sesame Workshop (originally \"Children's Television Workshop\" or CTW), the organization famous for the creation of the children's television show \"Sesame Street\", which was also co-created by her.  Cooney grew up in Phoenix, Arizona and earned a B.A. degree in education from the University of Arizona in 1951.  After working for the State Department in Washington, D.C. and as a journalist in Phoenix, she worked as a publicist for television and production companies in New York City.  In 1961, she became interested in working for educational television, and became a documentary producer for New York's first educational TV station WNET (Channel 13).  Many of the programs she produced won local Emmys.\n\nLloyd Morrisett: Lloyd Newton Morrisett, Jr. (born November 2, 1929) is an American experimental psychologist with a career in education, communications, and philanthropy.  He is one of the founders of the Sesame Workshop, the organization famous for the creation of the children's television shows \"Sesame Street\" which was also co-created by him, \"The Electric Company\", and many others.\n\nGalli Galli Sim Sim: Galli Galli Sim Sim (Devanagari: गली गली सिम सिम) is the Hindi language adaptation of the American children's television series \"Sesame Street\" (famous for its Muppets), for India.  It is co-produced by Sesame Workshop and Turner Entertainment, through Miditech.  The show's Indian production company is known as Sesame Workshop India.\n\nSesame Street: Sesame Street is a long-running American children's television series, produced by Sesame Workshop (formerly known as the Children's Television Workshop) and created by Joan Ganz Cooney and Lloyd Morrisett.  The program is known for its educational content, and images communicated through the use of Jim Henson's Muppets, animation, short films, humor, and cultural references.  The series premiered on November 10, 1969, to positive reviews, some controversy, and high viewership; it has aired on the U.S.'s national public television provider (PBS) since its debut, with its first run moving to premium channel HBO on January 16, 2016.\n\nSesame Workshop: Sesame Workshop (SW), formerly Children's Television Workshop (CTW), is an American non-profit organization which has been responsible for the production of several educational children's programs—including its first and best-known, \"Sesame Street\"—that have been televised internationally.  Television producer Joan Ganz Cooney and foundation executive Lloyd Morrisett developed with the idea to form an organization to produce \"Sesame Street\", a television series which would help children, especially those from low-income families, prepare for school.  They spent two years, from 1966 to 1968, researching, developing, and raising money for the new series.  Cooney was named as the Workshop's first executive director, which was termed \"one of the most important television developments of the decade\".\n\nMichael H. Levine: Michael H. Levine is the founder and executive director of the Joan Ganz Cooney Center at Sesame Workshop, an independent research group founded by Sesame Workshop focused on fostering innovation in children’s learning through digital media.\n\nThe Joan Ganz Cooney Center: The Joan Ganz Cooney Center (informally, the Cooney Center) is an independent, non-profit, non-partisan research and innovation group founded by Sesame Workshop in order to advance children’s literacy skills and foster innovation in children’s learning through digital media.\n\nSesame Street international co-productions: \"Sesame Street\" international co-productions are educational children's television series based on the American \"Sesame Street\" but tailored to the countries in which they are produced.  Shortly after the debut of \"Sesame Street\" in the United States in 1969, television producers, teachers, and officials of several countries approached the show's producers and the executives of Sesame Workshop (2000-present) about the possibility of airing international versions of \"Sesame Street\".  Creator Joan Ganz Cooney hired former CBS executive Michael Dann to field offers to produce versions of the show in other countries.\n\nDavid Connell (television producer): David Connell (1931–1995) was the original executive producer for \"Sesame Street\", and Children's Television Workshop's vice-president in charge of production.  Connell, who had been a producer for the CBS children's program \"Captain Kangaroo\", played a key role in establishing the basic format of the \"street\" skits.  He was also the principal creative behind The Man from Alphabet, a series of live action skits starring Gary Owens which failed in child tests and were never aired on \"Sesame Street\".  Connell received his B.A. in 1955 and his M.A. in 1956, both from the University of Michigan.\n\nList of Sesame Street Muppets: The Muppets are a group of puppet characters created by Jim Henson, many for the purpose of appearing on the children's television program \"Sesame Street\".  Henson's involvement in \"Sesame Street\" began when he and Joan Ganz Cooney, one of the creators of the show, met in the summer of 1968, at one of the show's five three-day curriculum planning seminars in Boston.  Author Christopher Finch reported that director Jon Stone, who had worked with Henson previously, felt that if they could not bring him on board, they should \"make do without puppets\".\n\nQuestion: Who was the original executive producer of the children's television series, produced by Sesame Workshop and created by Joan Ganz Cooney and Lloyd Morrisett?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the original executive producer.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The specific role held by the producer.\"\n    },\n    \"produced_show\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series produced.\"\n    },\n    \"associated_organization\": {\n      \"type\": \"string\",\n      \"description\": \"The organization the producer was associated with for this role.\"\n    },\n    \"other_notable_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other significant roles held by the producer mentioned in the context.\"\n    },\n    \"education\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"degree\": {\n            \"type\": \"string\"\n          },\n          \"institution\": {\n            \"type\": \"string\"\n          },\n          \"year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"degree\",\n          \"institution\",\n          \"year\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Educational background of the producer.\"\n    }\n  },\n  \"required\": [\n    \"producer_name\",\n    \"role\",\n    \"produced_show\",\n    \"associated_organization\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "producer_name": {
        "type": "string",
        "description": "The name of the original executive producer."
      },
      "role": {
        "type": "string",
        "description": "The specific role held by the producer."
      },
      "produced_show": {
        "type": "string",
        "description": "The name of the television series produced."
      },
      "associated_organization": {
        "type": "string",
        "description": "The organization the producer was associated with for this role."
      },
      "other_notable_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other significant roles held by the producer mentioned in the context."
      },
      "education": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "degree": {
              "type": "string"
            },
            "institution": {
              "type": "string"
            },
            "year": {
              "type": "integer"
            }
          },
          "required": [
            "degree",
            "institution",
            "year"
          ],
          "additionalProperties": false
        },
        "description": "Educational background of the producer."
      }
    },
    "required": [
      "producer_name",
      "role",
      "produced_show",
      "associated_organization"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

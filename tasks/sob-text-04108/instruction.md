{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRudyard Kipling: Joseph Rudyard Kipling ( ; 30 December 1865 – 18 January 1936) was an English journalist, short-story writer, poet, and novelist.\n\nGeorge Wylie Henderson: George Wylie Henderson (June 14, 1904 – 1965) was an American writer of the Harlem Renaissance.\n\nGeorge Wylie Hutchinson: George Wylie Hutchinson (1852–1942) was a painter and leading illustrator in Britain and was from Great Village, Nova Scotia, Canada.  He illustrated the works of Arthur Conan Doyle, Rudyard Kipling, Hall Caine, Robert Louis Stevenson and Israel Zangwill.  His paintings inspired the poem \"Large Bad Picture\" and \"Poem\", both by Elizabeth Bishop, his great grand niece.  Hutchinson was a contributor to and subject of the novel \"The Master\" (1895) by Israel Zangwill, with whom he was a close friend.\n\nGeorge Wylie (politician): George Wylie was a politician in Wisconsin.  Wylie was a member of the Wisconsin State Assembly from 1897 to 1899 and of the Wisconsin State Senate from 1903 to 1905.  He was a Republican.\n\nGeorge W. Easton: George Wylie Easton (1883–1966) was a Scottish businessman, footballer and sportsperson.  He lived in Finland from 1903 to 1939 and worked on the timber trade mostly in the city of Viipuri.  Easton was an enthusiast sportsman who was interested in football, athletics and curling.\n\nHutchinson (publisher): Hutchinson began as Hutchinson & Co. (Publishers) Ltd., an English book publisher, founded in 1887 by Sir George Hutchinson and later run by his son, Walter Hutchinson (1887–1950).  Hutchinson's published books and magazines such as \"The Lady's Realm\", \"Adventure-story Magazine\", \"Hutchinson's Magazine\" and \"Woman\".\n\nDalbir Chetan: Dalbir Singh Jhand known as Punjabi writer Dalbir Chetan was a foremost short-story writer of contemporary Punjabi literature.  He had won awards, both regional and national, and is a widely translated author.  He retired as Indian Air Force officer.  The renowned Punjabi writer Dalbir Chetan (60), whose works were translated into a number of South-East Asian languages, is no more.  Though not a prolific writer, he was the author of four thought-provoking short story books — Rishteyian De Aar Paar, Raat Baraate, Khara Badal and Mehndi Bazaar book's main story Mehndi Bazaar was translated and reviewed in journal South Asian Review.  His book Mehndi Bazaar was translated into seven South-East Asian languages and selected in Twenty Stories from South Asia.  Many of his stories were translated into Urdu, English, Hindi, Oriya, Telugu and Gujarati languages.  Some of his short stories were telecast on television.  He also edited an anthology \"Asi Javaab Dinde Haan\", which won him appreciation.\n\nI, James Blunt: I, James Blunt is a 1942, wartime alternate history short-story by English journalist H. V. Morton.  It takes the form of a diary written by an English tradesman chronicling the Nazi occupation of Great Britain in the fall of 1944.  The short-story was commissioned by the Ministry of Information as propaganda and is Morton's only work of fiction beside his travel journalism writings for which he is better known.  George Orwell described the novel as \"a good flesh creeper, founded on the justified assumption that the mass of the English people haven't heard of fascism.\"\n\nJohn Wylie (footballer): John George Wylie (5 October 1854 – 30 July 1924) was an English amateur footballer who played as a forward.  He won the FA Cup with Wanderers in 1878 and played once for England in 1878.  He also took part as an athlete, winning the Pentathlon at the National Olympian Games in 1879.\n\nGeorge W. P. Hunt: George Wylie Paul Hunt (November 1, 1859 – December 24, 1934) was an American politician and businessman.  He was the first Governor of Arizona, serving a total of seven terms, along with President of the convention that wrote Arizona's constitution.  In addition, Hunt served in both houses of the Arizona Territorial Legislature and was posted as U.S. Minister to Siam.\n\nQuestion: George Wylie Hutchinson illustrated the works of which English journalist and short-story writer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"illustrator\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the illustrator.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the illustrator.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the illustrator.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"illustrated_author\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the author whose works were illustrated.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the author.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions of the author.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the relationship between the illustrator and the author's works.\"\n    }\n  },\n  \"required\": [\n    \"illustrator\",\n    \"illustrated_author\",\n    \"relationship_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "illustrator": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the illustrator."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the illustrator."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the illustrator."
          }
        },
        "required": [
          "name",
          "nationality",
          "profession"
        ],
        "additionalProperties": false
      },
      "illustrated_author": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the author whose works were illustrated."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the author."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions of the author."
          }
        },
        "required": [
          "name",
          "nationality",
          "professions"
        ],
        "additionalProperties": false
      },
      "relationship_type": {
        "type": "string",
        "description": "Describes the relationship between the illustrator and the author's works."
      }
    },
    "required": [
      "illustrator",
      "illustrated_author",
      "relationship_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGhosts of Abu Ghraib: Ghosts of Abu Ghraib is a 2007 documentary film, directed by Rory Kennedy, that examines the events of the 2004 Abu Ghraib torture and prisoner abuse scandal.  The film premiered January 19, 2007 at the 2007 Sundance Film Festival.\n\nLem Billings: Kirk LeMoyne \"Lem\" Billings (April 15, 1916 – May 28, 1981) was the close and long-time friend of President John F. Kennedy and the Kennedy family.  Billings was a prep school roommate of Kennedy, an usher at his wedding and a campaigner for his successful 1960 presidential bid.  Joseph Kennedy Sr. called him \"my second son,\" and he sometimes acted as escort to several of the Kennedy women.  Billings served with Sargent Shriver as a trustee for the Kennedy family trusts.\n\nLast Days in Vietnam: Last Days in Vietnam is a 2014 American documentary film written, produced and directed by Rory Kennedy.  The film had its world premiere at 2014 Sundance Film Festival on January 17, 2014.\n\nRory Kennedy: Rory Elizabeth Katherine Kennedy (born December 12, 1968) is an American documentary filmmaker and youngest child of U.S. Senator Robert Kennedy and Ethel Kennedy.\n\nMark Higgins (driver): Mark Higgins (born 21 May 1971) is a Manx rally driver competing in the British Rally Championship.  His co-driver was Rory Kennedy.\n\nRosa Namises: Visolela Rosalinda \"Rosa\" Namises (born 1958), nicknamed the \"Rosa Luxemburg of Namibia\", is a Namibian politician and human-rights activist.  She is a former Member of Parliament and founding member and former secretary-general of the Namibian Congress of Democrats (CoD).  A prominent voice on gender issues, human-rights violations, and violence against women and children in Namibia, she is the director of Woman Solidarity Namibia and works at the \"Dolam Residential Child Care\" centre, a day-care centre for vulnerable children.\n\nStreet Fight (film): Street Fight is a 2005 documentary film by Marshall Curry, chronicling Cory Booker's 2002 campaign against Sharpe James for Mayor of Newark, New Jersey.  Other credits include Rory Kennedy (executive producer), Liz Garbus (executive producer), Mary Manhardt (additional editor), Marisa Karplus (associate producer), and Adam Etline (story consultant).\n\nEthel Kennedy: Ethel Skakel Kennedy (born April 11, 1928) is an American human-rights campaigner and widow of Senator Robert F. Kennedy, who was assassinated while running for nomination as Democratic presidential candidate in 1968.\n\nHuman rights in Sierra Leone: Human rights in Sierra Leone are in a rather deplorable state, but have improved gradually since the end of its civil war in 2002.  Among the major human-rights problems in Sierra Leone today, according to a 2011 U.S. State Department report, are “security force abuse and use of excessive force with detainees, including juveniles; harsh conditions in prisons and jails; official impunity; arbitrary arrest and detention; prolonged detention, excessive bail, and insufficient legal representation; interference with freedom of speech and press; forcible dispersion of demonstrators; widespread official corruption; societal discrimination and violence against women, discrimination based on sexual orientation; female genital mutilation (FGM); child abuse; trafficking in persons, including children; and forced and child labor.”\n\nAmerican Hollow: American Hollow is a 1999 American documentary film directed and produced by Rory Kennedy. The film has been music composed by Bill Frisell.\n\nQuestion: Rory Kennedy is the child of which human-rights campaigner?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"child\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the child.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the child.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"parent\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the parent.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role or profession of the parent as described in the context.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the parent.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the relationship between the child and the parent.\"\n    }\n  },\n  \"required\": [\n    \"child\",\n    \"parent\",\n    \"relationship_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "child": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the child."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the child."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "parent": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the parent."
          },
          "role": {
            "type": "string",
            "description": "The specific role or profession of the parent as described in the context."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the parent."
          }
        },
        "required": [
          "name",
          "role",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "relationship_type": {
        "type": "string",
        "description": "Describes the relationship between the child and the parent."
      }
    },
    "required": [
      "child",
      "parent",
      "relationship_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

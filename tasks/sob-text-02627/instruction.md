{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAll Change: All Change was an English children's television show on ITV in two series.  Originally broadcast in 1989 and 1991, it starred Frankie Howerd, Peggy Mount, Maggie Steed, Tony Haygarth and Pam Ferris.  The series was devised by Morwenna Banks and Chris England.\n\nSuperfrank!: Superfrank!  was a 1987 one-hour television special starring English comedian Frankie Howerd OBE.  The special show marked his return to television performance after an absence of five years.\n\nUp the Front: Up the Front is a 1972 British comedy film.  It is the third film spin-off from the TV series \"Up Pompeii! \" (the previous film being \"Up the Chastity Belt\" set in the Middle Ages which followed on from the \"Up Pompeii\" film), directed by Bob Kellett, it stars Frankie Howerd as Lurk (a descendant of the slave Lurcio in Up Pompeii), a coward who is hypnotised into bravery.\n\nUp Pompeii (film): Up Pompeii is a 1971 British sex comedy film directed by Bob Kellett and starring Frankie Howerd and Michael Hordern.  The film was shot at Elstree Film Studios, Borehamwood, England and is based on characters that first appeared in the British television sitcom \"Up Pompeii! \" (1969–1975).\n\nSunny Rogers: Sunny Rogers (10 May 1913 – 30 December 2005) was an English entertainer best known for her work with comedian Frankie Howerd.\n\nBarry Cryer: Barry Charles Cryer OBE (born 23 March 1935) is an English writer, comedian and actor.  Cryer has written for many noted performers, including Dave Allen, Stanley Baxter, Jack Benny, Rory Bremner, George Burns, Jasper Carrott, Tommy Cooper, Les Dawson, Dick Emery, Kenny Everett, Bruce Forsyth, David Frost, Bob Hope, Frankie Howerd, Richard Pryor, Spike Milligan, Mike Yarwood, The Two Ronnies and Morecambe and Wise.\n\nMiles Tredinnick: Miles Tredinnick, also known as Riff Regan, (born Warrington 18 February 1955) is a rock musician, songwriter and a stage and screenwriter.  In the 1970s, he was the lead singer with the British rock band London.  Afterwards he went on to write comedy plays for the stage.  He has also written scripts for Frankie Howerd, including the television special \"Superfrank! \" and the stage comedy \"Up Pompeii! \"\n\nPeter Sellers: Peter Sellers, CBE (born Richard Henry Sellers; 8 September 1925 – 24 July 1980) was an English film actor, comedian and singer.  He performed in the BBC Radio comedy series \"The Goon Show\", featured on a number of hit comic songs and became known to a worldwide audience through his many film characterisations, among them Chief Inspector Clouseau in \"The Pink Panther\" series of films.\n\nFurther Up the Creek: Further Up the Creek is a 1958 British comedy film written and directed by Val Guest and starring David Tomlinson, Frankie Howerd, Shirley Eaton, Thora Hird, Desmond Llewelyn and Lionel Jeffries.  It served as a follow up to \"Up the Creek\", with Peter Sellers not reprising his role because it clashed with the filming of \"The Mouse That Roared\".  Frankie Howerd was drafted in to replace him.\n\nThe Howerd Confessions: The Howerd Confessions is a British comedy television series which originally aired between 2 September and 7 October 1976 on ITV.  It featured comedian Frankie Howerd \"confessing\" various indiscretions.  The director/producer was Michael MIlls, with scripts by Dave Freeman, Dick Hills, Hugh Stuckey and Peter Robinson.\n\nQuestion: What is the birthdate of this English film actor, comedian, and singer, who was replaced by Frankie Howerd in Further Up the Creek?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person described.\"\n    },\n    \"person_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of roles or professions of the person.\"\n    },\n    \"replaced_in_film\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film where the person was replaced.\"\n    },\n    \"replacement_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who replaced the person in the film.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birthdate of the person.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_roles\",\n    \"replaced_in_film\",\n    \"replacement_actor\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person described."
      },
      "person_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of roles or professions of the person."
      },
      "replaced_in_film": {
        "type": "string",
        "description": "The name of the film where the person was replaced."
      },
      "replacement_actor": {
        "type": "string",
        "description": "The name of the actor who replaced the person in the film."
      },
      "birth_date": {
        "type": "string",
        "description": "The birthdate of the person."
      }
    },
    "required": [
      "person_name",
      "person_roles",
      "replaced_in_film",
      "replacement_actor",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

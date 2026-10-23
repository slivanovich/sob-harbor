{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPark Hyatt Washington: The Park Hyatt Washington is a luxury hotel located at 1201 24th Street NW in the West End neighborhood of Washington, D.C., in the United States.  The operator is Hyatt Hotels Corporation, which since the hotel's opening has branded the structure one of its luxury Park Hyatt properties.  The hotel, a Postmodernist structure which opened in 1986, hosts the Blue Duck Tavern, a restaurant which consistently ranks as one of the city's best.\n\nTorrent duck: The torrent duck (\"Merganetta armata\") is a member of the duck, goose and swan family Anatidae.  It is the only member of the genus Merganetta.  Today it is placed in the shelduck subfamily Tadorninae after the \"perching duck\" assemblage where it was formerly assigned to was dissolved because it turned out to be paraphyletic .  Its closest relative may be the blue duck of New Zealand .\n\nBelle Starr: Myra Maybelle Shirley Reed Starr (February 5, 1848 – February 3, 1889), better known as Belle Starr, was a notorious American outlaw.\n\nBlue duck: The blue duck (\"Hymenolaimus malacorhynchos\") is a member of the duck, goose and swan family Anatidae endemic to New Zealand.  It is the only member of the genus Hymenolaimus.  Its exact taxonomic status is still unresolved, but it appears to be most closely related to the tribe Anatini, the dabbling ducks.  The Māori name, sometimes used in English, is whio (pronounced \"fee-oh\"), which is an onomatopoetic rendition of the males' call.\n\nPomeranian duck: The Pomeranian or Pommern duck (in German \"Pommernente\") is a breed of domesticated duck.  It is a landrace originating in German baltic sea coast region called Pomerania.  Pomeranian ducks share the same ancestors with other northern European duck breeds, such as the Shetland duck and Swedish Blue duck.\n\nFilm still: A film still (sometimes called a publicity still or a production still) is a photograph taken on or off the set of a movie or television program during production.  These photographs are also taken in formal studio settings and venues of opportunity such as film stars' homes, film debut events, and commercial settings.  The photos were taken by studio photographers for promotional purposes.  Such stills consisted of posed portraits, used for public display or free fan handouts, which are sometimes autographed.  They can also consist of posed or candid images taken on the set during production, and may include stars, crew members or directors at work.\n\nBlue Duck (outlaw): Blue Duck, sometimes referred to as Bluford Duck, (1858 – 1895) was an outlaw of the Old West, probably best known for a photograph taken of him around the mid-1880s, in which he posed with Belle Starr, a famous Old West female outlaw.\n\nBlue Duck River: The Blue Duck River is a river of New Zealand.  A tributary of the Dart River, it rises to the south of the Blue Duck Glacier, flowing into that river east of Cattle Flat.\n\nBlue Duck (disambiguation): The blue duck (\"Hymenolaimus malacorhynchos\") is a species of duck, endemic to New Zealand.\n\nIslesford Historical Museum and Blue Duck Ships Store: Islesford Historical Museum and Blue Duck Ships Store\n\nQuestion: What country is the woman who posed in a photograph with Blue Duck from?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"outlaw_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the female outlaw.\"\n    },\n    \"outlaw_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin of the female outlaw.\"\n    },\n    \"associated_outlaw_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the outlaw she posed with.\"\n    },\n    \"association_type\": {\n      \"type\": \"string\",\n      \"description\": \"The nature of the association between the two outlaws.\"\n    }\n  },\n  \"required\": [\n    \"outlaw_name\",\n    \"outlaw_country_of_origin\",\n    \"associated_outlaw_name\",\n    \"association_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "outlaw_name": {
        "type": "string",
        "description": "The name of the female outlaw."
      },
      "outlaw_country_of_origin": {
        "type": "string",
        "description": "The country of origin of the female outlaw."
      },
      "associated_outlaw_name": {
        "type": "string",
        "description": "The name of the outlaw she posed with."
      },
      "association_type": {
        "type": "string",
        "description": "The nature of the association between the two outlaws."
      }
    },
    "required": [
      "outlaw_name",
      "outlaw_country_of_origin",
      "associated_outlaw_name",
      "association_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

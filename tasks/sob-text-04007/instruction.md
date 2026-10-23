{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCharlene McKenna: Charlene Lee McKenna (Irish: \"Searlaoin Nic Chionaoith\" ; born 26 March 1984) is an Irish actress.  Born in Glaslough, County Monaghan, she became a household name and face in Ireland after starring as Jennifer in the television series \"Pure Mule\" in 2005.  She has had numerous other roles in television dramas in Ireland, including \"Raw\", \"Single-Handed 2\" and \"Whistleblower\".  She won the Best Actress (Television) award at the Irish Film and Television Awards in 2009 for \"Raw\" and won the Outstanding Actress in a Mini-Series award for her role in \"Whistleblower\" at the Monte Carlo Television Festival in June 2009.\n\nThe Bostonians (film): The Bostonians is a 1984 British romantic drama film based on Henry James's novel of the same name.  The film stars Vanessa Redgrave, Christopher Reeve, Madeleine Potter and Jessica Tandy.  The movie received respectable reviews and showings at arthouse theaters in New York, London and other cities.  Vanessa Redgrave received 1984 Golden Globe and Academy Award nominations for Best Actress, and the movie earned other award nominations for its costume design.\n\nFionnula Flanagan: Fionnghuala Manon \"Fionnula\" Flanagan (born 10 December 1941) is an Irish actress and political activist.\n\nA Passage to India (film): A Passage to India is a 1984 British period drama film written and directed by David Lean.  The screenplay is based on the play of the same name by Santha Rama Rau, which was based on the novel of the same name by E.M. Forster.\n\nSabina Coyne: Sabina Mary Coyne (born 5 May 1944) is an Irish actress, political activist and the wife of the current President of Ireland, Michael D. Higgins.\n\nReflections (1984 film): Reflections is a 1984 British drama film directed by Kevin Billington and starring Gabriel Byrne, Donal McCann and Fionnula Flanagan.\n\nWhite Elephant (1984 film): White Elephant is a 1984 British comedy drama film directed by Werner Grusch and starring Peter Firth, Peter Sarpong and Nana Seowg.  The plot involves a ruthless white man determined to break through thousands of years of tradition to sell microchips in Africa.  A young British businessman goes to Ghana to modernise a furniture factory by introducing computers.  Unbeknownst to him, the spirits of African tradition are already working against him and are determined to make him pay.  He encounters fierce resistance from the Ghanaians, and this eventually leads him to better appreciate their culture.\n\nNineteen Eighty-Four (1984 film): Nineteen Eighty-Four, also known as 1984, is a 1984 British dystopian drama film written for the screen and directed by Michael Radford, based upon George Orwell's novel of the same name.  Starring John Hurt, Richard Burton, Suzanna Hamilton, and Cyril Cusack, the film follows the life of Winston Smith in Oceania, a country run by a totalitarian socialist government.\n\nGive My Regards to Broad Street (film): Give My Regards to Broad Street is a 1984 British musical drama film directed by Peter Webb, which starred Paul McCartney, Bryan Brown and Ringo Starr.  The film covers a fictional day in the life of Paul McCartney, who wrote the film for the screen, and McCartney, Starr and Linda McCartney all appeared as themselves.  Despite \"Give My Regards to Broad Street\" being unsuccessful in the box office financially and critically, its soundtrack album sold well.  The title is a take on George M. Cohan's classic show tune \"Give My Regards to Broadway\" which made reference to London's Broad Street railway station, which would close in 1986.\n\nSecret Places: Secret Places is a 1984 British drama film directed by Zelda Barron and starring Marie Theres Relin, Tara MacGowran, Claudine Auger and Jenny Agutter.\n\nQuestion: Name the Irish actress and political activist who starred in the 1984 British drama film Reflections?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actress.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actress.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the actress.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"nationality\",\n    \"professions\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The full name of the actress."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the actress."
      },
      "professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the actress."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "title",
          "year",
          "genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actress_name",
      "nationality",
      "professions",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWilliam J. Blake: William James Blake (1894–1968) was a broker, novelist and Marxist political economist.  His birth name was Wilhelm Blech.  His first marriage ended in divorce, and he then married Australian novelist Christina Stead, with whom he had been living since the late 1920s.  Blake's father was physician, surgeon, and medical educator Gustavus M. Blech, M.D.\n\nLe Marteau sans maître: Le Marteau sans maître (] , The Hammer without a Master) is a composition by French composer Pierre Boulez.  First performed in 1955, it sets the surrealist poetry of René Char for contralto and six instrumentalists.\n\nThe Man Who Loved Children: The Man Who Loved Children is a 1940 novel by Australian writer Christina Stead.  It was not until a reissue edition in 1965, with an introduction by poet Randall Jarrell, that it found widespread critical acclaim and popularity.  \"Time\" magazine included the novel in its \"TIME 100 Best English-language Novels from 1923 to 2005\".  The novel has been championed by novelists Robert Stone, Jonathan Franzen and Angela Carter.  Carter believed Stead's other novels \"Cotters England\"; \"A Little Tea, A Little Chat\"; and \"For Love Alone\" to be as good, if not better than \"The Man Who Loved Children\".\n\nRoger Milliot: Roger Milliot (1927, Le Creusot - 1968) was a French poet and painter.  He served as a soldier in Indochina and as such had a pension.  His health problems prevented him from becoming an ornamentalist.  Like his idol René Char, he preferred provincial life to that of Paris and lived in Montauban, where there is now a museum of his paintings, mostly portraits of women.  His depression and feelings of frustration led him to suicide by drowning in the Seine river.  His poems were published posthumously.\n\nThe Library Is on Fire: The Library is on Fire is an American indie rock band formed by singer/guitarist Steve Five in 2007.  Their sound has been described as art punk.  The band originally began from a manifesto of the same name written by Five.  Five took the name from a poem by French war poet René Char while working at Strand Bookstore, after weekly meetings over coffee with Television guitarist Tom Verlaine.  The band headlined their first New York show at Glasslands Gallery in 2008, with future Grammy nominees The Ting Tings opening.\n\nChristina Stead: Christina Stead (17 July 190231 March 1983) was an Australian novelist and short-story writer acclaimed for her satirical wit and penetrating psychological characterisations.  Christina Stead was a committed Marxist, although she was never a member of the Communist Party.  She spent much of her life outside Australia.\n\nLetty Fox: Her Luck: Letty Fox: Her Luck is Australian-born author Christina Stead’s sixth novel.  It is a tribute to the drama of the urban environment and its role in socializing its occupants.  Published in 1946, Stead wrote the lengthy \"Letty Fox\" after living in New York City for seven years.  The cosmopolitan setting serves well as the theater in which Stead develops her characters through their adventures with numerous careers, love affairs, familial obligations, and sensitivities to reputation.  To this end, \"Letty Fox\" has been described as “a modern picaresque novel and psychological novel at the same time.”\n\nRené Char: René Char (] ; 14 June 1907 – 19 February 1988) was a 20th-century French poet and member of the French Resistance.\n\nLe Visage nuptial: Le Visage nuptial (\"The Nuptial Face\") is a secular cantata for soprano, contralto, choir of women and orchestra by Pierre Boulez.  Originally composed in 1946–47 on a poem by René Char for two voices, two ondes Martenot, piano and percussion, the work, revised in 1951–52 in a version for voices and orchestra, was premiered on 4 December 1957 in Cologne conducted by the composer.  The score was further revised in 1989, removing the quarter tones present in the second and fifth parts of the 1951–52 version, while revising the orchestration.  A version with final revisions by the composer was premiered on 25 February 2014 at the Cité de la Musique in Paris during the closing concert of the festival \"Présences\" of Radio France.\n\nDavid Crook: David Crook (14 August 1910 – 1 November 2000) was a British-born Communist ideologue, activist and spy, long resident in China.  A committed Marxist from 1931, he joined the International Brigades during the Spanish Civil War (1936–39), then was recruited by the KGB, the Soviet secret police, and was sent to China during the Second Sino-Japanese War (1937–45).  There he met and married his wife, Isabel, a teacher and social activist.  Following the Second World War and the Chinese Civil War, the couple stayed in China and taught English.\n\nQuestion: Which activist, Christina Stead or René Char, was a committed Marxist?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"activist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the activist who was a committed Marxist.\"\n    },\n    \"is_marxist\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the activist was a committed Marxist.\"\n    },\n    \"reasoning_for_marxism\": {\n      \"type\": \"string\",\n      \"description\": \"The direct quote from the context confirming the activist's Marxist commitment.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the activist.\"\n    },\n    \"death_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The death year of the activist.\"\n    },\n    \"associated_novels\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of novels written by the activist.\"\n    }\n  },\n  \"required\": [\n    \"activist_name\",\n    \"is_marxist\",\n    \"reasoning_for_marxism\",\n    \"birth_year\",\n    \"death_year\",\n    \"associated_novels\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "activist_name": {
        "type": "string",
        "description": "The name of the activist who was a committed Marxist."
      },
      "is_marxist": {
        "type": "boolean",
        "description": "Indicates whether the activist was a committed Marxist."
      },
      "reasoning_for_marxism": {
        "type": "string",
        "description": "The direct quote from the context confirming the activist's Marxist commitment."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the activist."
      },
      "death_year": {
        "type": "integer",
        "description": "The death year of the activist."
      },
      "associated_novels": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of novels written by the activist."
      }
    },
    "required": [
      "activist_name",
      "is_marxist",
      "reasoning_for_marxism",
      "birth_year",
      "death_year",
      "associated_novels"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHristo Smirnenski: Hristo Smirnenski (Bulgarian: Христо Смирненски ), born Hristo Izmirliev, (September 17, 1898, OS - June 18, 1923) was a Bulgarian poet and prose writer who joined the Communist Party and whose works championed socialist ideals in a light-hearted and humane style.  He died at the age of 25, leaving a well regarded body of work produced over a mature career of only three years.\n\nKen Loach: Kenneth Charles Loach (born 17 June 1936) is an English director of television and independent film.  He is known for his socially critical directing style and for his socialist ideals, which are evident in his film treatment of social issues such as poverty (\"Poor Cow\", 1967), homelessness (\"Cathy Come Home\", 1966) and labour rights (\"Riff-Raff\", 1991, and \"The Navigators\", 2001).\n\nMy Name Is Joe: My Name Is Joe is a 1998 British film directed by Ken Loach.  The film stars Peter Mullan as Joe Kavanagh, an unemployed recovering alcoholic in Glasgow who meets and falls in love with a health visitor.  David McKay plays his troubled friend Liam.  The film's title is a reference to the ritualised greeting performed in Alcoholics Anonymous meetings, as portrayed in the film's opening scene.\n\nWilliam Carr Smith: William Carr Smith (1857–1930) was a Church of England clergyman, best known as the rector of St James' Church, Sydney from 1896 to 1910, whose Anglo-Catholic and Christian Socialist ideals transformed Sydney's oldest church.  Carr Smith's teaching was said to be \"continuous, methodical, very direct, very plain, and quite fearless\".\n\nTang Shu Shuen: Tang Shu Shuen (; born 1941), also known as Cecile Tang Shu Shuen, is a former Hong Kong film director.  Though her film career was brief, she was a trailblazer for socially critical art cinema in Hong Kong's populist film industry, as well as its first noted woman director.\n\nAlbert Chavannes: Albert Chavannes (February 23, 1836 – May 3, 1903) was a Swiss-born American author, philosopher, and sociologist, active primarily in the late 19th century.  He is best known for his two utopian novels, \"The Future Commonwealth\" and \"In Brighter Climes\", which discuss a fictional futuristic society, \"Socioland,\" where the economy is governed by socialist ideals rather than capitalism, and where morality is based on social scientific experimentation, rather than traditional religion.  Chavannes was also one of the earliest social theorists to extensively discuss exchange theory, and his ideas on \"magnetism\" (magnetation) influenced writers such as J. William Lloyd and Ida C. Craddock.\n\nI'm Just a Country Boy: \"I'm Just a Country Boy\" is a song written by Fred Hellerman and Marshall Baker.  In 1954, the song was recorded by Harry Belafonte accompanied by Hugo Winterhalter And His Orchestra (RCA Victor) and released on 78 rpm and 45 rpm record.  It was the B-side of the record, \"Hold 'Em Joe\" (Calypso) being the A-side.  The print on the record informs us that the song was written by Fred Brooks and Marshall Barer, noting that Fred Brooks was a pseudonym for Fred Hellerman (of The Weavers fame) who was blacklisted in the McCarthy era for his socialist ideals.\n\nAustralian Fabian Society: The Australian Fabians (also known as the Australian Fabian Society) was established in 1947.  Inspired by the Fabian Society in the United Kingdom, it is dedicated to Fabianism, the focus on the advancement of socialist ideas through gradual influence and patiently promoting socialist ideals to intellectual circles and groups with power.\n\nDuke St. Rollins: Duke St. Rollins is a U.S-based politically progressive Internet troll on Facebook who received mainstream press notoriety for his socially critical and witty commentary in reply to posts made by major U.S. political and conservative media figures.  His outputs have been dubbed by mainstream media journalists as \"extraordinary\" and coming from \"a performance artist.\"  Among his favored targets are Governor Jan Brewer of Arizona, Sheriff Joe Arpaio of Maricopa County, Arizona, and Fox News Channel program host Sean Hannity.\n\nEnvy (novel): Envy (Russian: \"Зависть\") is a novel published in 1927 by the Russian novelist Yuri Olesha.  It is remarkable for its poetic style, undulating modes of transition between the scenes, innovative structure, biting satire, and ruthless examination of Socialist ideals.\n\nQuestion: What English director known for his socially critical directing style and socialist ideals directed the film My Name is Joe?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director.\"\n    },\n    \"director_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the director.\"\n    },\n    \"known_for_style\": {\n      \"type\": \"string\",\n      \"description\": \"The directing style the director is known for.\"\n    },\n    \"ideals\": {\n      \"type\": \"string\",\n      \"description\": \"The ideals championed by the director.\"\n    },\n    \"film_directed\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film directed.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"director_nationality\",\n    \"known_for_style\",\n    \"ideals\",\n    \"film_directed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the director."
      },
      "director_nationality": {
        "type": "string",
        "description": "The nationality of the director."
      },
      "known_for_style": {
        "type": "string",
        "description": "The directing style the director is known for."
      },
      "ideals": {
        "type": "string",
        "description": "The ideals championed by the director."
      },
      "film_directed": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film directed."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "director_name",
      "director_nationality",
      "known_for_style",
      "ideals",
      "film_directed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

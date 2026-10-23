{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLawrence Dobkin: Lawrence \"Larry\" Dobkin (September 16, 1919 – October 28, 2002) was an American television director, character actor and screenwriter whose career spanned seven decades.\n\nJames Ottaway: James Ottaway (25 July 1908 – 16 June 1999) was a British film, television and stage actor whose career spanned seven decades.\n\nGilbert Roland: Gilbert Roland (December 11, 1905May 15, 1994) was a Mexican-born American film and television actor whose career spanned seven decades from the 1920s until the 1980s.  He was twice nominated for the Golden Globe Award in 1952 and 1964, and inducted to the Hollywood Walk of Fame in 1960.\n\nJames Best: James Best (born Jewel Franklin Guy; July 26, 1926 – April 6, 2015) was an American television, film, character, voice, and stage actor, as well as a writer, director, acting coach, artist, college professor, and musician, whose career spanned seven decades of television.  He appeared as a guest on various country music and talk shows.\n\nBuddy Ebsen: Christian Ludolf \"Buddy\" Ebsen Jr. (April 2, 1908 – July 6, 2003) was an American singer, dancer, author, film, television and character actor, whose career spanned seven decades.  He had also appeared as a guest on several talk and variety shows.  The SAG-AFTRA records also show him as Frank \"Buddy\" Ebsen.\n\nWinchester '73: Winchester '73 is a 1950 American Western film directed by Anthony Mann starring James Stewart, Shelley Winters, Dan Duryea and Stephen McNally.  Written by Borden Chase and Robert L. Richards, the film is about the journey of a prized rifle from one ill-fated owner to another and a cowboy's search for a murderous fugitive.  The movie features early film performances by Rock Hudson as an American Indian, Tony Curtis, and James Best.  The film received a Writers Guild of America Award nomination for Best Written American Western.  This is the first Western film collaboration between Anthony Mann and James Stewart.  It was filmed in black and white.\n\nNorris Houghton: Charles Norris Houghton (26 December 1909 – 9 October 2001) was a renowned theatre visionary whose career spanned seven decades.  Credited with over 50 theatre productions, he was stage manager, scenic designer, producer, director, theatre manager, academician, author, and public policy advocate: these myriad roles reflect his chosen life as a “generalist,” a multifaceted “theatre man.”  He is celebrated for accomplishments that reflect this span: as the premier American expert of 20th-century Russian Theatre; as a major force in creating the “off-Broadway” movement and inspiring live theater throughout the country; as a mentor to actors and innovators in world theatre; as an influential advocate of arts education; and as a student and educator of global theater chosen by prestigious foundations to study and report on theater across the U.S., Europe, and Asia.  His career culminated with his accomplishments as a distinguished scholar and teacher, selected to teach and promote theatre as part of a liberal education in such prominent universities as Princeton, Columbia, and Vassar; his academic career was completed at the State University of New York, where he helped create the SUNY Purchase campus and served as founding Dean of Theatre and Film.  A prolific author, this multifaceted life is documented in his books and articles, and his work has been the subject of analysis and commentary by admiring colleagues and reviewers in numerous articles, books, journals, and newspapers.  His books and papers are preserved for study in prestigious university and college library, archives, and rare book collections.\n\nGladys Cooper: Dame Gladys Constance Cooper, DBE (18 December 1888 – 17 November 1971) was an English actress whose career spanned seven decades on stage, in films and on television.\n\nMichael Hordern on stage, screen and radio: Michael Hordern (1911–1995) was an English actor whose career spanned seven decades.  He made more than 160 film appearances, usually in supporting character roles, and appeared in over 100 theatrical productions, most of them Shakespeare.\n\nEstelle Harman: Estelle Harman (September 11, 1922 – April 15, 1995) was an acting coach in Los Angeles.  She began as an acting instructor at UCLA in the 1950s, then was hired by Universal Studios as Head of Talent to groom their stable of film actors, which included Rock Hudson, Bill Bixby, Tony Curtis and Audie Murphy.\n\nQuestion: Winchester '73 features early film performances by Rock Hudson as an American Indian, Tony Curtis, and which American television, film, character, voice, and stage actor, as well as a writer, director, acting coach, artist, college professor, and musician, whose career spanned seven decades of television?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"identified_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor identified in the question.\"\n        },\n        \"career_span_decades\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of decades the actor's career spanned.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions held by the identified actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"career_span_decades\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"other_early_performance_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of other actors mentioned for early film performances in the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_details\",\n    \"identified_actor\",\n    \"other_early_performance_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "identified_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor identified in the question."
          },
          "career_span_decades": {
            "type": "integer",
            "description": "The number of decades the actor's career spanned."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions held by the identified actor."
          }
        },
        "required": [
          "name",
          "career_span_decades",
          "professions"
        ],
        "additionalProperties": false
      },
      "other_early_performance_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of other actors mentioned for early film performances in the movie."
      }
    },
    "required": [
      "movie_details",
      "identified_actor",
      "other_early_performance_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

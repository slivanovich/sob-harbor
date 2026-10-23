{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSwingers (1996 film): Swingers is a 1996 American comedy-drama film about the lives of single, unemployed actors living on the 'eastside' of Hollywood, California during the 1990s swing revival.  Written by Jon Favreau and directed by Doug Liman, the film starred Favreau and Vince Vaughn, and also featured performances by Ron Livingston and Heather Graham.\n\nJulianne Moore: Julianne Moore (born Julie Anne Smith; December 3, 1960) is an American actress, prolific in films since the early 1990s.  She is particularly known for her portrayals of emotionally troubled women in both independent and Hollywood films, and has received many accolades, including the 2014 Academy Award for Best Actress.\n\nA Novel Romance: A Novel Romance is a 2011 comedy-drama film about a chance meeting between two strangers that leads the unlikely pair to become roommates, and despite their differences, the two eventually realize that they have spent all their lives waiting for one another.  The film is produced by Morris S. Levy and directed by Allie Dvorin.  It stars Steve Guttenberg, Milena Govich and Shannon Elizabeth, with cinematography by Jon Miguel Delgado, editing by Glenn Conte, and a musical score by Michelangelo Sosnowitz.\n\nB.S. I Love You: B.S. I Love You is an American comedy-drama film from 1971.  It was directed and written by Steven Hilliard Stern, and starred Peter Kastner.  The supporting cast included Gary Burghoff, Louise Sorel, Joanna Cameron and Joanna Barnes.  The style of the film is like many others of its era, taking its cues from \"The Graduate\" and the raunchiness of the early 1970s, as Kastner plays a youthful TV commercials producer whose quest in life is to bed as many women as possible, while trying to remain faithful to his childhood sweetheart who remains in tow, awaiting the day they will marry.\n\nRoommates (1995 film): Roommates is a 1995 American comedy-drama film, starring Peter Falk, D.B. Sweeney and Julianne Moore, directed by Peter Yates.  The original music score was composed by Elmer Bernstein.  The film was marketed with the tagline \"Some people talk.  Some people listen.  When you're 107 and going strong, you do whatever you want.\"\n\nThe Poor Little Rich Girl: The Poor Little Rich Girl is a 1917 American comedy-drama film directed by Maurice Tourneur.  Adapted by Frances Marion from the 1913 play by Eleanor Gates.  The Broadway play actually starred future screen actress Viola Dana.  The film stars Mary Pickford, Madlaine Traverse, Charles Wellesley, Gladys Fairbanks (returning from the play) and Frank McGlynn, Sr.\n\nThe Grass Harp (film): The Grass Harp is a 1995 American comedy-drama film based on the novella by Truman Capote; the screenplay was the final work of Oscar-winning screenwriter Stirling Silliphant.  The film was directed by Charles Matthau, and starred Piper Laurie, Sissy Spacek, the director's father Walter Matthau, Edward Furlong, and Nell Carter.  Piper Laurie won the Best Supporting Actress award from the Southeastern Film Critics Association for her work on the film.\n\nMermaids (1990 film): Mermaids is a 1990 American comedy-drama film directed by Richard Benjamin and starring Cher, Bob Hoskins, Winona Ryder (who was nominated for a Golden Globe Award for best supporting actress for her role), and Christina Ricci in her first film role.  It is based on the 1986 novel of the same title written by Patty Dann.  It was shot in and around the town of Rockport, Massachusetts, Gloucester, Massachusetts, Ipswich, Massachusetts, Lincoln, Massachusetts and Pawtucket, Rhode Island.\n\nReality Bites: Reality Bites is a 1994 American romantic comedy-drama film written by Helen Childress and directed by Ben Stiller.  It stars Winona Ryder, Ethan Hawke and Stiller, with supporting roles by Janeane Garofalo and Steve Zahn.  The plot follows Lelaina (Ryder), an aspiring videographer working on a documentary called \"Reality Bites\" about the disenfranchised lives of her friends and roommates.  Their challenges exemplify some of the career and lifestyle choices faced by Generation X.\n\nMe, Natalie: Me, Natalie is a 1969 American comedy-drama film directed by Fred Coe about a homely young woman from Brooklyn who moves to Greenwich Village and finds romance with an aspiring painter.  The screenplay by A. Martin Zweiback is based on an original story by Stanley Shapiro.  Patty Duke, who starred in the title role, won a Golden Globe Award for her performance.  The film also starred James Farentino, Salome Jens, Elsa Lanchester, Martin Balsam and Nancy Marchand.  Al Pacino made his film debut with a bit part.\n\nQuestion: What American actress from the early 1990s starred in the American comedy-drama film Roommates?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        },\n        \"active_period_start\": {\n          \"type\": \"string\",\n          \"description\": \"The period when the actress became prolific in films.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"active_period_start\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          },
          "active_period_start": {
            "type": "string",
            "description": "The period when the actress became prolific in films."
          }
        },
        "required": [
          "name",
          "nationality",
          "active_period_start"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

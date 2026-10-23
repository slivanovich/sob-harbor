{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouth Side Writers Group: The South Side Writers Group (occasionally called South Side Writers' Group) was a circle of African-American writers and poets formed in the 1930s in Chicago, which included Richard Wright, Arna Bontemps, Margaret Walker, Fenton Johnson, Theodore Ward, Garfield Gordon, Frank Marshall Davis, Julius Weil, Dorothy Sutton, Russell Marshall, Robert Davis, Marion Perkins, Arthur Bland, Fern Gayden, and Alberta Sims .  Consisting of some twenty authors, the group championed the New Realism movement and Social realism.  The group met at the Abraham Lincoln Centre on South Cottage Grove Avenue near the Bronzeville District.\n\nTrade unions in Ecuador: Disunited and poorly organized for most of its history, trade unions in Ecuador developed only slowly and had only a marginal political impact.  Precise figures on unionization in the late 1980s were practically nonexistent, even within the unions themselves.  The organized labor movement in Ecuador was divided into four confederations and a number of independent federations.  At the local level, labor organizations also took the form of artisan guilds, cooperatives, and neighborhood associations.  In addition to representing only a minority of the workers in all sectors of employment (approximately one-fifth), the labor movement traditionally was weakened by rivalry and government repression.  Nevertheless, it had influence disproportionate to its numbers as a result of the concentration of trade unions in urban areas, mainly Quito and Guayaquil, its organizational power, and the political impact of strikes and demonstrations on governments that did not enjoy strong support.\n\nCesar Chavez Day: Cesar Chavez Day is a federal commemorative holiday in the U.S. by proclamation of President Obama in 2014.  On March 31 of each year, it celebrates the birth and legacy of the civil rights and labor movement activist Cesar Chavez.\n\nFrank Marshall Davis: Frank Marshall Davis (December 31, 1905 – July 26, 1987) was an American journalist, poet, political and labor movement activist, and businessman.\n\nChicago Black Renaissance: The Chicago Black Renaissance (also known as the Black Chicago Renaissance) was a creative movement that blossomed out of the Chicago Black Belt on the city's South Side and spanned the 1930s and 1940s before a transformation in art and culture in the mid-1950s through the turn of the century.  The movement included such famous African-American writers as Richard Wright, Margaret Walker, Gwendolyn Brooks, Arna Bontemps, and Lorraine Hansberry, as well as musicians Thomas A. Dorsey, Louis Armstrong, and Earl Hines.  During the Great Migration, which brought tens of thousands of African-Americans to Chicago's South Side, African-American writers, artists, and community leaders began promoting racial pride and a new black consciousness, similar to that of the Harlem Renaissance in New York City.  Unlike the Harlem Renaissance, the Chicago Black Renaissance did not receive the same amount of publicity on a national setting.  This was due to several factors, including the lower profile participants in the movement, the lack of wealthy patrons investing in the movement, and a geographical distance from New York as a publishing center.\n\nCarl Minkley: Carl Minkley (November 14, 1866 – July 26, 1937) was an interior decorator, housepainter, labor movement activist and Socialist Party of America politician from Milwaukee, Wisconsin who served two terms in the Wisconsin State Assembly (as well as being an alderman for the City of Milwaukee).\n\nEva Valesh: Eva McDonald Valesh (1866–1956) was an American journalist and labor rights activist.  Valesh was an activist for, and reported on conditions of laborers in Minnesota's garment factories.  She was also a speaker for the Knights of Labor movement and the National Farmer's Alliance.\n\nFrances Nacke Noel: Frances Nacke Noel (January 5, 1873 – April 24, 1963) was a women’s labor activist and suffragette, and was known as \"the most eloquent female orator of Southern California\" in the early 20th century.  Nacke acted as one of the primary female labor and suffrage leaders in the Los Angeles labor movement.  She was one of the first \"progressive activists\" to tie to the suffragette movement to the labor movement, thereby achieving mutual goals of emancipation of both women and workers.  Through her oration and organization, Nacke was a key contributor to the passing of the suffrage movement in Los Angeles.  A large part of Nacke’s platform throughout her life was compromising the differences between class divisions in the labor movement.\n\nAfrican-American literature: African-American literature is the body of literature produced in the United States by writers of African descent.  It begins with the works of such late 18th-century writers as Phillis Wheatley.  Before the high point of slave narratives, African-American literature was dominated by autobiographical spiritual narratives.  The genre known as slave narratives in the 19th century were accounts by people who had generally escaped from slavery, about their journeys to freedom and ways they claimed their lives.  The Harlem Renaissance of the 1920s was a great period of flowering in literature and the arts, influenced both by writers who came North in the Great Migration and those who were immigrants from Jamaica and other Caribbean islands.  African-American writers have been recognized by the highest awards, including the Nobel Prize to Toni Morrison.  Among the themes and issues explored in this literature are the role of African Americans within the larger American society, African-American culture, racism, slavery, and social equality.  African-American writing has tended to incorporate oral forms, such as spirituals, sermons, gospel music, blues, or rap.\n\nSatrio Arismunandar: Satrio Arismunandar (born 1961) was a student movement activist from Indonesia.  He founded the Alliance of Independent Journalists (AJI) in 1994, as an organization that opposed the Suharto regime.  Its involvement in the labor movement led to him being forced to step down from the daily newspaper Kompas in 1995.\n\nQuestion: The South Side Writers Group was a circle of African-American writers and poets formed in the 1930s which included an an American journalist, poet, political and labor movement activist and what? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the writers' group.\"\n    },\n    \"formation_period\": {\n      \"type\": \"string\",\n      \"description\": \"The decade when the group was formed.\"\n    },\n    \"member_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"member_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the specific member being described.\"\n        },\n        \"known_professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions or roles attributed to the member that were explicitly mentioned in the question.\"\n        },\n        \"additional_profession\": {\n          \"type\": \"string\",\n          \"description\": \"The additional profession or role of the member that completes the description.\"\n        }\n      },\n      \"required\": [\n        \"member_name\",\n        \"known_professions\",\n        \"additional_profession\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"group_name\",\n    \"formation_period\",\n    \"member_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "group_name": {
        "type": "string",
        "description": "The name of the writers' group."
      },
      "formation_period": {
        "type": "string",
        "description": "The decade when the group was formed."
      },
      "member_details": {
        "type": "object",
        "properties": {
          "member_name": {
            "type": "string",
            "description": "The name of the specific member being described."
          },
          "known_professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions or roles attributed to the member that were explicitly mentioned in the question."
          },
          "additional_profession": {
            "type": "string",
            "description": "The additional profession or role of the member that completes the description."
          }
        },
        "required": [
          "member_name",
          "known_professions",
          "additional_profession"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "group_name",
      "formation_period",
      "member_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

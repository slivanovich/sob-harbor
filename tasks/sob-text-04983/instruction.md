{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Class Struggle (magazine): The Class Struggle was a bi-monthly Marxist theoretical magazine published in New York City by the Socialist Publication Society.  The SPS also published a series of pamphlets, mostly reprints from the magazine during the short period of its existence.  Among the initial editors of the publication were Ludwig Lore, Marxist theoreticians Louis B. Boudin and Louis C. Fraina, the former of whom left the publication in 1918.  In the third and final year of the periodical, \"The Class Struggle\" emerged as one of the primary English-language voices of the left wing factions within the American Socialist Party and its final issue was published in 1919 by the nascent Communist Labor Party of America.\n\nThe Beverly Hills Hotel: The Beverly Hills Hotel, also called \"The Beverly Hills Hotel and Bungalows\", is located on Sunset Boulevard in Beverly Hills, California.  One of the world's best-known hotels, it is closely associated with Hollywood film stars, rock stars and celebrities.  The hotel has 208 guest rooms and suites, and 23 bungalows, each designed in the peachy pink and green colors which are a trademark of the hotel.\n\nBeverly Hills Chihuahua: Beverly Hills Chihuahua is a 2008 American family comedy film produced by Walt Disney Pictures, the first in the \"Beverly Hills Chihuahua\" series.  It is directed by Raja Gosnell and was released on October 3, 2008.  The films stars Piper Perabo, Jamie Lee Curtis and Manolo Cardona as the human leads and Drew Barrymore, George Lopez and Andy Garcia in voice-over roles.  The plot centers on a Chihuahua, Chloe, who gets dognapped in Mexico and has to escape from an evil Doberman, El Diablo, with a help from a lonely German Shepherd, Delgado and a hyperactive male Chihuahua, Papi, who has a desperate crush on her.  A sequel, \"Beverly Hills Chihuahua 2\", was released on direct-to-DVD on February 1, 2011, and \"\" was released on September 18, 2012.\n\nBeverly Hills Cop II: Beverly Hills Cop II is a 1987 American action comedy film directed by Tony Scott, written by Larry Ferguson and Warren Skaaren and starring Eddie Murphy.  It is the sequel to the 1984 film \"Beverly Hills Cop\" and the second installment in the \"Beverly Hills Cop\" series.  Murphy returns as Detroit police detective Axel Foley, who reunites with Beverly Hills detectives Billy Rosewood (Judge Reinhold) and John Taggart (John Ashton) to stop a robbery/gun-running gang after Captain Andrew Bogomil (Ronny Cox) is shot and seriously wounded.\n\nBeverly Hills Cop III: Beverly Hills Cop III is a 1994 American action comedy film starring Eddie Murphy and directed by John Landis, who had previously worked with Murphy on \"Trading Places\" and \"Coming to America\".  It is the third film in the \"Beverly Hills Cop\" trilogy, and a sequel to \"Beverly Hills Cop II\".\n\nRebecca Schaeffer: Rebecca Lucile Schaeffer (November 6, 1967 – July 18, 1989) was an American model and actress.\n\nBeverly Hills Playhouse: The Beverly Hills Playhouse is an acting school with theaters and training facilities in Beverly Hills, California, and also in Los Angeles, San Francisco, and New York City.  It is one of the oldest acting schools and theatres in Los Angeles County, California.  It is located at 254 South Robertson Boulevard in Beverly Hills.\n\nAggravation of class struggle under socialism: The theory of aggravation of the class struggle along with the development of socialism was one of the cornerstones of Stalinism in the internal politics of the Soviet Union.  Although the term \"class struggle\" was introduced by Marx and Engels, and \"aggravation of class struggle\" was an expression originally coined by Vladimir Lenin in 1919 to refer to the dictatorship of the proletariat, the theory of \"class struggle under socialism\" was put forward by Joseph Stalin in 1933 and supplied a theoretical base for the claim that ongoing repression of \"capitalist elements\" is necessary.  Stalin believed that residual bourgeois elements would persist within the country and that, with support from Western powers, they would try to infiltrate the party.  A variation of the theory was also adopted by Mao Zedong in China.\n\nScenes from the Class Struggle in Beverly Hills: Scenes from the Class Struggle in Beverly Hills is a 1989 American black comedy film co-written and directed by Paul Bartel.  \"Scenes\" re-unites Bartel with his \"Eating Raoul\" co-stars Mary Woronov and Robert Beltran.  \"Scenes\" also stars Jacqueline Bisset, Ray Sharkey, Ed Begley, Jr., Wallace Shawn, Paul Mazursky, and Rebecca Schaeffer.\n\nBeverly Hills Cop (franchise): Beverly Hills Cop is a series of American action comedy films and an unaired television pilot based on characters created by Daniel Petrie, Jr. and Danilo Bach.  The films star Eddie Murphy as Axel Foley, a street-smart Detroit cop who travels to Beverly Hills, California to investigate crimes, even though it is out of his jurisdiction.  There, he meets Detective Billy Rosewood (Judge Reinhold), Sergeant John Taggart (John Ashton), and Lieutenant Andrew Bogomil (Ronny Cox).  Ashton and Cox do not appear in \"Beverly Hills Cop III\".  Murphy, Reinhold, and Gil Hill, who plays Axel's boss, Inspector Todd, are the only actors who appear in all three films.  Harold Faltermeyer produced the now famous \"Axel F\" theme song heard throughout the series.  The series as a whole have been distributed by Paramount Pictures.  The films have made a total of $735,534,503 at the worldwide box office.\n\nQuestion: Scenes from the Class Struggle in Beverly Hills, an 1989 American black comedy that stars Mary Moronov, also featured one of the last performances of which Amerian model and actress? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"featured_actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the actress.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"featured_actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "featured_actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the actress."
          }
        },
        "required": [
          "name",
          "profession"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_genre",
      "featured_actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

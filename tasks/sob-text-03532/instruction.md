{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBangladesh Film Directors Association: Bangladesh Film Directors Association is the pan-national trade body of film directors in Bangladesh.  The Bangladesh Film Directors Association’s General Secretary is Badiul Alam Khokon.  Mushfiqur Rahman Gulzar is the president of Bangladesh Film Directors Association.\n\nMichael Anderson (director): Michael Joseph Anderson, Sr. (born 30 January 1920) is an English film director, best known for directing the Second World War film \"The Dam Busters\" (1955), the epic \"Around the World in 80 Days\" (1956) and the dystopian sci-fi film \"Logan's Run\" (1976).\n\nSchool Daze: School Daze is a 1988 American musical comedy drama film, written and directed by Spike Lee, and starring Larry Fishburne, Giancarlo Esposito, and Tisha Campbell-Martin.  Based in part on Spike Lee's experiences at Atlanta's Morehouse College, Spelman College, Morris Brown College and Clark Atlanta University, it is a story about fraternity and sorority members clashing with other students at a historically black college during homecoming weekend.  It also touches upon issues of colorism and hair texture bias within the African-American community.  The second feature film by Spike Lee, \"School Daze\" was released on February 12, 1988 by Columbia Pictures.\n\nGirl 6: Girl 6 is a 1996 American comedy-drama film by director Spike Lee about a phone sex operator.  Theresa Randle played the title character, and playwright Suzan-Lori Parks wrote the screenplay.  The soundtrack is composed entirely of songs written by Prince.  The film was screened in the Un Certain Regard section at the 1996 Cannes Film Festival.  Directors Quentin Tarantino and Ron Silver make cameo appearances as film directors at a pair of interesting auditions.  It is the first film directed by Lee in which he did not write the screenplay.\n\nFurious George: Furious George is a punk rock band on Lookout Records and later, Recess Records.  Fronted by George Tabb, it also included Evan Cohen (and later, Stevie \"Ramone\" Burkes) on bass guitar and Michael Harper on drums. Furious George released two full-length albums: \"Gets a Record\" in 1997, and \"V.M. Live\" in 1999, as well as a series of singles and EPs.  George Tabb's band played as the character Richie's (Adrien Brody) punk band in the Spike Lee film \"Summer of Sam\", released in 1999.  Dee Dee Ramone and Joey Ramone have provided guest vocals on some of the band's work.  Furious George is listed in the Encyclopedia of Punk by Brian Cogan with a foreword by Penelope Spheeris.  The band name is a parody to the book character, Curious George.\n\nCrooklyn (soundtrack): Crooklyn is the title of the soundtrack to the 1994 Spike Lee film of the same name.  The soundtrack was released in two parts.  Volume One was released May 10, 1994 just prior to the film's release and Volume Two was released in 1995, both on MCA Records.  The soundtrack albums feature music that was popular during the 1970s, two exceptions being \"Crooklyn\" by The Crooklyn Dodgers and \"People Make the World Go Round\" by Marc Dorsey, both of which were recorded specifically for the film.  The two albums comprise 28 songs from the film, though some tracks, such as \"Hey Joe\" by The Jimi Hendrix Experience are omitted from both releases.\n\nSamuel L. Jackson filmography: Samuel L. Jackson is an American actor and film producer.  In 2009, the collective total of all box office receipts for films that Jackson has starred in (including minor roles and cameos) is the highest of any on-screen actor.  As of December 2015, Jackson appeared in over one hundred films with a worldwide box office gross of approximately $16 billion to date.  Jackson's film career started in 1972 with a role in the film \"Together for Days\".  Over the next nineteen years Jackson was cast in multiple films as minor characters up until his breakthrough role as Gator, a crack addict, in the 1991 Spike Lee film \"Jungle Fever\", for which he won a special jury prize for best supporting actor at the Cannes International Film Festival.\n\nSpike Lee: Shelton Jackson \"Spike\" Lee (born March 20, 1957) is an American film director, producer, writer, and actor.  His production company, 40 Acres and a Mule Filmworks, has produced over 35 films since 1983.\n\nAlbert Hall (actor): Albert W. Hall (born November 10, 1937) is an American actor.  He is best known for portraying Chief Phillips in the 1979 war film \"Apocalypse Now\" and Judge Seymore Walsh in \"Ally McBeal\" and \"The Practice\".  He is also widely recognized for his role as Brother Baines in the 1992 Spike Lee film \"Malcolm X\", where he acted opposite film star Denzel Washington, who appeared in the title role of slain African-American Muslim, former Nation of Islam minister, and human rights activist Malcolm X.\n\nAndre Bellos: Andre Bellos (born August 13, 1987) is an American actor, singer and dancer who has appeared in the Spike Lee film \"Chi-Raq\" and Lee Daniels' television series \"Empire\".\n\nQuestion: Are Michael Anderson and Spike Lee film directors?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"is_answer_true\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals are film directors, false otherwise.\"\n    },\n    \"directors_identified\": {\n      \"type\": \"array\",\n      \"description\": \"List of individuals mentioned and their director status.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_director\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is identified as a film director.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the director, if specified.\"\n          },\n          \"birth_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The birth year of the director, if specified.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_director\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"total_directors_found\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of individuals identified as film directors from the question.\"\n    }\n  },\n  \"required\": [\n    \"is_answer_true\",\n    \"directors_identified\",\n    \"total_directors_found\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "is_answer_true": {
        "type": "boolean",
        "description": "True if both individuals are film directors, false otherwise."
      },
      "directors_identified": {
        "type": "array",
        "description": "List of individuals mentioned and their director status.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_director": {
              "type": "boolean",
              "description": "True if the individual is identified as a film director."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the director, if specified."
            },
            "birth_year": {
              "type": "integer",
              "description": "The birth year of the director, if specified."
            }
          },
          "required": [
            "name",
            "is_director"
          ],
          "additionalProperties": false
        }
      },
      "total_directors_found": {
        "type": "integer",
        "description": "The total number of individuals identified as film directors from the question."
      }
    },
    "required": [
      "is_answer_true",
      "directors_identified",
      "total_directors_found"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

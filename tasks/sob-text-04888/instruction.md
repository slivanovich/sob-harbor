{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHalloween 4: The Return of Michael Myers: Halloween 4: The Return of Michael Myers is a 1988 American slasher film and the fourth installment in the \"Halloween\" film series.  Directed by Dwight H. Little and written by Alan B. McElroy, it focuses on Michael Myers returning home to kill his niece Jamie Lloyd (Danielle Harris), the daughter of Laurie Strode, with Dr. Sam Loomis (Donald Pleasence) once more pursuing him.\n\nHalloween 5: The Revenge of Michael Myers: Halloween 5: The Revenge of Michael Myers is a 1989 American slasher film and the fifth installment in the \"Halloween\" film series.  It was directed and co-written by Dominique Othenin-Girard and starred Donald Pleasence, who again portrayed Dr. Sam Loomis, and Danielle Harris, who reprised her role as Jamie Lloyd.  The film takes place exactly one year after the events depicted in \"\".  Michael Myers has returned to the sleepy town of Haddonfield, Illinois to murder his niece, Jamie, who is now mute.  Dr. Loomis tries to save the day with the help of Sheriff Meeker.\n\nHalloween II (1981 film): Halloween II is a 1981 American slasher film and the second installment in the \"Halloween\" film series.  Directed by Rick Rosenthal, written and produced by John Carpenter and Debra Hill, it is a direct sequel to Carpenter's \"Halloween\", immediately picking up where it had left off.  Set on the same night of October 31, 1978, Michael Myers follows survivor Laurie Strode (Jamie Lee Curtis) to a nearby hospital while Dr. Sam Loomis (Donald Pleasence) is still in pursuit of his patient.\n\nFatal Games: Fatal Games (originally known as The Killing Touch and also released as Olympic Nightmare) is a 1984 American slasher film written and directed by Michael Elliott and starring Sally Kirkland, Lynn Banashek, Sean Masterson, Michael O'Leary, Teal Roberts, and Spice Williams-Crosby.  The plot consists of a mad slasher wielding a javelin killing off various members of a high school gymnastics team.  The film shares many of its plot points with an earlier slasher film, \"Graduation Day\".\n\nHalloween (1978 film): Halloween is a 1978 American slasher film directed and scored by John Carpenter, co-written with producer Debra Hill, and starring Donald Pleasence and Jamie Lee Curtis in her film debut.  The film is the first installment of the \"Halloween\" franchise.  In the film, on Halloween night in 1963, Michael Myers murders his sister in the fictional Midwestern town of Haddonfield, Illinois.  He escapes on October 30, 1978 from Smith's Grove Sanitarium, and returns home to kill again.  Michael's psychiatrist, Dr. Sam Loomis, knowing Michael's intentions, gives chase.  The next day, Halloween, Michael stalks teenager Laurie Strode.\n\nMichael Myers (Halloween): Michael Myers is a fictional character from the \"Halloween\" series of slasher films.  He first appears in John Carpenter's \"Halloween\" (1978) as a young boy who murders his older sister, then fifteen years later returns home to murder more teenagers.  In the original \"Halloween\", the adult Michael Myers, referred to as The Shape in the closing credits, was portrayed by Nick Castle for most of the film, with Tony Moran and Tommy Lee Wallace substituting in during the final scenes.  The character was created by Debra Hill and John Carpenter and has appeared in nine films, as well as novels, multiple video games, and several comic books.\n\nHalloween (2007 film): Halloween is a 2007 American slasher film written, directed, and produced by Rob Zombie.  The film is a remake/reimagining of the 1978 horror film of the same name; the first in the rebooted \"Halloween\" film series and the ninth installment of the \"Halloween\" franchise.  The film stars Tyler Mane as the adult Michael Myers, Malcolm McDowell as Dr. Sam Loomis, and Scout Taylor-Compton as Laurie Strode; Daeg Faerch portrays a ten-year-old Michael Myers.  Rob Zombie's \"reimagining\" follows the premise of John Carpenter's original, with Michael Myers stalking Laurie Strode and her friends on Halloween night.  Zombie's film goes deeper into the character's psyche, trying to answer the question of what drove him to kill people, whereas in Carpenter's original film Michael did not have an explicit reason for killing.\n\nHalloween (soundtrack): Halloween is a soundtrack album composed and performed by John Carpenter, featuring the score to the 1978 film \"Halloween\".  It was released in Japan in 1979 through Columbia Records and in the USA in 1983 through Varèse Sarabande.  An expanded 20th Anniversary Edition was released in 1998 through Varèse Sarabande.\n\nHalloween: The Curse of Michael Myers: Halloween: The Curse of Michael Myers is a 1995 American slasher film and the sixth installment in the \"Halloween\" film series.  Directed by Joe Chappelle from a screenplay by Daniel Farrands, the plot involves the \"Curse of Thorn\", a mystical symbol first shown in \"\" and revealed in the film to be the source of Michael Myers' immortality.  The cast includes Paul Rudd as Tommy Doyle, a returning character from the original \"Halloween\" film, and Donald Pleasence reprising his role as protagonist Dr. Sam Loomis in his final film appearance.  Jamie Lloyd's appearance in the beginning of the film ties up loose ends from \"The Revenge of Michael Myers\".\n\nHalloween II (2009 film): Halloween II is a 2009 American slasher film written, directed, and produced by Rob Zombie.  The film is a sequel to Zombie's 2007 remake of 1978's \"Halloween\", and the tenth installment of the franchise.  Picking up where the 2007 film ended and then jumping ahead one year, \"Halloween II\" follows Laurie Strode as she deals with the aftermath of the previous film's events, Dr. Loomis who is trying to capitalize on those events by publishing a new book that chronicles everything that happened, and Michael Myers as he continues his search for Laurie so that he can reunite with his sister.  The film sees the return of lead cast members from the 2007 film Malcolm McDowell, Scout Taylor-Compton, and Tyler Mane, who portray Dr. Loomis, Laurie Strode, and Michael Myers, respectively.\n\nQuestion: Who composed the soundtrack to the 1978 American slasher film that featured character Michael Myers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"main_character\": {\n          \"type\": \"string\",\n          \"description\": \"The primary character featured in the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"main_character\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"soundtrack_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"composer\": {\n          \"type\": \"string\",\n          \"description\": \"The composer of the film's soundtrack.\"\n        }\n      },\n      \"required\": [\n        \"composer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The direct answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"soundtrack_information\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "main_character": {
            "type": "string",
            "description": "The primary character featured in the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "main_character"
        ],
        "additionalProperties": false
      },
      "soundtrack_information": {
        "type": "object",
        "properties": {
          "composer": {
            "type": "string",
            "description": "The composer of the film's soundtrack."
          }
        },
        "required": [
          "composer"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The direct answer to the question."
      }
    },
    "required": [
      "film_details",
      "soundtrack_information",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

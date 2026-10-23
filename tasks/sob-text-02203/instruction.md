{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAnaconda (film): Anaconda is a 1997 adventure horror film by Peruvian director Luis Llosa, starring Jennifer Lopez, Ice Cube, Jon Voight, Eric Stoltz, Jonathan Hyde and Owen Wilson.  It centers on a documentary film crew who have been taken hostage by a snake hunter who is going after the legendary giant anaconda, which is discovered in the Amazon rainforest.\n\nCotton Candy (film): Cotton Candy is a 1978 American made-for-television drama film directed by Ron Howard and broadcast on NBC.  It is also known as Ron Howard's Cotton Candy.\n\nLuis Llosa: Luis Llosa (born 1951) is a Peruvian film director.  He is best known for \"Sniper\", \"The Specialist\", and \"Anaconda\".\n\nRichie Cunningham: Richard J. \"Richie\" Cunningham is a fictional character played by Ron Howard on the sitcom \"Happy Days\".  He is the second son of Howard and Marion Cunningham, brother of Joanie Cunningham and Chuck Cunningham, and a friend of Fonzie, Ralph Malph, and Potsie Weber.  Cunningham was the original lead character, but was supplanted by Fonzie when that character's popularity came to dwarf that of Cunningham and the other characters (however, Ron Howard and Henry Winkler (Fonzie) continued to share top billing in the opening credits of the show).\n\nRance Howard: Rance Howard (born November 17, 1928) is an American actor who has starred in film and on television.  He is the father of actor and filmmaker Ron Howard and actor Clint Howard, and grandfather of the actress Bryce Dallas Howard.\n\nCrime Zone: Crime Zone (also known as Calles Peligrossas in Peru) is a 1989 American–Peruvian dystopian science fiction film directed by Luis Llosa, written by Daryl Haney, and starring David Carradine, Peter Nelson, Sherilyn Fenn, and Michael Shaner.  Carradine plays a mysterious stranger who recruits young lovers in an illicit romance (Nelson and Fenn) to commit a crime spree in a futuristic police state, promising them an avenue for escape.  The film was executive produced by Roger Corman, who came up with the original concept.  Due to a perceived lack of Peruvian qualities, it was better received by American than Peruvian critics.  Corman's New Concorde co-produced and distributed it.  After its Los Angeles premiere, it was released on VHS by MGM/UA.\n\nThe Specialist: The Specialist is a 1994 American action thriller spy film directed by Luis Llosa, starring Sylvester Stallone, Sharon Stone, James Woods, Eric Roberts and Rod Steiger.  It is loosely based on \"The Specialist\" series of novels by John Shirley.\n\nHour of the Assassin (1987 film): Hour of the Assassin (also known as Spanish: A merénylet órája , Spanish: Misión en los Andes ) is a 1987 action–drama film starring Erik Estrada, Robert Vaughn, Alfredo Álvarez Calderón, Orlando Sacha, , and Lourdes Berninzon.  The film was directed by Luis Llosa Urquidi and written by Matt Leipzig.  \"Hour of the Assassin\" was executive produced by Roger Corman.\n\nRon Howard: Ronald William Howard (born March 1, 1954) is an American actor and filmmaker.  Howard is best known for playing two high-profile roles in television sitcoms in his youth and directing a number of successful feature films later in his career.\n\nFire on the Amazon: Fire on the Amazon is a 1993 American-Peruvian drama-adventure film directed by Luis Llosa and starring Craig Sheffer and Sandra Bullock.\n\nQuestion: Who is also an actor, Luis Llosa or Ron Howard?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is identified as an actor.\"\n    },\n    \"is_actor\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the person is an actor, false otherwise.\"\n    },\n    \"roles_as_actor\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Specific roles or types of roles the person played as an actor.\"\n    },\n    \"other_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other professions or roles the person is known for, besides acting.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"is_actor\",\n    \"roles_as_actor\",\n    \"other_professions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who is identified as an actor."
      },
      "is_actor": {
        "type": "boolean",
        "description": "True if the person is an actor, false otherwise."
      },
      "roles_as_actor": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Specific roles or types of roles the person played as an actor."
      },
      "other_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other professions or roles the person is known for, besides acting."
      }
    },
    "required": [
      "person_name",
      "is_actor",
      "roles_as_actor",
      "other_professions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNo Minor Vices: No Minor Vices is a 1948 American black-and-white comedy film written by Arnold Manoff and directed by Lewis Milestone with Robert Aldrich as 1st assistant director.  Created for David Loew's Enterprise Productions, it was the first of three films distributed by Metro-Goldwyn-Mayer after parting ways with United Artists, and was the last of four films made by Dana Andrews for director Milestone.\n\nLewis Milestone: Lewis Milestone (born Leib Milstein; September 30, 1895 – September 25, 1980) was a Moldovan-born American motion picture director.  He is known for directing \"Two Arabian Knights\" (1927) and \"All Quiet on the Western Front\" (1930), both of which received Academy Awards for Best Director.  He also directed \"The Front Page\" (1931 – nomination), \"The General Died at Dawn\" (1936), \"Of Mice and Men\" (1939), \"Ocean's 11\" (1960), and received the directing credit for \"Mutiny on the Bounty\" (1962), though Marlon Brando largely appropriated his responsibilities during its production.\n\nThe Widow (1955 film): The Widow (U.S. title) is a 1955 Italian black-and-white romantic drama film directed by Lewis Milestone and written by Milestone and Louis Stevens, based upon the novel \"La Vedova\" by Susan York.  Produced and originally released under the title La Vedova X, the film had theatrical release in Italy in 1955, limited release in the United States in 1957, and was released in France on June 4, 1959 under the title \"La Veuve\".  This was the last Milestone film involving his own writing.\n\nAaron Katz (filmmaker): Aaron Katz (born October 29, 1981) is an award-winning independent American filmmaker from Portland, Oregon.\n\nKangaroo (1952 film): Kangaroo is a 1952 American Technicolor film directed by Lewis Milestone.  It is also known as The Australian Story (American subtitle).  The first Technicolor movie filmed on-location in Australia.  Strong winds on location forced Milestone to re-dub much of the exterior dialogue.\n\nFine Manners: Fine Manners is a 1926 American black-and-white silent comedy film directed initially by Lewis Milestone and completed by Richard Rosson for Famous Players-Lasky/Paramount Pictures.  After an argument with actress Gloria Swanson, director Milestone walked off the project, causing the film to be completed by Rosson, who had picked up directorial tricks while working as an assistant director to Allan Dwan.  The success of the film, being Rosson's first directorial effort since he co-directed \"Her Father's Keeper\" in 1917 with his brother Arthur Rosson, won him a long-term contract with Famous Players-Lasky.\n\nThe Front Page (1931 film): The Front Page is a 1931 American pre-Code comedy film, directed by Lewis Milestone and starring Adolphe Menjou and Pat O'Brien.  Based on a Broadway play of the same name, the film was produced by Howard Hughes, written by Bartlett Cormack and Charles Lederer, and distributed by United Artists.  The supporting cast includes Mary Brian, George E. Stone, Matt Moore, Edward Everett Horton and Walter Catlett.  At the 4th Academy Awards, the film was nominated for Best Picture, Milestone for Best Director, and Menjou for Best Actor.\n\nSeven Sinners (1925 film): Seven Sinners is a 1925 black-and-white silent crime comedy film directed by Lewis Milestone and written by Milestone and Darryl F. Zanuck.  The film was produced by Warner Bros.  Pictures.\n\nThe North Star (1943 film): The North Star (also known as Armored Attack in the US) is a 1943 war film produced by Samuel Goldwyn Productions and distributed by RKO Radio Pictures.  It was directed by Lewis Milestone, written by Lillian Hellman and featured production design by William Cameron Menzies.  The film starred Anne Baxter, Dana Andrews, Walter Huston, Walter Brennan and Erich von Stroheim.  The music was written by Aaron Copland, the lyrics by Ira Gershwin, and the cinematography was by James Wong Howe.  The film also marked the debut of Farley Granger.\n\nCold Weather: Cold Weather is an American mystery film written by Aaron Katz, Ben Stambler, and Brendan McFadden and directed by Katz with Stambler and McFadden producing.  The film stars Cris Lankenau as a former forensic science student investigating the mysterious disappearance of his ex-girlfriend.  The film was shot and set in Portland, Oregon, which was also the setting of Katz's debut feature, \"Dance Party USA\".\n\nQuestion: Lewis Milestone and Aaron Katz, are both of which nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"directors\": {\n      \"type\": \"array\",\n      \"description\": \"List of directors mentioned in the question with their nationalities.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the director.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the director.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The common nationality shared by all listed directors.\"\n    },\n    \"number_of_directors_found\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of directors whose nationality was identified.\"\n    }\n  },\n  \"required\": [\n    \"directors\",\n    \"common_nationality\",\n    \"number_of_directors_found\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "directors": {
        "type": "array",
        "description": "List of directors mentioned in the question with their nationalities.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the director."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the director."
            }
          },
          "required": [
            "name",
            "nationality"
          ],
          "additionalProperties": false
        }
      },
      "common_nationality": {
        "type": "string",
        "description": "The common nationality shared by all listed directors."
      },
      "number_of_directors_found": {
        "type": "integer",
        "description": "The total number of directors whose nationality was identified."
      }
    },
    "required": [
      "directors",
      "common_nationality",
      "number_of_directors_found"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

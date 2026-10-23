{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Dos Passos: John Roderigo Dos Passos ( ; January 14, 1896 – September 28, 1970) was an American novelist and artist active in the first half of the twentieth century.  Born in Chicago, Illinois, he graduated from Harvard College in 1916.  He was well-traveled, visiting Europe and the Middle East, where he learned about literature, art, and architecture.  During World War I, he was an ambulance driver for American volunteer groups in Paris and Italy before joining the United States Army Medical Corps.\n\nSpence's Point: Spence's Point is a historic estate on the Potomac River near Westmoreland, Virginia.  Also known as theJohn R. Dos Passos Farm, it was the home of writer John Dos Passos (1896–1970) for the last 25 years of his life.  It was declared a National Historic Landmark in 1971.\n\nJoe R. Lansdale: Joe Richard Lansdale (born October 28, 1951) is an American writer, author, martial arts expert, and martial arts instructor.\n\nAtomic Chili: \"Atomic Chili: The Illustrated Joe R. Lansdale\" by Lansdale et al., (Klaw, ed.)  (Mojo Press, 1998) is a collection of previously written stories by Joe R. Lansdale, adapted into comic book form by assorted artists and writers.  The book was designed by John Picacio, and featured a cover by Dave Dorman.\n\nThe International (play): The International is a play by the American playwright John Howard Lawson.  It was first produced by the New Playwrights' Theatre in New York, opening on January 12 1928.  Lawson directed this production, while John Dos Passos designed the sets, Edward A. Ziman composed its music, Don Oscar Becque choreographed the dances, and Helen Johnson designed the costumes.\n\nAmerican Writers Association: The American Writers Association (AWA) was an organization formed in 1946 in opposition to an attempt to introduce a form of trade unionism for authors.  Its members included writers such as Bruce Barton, John Dos Passos, John Erskine, James T. Farrell, John T. Flynn, Rupert Hughes, Zora Neale Hurston, Clarence Budington Kelland, Clare Boothe Luce, Eugene Lyons, Margaret Mitchell, Ayn Rand, Dorothy Thompson and Louis Waldman.\n\nMaurice Coindreau: Maurice-Edgar Coindreau (December 24, 1892 – October 20, 1990) was a literary critic and translator of fiction from English into French and Spanish.  He is notable for having introduced many canonical American authors of the 20th century—such as William Faulkner, John Dos Passos, John Steinbeck, and Ernest Hemingway—to the French-speaking public.\n\nAdventures of a Young Man: Adventures of a Young Man is a 1939 novel by John Dos Passos, which eventually became the first in this writer's District of Columbia Trilogy.\n\nBy Bizarre Hands: By Bizarre Hands is the first collection of short stories by American writer Joe R. Lansdale, published in 1989.  The collection was nominated for a Bram Stoker Award for best fiction collection, and contains two stories which won Stokers.  It has an introduction by Lewis Shiner.  This book was re-issued as By Bizarre Hands Rides Again in 2010.  The re-issue contains a new introduction by Joe R. Lansdale and new artwork by Alex McVey.  This book is limited to 300 copies and is signed by both writer and artist.  It also contains two stories not in the original issue.\n\nThree Soldiers: Three Soldiers is a 1921 novel by the American writer and critic John Dos Passos.  It is one of the American war novels of the First World War, and remains a classic of the realist war novel genre.  H.L. Mencken, then practising primarily as an American literary critic, praised the book in the pages of \"The Smart Set\".  \"Until \"Three Soldiers\" is forgotten and fancy achieves its inevitable victory over fact, no war story can be written in the United States without challenging comparison with it—and no story that is less meticulously true will stand up to it.  At one blast it disposed of oceans of romance and blather.  It changed the whole tone of American opinion about the war; it even changed the recollections of actual veterans of the war.  They saw, no doubt, substantially what Dos Passos saw, but it took his bold realism to disentangle their recollections from the prevailing buncombe and sentimentality.\"\n\nQuestion: What profession does John Dos Passos and Joe R. Lansdale have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession that both individuals have in common.\"\n    },\n    \"person_details\": {\n      \"type\": \"array\",\n      \"description\": \"Details for each person, including their name and all professions listed in the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"professions_listed\": {\n            \"type\": \"array\",\n            \"description\": \"A list of all professions attributed to this individual in the context.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"professions_listed\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"number_of_people_sharing_profession\": {\n      \"type\": \"integer\",\n      \"description\": \"The count of individuals who share this common profession.\"\n    }\n  },\n  \"required\": [\n    \"shared_profession\",\n    \"person_details\",\n    \"number_of_people_sharing_profession\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_profession": {
        "type": "string",
        "description": "The profession that both individuals have in common."
      },
      "person_details": {
        "type": "array",
        "description": "Details for each person, including their name and all professions listed in the context.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "professions_listed": {
              "type": "array",
              "description": "A list of all professions attributed to this individual in the context.",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "name",
            "professions_listed"
          ],
          "additionalProperties": false
        }
      },
      "number_of_people_sharing_profession": {
        "type": "integer",
        "description": "The count of individuals who share this common profession."
      }
    },
    "required": [
      "shared_profession",
      "person_details",
      "number_of_people_sharing_profession"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

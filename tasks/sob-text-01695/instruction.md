Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Tennessee State Prison: Tennessee State Prison is a former correctional facility located near downtown Nashville, Tennessee.  Opened in 1898, the prison has been closed since 1992.  It has been the location for the films "Nashville", "Marie", "Ernest Goes to Jail", "Against the Wall", "The Green Mile", "The Last Castle", two of Eric Church's music videos "Lightning" and "Homeboy", and Pillar's "Bring Me Down" music video.  Most recently VH1's "Celebrity Paranormal Project" filmed there for the third episode of the series (titled "The Warden") as well as the last episode of the first season (titled "Dead Man Walking").  The prison was referred to as "The Walls Maximum Security Prison" in both episodes to protect the location's privacy.

John Mahoney: John Mahoney (born 20 June 1940) is a British-American actor.  Born in Blackpool, Lancashire, England, Mahoney started his career on the stage in 1977 as the body double for Steve McQueen and moved into film in 1980.  He played Martin Crane in the American sitcom "Frasier" on NBC from 1993 to 2004.  He has also worked as a voice actor, and performed on Broadway and in Chicago theatre.

Castle Drogo: Castle Drogo is a country house and castle near Drewsteignton, Devon, England: grid reference SX 722901.  It was built from 1911 to 1930 for Julius Drewe (businessman and founder of the Home and Colonial Stores) to designs by architect Edwin Lutyens, and is a Grade I listed building.  It is currently undergoing a conservation project (2013–2018) to finally make it watertight.  It was the last castle built in England.  The gardens are Grade II* listed in the National Register of Historic Parks and Gardens.

John Houseman: John Houseman (born Jacques Haussmann; September 22, 1902October 31, 1988) was a British-American actor and producer who became known for his highly publicized collaboration with director Orson Welles from their days in the Federal Theatre Project through to the production of "Citizen Kane" and his storied collaboration with writer Raymond Chandler's intoxicated screenplay rendering as producer of "The Blue Dahlia."  He is perhaps best known for his role as Professor Charles W. Kingsfield in the film "The Paper Chase" (1973), for which he won the Academy Award for Best Supporting Actor.  He reprised his role as Kingsfield in the subsequent television series adaptation of "The Paper Chase".  Houseman was also known for his commercials for the brokerage firm Smith Barney.  He had a distinctive Mid-Atlantic English accent, in common with many actors of his generation.

Delroy Lindo: Delroy George Lindo (born November 18, 1952) is a British-American actor and theatre director.  Lindo has been nominated for Tony and Screen Actors Guild awards and has won a Satellite Award.  He is perhaps best known for his roles in a trio of Spike Lee films, especially as West Indian Archie in Lee's "Malcolm X" (1992) and Woody Carmichael in "Crooklyn" (1994), Catlett in "Get Shorty", Arthur Rose in "The Cider House Rules", and Detective Castlebeck in "Gone in 60 Seconds" (2000).  Lindo starred as Alderman Ronin Gibbons in the TV series "The Chicago Code" (2011) and as Winter on the series "Believe," which premiered in 2014.

Dyserth Castle: Dyserth Castle (Welsh: "Castell Diserth" ) is a castle site in Denbighshire in the country of Wales.  It is a scheduled monument protected ancient borough on a ridge north of the village of Dyserth.  It was the last castle of the British fortified defences on the Clwydian hill range in the Middle Ages.  The nearby village of Dyserth got its name from the castle.

Ako Mitchell: Ako Mitchell is a British-American actor and filmmaker.  Ako directed and co-wrote the short film "I'm in the corner with the bluebells" part of the international shorts competition at the 2014 Toronto International Film Festival.  Ako recently played “Klook” in “Klook’s Last Stand” at London’s Park Theatre where he received an Off West End Awards Best Actor nomination.  He also recently played esteemed British actor Lenny Henry's brother in Fences in the West End.  Ako has also worked at London’s Donmar Warehouse and played opposite Patina Miller in Sister Act at The London Palladium.  Ako’s credits also include: Pilot in Nick Lloyd Webber’s The Little Prince (Savoy Theatre); Mitch in Spelling Bee (Donmar Warehouse); Mufasa in The Lion King (Lyceum Theatre-West End); Coalhouse Walker Jr. in Ragtime (Charing Cross Theatre) and Dennis in Lake Placid: The Final Chapter (Film).  Ako also Co-produced the documentary film 500 Years Later, a winner at the Pan-African Film Festival, Black Berlin International Cinema and Harlem International Film Festival.

The Last Castle: The Last Castle is a 2001 American action drama film directed by Rod Lurie, starring Robert Redford, James Gandolfini, Mark Ruffalo and Delroy Lindo.

Wentworth Miller: Wentworth Earl Miller III (born June 2, 1972) is a British-American actor, model, and screenwriter.  He rose to prominence following his role as Michael Scofield in the five seasons of the Fox series "Prison Break", for which he received a Golden Globe Award nomination for Best Actor in a Leading Role.  He made his screenwriting debut with the 2013 thriller film "Stoker".  In 2014, he began playing Leonard Snart/Captain Cold in a recurring role on The CW series "The Flash" before becoming a series regular on the spin-off "Legends of Tomorrow".  Miller reprised his role as Michael Scofield for the fifth season of the limited-run "Prison Break" revival, which aired on April 4, 2017 and concluded on May 30, 2017.

Bryan Fisher: Bryan Fisher (born August 1, 1980) is a British-American actor who is best known for his role as Jason McNamara, Carmen's boyfriend in "George Lopez".  He has also guest starred in many other shows such as The Invisible Man, The Chronicle, and also starred in the 2006 TV movie "Jekyll + Hyde".

Question: What British-American actor born in 1952 starred in The Last Castle?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the actor."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the actor."
        },
        "nationalities": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of nationalities held by the actor."
        }
      },
      "required": [
        "name",
        "birth_year",
        "nationalities"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "starred_in_film": {
      "type": "boolean",
      "description": "Indicates whether the actor starred in the specified film."
    }
  },
  "required": [
    "actor_details",
    "film_details",
    "starred_in_film"
  ],
  "additionalProperties": false
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2012 Summer Paralympics opening ceremony: The 2012 Summer Paralympics opening ceremony was held on 29 August 2012, starting at 20:30 BST and marking the official opening of the 2012 Summer Paralympics in London, England.  The show – named Enlightenment – had Jenny Sealey and Bradley Hemmings as its artistic directors, leading a team that included Jon Bausor as set designer and Moritz Junge as costume designer.  Queen Elizabeth II officially opened the Games.  The ceremony was performed in the Olympic stadium in London in front of a capacity audience of 80,000 people.\n\nMiller's Crossing: Miller's Crossing is a 1990 American neo-noir gangster film, with elements of black comedy, written, directed and produced by the Coen brothers, and starring Gabriel Byrne, Marcia Gay Harden, John Turturro, Jon Polito, J. E. Freeman, and Albert Finney.  The plot concerns a power struggle between two rival gangs and how the protagonist, Tom Reagan (Byrne), plays both sides off against each other.\n\nHomeward Bound II: Lost in San Francisco: Homeward Bound II: Lost in San Francisco is a 1996 American adventure comedy film and a sequel to the 1993 film \"\".  Directed by David R. Ellis, the film features the three animals from the first film, Shadow the Golden Retriever (voiced by Ralph Waite, replacing Don Ameche, who died in 1993), Sassy the Himalayan cat (Sally Field), and Chance the American Bulldog (Michael J. Fox).  It also features the voice work of Sinbad, Carla Gugino, Tisha Campbell-Martin, Stephen Tobolowsky, Jon Polito, Adam Goldberg, Al Michaels, Tommy Lasorda, and Bob Uecker.\n\nWendy and Lucy: Wendy and Lucy is a 2008 American drama film directed by Kelly Reichardt.  Reichardt and Jon Raymond adapted the screenplay from his short story \"Train Choir\".  The film stars Michelle Williams and Will Patton.  It had its world premiere at the 2008 Cannes Film Festival and was screened at several additional film festivals before receiving a limited theatrical release in the United States on December 10, 2008.  In 2017, the film was named the twentieth-first \"Best Film of the 21st Century So Far\" by The New York Times.\n\nFlodders in America: Flodders in America (Dutch: Flodder in Amerika! ) , released in Quebec as \"Les Lavigueur Redéménagent\", is a 1992 Dutch comedy film directed by Dick Maas.  The film is the sequel of the successful film \"Flodder\" from 1986.  It was filmed on location in New York and stars Dutch actors Huub Stapel, Nelly Frijda, Tatjana Simic, Rene van 't Hof, Lou Landre, Gerard Joling, Dick Rienstra, and American actor Jon Polito as nightclub owner Larry Rosenbaum.\n\nJon Polito: Jon Raymond Polito (December 29, 1950 – September 1, 2016) was an American character actor and voice artist.  In a film and television career spanning 35 years, he amassed over 220 credits.  Notable television roles included Detective Steve Crosetti in the first two seasons of \"\" and on the first season of \"Crime Story\".  He also appeared in several films including \"The Rocketeer\", \"The Crow\" and \"Gangster Squad\", but was mostly known for his work with the Coen brothers.  He appeared in five of their films, including \"Miller's Crossing\", \"Barton Fink\" and \"The Big Lebowski\".\n\nThe Man Who Wasn't There (2001 film): The Man Who Wasn't There is a 2001 American neo-noir crime film written, produced and directed by Joel and Ethan Coen.  Billy Bob Thornton stars in the title role.  Also featured are Tony Shalhoub, Scarlett Johansson, James Gandolfini, and Coen regulars Frances McDormand, Michael Badalucco, Richard Jenkins and Jon Polito.  Joel Coen won the Best Director Award at the 2001 Cannes Film Festival.  Ethan Coen, Joel Coen's brother and co-director of the film, did not receive the Best Director Award as he was not credited as a director.\n\nLatin Classics Mijares: Latin Classics - Mijares is the sixth compilation album by Mexican pop singer Mijares.  It is part of an EMI International series, all with similar artwork featuring compilations of artists included Jon Secada, Los Mismos, Alvaro Torres, Los Alegres de Terán, Mazz, Emilio Navaira, Grupo Modelo, Baron de Apodaca, Jose Luis Perales, Ednita Nazario, Daniela Romo, Barrio Boyzz, Paulina Rubio, Paloma San Basilio, La Tropa F, Pandora (musical group), Los Donneños, Myriam Hernandez, Jose Feliciano, La Mafia, Luis Miguel, Laura Canales and Ram Herrera.\n\nThe Big Lebowski: The Big Lebowski is a 1998 British-American crime comedy film written, produced, and directed by Joel and Ethan Coen.  It stars Jeff Bridges as Jeffrey \"The Dude\" Lebowski, a Los Angeles slacker and avid bowler.  He is assaulted as a result of mistaken identity, after which The Dude learns that a millionaire also named Jeffrey Lebowski was the intended victim.  The millionaire Lebowski's trophy wife is kidnapped, and he commissions The Dude to deliver the ransom to secure her release; but the plan goes awry when the Dude's friend Walter Sobchak (John Goodman) schemes to keep the ransom money.  Julianne Moore and Steve Buscemi also star, with David Huddleston, John Turturro, Philip Seymour Hoffman, Sam Elliott, Tara Reid, David Thewlis and Flea appearing in supporting roles.\n\nNorth Country Maid: North Country Maid is the fourth studio album by Marianne Faithfull.  It was released only in the United Kingdom.  The arrangements were by Jon Mark and Mick Taylor.  Gus Dudgeon was the engineer and Gered Mankowitz was the photographer.  The guitarists included Jon Mark and Big Jim Sullivan.\n\nQuestion: What are the names of the brothers that directed a film that included Jon Raymond Polito?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"directing_brothers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"films_featuring_jon_polito\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Films directed by the brothers that included Jon Polito.\"\n    },\n    \"number_of_films\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of films directed by the brothers that featured Jon Polito.\"\n    }\n  },\n  \"required\": [\n    \"directing_brothers\",\n    \"films_featuring_jon_polito\",\n    \"number_of_films\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "directing_brothers": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        }
      },
      "films_featuring_jon_polito": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Films directed by the brothers that included Jon Polito."
      },
      "number_of_films": {
        "type": "integer",
        "description": "The total count of films directed by the brothers that featured Jon Polito."
      }
    },
    "required": [
      "directing_brothers",
      "films_featuring_jon_polito",
      "number_of_films"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

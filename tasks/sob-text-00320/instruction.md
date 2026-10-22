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
William Riley Dunham: William Riley Dunham (1856–1921), “the man known by name by more men, women and children than any other one man in Tipton County,” according to a 1912 issue of the Kempton Courier, was a member of the Indiana General Assembly, representing Hamilton and Tipton counties from 1913-1915.  William Riley was born to Samuel Goodnight Dunham and Eliza Matilda Reese, President Barack Obama's great-great-great grandparents, making him President Barack Obama's great-great-great uncle.  William Riley died in 1921 of "traveling sickness."

Revolutionary Struggle (Ireland): Revolutionary Struggle was a small militant Irish Althusserian group active in Dublin from 1975 until 1985.  It produced a quarterly magazine entitled "The Ripening of Time" which provided a Marxist-Leninist analysis of the political situation in Ireland.  The group was led by Michael Youlton, a man known as "Mick the Greek", and was heavily influenced by Italian groups such as the Red Brigades and Prima Linea.

Avner the Eccentric: Avner Eisenberg "Avner the Eccentric" (born August 26, 1948) is an American vaudeville performer, clown, mime, juggler, and sleight of hand magician.  He played the title role (the Holy Man known as the "Jewel") in the 1985 film "The Jewel of the Nile".  John Simon described him in 1984 as "A clown for the thinking man and the most exacting child."

La Vampire Nue: La Vampire Nue (English title: "The Nude Vampire") is a 1970 film directed by Jean Rollin.  It concerns a suicide cult led by a mysterious man known as "The Master".  The film was influenced by the 1963 Georges Franju classic "Judex".

Ross Ulbricht: Ross William Ulbricht (born March 27, 1984) is a former darknet market operator, best known for being convicted of creating and running the Silk Road website until his arrest.  He was known under the pseudonym "Dread Pirate Roberts".

Onchan Village Hall: Onchan Village Hall is one of eleven buildings in the Isle of Man known to have been built by Baillie Scott.  The Scottish architect and designer then resident on the Isle of Man had won the commission for the building through a design competition held by Onchan Commissioners for the proposed new hall.  The building was constructed in 1897-8 and it is still in regular use today.

Chris Tarbell: Christopher "Chris" Tarbell is a former FBI special agent who infiltrated both Anonymous and the Silk Road.  He was involved in the tracking and arrest of both Sabu (of Anonymous) and Dread Pirate Roberts of Silk Road (Ross Ulbricht).  He turned Sabu into an informant against the hacker group Lulzsec.  He later led the team that led to the arrest of Ross Ulbricht in the Glen Park Public Library.

Manhunt: Unabomber: Manhunt: Unabomber is an American drama miniseries created by Andrew Sodroski.  The series stars Paul Bettany, Jane Lynch, Sam Worthington, Katja Herbers, Chris Noth, Michael Nouri and Brían F. O'Byrne.  The series depicts a fictionalized account of the true story of the FBI's hunt for the man known as the Unabomber.  The miniseries premiered on August 1, 2017, on Discovery Channel.

E. D. Morel: Edmund Dene Morel, originally Georges Eduard Pierre Achille Morel de Ville (10 July 1873 – 12 November 1924), was a British journalist, author, pacifist, and politician.  In collaboration with Roger Casement, Morel led a campaign against slavery in the Congo Free State, founding the Congo Reform Association and running the "West African Mail".  He played a significant role in the British pacifist movement during the First World War, participating in the foundation and becoming secretary of the Union of Democratic Control, at which point he broke with the Liberal Party.  After the war he joined the Independent Labour Party.  Bertrand Russell said of Morel, "No other man known to me has had the same heroic simplicity in pursuing and proclaiming political truth."

Ernie Nevers: Ernest Alonzo Nevers (June 11, 1903 – May 3, 1976), sometimes known by the nickname "Big Dog", was an American football and baseball player and football coach.  Widely regarded as one of the best football players in the first half of the 20th century, he played as a fullback and was a triple-threat man known for his talents in running, passing, and kicking.  He was inducted with the inaugural classes of inductees into both the College Football Hall of Fame in 1951 and the Pro Football Hall of Fame in 1963.  He was also named in 1969 to the NFL 1920s All-Decade Team.

Question: Chris Tarbell led the team that arrested a man known under as? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "agent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual who led the team."
        },
        "role": {
          "type": "string",
          "description": "The role or affiliation of the agent."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "arrested_person": {
      "type": "object",
      "properties": {
        "alias": {
          "type": "string",
          "description": "The pseudonym or alias the arrested person was known by."
        },
        "full_name": {
          "type": "string",
          "description": "The full name of the arrested person."
        },
        "organization": {
          "type": "string",
          "description": "The organization or website the arrested person was associated with."
        }
      },
      "required": [
        "alias",
        "full_name",
        "organization"
      ],
      "additionalProperties": false
    },
    "event_details": {
      "type": "object",
      "properties": {
        "action": {
          "type": "string",
          "description": "The action performed by the agent's team."
        },
        "location": {
          "type": "string",
          "description": "The location where the arrest took place."
        }
      },
      "required": [
        "action",
        "location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "agent",
    "arrested_person",
    "event_details"
  ],
  "additionalProperties": false
}

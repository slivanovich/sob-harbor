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
Jeff Celentano: Jeff Celentano (born May 24, 1960), also credited as Jeff Weston, is an American actor, screenwriter, and director.  As a character actor, Celentano has starred in such films as "", "Puppet Master II", and "Demonic Toys".  In 1994, he turned to directing with his first short film, "Dickwad".  He also directed "Under the Hula Moon", "Gunshy", and most recently "Moscow Heat".  Celentano is an acting teacher and is the Executive Director of Drama at The Performer's Academy in Laguna Woods, California.  Celentano was born and raised in Pemberton, New Jersey.  He has been married to the actress Musetta Vander since 1988.

Hugh Hudson: Hugh Hudson (born 25 August 1936) is an English film director.  He was among a generation of British directors who would begin their career making documentaries and television commercials before going on to have success in films.  Hudson directed the 1981 Academy Award and BAFTA Award Best Picture "Chariots of Fire", a film ranked 19th in the British Film Institute's list of Top 100 British films.

The Journey Home (film): The Journey Home (originally titled Midnight Sun) is a 2014 Canadian-Italian family adventure-drama film starring Dakota Goyo, Goran Višnjić, and Bridget Moynahan, written by Hugh Hudson, directed by Roger Spottiswoode and Brando Quilici.  Filmed on location in Ontario and Manitoba, Canada, it follows a young man (Goyo), who works to reunite a lost polar bear cub with its mother.  It premiered in November of 2014, and received generally mixed-to-positive reviews.

Breaking Point (2009 film): Breaking Point is a 2009 action-drama film starring Tom Berenger, Busta Rhymes, Musetta Vander and Sticky Fingaz.  It is directed by Jeff Celentano with a screenplay written by Vincent Campanella.  The film was showcased in Cannes and was released theatrically on December 4, 2009.

Altamira (film): Finding Altamira (released as Altamira in Spain) is a 2016 Spanish biographical drama film starring Antonio Banderas, and directed by Hugh Hudson.  It is Hudson's first fiction film since "I Dreamed of Africa" in 2000.

Under the Hula Moon: Under the Hula Moon is an action comedy film from 1995 directed by Jeff Celentano.  It features the talents of Stephen Baldwin, Emily Lloyd, Chris Penn, and Musetta Vander.

Moscow Heat: Moscow Heat (Russian: Московская жара ) is a 2004 Russian action film directed by Jeff Celentano.

Gunshy: Gunshy is an American 1998 crime drama film directed by Jeff Celentano and starring William Petersen, Michael Wincott, and Diane Lane.

Hudson Boatworks: Hudson Boat Works is a rowing racing shell manufacturer based in London, Ontario.  Jack Coughlan and his brother-in-law Hugh Hudson founded the company in 1981, and Jack remains Owner and President today.  In March 2007, Hudson began production of their "Shark" line of boats.  Designed by Britt Chance, US Naval Architect, Luis Tarrataca, Hudson Design Engineer, and Jack Coughlan, Head of Hudson R&D, the Great White 1x and the Hammerhead 8+ shells and claim to be; faster than ever, more stable, and more comfortable for the rowers.  Hudson is the official boat manufacturer for the Canadian and American National Teams.

Primary Suspect: Primary Suspect is a 2000 American action-thriller-mystery film written by D.Alvelo and Marc Bienstock and directed by Jeff Celentano.  The film stars William Baldwin, Brigitte Bako, and Lee Majors.

Question: Who were Jeff Celentano and Hugh Hudson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "summary_of_shared_profession": {
      "type": "string",
      "description": "A summary statement identifying the primary shared profession of the individuals."
    },
    "individuals_identified": {
      "type": "array",
      "description": "A list of individuals and their identified roles.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the individual."
          },
          "primary_role": {
            "type": "string",
            "description": "The most prominent role of the individual based on the context."
          },
          "all_roles_mentioned": {
            "type": "array",
            "description": "All professions and roles mentioned for the individual in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "primary_role",
          "all_roles_mentioned"
        ],
        "additionalProperties": false
      }
    },
    "count_of_individuals": {
      "type": "integer",
      "description": "The total number of individuals identified."
    }
  },
  "required": [
    "summary_of_shared_profession",
    "individuals_identified",
    "count_of_individuals"
  ],
  "additionalProperties": false
}

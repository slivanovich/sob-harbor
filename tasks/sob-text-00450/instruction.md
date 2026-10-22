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
American Foxhound: The American Foxhound is a breed of dog that is a cousin of the English Foxhound.  They are scent hounds, bred to hunt foxes by scent.

Stephens Cur: The Stephens Cur (a.k.a. Stephens' Stock Cur), is a scent hound that belongs to the Cur dog breed.  They were originally bred by the Stephens family in southeastern Kentucky.  The dogs known as "Little black dog" were bred by generations of that family for over a century.  In 1970, they were recognized as separate and distinct breed of Cur.  The dog is mostly black with white markings, but more than a third white is not permissible.  It is good for hunting raccoon and squirrel, but can also be used to bay wild boar.  They are registered with the United Kennel Club

Fox hunting: Fox hunting is an activity involving the tracking, chase and, if caught, the killing of a fox, traditionally a red fox, by trained foxhounds or other scent hounds, and a group of unarmed followers led by a "master of foxhounds" ("master of hounds"), who follow the hounds on foot or on horseback.

English Foxhound: The English Foxhound is one of the four foxhound breeds of dog.  It is a cousin of the American Foxhound.  They are scent hounds, bred to hunt foxes by scent.

Sighthound: Sighthounds, also called "gazehounds", primarily hunt by sight and speed, rather than by scent and endurance as scent hounds do.

Scent hound: Scent hounds (or scenthounds) are a type of hound that primarily hunts by scent rather than sight.  These breeds are hunting dogs and are generally regarded as having some of the most sensitive noses among canines.

Billy (dog): The Billy is a large scenthound originating from central western France.

Porcelaine: The Porcelaine ] is a breed of dog originating from France.  It is believed to be the oldest of the French scent hounds. Its alternate name is the Chien de Franche-Comté, named after a French region bordering Switzerland.  This caused some debate over the dog's origin, but it has been decided that it is a French dog.

Paper Chase (game): Paper Chase (also known as Hare and Hounds or Chalk Chase) is a racing game played outdoors (best played within a wood or even a shrubbery maze) with any number of players.  At the start of the game, one person is designated the 'hare' and everyone else in the group are the 'hounds'.  The 'hare' starts off ahead of everyone else leaving behind themselves a trail of paper shreds (or chalk marks in an urban environment) which represents the scent of the hare.  Just as scent is carried on the wind, so too are the bits of paper, sometimes making for a difficult game.  After some designated time, the hounds must chase after the hare and attempt to catch them before they reach the ending point of the race.  It is generally done over a long distance, but shorter courses can be set.  If the hare makes it to the finish line, they get to choose the next hare, or to be the hare themselves.  Similarly, the person who catches the hare gets to choose the next hare.

Mink hunting: Mink hunting is a country sport involving the hunting of American mink with scent hounds along the waterways which make up their habitat, in a manner similar to fox hunting.  Mink hunting took place in the countryside in the UK and Ireland, but since 2005 traditional mink hunting has been banned in England and Wales.

Question: Are the Stephens Cur and Billy scent hounds from the same region?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question": {
      "type": "string",
      "description": "The original question asked."
    },
    "are_both_scent_hounds": {
      "type": "boolean",
      "description": "Indicates if both dog breeds mentioned in the question are classified as scent hounds."
    },
    "are_from_same_region": {
      "type": "boolean",
      "description": "The direct answer to whether the two dog breeds originate from the same region."
    },
    "breed_details": {
      "type": "array",
      "description": "Details for each dog breed mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "type": {
            "type": "string",
            "description": "The classification of the dog breed (e.g., 'scent hound', 'sighthound')."
          },
          "origin_region": {
            "type": "string",
            "description": "The geographical region or country of origin for the breed."
          }
        },
        "required": [
          "name",
          "type",
          "origin_region"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question",
    "are_both_scent_hounds",
    "are_from_same_region",
    "breed_details"
  ],
  "additionalProperties": false
}

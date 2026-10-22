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
Eric Cartman: Eric Theodore Cartman, often referred to as just Cartman, is a main character in the animated television series "South Park", created by Matt Stone and Trey Parker, and voiced by Trey Parker.  Cartman, generally referred to by his surname, is one of four central characters in "South Park", along with his friends Stan Marsh, Kyle Broflovski, and Kenny McCormick.  Cartman first appeared, originally named Kenny, in prototypical form in a 1992 animated short "Jesus vs. Frosty", and a 1995 animated short "Jesus vs. Santa", and first appeared on television in the pilot episode of "South Park", "Cartman Gets an Anal Probe", on August 13, 1997.

Make Love, Not Warcraft: "Make Love, Not Warcraft" is the eighth episode in the tenth season of the American animated television series "South Park".  The 147th episode overall, it first aired on Comedy Central in the United States on October 4, 2006.  In the episode, Cartman, Kyle, Stan, and Kenny enjoy playing the popular massively multiplayer online role-playing game "World of Warcraft".  When a high level player goes around killing other players in the game, they start playing the game every day to try to stop him.  The episode was written and directed by series co-creator Trey Parker.  In 2015, he and co-creator Matt Stone listed it as their third favorite episode of the series.

Wing (South Park): "Wing" is the third episode in the ninth season of the American animated television series "South Park".  It was written by series co-creator Trey Parker and first aired on Comedy Central in the United States on March 23, 2005.  The episode was the 128th overall and was named after New Zealand singer Wing, who stars in the episode in an eponymous part loosely based on herself.  The message of the episode equates talent agents to Chinese slave traders.

Handicar: "Handicar" is the fourth episode in the eighteenth season of the American animated television series "South Park".  The 251st episode overall, it was written and directed by series co-creator Trey Parker.  The episode premiered on Comedy Central in the United States on October 15, 2014.  The episode lampoons several trends in the automotive industry including ride-share apps such as Uber and Lyft, Matthew McConaughey's celebrity endorsement of Lincoln, and Tesla, culminating in a "Wacky Races"-style marathon.  The episode does not feature any appearance by the four main characters of "South Park": Stan, Kyle, Cartman and Kenny.

Stan Marsh: Stanley Randall "Stan" Marsh is the protagonist of the animated television series "South Park".  He is voiced by and loosely based on series co-creator Trey Parker.  Stan is one of the show's four central characters, along with his friends Kyle Broflovski, Kenny McCormick and Eric Cartman.  He debuted on television when "South Park" first aired on August 13, 1997, after having first appeared in "The Spirit of Christmas" shorts created by Parker and long-time collaborator Matt Stone in 1992 ("Jesus vs. Frosty") and 1995 ("Jesus vs. Santa").

Royal Pudding: "Royal Pudding" is the third episode of the fifteenth season of the American animated television series "South Park", and the 212th episode of the series overall.  "Royal Pudding" premiered in the United States on Comedy Central on May 11, 2011.  In the episode, which parodies the 2011 Wedding of Prince William and Catherine Middleton, the Prince of Canada's fiancee is abducted from their wedding altar, leading Ike Broflovski to answer the call to rescue her.  "Royal Pudding" was written and directed by series co-creator Trey Parker, and was rated TV-MA L in the United States.  The episode aired 12 days after the wedding.

Tonsil Trouble: "Tonsil Trouble" is the first episode in the twelfth season of the American animated television series "South Park", and the 168th episode of the series overall.  Written and directed by series co-creator Trey Parker, it first aired on Comedy Central in the United States on March 12, 2008.  In the episode, Cartman contracts HIV during a blood-transfusion.  When Kyle laughs at Cartman's misfortune, Cartman intentionally infects Kyle with his disease as well.

South Park: Bigger, Longer &amp; Uncut: South Park: Bigger, Longer & Uncut is a 1999 American adult animated musical comedy film based on the Comedy Central animated television series "South Park".  The film was directed by series creator Trey Parker and stars the regular television cast of Parker, Matt Stone, Mary Kay Bergman, and Isaac Hayes, with guest performances by George Clooney, Eric Idle and Mike Judge.  The film follows the four boys Stan Marsh, Kyle Broflovski, Eric Cartman, and Kenny McCormick as they sneak into an R-rated film featuring Canadian actors Terrance and Phillip and begin cursing incessantly.  Eventually, their mothers pressure the United States to wage war against Canada for allegedly corrupting their children.

Kenny McCormick: Kenneth "Kenny" McCormick is a main character in the animated adult television series "South Park", along with his friends Stan Marsh, Kyle Broflovski, and Eric Cartman.  His oft-muffled and indiscernible speech—the result of his parka hood covering his mouth—is provided by co-creator Matt Stone.  He debuted on television when "South Park" first aired on August 13, 1997, after having first appeared in "The Spirit of Christmas" shorts created by Stone and long-time collaborator Trey Parker in 1992 ("Jesus vs. Frosty") and 1995 ("Jesus vs. Santa").

Kyle Broflovski: Kyle Broflovski (sometimes spelled Kyel Broflovski, Broslovski, Broslofski, Brovlofski or Broflofski) is a main character in the Comedy Central series "South Park".  He is voiced by and loosely based on co-creator Matt Stone.  Kyle is one of the show's four central characters, along with his friends Stan Marsh, Kenny McCormick, and Eric Cartman.  He debuted on television when "South Park" first aired on August 13, 1997, after having first appeared in "The Spirit of Christmas" shorts created by Stone and long-time collaborator Trey Parker in 1992 ("Jesus vs. Frosty") and 1995 ("Jesus vs. Santa").

Question: Kyle Broflovski is a central character along with which character voiced by and loosely based on series co-creator Trey Parker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "query_character_name": {
      "type": "string",
      "description": "The name of the character mentioned in the question as a central character."
    },
    "target_character_details": {
      "type": "object",
      "description": "Details about the character that fits the description in the question.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the identified character."
        },
        "is_central_character": {
          "type": "boolean",
          "description": "Indicates if the character is a central character."
        },
        "voiced_by_creator": {
          "type": "string",
          "description": "The name of the series co-creator who voices the character."
        },
        "loosely_based_on_creator": {
          "type": "string",
          "description": "The name of the series co-creator the character is loosely based on."
        }
      },
      "required": [
        "name",
        "is_central_character",
        "voiced_by_creator",
        "loosely_based_on_creator"
      ],
      "additionalProperties": false
    },
    "creator_info": {
      "type": "object",
      "description": "Information about the series co-creator mentioned.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the series co-creator."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the series creation."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "query_character_name",
    "target_character_details",
    "creator_info"
  ],
  "additionalProperties": false
}

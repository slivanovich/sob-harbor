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
Pam Ewing: Pamela Barnes Ewing is a fictional character from the CBS primetime soap opera, "Dallas".  Pamela is portrayed by actress Victoria Principal, first appearing on the show in the first episode, entitled "Digger's Daughter", which was first broadcast on April 2, 1978.  "Dallas" follows the trials of the wealthy Ewing oil family in the city of Dallas, Texas, which Pam has married into.  Principal played Pam until the end of the tenth season of "Dallas" in 1987, when the character crashes into a truck carrying butane and propane and her body is severely burned.  After this, she is briefly played by actress Margaret Michaels in an attempt to write the character out.  Pamela's storylines in season 1 focus on her relationship with her new husband, Bobby Ewing (Patrick Duffy), and her fight against the considerable suspicion and hostility from within the Ewing family, due to Pamela being a member of the Barnes family.  Pamela's love for Bobby remains a strong character trait throughout her tenure on the show, noted for its similarities to "Romeo and Juliet", with two people from hostile families falling in love.

Mike Barnes (Hollyoaks): Michael "Mike" Barnes is a fictional character from the British Channel 4 soap opera "Hollyoaks", played by Tony Hirst.  He first appeared on 9 January 2006.  In 2010, soap opera magazine "Inside Soap" reported that the character would leave in late January with love interest Zoe Carpenter (Zoë Lister).  This was later confirmed.  The character briefly returned in August 2016 and again in March 2017, where his youngest daughter Amy Barnes (Ashley Slanina-Davies) was killed-off in a "whodunit" storyline.  He returned again in September 2017 giving evidence against Ste Hay (Kieron Richardson) during Amy's murder trial.

Ruth Wilkinson: Ruth Wilkinson (previously Hails) is a fictional character from the Australian soap opera "Neighbours", played by Ailsa Piper.  She made her first on-screen appearance on 3 October 1996.  Ruth was a divorced single mother, who came to Erinsborough as Helen Daniels' new physiotherapist.  Ruth began a relationship with Philip Martin, which attracted some opposition from their children.  Ruth and Philip also had to cope with Ruth's long lost son, Ben, arriving to meet his mother.  Philip and Ruth married in 1998, amid a breast cancer scare for Ruth.  Producers decided to write the Martin family out of "Neighbours" and they departed on 20 October 1999.  In 2005, Piper reprised her role for the show's 20th anniversary.

Eliza Clark (actress): Eliza Clark is an American actress and playwright.  She is the sister of Spencer Treat Clark.  She has acted in minor parts in movies and commercials.  In 1990 she briefly played Jessica Buchanan on the soap opera "One Life to Live".

Lee Meriwether: Lee Ann Meriwether (born May 27, 1935) is an American actress, former model, and the winner of the 1955 Miss America pageant.  She is known for her role as Betty Jones, Buddy Ebsen's secretary and daughter-in-law in the long-running 1970s crime drama "Barnaby Jones".  The role earned her two Golden Globe Award nominations in 1975 and 1976, and an Emmy Award nomination in 1977.  She is also known for her role as Herman Munster's long-haired wife, Lily Munster, on the 1980s sitcom "The Munsters Today", as well as for her portrayal of Catwoman, replacing Julie Newmar in the film version of "Batman" (1966), and for a co-starring role on the science fiction series "The Time Tunnel".  Meriwether had a recurring role as Ruth Martin on the daytime soap opera "All My Children" until the end of the series in September 2011.

Ailsa Stewart: Ailsa Stewart (née O'Rourke, previously Hogan) is a fictional character from the Australian soap opera "Home and Away".  She was married to Alf Stewart and had a son Duncan.  She was played by actress Judy Nunn for 13 and a half years.  When Nunn left the show she was one of only four original cast members .  The role of Ailsa was briefly played by theatre star Nancye Hayes whilst Nunn was taking leave due to illness in 2000.

Spirit of '76 (Marvel Comics): The Spirit of '76 (real name William Naslund) is a fictional character appearing in American comic books published by Marvel Comics.  Created by writer Roy Thomas and artist Frank Robbins as part of a World War II-era superhero team, the Crusaders, and patterned on the DC Comics group the Freedom Fighters, the character first appeared in "The Invaders" #14 (March 1977).  The Spirit of '76 was the equivalent of Freedom Fighters member Uncle Sam, originally a Quality Comics character.  In the stories, the character briefly assumed the role of Captain America after the original – Steve Rogers – was presumed dead.  However, he was killed in action.

Cloris Leachman: Cloris Leachman (born April 30, 1926) is an American actress and comedian.  In a career spanning over seven decades she has won eight Primetime Emmy Awards (record tied with Julia Louis-Dreyfus), one Daytime Emmy Award and one Academy Award for her role in "The Last Picture Show" (1971).

Ruth Martin (Lassie): Ruth Martin is a fictional character on the long-running television series ""Lassie" (1954–1973).  She was briefly played by Cloris Leachman before June Lockhart stepped into the role.  The character makes her first appearance mid-fourth season (1957) and her last in the first episode of the eleventh season (1964); she appears in 208 episodes in total.

Emily Stewart: Emily Ryan (maiden name Stewart; previously Snyder, Munson and Hughes) is a fictional character on the daytime soap opera "As the World Turns".  She has been portrayed by Kelley Menighan Hensley since July 1992.  Ten years later, the actress received her first Daytime Emmy Award nomination for Outstanding Supporting Actress.  The character briefly appeared on the CBS soap, "The Young and the Restless", on 23 March 2007, asking Amber Moore about information on her sister and biological daughter, Alison Stewart.

Question: Ruth Martin was a character briefly played by which American actress and comedian?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the fictional character."
    },
    "show_name": {
      "type": "string",
      "description": "The television series where the character appeared."
    },
    "actress_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions of the actress."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions"
      ],
      "additionalProperties": false
    },
    "role_duration": {
      "type": "string",
      "description": "Description of how long the actress played the role."
    }
  },
  "required": [
    "character_name",
    "show_name",
    "actress_details",
    "role_duration"
  ],
  "additionalProperties": false
}

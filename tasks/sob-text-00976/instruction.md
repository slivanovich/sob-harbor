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
Wo Fat: Wo Fat is the name of a fictional villain in the long-running CBS series "Hawaii Five-O".  On the show, Wo Fat is the nemesis of Steve McGarrett (Jack Lord and Alex O'Loughlin), the head of Hawaii's (fictional) special task force, Five-O.

Steve McGarrett: Steve McGarrett is a fictional character from "Hawaii Five-O" who serves as the leader of the Hawaii Five-0 (5−0) crime task force.  McGarrett was originally played by Jack Lord and also by Alex O'Loughlin in the remake.  He is partner to Detective Danny "Danno" Williams.

Sid Fernandez: Charles Sidney Fernandez (born October 12, 1962) was a Major League Baseball left-handed pitcher from 1983 to 1997 .  Born in Honolulu, Hawaii, Fernandez was proud of his roots and wore uniform number 50 in honor of Hawaii being the 50th state.  The theme song to "Hawaii Five-O" was often played before his starts at Shea Stadium during his days with the New York Mets.

Squad Five-O: Squad Five-O was a punk rock band from Savannah, Georgia.  Like their initial ska-punk stylings, their name was derived from a cross between the television shows "Hawaii Five-O" and the "The Mod Squad".  Between 1997 and 2006 the band grew lyrically and in popularity, and also shifted its style significantly.  Over the course of their career they moved from a very small indie Christian label to the major label Capitol Records and released five albums in the process.

Al Harrington (actor): Al Harrington (born Tausau Ta'a on December 12, 1935) is an American television actor.  He is best known for his role as "Det. Ben Kokua" on the CBS television series "Hawaii Five-O" and as Mamo Kahike on the 2010 reboot of Hawaii Five-0 playing the owner of a surf shop and a bus driver in the off season.  He had previously appeared in five episodes of the series as other characters.

Hawaii (TV series): Hawaii is a United States television series produced and distributed by NBC Universal Television for the NBC television network.  Originally titled "Pearl City", this police drama was produced with the series "Hawaii Five-O" in mind, and debuted on August 31, 2004.  Written by Executive Producer Jeff Eastin, the series revolves around a fictional elite crime unit of the Honolulu Police Department headed by veteran detective and local legend Sean Harrison (Michael Biehn) and John Declan (Sharif Atkins), a former Chicago Police Department detective transferred to Hawaii for his talents.

Five-O (mobile application): Five-O is a mobile application created by three African-American siblings from Georgia, USA.  The three, Ima, Asha, and Caleb Christian, aged 16, 15, and 14 respectively, in 2014, created the application as an attempt to provide a solution to the issues generated from interaction between law enforcement and citizens, such as the shooting of Michael Brown, and their own traumatic experience with two police officers.  The application was launched on 18 August 2014.  The application is available on both Android and iOS platforms, and has been developed in collaboration with Pinetart Inc., a company developing mobile applications they have founded.  The term Five-O is American slang for law enforcement, based on Hawaii Five-O, a television programme.

Alex O'Loughlin: Alex O'Loughlin (born 24 August 1976) is an Australian actor, who plays Lieutenant Commander Steve McGarrett on CBS' remake of the TV series "Hawaii Five-0".  He had starring roles in the films "Oyster Farmer" (2004) and "The Back-up Plan" (2010), as well as on such television series as "Moonlight" (2008) and "Three Rivers" (2009).

Maggi Parker: Maggi Parker is an American actress, born in Nashua, New Hampshire.  She also starred in 14 episodes of the US crime drama "Hawaii Five-O" during the years 1968 and 1969, playing the secretary.  A teacher and school principal for 17 years with a B.E. in education.  She has lived in Hawaii since the late 50's and worked for the royal family of Hawaii for 43 years.  Maggi has been an inspiration to many to attend college to further their education.

Herman Wedemeyer: Herman John Wedemeyer (May 20, 1924 – January 25, 1999) was an American actor, football player, and politician.  He is best known for portraying Sergeant/Detective "Duke" Lukela on the crime drama "Hawaii Five-O" (1972–1980).  However, he appeared on the first episode of Hawaii Five-O as Lt. Balta of HPD.

Question: Which character does Alex O'Loughlin play in "Hawaii Five-O"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "character_rank": {
      "type": "string",
      "description": "The rank or title of the character."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "series_name"
  ],
  "additionalProperties": false
}

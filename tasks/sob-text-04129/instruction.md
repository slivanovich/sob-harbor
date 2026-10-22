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
Justin Pearson (stuntman): Justin Pearson (born 1971) is a British stunt man and stunt coordinator who is best known for his stunt work in "Harry Potter and the Deathly Hallows – Part 2" (2011) and "Skyfall" (2012), for which he received Screen Actors Guild Awards in 2012 and 2013 respectively, as part of a stunt ensemble.

Patrick Condren: Patrick Condren (born 1967) is an Irish actor, stunt professional, and a former Irish Heavyweight Kickboxing Champion.  He was the first Irishman to be nominated at the Taurus World Stunt Awards following his work in the film, "Intermission", whereby in the biggest single stunt ever filmed in Ireland, a double-decker bus was flipped 20m into the air.

Mike Dopud: Mike Dopud (Serbian: Majk Dopuđ , "Мајк Допуђ"; born June 10, 1968) is a Canadian actor, stuntman, and athlete.  He is known for playing Detective Smits in "White Noise" the 2005 action-horror film, Agent Turner in "Alone in the Dark" a 2005 action-horror film, playing Vic Hadfield in the Canadian miniseries Canada Russia '72, and for playing Michael 'The Assassin' in the "Rollerball" 2002 film remake.  He also took on several minor roles on "Stargate SG-1" and "Stargate Atlantis", as well as performing many stunts on both shows, before taking on a bigger role as Varro on "Stargate Universe".  He was nominated for a Taurus World Stunt Award in 2005 for his work in "Walking Tall".

David Leitch (director): He was a stunt double for Brad Pitt five times and two times for Jean-Claude Van Damme.  Leitch and his crew won two awards for "The Bourne Ultimatum" at the Screen Actors Guild Awards and Shared a World Stunt Awards with Kai Martin.

Romain Thievin: Romain Gerard Michel Thievin (born March 13, 1979) is a five-time French champion in car racing and also a co-presenter of FAST CLUB, a car TV show broadcasting on W9 channel in France and Belgium.  Romain is also an accomplished stunt driver, having worked on more than 150 movies.  In 2003, he won a Taurus World Stunt Award for his work in The Bourne Identity.

Dietrich Mateschitz: Dietrich Mateschitz (born 20 May 1944) is an Austrian billionaire businessman.  He co-founded the Red Bull energy drink company, and holds 49% of the company's shares.  Mateschitz's net worth, as of 2017 , is estimated to be $15.4 billion.

Taurus World Stunt Awards: The Taurus World Stunt Awards is a yearly award ceremony held midyear that honors stunt performers in movies.  It is held each year in Los Angeles.  The first awards were given out in 2001.  However the deciding committee has been around since the year 2000.  The awards were created by Dietrich Mateschitz, the founder of Red Bull.

Peter Hein: Peter Hein is an Indian fight master/action choreographer and stunt coordinator who has worked in many South Indian film productions.  He became famous for his action sequences in films such as "Anniyan" (2005), "Sivaji" (2007), "Ghajini" (2008), "Magadheera" (2009), "Enthiran" (2010), "Raavanan" (2010), "7aum Arivu" (2011), "Kochadaiyaan" (2014),"<a href="">"(2015), "" (2015) and "Pulimurugan" (2016).  He has been nominated for the noted Taurus World Stunt Award against many big Hollywood names.  He received a Filmfare Award for Best Action for his work in "Ghajini (2008 film)".  Stunt masters such as Anal Arasu and Silva have worked as fighters and assistants to him.  He received the very first National Film Award for Best Stunt Choreographer for his work in "Pulimurugan".

Viktor Ivanov (stunt coordinator): Viktor Ivanov (sometimes credited as Victor Ivanov) is a Russian film director and veteran stunt coordinator best known for the feature film "White Gold" and for his design of the spectacular car chase through the streets of Moscow in "The Bourne Supremacy", for which he won the "Best Vehicle" award at the 2005 Taurus World Stunt Awards.

British National (Overseas): British National (Overseas), commonly known as BN(O), is one of the major classes of British nationality under British nationality law.  Holders of this nationality are British nationals and Commonwealth citizens, but not British citizens.  The nationality itself does not grant right of abode anywhere in the world, including United Kingdom or Hong Kong, but most BN(O)s possess either right of abode or right to land in Hong Kong.  BN(O)s are subject to British immigration controls and do not have the automatic right to live or work in the United Kingdom.

Question: What is the nationality of the creator of the Taurus World Stunt Awards?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_name": {
      "type": "string",
      "description": "The name of the stunt award."
    },
    "creator_details": {
      "type": "object",
      "properties": {
        "creator_name": {
          "type": "string",
          "description": "The name of the person who created the award."
        },
        "creator_nationality": {
          "type": "string",
          "description": "The nationality of the award creator."
        }
      },
      "required": [
        "creator_name",
        "creator_nationality"
      ],
      "additionalProperties": false
    },
    "award_founding_year": {
      "type": "integer",
      "description": "The year the first awards were given out."
    }
  },
  "required": [
    "award_name",
    "creator_details",
    "award_founding_year"
  ],
  "additionalProperties": false
}

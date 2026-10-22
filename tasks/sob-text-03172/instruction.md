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
Chester I. Campbell: "Chester Campbell redirects here.  For the fictional character, Chester Campbell, see Peaky Blinders (TV series)"

Matthew Postlethwaite: Matthew Postlethwaite (born 25 September in Whitehaven, Cumbria) is a British actor, singer and artist.  He played Nipper in the television series "Peaky Blinders".  He has an identical twin brother, Jeffrey Postlethwaite, who also is an actor.

Mariner 8: Mariner-H (Mariner Mars '71), also commonly known as Mariner 8, was (along with Mariner 9) part of the Mariner Mars '71 project.  It was intended to go into Mars orbit and return images and data, but a launch vehicle failure prevented Mariner 8 from even achieving an Earth orbit and the spacecraft reentered into the Atlantic Ocean shortly after launch.

Paul Anderson (actor): Paul Anderson is an English actor of film and stage.  He came to prominence for portraying Arthur Shelby in "Peaky Blinders" and Sebastian Moran in "".

'71 (film): <nowiki>'71</nowiki> is a 2014 British historical thriller film set in Northern Ireland, written by Gregory Burke and directed by Yann Demange.  It stars Jack O'Connell, Sean Harris, David Wilmot, Richard Dormer, Paul Anderson and Charlie Murphy, and tells the story of a British soldier who becomes separated from his unit during a riot in Belfast at the height of the Troubles in 1971.  Filming began on location in Blackburn, Lancashire, in April 2013 and continued in Sheffield and Liverpool.  The film was funded by the British Film Institute, Film4, Creative Scotland and Screen Yorkshire.  The film had its premiere in the competition section of the 64th Berlin International Film Festival, held in February 2014.

Peaky Blinders (TV series): Peaky Blinders is a British television crime drama based upon the exploits of the Peaky Blinders gang, which operated in Birmingham, England, during the aftermath of World War I.  The series, created by Steven Knight and produced by Caryn Mandabach Productions and Tiger Aspect Productions, centres around and stars Cillian Murphy as Tommy Shelby, the gang's leader, and Sam Neill as Chester Campbell, a commissioned detective tasked with suppressing the gang.

Finn Cole: Finn Cole (born 9 November 1995) is an English actor from Kingston, London.  He is most well known for his role in the BBC series "Peaky Blinders" as Michael Gray.  He is currently starring as Joshua 'J' Cody in TNT's "Animal Kingdom".

Kate Phillips (actress): Kate Phillips is a British actress best known for her roles in "Peaky Blinders", "Wolf Hall" and the 2016 BBC adaptation of "War & Peace".  After three years study at Leeds University Philips secured a place at The Guildhall School of Music and Drama in London.  After graduation she returned to Leeds to appear as Abigail Williams in "The Crucible" at the West Yorkshire Playhouse.  By this time she had already filmed her scenes for the BBC's adaptation of "Wolf Hall" in which she played Jane Seymour, a role she had been offered whilst still studying at Guildhall.  There was some mild controversy following the initial airing of "Wolf Hall" after some historians's described Philips as 'too pretty' to play Henry VIII's third wife.  This criticism was disregarded by several critics who praised Philips' performance with "Screen Daily" naming her as a 'Star of Tomorrow'.  She went on to secure roles in "War & Peace", "Peaky Blinders" and "The Crown".

Cillian Murphy: Cillian Murphy ( ; born 25 May 1976) is an Irish actor of stage and screen.  Since making his debut in his home country in the late 1990s, Murphy has also become a presence in British and American cinemas noted by critics for his performances in many independent and mainstream films.  He is best known as Damien in "The Wind That Shakes the Barley", Jim in "28 Days Later" (2002), the Scarecrow in "The Dark Knight Trilogy" (2005–12), Jackson Rippner in "Red Eye" (2005), Robert Capa in "Sunshine" (2007), Robert Fischer in "Inception" (2010) and Thomas Shelby in the BBC series "Peaky Blinders".

Sam Neill: Nigel John Dermot Neill {'1': ", '2': ", '3': ", '4': "} (born 14 September 1947), known professionally as Sam Neill, is a New Zealand actor who first achieved leading roles in films such as "" and "Dead Calm" and on television in "Reilly, Ace of Spies".  He won a broad international audience in 1993 for his roles as Alisdair Stewart in "The Piano" and Dr. Alan Grant in "Jurassic Park", a role he reprised in 2001's "Jurassic Park III".  Neill also had notable roles in "Merlin", "The Hunt for Red October", "Peaky Blinders", and "The Tudors".  In 2016, he starred in "Hunt for the Wilderpeople" alongside Julian Dennison, to great acclaim.

Question: '71 stars an actor who played what character in "Peaky Blinders"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "tv_series_title": {
      "type": "string",
      "description": "The title of the TV series mentioned in the question."
    },
    "actor_who_starred_in_both": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who starred in both the film and the TV series."
        },
        "character_in_tv_series": {
          "type": "string",
          "description": "The character portrayed by the actor in the specified TV series."
        }
      },
      "required": [
        "name",
        "character_in_tv_series"
      ],
      "additionalProperties": false
    },
    "answer_character_name": {
      "type": "string",
      "description": "The name of the character from 'Peaky Blinders' played by an actor who also starred in '71."
    }
  },
  "required": [
    "film_title",
    "tv_series_title",
    "actor_who_starred_in_both",
    "answer_character_name"
  ],
  "additionalProperties": false
}

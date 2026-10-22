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
Veterans Day: Veterans Day is an official United States public holiday, observed annually on November 11, that honors military veterans; that is, persons who served in the United States Armed Forces.  It coincides with other holidays, including Armistice Day and Remembrance Day, celebrated in other countries that mark the anniversary of the end of World War I; major hostilities of World War I were formally ended at the 11th hour of the 11th day of the 11th month of 1918, when the Armistice with Germany went into effect.  The United States previously observed Armistice Day.  The U.S. holiday was renamed Veterans Day in 1954.

Graeme Devine: Graeme Devine is a computer game designer and programmer who co-founded Trilobyte, created bestselling games "The 7th Guest" and "The 11th Hour", and helped design id Software's "Quake III Arena".  He was also Chairman of the International Game Developers Association (IGDA) from 2002–2003.  One of Graeme's trademarks is his Scooby-Doo wardrobe.  He has said of his work that "I've not stuck to any one genre, platform or IP throughout my career, and I hope people eventually work out that's just fine."

Remembrance Day: Remembrance Day (sometimes known informally as Poppy Day) is a memorial day observed in Commonwealth of Nations member states since the end of the First World War to remember the members of their armed forces who have died in the line of duty.  Following a tradition inaugurated by King George V in 1919, the day is also marked by war remembrances in many non-Commonwealth countries.  Remembrance Day is observed on 11 November in most countries to recall the end of hostilities of World War I on that date in 1918.  Hostilities formally ended "at the 11th hour of the 11th day of the 11th month", in accordance with the armistice signed by representatives of Germany and the Entente between 5:12 and 5:20 that morning.  ("At the 11th hour" refers to the "passing" of the 11th hour, or 11:00 am.)  The First World War officially ended with the signing of the Treaty of Versailles on 28 June 1919.

The 11th Hour (newspaper): The 11th Hour News Weekly is an arts and entertainment alternative weekly published in Macon, Statesboro and Valdosta, Georgia.  Beginning in Statesboro in 2001 as a newsletter on bars and nightclubs, it developed into a full-scale A&E publication, featuring leisure events in the college town.  In 2003, "The 11th Hour" opened a main office in Macon.  With its growing popularity, the newsweekly expanded distribution of the Macon version to the surrounding Middle Georgia cities of Milledgeville and Warner Robins.  Valdosta’s version of "The 11th Hour" began in 2004; its readers are students at Valdosta State University and other supporters of the South Georgia art community

11th Hour (novel): 11th Hour is the 11th novel of the "Women’s Murder Club" series written by American author James Patterson.  The main character of this series is Sgt. Lindsay Boxer.  The series is a set in San Francisco and the Women's Murder Club is a small group of women who meet with Boxer to help solve sensational crimes in the city.  Throughout the series, the membership of the Women's Murder Club has had some changes.

The 11th Hour (video game): The 11th Hour is a 1995 interactive movie puzzle adventure game with a horror setting.  It is the sequel to the 1993 game "The 7th Guest".  It was developed by Trilobyte and used a later version of the "Groovie" graphic engine than that used by "The 7th Guest".  "The 11th Hour" also features the music of George "The Fat Man" Sanger and Team Fat.

Audience of One (film): Audience of One is an award-winning 2007 documentary film directed by Michael Jacobs that was premiered on 9 March 2007 at South by Southwest in Austin, Texas.

WAAKE-UP!: WAAKE-UP!  (World Awareness and Action Koalition of Equal United Progressives) was a student and community coalition at the University of Colorado Boulder (CU-Boulder) active from 1998 to 2001.  WAAKE-UP!  adopted the motto "Action without Awareness is ignorant.  Awareness without Action is immoral."  WAAKE-UP!  supported many progressive causes, but were best known for the "Sweatshop Campaign," demanding that University of Colorado apparel be made in factories supporting fair labor conditions, specifically those endorsed by the Worker Rights Consortium.  The Sweatshop Campaign was not successful, but its goals were later fulfilled by WAAKE-UP! 's successor organizations, 180 at 11 (180 degrees at the 11th hour), CASA (Coalition Against Sweatshop Apparel) and WWJC (World Workers Justice Committee).  Like many other progressive organizations in Colorado their actions were recorded in the Denver Police Spy Files.

The 11th Hour (2007 film): The 11th Hour is a 2007 documentary film, created, produced, co-written and narrated by Leonardo DiCaprio, on the state of the natural environment.  It was directed by Leila Conners Petersen and Nadia Conners and financed by Adam Lewis and Pierre André Senizergues, and distributed by Warner Independent Pictures.

Uncle Henry's Playhouse: Uncle Henry's Playhouse (released in the UK as Uncle Henry's MindBlower) is the third game in the "The 7th Guest" series.  Functionally the game is a compilation game mostly composed of the puzzles from Trilobyte's games "The 7th Guest", "The 11th Hour", and "Clandestiny", but featuring little plot.  The game has been noted for its low sales figures (27 in the US) and its rarity/obscurity relative to its blockbuster predecessors, "The 7th Guest" and "The 11th Hour".

Question: What do The 11th Hour and Audience of One have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_film_type": {
      "type": "string",
      "description": "The common type of film shared by both entities."
    },
    "common_release_year": {
      "type": "integer",
      "description": "The common release year for both films."
    },
    "compared_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "type": {
            "type": "string",
            "description": "The specific type of the entity as described in the context."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      },
      "description": "A list of the entities being compared."
    }
  },
  "required": [
    "common_film_type",
    "common_release_year",
    "compared_entities"
  ],
  "additionalProperties": false
}

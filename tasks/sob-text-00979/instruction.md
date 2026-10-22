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
Arnold, Nottinghamshire: Arnold is a market town, unparished area and suburb of the city of Nottingham, in the English ceremonial county of Nottinghamshire.  It is situated to the north-east of Nottingham's city boundary, and is in the local government district of Gedling Borough.  Since 1968 Arnold has had a market, and the town used to have numerous factories associated with the hosiery industry.  Arnold's town centre is the largest in Gedling Borough (whose headquarters are located in the town) and the most important in the northeastern part of the Greater Nottingham conurbation.  Nottinghamshire Police have been headquartered in Arnold since 1979.  At the time of the 2011 Census, Arnold had a population of 37,768.

Rocky: Rocky is a 1976 American sports drama film directed by John G. Avildsen and both written by and starring Sylvester Stallone.  It tells the rags to riches American Dream story of Rocky Balboa, an uneducated but kind-hearted working class Italian-American boxer working as a debt collector for a loan shark in the slums of Philadelphia.  Rocky starts out as a small-time club fighter, and later gets a shot at the world heavyweight championship.  The film also stars Talia Shire as Adrian, Burt Young as Adrian's brother Paulie, Burgess Meredith as Rocky's trainer Mickey Goldmill, and Carl Weathers as the champion, Apollo Creed.

My Demon Lover: My Demon Lover is a 1987 American comedy film directed by Charlie Loventhal and written by Leslie Ray.  The film stars Scott Valentine, Michele Little, Robert Trebor, Gina Gallego, Alan Fudge, Calvert DeForest and Arnold Johnson.  The film was released on April 24, 1987, by New Line Cinema.

Maud Johnson: Maud Battle Johnson (ca. 1918 – September 5, 1985) was an US journalist and author of romance novels. Johnson began her writing career working for newspapers in North Carolina, eventually becoming managing editor of the "Rocky Mount Evening Telegram".  Her novels for teen-aged girls included a romance series set in Virginia — where Johnson later died of cancer — the novels, beginning in 1979 with "I'm Christy" and continuing through "Christy's Choice", "Christy's Love," and "Christy's Senior Year", were best sellers but were critically panned as "corny" and "bland."  Johnson died in Richmond, Virginia, but was buried in Pineview Cemetery in Rocky Mount; her final novel, "Dating Blues", was published after her death.

Arnold Johnson (actor): Arnold Herbert Johnson (November 15, 1921 – April 10, 2000) was an American actor who played the lead role in the film "Putney Swope" (1969); in the film, his voice was dubbed by Robert Downey, Sr. because Johnson could never remember his lines.  Johnson appeared in "Shaft (1971 film)" as Cul, a friend of John Shaft and the owner of a shoeshine parlor.  He also played a role in the film "My Demon Lover" (1987) and had roles in "Rocky" (1976) and "Menace II Society" (1993), as Thomas, the religious Christian grandfather of the lead character Caine (played by Tyrin Turner).

Rocky Steps: The 72 stone steps before the entrance of the Philadelphia Museum of Art, in Philadelphia, Pennsylvania, have become known as the "Rocky Steps" as a result of their appearance in the triple-Oscar-winning film "Rocky" and all of the series' sequels except for "Rocky IV", in which the eponymous character runs up the steps to the song "Gonna Fly Now".  Tourists often mimic Rocky's famous climb, a metaphor for an underdog or an everyman rising to a challenge.  A bronze "Rocky" statue was briefly situated at the top of the steps for the filming of "Rocky III".  This statue, now located at the bottom right of the steps, is a popular photo opportunity for visitors.  The top of the steps offers a commanding view of Eakins Oval, the Benjamin Franklin Parkway, and Philadelphia City Hall.

Arnold Johnson (physician): Arnold Johnson, M.D., C.M., FRCPC, (1916 – October 19, 2006) was a Canadian cardiologist and founder of the Department of Cardiology at McMaster University.  He is most well known for performing the first heart catheterization procedure for congenital heart disease in Canada in 1946.

Roy Mack: Roy Mack, born McGillicuddy, (c. 1889 – February 11, 1960) was the co-owner of the Philadelphia Athletics of the American League with his brother Earle Mack from 1950 through 1954 .  In 1954, the brothers sold the Athletics to Arnold Johnson, who moved the team to Kansas City, Missouri one season later.  Mack was the son of Hall of Fame manager and former Athletics owner Connie Mack.  Roy was a graduate of Worcester Academy in Worcester, Massachusetts.

Putney Swope: Putney Swope, a 1969 satirical comedy film written and directed by Robert Downey Sr. and starring Arnold Johnson as Swope, is a comedy satirizing the advertising world, the portrayal of race in Hollywood films, the white power structure, and the nature of corporate corruption.

Arnold Johnson (musician): Arnold Johnson (March 23, 1893, Chicago - July 25, 1975, St. Petersburg, Florida) was an American big band pianist, arranger, composer, and leader during the swing jazz era.

Question: What industry are both Arnold Johnson and Rocky popular?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_industry": {
      "type": "string",
      "description": "The industry that both Arnold Johnson and Rocky are popular in."
    },
    "entities_involved": {
      "type": "array",
      "description": "Details about the entities that share popularity in this industry.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "type": {
            "type": "string",
            "description": "The type of entity (e.g., 'actor', 'film')."
          }
        },
        "required": [
          "name",
          "type"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why this industry is common to both."
    }
  },
  "required": [
    "common_industry",
    "entities_involved",
    "reasoning"
  ],
  "additionalProperties": false
}

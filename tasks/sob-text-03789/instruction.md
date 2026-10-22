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
Hugh, Count of Vermandois: Hugh (1057 – October 18, 1101), called the Great (Latin "Hugo Magnus"), was a younger son of Henry I of France and Anne of Kiev and younger brother of Philip I.  He was Count of Vermandois in right of his wife ("jure uxoris").  His nickname "Magnus" (greater or elder) is probably a bad translation into Latin of a French nickname, "le Maisné", meaning "the younger", referring to Hugh as younger brother of the King of France.

Vincent Meli: Vincent "Little Vince" Meli (January 2, 1921 – January 7, 2008) was a Detroit mobster and acting underboss of the Detroit crime family.  The nephew of Angelo Meli, he succeeded longtime crime boss Anthony Zerilli following his imprisonment.

Milwaukee crime family: The Milwaukee crime family or Balistrieri crime family is an American Mafia crime family based in Milwaukee, Wisconsin.  The crime family was considered a branch of the Chicago Outfit.  The family's most influential boss was Frank "Mr. Big" Balistrieri, who was greatly involved in the Las Vegas skimming casinos. Today, the crime family is nearly extinct, since Balistrieri died in 1993, with the "Chicago Outfit" gaining control over some of the illegal rackets in the area.

Joseph Zerilli: Joseph Zerilli (December 10, 1897 – October 30, 1977) was a Prohibition-era Detroit gangster who led the crime family known as the Detroit Partnership from the 1930s through the 1970s.

Patriarca crime family: The Patriarca crime family (pronounced ] ) is also known as the New England crime family, the Providence crime family, the Boston crime family, the Boston Mafia, the Providence Mafia, the New England Mafia, or The Office and is an Italian-American Mafia crime family based in New England.  The crime family has two distinct factions, one active in Providence, Rhode Island and the other in Boston, Massachusetts.

William Grasso: William "Wild Guy" Grasso was an Italian-American gangster from East Haven, Connecticut who served as underboss to Raymond Patriarca, Jr. (a.k.a. "Junior") in the Patriarca crime family, also known as the New England crime family, the Providence crime family or the Boston crime family.  The Patriarca family is a Mafia crime family based in New England.  Succeeding his father Raymond L.S. Patriarca as boss after his father's death in 1984, Junior was considered a weak leader.  He managed to keep the peace in his crime family due to the support of the Gambino crime family of New York.  When Junior's original underboss Ilario "Larry Baione" Maria Antonio Zannino was sentenced to thirty years in prison in 1987, it further weakened Junior's position.  With Zannino in jail, Grasso became underboss.

Vito Giacalone: Vito William "Billy Jack" Giacalone (April 16, 1923 – February 19, 2012) was an American organized crime figure in Detroit, serving as a capo in the Detroit Partnership.  He was the younger brother of Anthony "Tony Jack" Giacalone, also a capo in the Detroit Partnership.

Genovese crime family New Jersey faction: The Genovese crime family's New Jersey faction is a group of mobsters within the Genovese crime family that control the family's interests in organized crime activities in the state of New Jersey.  The New Jersey faction of the Genovese crime family has maintained a strong presence in the Northern New Jersey area since the prohibition era.  The faction is divided into multiple crews and has increased in power over the years with members controlling illegal activities in labor racketeering, loansharking, extortion, and illegal gambling.  Members within the faction have held top leadership position in the Genovese crime family dating back to the 1930s with underboss Guarino "Willie" Moretti.  From the 1990s until his death in 2010, Tino "the Greek" Fiumara had been in control of the New Jersey faction.

DeCavalcante crime family: The DeCavalcante crime family is an Italian-American organized crime family that operates in Elizabeth, New Jersey and surrounding areas in the state and is part of the nationwide criminal phenomenon known as the American Mafia (or Cosa Nostra).  It operates on the other side of the Hudson River from the Five Families of New York, but it maintains strong relations with many of them, as well as with the Philadelphia crime family and the Patriarca crime family of New England.  Its illicit activities include bookmaking, building, cement, and construction violations, bootlegging, corruption, drug trafficking, extortion, fencing, fraud, hijacking, illegal gambling, loan-sharking, money laundering, murder, pier thefts, pornography, prostitution, racketeering, and waste management violations.  The DeCavalcantes are, in part, the inspiration for the fictional DiMeo crime family of HBO's dramatic series "The Sopranos".  The DeCavalcante family was the subject of the CNBC program "Mob Money", which aired on June 23, 2010 and "The Real Sopranos" TV documentary (first airdate April 26, 2006) directed by Thomas Viner for the UK production company Class Films.

Detroit Partnership: The Detroit Partnership, also known as the Detroit crime family, Detroit Combination, Detroit Mafia, or Zerilli crime family (pronounced ] ) is an American Mafia crime family based in Detroit, Michigan.

Question: What was the nickname of the younger brother in the Zerilli crime family?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "crime_family_name": {
      "type": "string",
      "description": "The name of the crime family the brothers belong to."
    },
    "younger_brother": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the younger brother."
        },
        "nickname": {
          "type": "string",
          "description": "The nickname of the younger brother."
        },
        "role": {
          "type": "string",
          "description": "The role of the younger brother in the crime family."
        }
      },
      "required": [
        "full_name",
        "nickname",
        "role"
      ],
      "additionalProperties": false
    },
    "older_brother": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the older brother."
        },
        "nickname": {
          "type": "string",
          "description": "The nickname of the older brother."
        },
        "role": {
          "type": "string",
          "description": "The role of the older brother in the crime family."
        }
      },
      "required": [
        "full_name",
        "nickname",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "crime_family_name",
    "younger_brother",
    "older_brother"
  ],
  "additionalProperties": false
}

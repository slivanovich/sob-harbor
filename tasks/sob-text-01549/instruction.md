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
Renzo Gracie: Renzo Gracie ( ; ] ; born March 11, 1967) is a Brazilian mixed martial artist and Brazilian Jiu-Jitsu practitioner.  A member of the Gracie family of Brazil, Renzo is a 6th Degree Black in Brazilian Jiu-Jitsu under Carlos Gracie Jr..  He is the son of Robson Gracie, grandson of Carlos Gracie, nephew of Carlos Gracie, Jr. grandnephew of Helio Gracie, and the 1st cousin once removed of Royce Gracie.  In mixed martial arts, Renzo has competed in the Ultimate Fighting Championship, Pride Fighting Championships, K-1, RINGS, and International Fight League (head-coaching the New York Pitbulls).  He holds notable victories over five former UFC Champions: Frank Shamrock (UFC Light Heavyweight Champion), Carlos Newton (UFC Welterweight Champion), Pat Miletich (UFC Welterweight Champion), Maurice Smith (UFC Heavyweight Champion), and Oleg Taktarov (UFC 6 Tournament Winner)

Antônio Silva (fighter): Antônio Carlos Silva (born September 14, 1979) is a Brazilian mixed martial artist who formerly competed in the heavyweight division of the UFC.  He is a former EliteXC Heavyweight Champion, a former Cage Rage World Heavyweight Champion and a former Cage Warriors Super Heavyweight Champion.  He has also competed for K-1 Hero's, BodogFIGHT, Strikeforce and World Victory Road.  Known for being one of the five men (along with Tsuyoshi Kohsaka, Fabrício Werdum, Dan Henderson, and Matt Mitrione) to defeat Fedor Emelianenko in mixed martial arts competition.

Ebenezer Fontes Braga: Ebenezer "Pitbull" Fontes Braga (born April 14, 1969) is a retired Brazilian mixed martial artist.  He competed in the Light Heavyweight division.  He lost his last fight at JF 2 - Jungle Fight 2 against Fabrício Werdum on May 15, 2004.

Fabrício Werdum: Fabrício Werdum (] ; born July 30, 1977) is a Brazilian mixed martial artist and former UFC Heavyweight Champion.  He is also a two-time Brazilian jiu-jitsu world champion, a two-time Abu Dhabi Combat Club World Heavyweight Champion and European jiu-jitsu champion.  He holds black belts in Brazilian jiu-jitsu, Judo, and Muay Thai.  Werdum has competed in PRIDE, the UFC, Strikeforce, and Jungle Fight.

Frank Mir: Francisco Santos "Frank" Mir, III (born May 24, 1979) is an American mixed martial artist, who competes for Bellator MMA in the Heavyweight division.  He formerly competed in the Ultimate Fighting Championship (UFC) for sixteen years.  A former UFC Heavyweight Champion, he currently holds the record for most fights, victories, and submissions in UFC Heavyweight history, and is tied for 4th most UFC victories overall.  Up until his release, Mir possessed the longest uninterrupted tenure of any fighter in UFC history.  He is the first man to knock out and submit Antônio Rodrigo Nogueira.

Antônio Rogério Nogueira: Antônio Rogério Nogueira (] ; born June 2, 1976), better known as Minotouro or Little Nog, is a Brazilian mixed martial artist currently signed with the UFC.  He is the twin brother of Antônio Rodrigo Nogueira, the "Minotauro", earning Rogério the nickname "Minotouro".  A proficient amateur boxer, he was the 2006 and 2007 Brazilian Super Heavyweight Champion.  He also won a bronze medal in the 2007 Pan American Games.  As of April 1, 2016, he is #10 in official UFC Light Heavyweight rankings.

Vinny Magalhães: Vinicius de Magalhães (] ; born July 2, 1984), is a Brazilian mixed martial artist who competes in the World Series of Fighting's Light Heavyweight division.  He was a finalist in "" and has fought five times within two stints with the Ultimate Fighting Championship.  He is the former Titan FC Light Heavyweight Champion, M-1 Global Light Heavyweight Champion and is also a multiple time jiu-jitsu gi and no-gi world champion.  Magalhães currently fights in the light heavyweight division of the Absolute Championship Berkut.

Ronny Markes: Ronny Marki Sales da Silva (born April 21, 1988) is a Brazilian mixed martial artist currently competing in the Light Heavyweight division.  A professional competitor since 2007, Markes has formerly competed for the UFC, the World Series of Fighting, King of the Cage, and M-1 Global.  He is the current King of the Cage Super Heavyweight Champion.

Rafael Cavalcante: Rafael Cavalcante (born April 5, 1980) is a Brazilian mixed martial artist who fights in the light heavyweight division.  He is currently a free agent.  He trains with Anderson Silva and Antônio Rodrigo Nogueira as part of the Black House camp.  He formerly competed in Strikeforce, where he was at one time Strikeforce Light Heavyweight Champion.  His nickname "Feijão" (] ) means "bean" in Portuguese.  Rafael was known as the first man to have defeated former UFC number-one middleweight contender, Yoel Romero.

Antônio Rodrigo Nogueira: Antônio Rodrigo Nogueira (] , born June 2, 1976), better known as Minotauro, is a semi-retired Brazilian mixed martial artist known for his technical mastery of Brazilian jiu-jitsu.  He won most of his fights via submissions.  He competed in the heavyweight division of the Ultimate Fighting Championship (UFC), where he is a former Interim UFC Heavyweight Champion.  He is the twin brother of UFC fighter Antônio Rogério Nogueira.  Nogueria rose to prominence in the Japanese promotion Pride Fighting Championships, where he was the first Pride Heavyweight Champion from November 2001 to March 2003, as well as a 2004 PRIDE FC Heavyweight Grand Prix Finalist.  He is one of only three men to have held championship titles in both Pride Fighting Championships and the Ultimate Fighting Championship (the others being Mauricio Rua and Mark Coleman).

Question: Antônio Carlos Silva, is a Brazilian mixed martial artist who formerly competed in the heavyweight division of the UFC, known for being one of the five men, along with Fabrício Werdum, a Brazilian mixed martial artist and former Heavyweight Champion, of which organization?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the fighter."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the fighter."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "championship": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the championship held by the fighter."
        },
        "organization": {
          "type": "string",
          "description": "The organization where the championship was held."
        }
      },
      "required": [
        "title",
        "organization"
      ],
      "additionalProperties": false
    },
    "is_former_champion": {
      "type": "boolean",
      "description": "Indicates if the fighter is a former champion of the specified title and organization."
    }
  },
  "required": [
    "fighter",
    "championship",
    "is_former_champion"
  ],
  "additionalProperties": false
}

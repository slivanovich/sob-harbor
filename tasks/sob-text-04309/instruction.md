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
Carl Crook: Carl Crook (born 10 November 1963 in Bolton) is an English amateur lightweight and professional light/light welterweight boxer of the 1980s and 1990s, who as an amateur was runner-up in the 1985 Amateur Boxing Association of England (ABAE) lightweight title, against Edmond McAuley (Hogarth ABC), boxing out of Chorley ABC, and as a professional won the British Boxing Board of Control (BBBofC) Central Area lightweight title, BBBofC British lightweight title, and Commonwealth lightweight title, and was a challenger for the EBU (European) lightweight title against Antonio Renzo, and Jean Baptiste Mendy, his professional fighting weight varied from 132 lb , i.e. lightweight to 137 lb , i.e. light welterweight.

Anthony Crolla: Anthony Crolla (born 16 November 1986) is a British professional boxer.  He held the WBA lightweight title from 2015 to 2016, and the British lightweight title from 2011 to 2012.

William Irwin (boxer): William "Billy" 'The Kid' Irwin ( (1968--) 20 1968 (age (2017)-(1968)-((11)<(05)or(11)==(05)and(29)<(20)) ) ) born Niagara Falls, Ontario, is a retired Canadian amateur lightweight and professional light/light welter/welterweight boxer of the 1990s and 2000s who as an amateur won a bronze medal in the Boxing at the 1991 Pan American Games in Havana, Cuba, losing to eventual silver medal winner Patrice Brooks of the United States, represented Canada at the 1991 World Amateur Boxing Championships in Sydney, Australia losing to Julien Lorcy of France, and represented Canada at the 1992 Summer Olympics in Barcelona, Spain, he was stopped in the second round of the lightweight division (– 60 kg) by Ronald Chavez of the Philippines, and as a professional won the Canadian Professional Boxing Council (CPBC) lightweight title, Canada lightweight title, International Boxing Organization (IBO) lightweight title, World Boxing Council (WBC) Continental Americas lightweight title, and Commonwealth lightweight title, and was a challenger for the International Boxing Federation (IBF) lightweight title against Paul Spadafora, and World Boxing Association (WBA) World lightweight title against Juan Díaz, his professional fighting weight varied from 133+1/2 lb , i.e. lightweight to 142 lb , i.e. welterweight.  He retired from boxing after losing to Juan Diaz in 2005, his second unsuccessful world title challenge.  His final record was 42(30)–6–0.

Gavin Rees: Gavin Rees (born 10 May 1980) is a Welsh former professional boxer who competed from 1998 to 2014.  He held the WBA super-lightweight title, as well as the European and British lightweight titles.

Terry Flanagan (boxer): Terry Flanagan (born 11 June 1989) is a British professional boxer.  He has held the WBO lightweight title since 2015, becoming the first Englishman to win a world title at lightweight.  He also held the British lightweight title in 2014, and won the Prizefighter tournament in 2012.  As of May 2017, he is ranked as the world's third best lightweight by the Transnational Boxing Rankings Board and "The Ring" magazine, and fourth by BoxRec.

Al Foreman: Al Foreman (3 November 1904 in London – 23 December 1954), was a British-born boxer of the 1910s, 1920s and 1930s who in the last four years of his career won the Canadian lightweight title, British Boxing Board of Control (BBBofC) British lightweight title, and British Empire lightweight title.  He unsuccessfully contended for the Canadian Featherweight title against Leo Roy in Montreal on May 8, 1924.  He first took the Canadian Lightweight title against Leo "Kid" Roy in 1928, and took the BBBofC British Lightweight Title on February 21, 1930, in a first-round knockout of reigning champion Fred Webster in the Whitechapel District of London.  He was an amazingly durable fighter having few if any knockouts counted against him in his career, yet knocking out an exceptionally high percentage of his opponents.

Bobby Vanzie: Bobby "Viper" Vanzie ( (1975--) 15 1975 (age (2017)-(1975)-((11)<(08)or(11)==(08)and(30)<(15)) ) ) born in Bradford is an English professional light/light welter/welterweight boxer of the 1990s and 2000s, who won the British Boxing Board of Control (BBBofC) Central Area lightweight title, BBBofC British lightweight title, and Commonwealth lightweight title, and was a challenger for the World Boxing Organization (WBO) Inter-Continental lightweight title against Yuri Ramanau, and BBBofC British lightweight title against Graham Earl, his professional fighting weight varied from 133 lb , i.e. lightweight to 144 lb , i.e. welterweight.

John Murray (boxer): John Murray (born 20 December 1984) is a British former professional boxer who competed from 2003 to 2014.  He held the English lightweight title from 2007 to 2008; the British lightweight title twice, from 2008 to 2010; and the European lightweight title from 2010 to 2011.  He also challenged once for the vacant WBA lightweight title in 2011.  John is the brother of British former Olympian Joe Murray.  Since retiring, Murray has opened his own gym – Murray Machines Gymnasium – in Reddish, where he trains both amateur and professional boxers.

Frank Johnson (boxer): Frank "Golden Boy" Johnson (27 November 1928 — 7 June 1970 (aged 41)) born in Manchester was an English professional feather/light/welter/middleweight boxer of the 1940s, and 1950s who won the British Boxing Board of Control (BBBofC) Central Area lightweight title, BBBofC British lightweight title, and British Empire lightweight title, and was a challenger for the British Empire lightweight title against Pat Ford, and BBBofC British welterweight title against Peter Waterman his professional fighting weight varied from 124 lb , i.e. featherweight to 149 lb , i.e. middleweight.  Frank Johnson was trained and managed by Jack Bates, and promoted by Jack Solomons.

John Watson (boxer): John Watson (Born 9 June 1983) is a British lightweight boxer, based in Liverpool, Merseyside, United Kingdom.  He has fought for the British lightweight title on two occasions, losing to Gavin Rees and Anthony Crolla.

Question: When was this British professional boxer born who, besides Gavin Rees, beat John Watson for the British lightweight title?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "boxer_name": {
      "type": "string",
      "description": "The name of the boxer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the boxer."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the boxer in 'DD Month YYYY' format."
    },
    "title_won": {
      "type": "string",
      "description": "The specific title won by the boxer against John Watson."
    },
    "opponent_beaten": {
      "type": "string",
      "description": "The name of the opponent who was beaten for the title."
    }
  },
  "required": [
    "boxer_name",
    "nationality",
    "birth_date",
    "title_won",
    "opponent_beaten"
  ],
  "additionalProperties": false
}

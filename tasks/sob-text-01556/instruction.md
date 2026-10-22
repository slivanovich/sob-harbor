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
Red Star Belgrade: Fudbalski klub Crvena zvezda (, ), commonly known in English as Red Star Belgrade (Serbian: Црвена звезда Београд / Crvena zvezda Beograd ) or simply Red Star, is a Serbian professional football club based in Belgrade, the major part of the Red Star multi-sport club.  They are the only Serbian and ex-Yugoslav club to have won the European Cup, having done so in 1991, and the only team from Southeast Europe to have won the Intercontinental Cup, also in 1991.  With 27 national championships and 24 national cups between Serbian and the former Yugoslav competitions, Red Star was the most successful club in former Yugoslavia and finished as first in the Yugoslav First League all-time table, and is the most successful club in Serbia.  However, since the 1991–92 season, Red Star has failed to qualify in the group stages of UEFA Champions League.

Dušan Veškovac: Dušan Veškovac (Serbian Cyrillic: Душан Вешковац; born 16 March 1986) is a Serbian professional footballer who plays as a defender for Napredak Kruševac.

OFK Beograd: Omladinski fudbalski klub Beograd (, English: "Belgrade Youth Football Club") is a Serbian professional football club based in Belgrade, more precisely from the Karaburma urban neighborhood.  It is currently the oldest club in the Serbian first league and is part of the OSD Beograd sport society.

Dušan Brković: Dušan Brković (Serbian Cyrillic: Душан Брковић; born 20 January 1989) is a Serbian professional footballer who plays as a defender for Hungarian club Debrecen.

Football in Serbia: Football is the most popular sport in Serbia.  The Football Association of Serbia ("FSS") is the national governing body and is responsible for overseeing all aspects of the game of football in the country, both professional and amateur.  The association organizes the professional Serbian Superliga (top tier) and is responsible for appointing the management of the men's, women's and youth national football teams in Serbia.  The association also organizes the Serbian First League (second) and Serbian League (third), operating the top 3 leagues.  The FSS is also responsible for organizing the Serbian Cup, the country's league cup competition.  It has been played from the end of the 19th century and there were a number of very successful Serbian football players and coaches throughout history.  One of Serbia's top football clubs Red Star Belgrade has won the prestigious European Champions Cup in 1991 and has also won the Intercontinental Cup the same year.  Its local rival Partizan Belgrade was the first Southeast and Eastern European football club to reach the European Champions Cup final, when it did so in 1966.  The most successful and popular teams are Red Star and Partizan from Belgrade as well as Vojvodina from Novi Sad.  An important role also played OFK Belgrade and Radnički Niš in the history of the Serbian football

FK Obilić: Fudbalski klub Obilić Beograd (Serbian Cyrillic: Фудбалски клуб Обилић Београд), commonly known as Obilić Belgrade or simply Obilić, is a Serbian football club based in Vračar, a neighbourhood of Belgrade.  Named after medieval Serbian hero Miloš Obilić, a legendary 14th-century knight, the club currently competes in the Third Belgrade league - Group A (three divisions lower than the Belgrade Zone League).

FK Vojvodina: Fudbalski klub Vojvodina (), commonly known as Vojvodina Novi Sad (; ) or simply Vojvodina and familiarly as Voša (), is a Serbian professional football club based in Novi Sad, Vojvodina, the second largest city in Serbia, and one of the most popular clubs in the country.  The club is the major part of the Vojvodina multi-sport club and currently the third oldest football club in the Serbian SuperLiga and the most successful football club in Serbia next to the rivals Red Star Belgrade and Partizan Belgrade.

Dušan Cvetinović: Dušan Cvetinović (Serbian Cyrillic: Душан Цветиновић; born 24 December 1988) is a Serbian professional footballer who plays as a defender for French club RC Lens.

Dušan Tadić: Dušan Tadić (Serbian Cyrillic: Душан Тадић; born 20 November 1988) is a Serbian professional footballer who plays for English club Southampton and the Serbia national team.  He is primarily a left-sided midfielder.

Dušan Anđelković: Dušan Anđelković (Serbian Cyrillic: Душан Анђелковић; born 15 June 1982) is a Serbian professional footballer who plays as a defender for Red Star Belgrade.

Question: Dušan Anđelković is a Serbian professional footballer who plays as a defender for what football club based in Belgrade

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the professional footballer."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the professional footballer."
    },
    "player_position": {
      "type": "string",
      "description": "The playing position of the professional footballer."
    },
    "club_name": {
      "type": "string",
      "description": "The name of the football club the player plays for."
    },
    "club_location": {
      "type": "string",
      "description": "The city where the football club is based."
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_position",
    "club_name",
    "club_location"
  ],
  "additionalProperties": false
}

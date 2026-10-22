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
Salman Iqbal: Salman Iqbal (Urdu: ‎ ) is a Pakistani media mogul.  He became the CEO of ARY Digital Network in 2014 after the death of Abdul Razzak Yaqoob.  In addition, Iqbal is the owner of the ARY Group, that was started by his Uncle Abdul Razzak Yaqoob and publisher of the Newsweek Middle East.

Aamer Iqbal (cricketer, born 1973): Iqbal Ahmed Aamer (born 2 June 1973 in Karachi; generally known as Aamer Iqbal) is a Pakistani former first-class cricketer active 1991–2007 who played mainly for Karachi Blues.  He represented his country at under-19 level.  Aamer Iqbal was a right-handed batsman and a wicket-keeper.  He scored 2,869 career runs with a highest score of 129, one of two centuries.  He held 155 catches in his 71 first-class appearances and completed ten stumpings.

ARY Musik: ARY Musik (Urdu: ‎ ) (formerly "The Musik") is a Pakistani Urdu-English music channel, first launched in 2003 from Dubai by Salman Iqbal.  This channel is a part of ARY Digital Network.  It features music genres including pop, rock, bhangra, classical, and folk.  It also airs interactive shows, celebrity interviews, comic fillers, theme shows, imaginative animations and live concerts.The channel's longest-running international music based show was "Music Hour with Wiqar Ali Khan", hosted in English and Pashtu.  ARY Musik is one of the first satellite channels to have live link-ups between its studios based in London, UK, USA, Pakistan, India, Bangladesh, Sri Lanka, Afghanistan and Dubai.

Jawani Phir Nahi Ani: Jawani Phir Nahi Ani is a 2015 Pakistani adventure and comedy film directed by Nadeem Beyg.  It was co-produced by Humayun Saeed, Salman Iqbal and Shahzad Nasib at Saeed's production house, Six Sigma Plus.  The film stars Humayun Saeed, Hamza Ali Abbasi, Ahmad Ali Butt, Vasay Chaudhry, Mehwish Hayat and Sohai Ali Abro.  The supporting cast includes Javed Sheikh, Ismail Tara, Bushra Ansari, Ayesha Khan, Sarwat Gillani and Uzma Khan.  The film is about a single man who is a divorce lawyer.  He takes his three married friends on a trip to help them escape their wives.

Karachi Kings in 2016: The Karachi Kings is a franchise cricket team that represents Karachi in the Pakistan Super League.  They are one of the five teams that had a competition in the 2016 Pakistan Super League.  The team was captained by Shoaib Malik and then by Ravi Bopara, and they stand on fourth position after winning just two matches from their eight matches in the PSL 2016.

National Stadium, Karachi: The National Stadium (Urdu: نیشنل اسٹڈیم‎ ) is a cricket stadium in Karachi, Pakistan.  It is currently used for cricket matches, it is the home ground of Karachi Kings, Pakistan Super League second expensive team and is home to many other Karachi's domestic cricket teams.  The stadium is able to hold 34,228 spectators, Its widely criticised that the city of this size with a population of over 15 million having such a small capacity stadium.  In the recent past, PCB has announced on different occasions that the capacity of the stadium will be increased to 90,000 but this approval looks a bit stale at the moment.

1st ARY Film Awards: The 1st ARY Film Awards or AFA'14 ceremony, presented by ARY Digital Network and Entertainment Channel, sponsored by Nokia, powered by ZONG and L'Oréal and took place on April 27, 2014 at the Golf Club, DHA Phase VIII, Karachi.  The ceremony was held recorded and televised on May 24, 2014.  During the ceremony ARY Digital Network and Entertainment Channel presented ARY Film Awards (commonly referred to as AFA's) in 29 categories and 4 special awards honoring the actors, technical achievements and films of 2013.  The ceremony, televised in Pakistan by ARY Digital and was produced by ARY Digital Network chairman Salman Iqbal.  ARY Film Awards became the most expensive event held in Pakistan.

Karachi Kings: Karachi Kings (Urdu: ‎ ; Sindhi: ڪراچي ڪنگز‎ ) is a Pakistani professional Twenty20 cricket team that competes in the Pakistan Super League.  The team is based in Karachi, the provincial capital of Sindh, Pakistan.  The team was formed in 2015, as a result of the formation of the Pakistan Super League by Pakistan Cricket Board (PCB). Team's home ground is National Stadium. The team is currently captained by Kumar Sangakkara and coached by Mickey Arthur a former South African cricketer.  It is owned by Salman Iqbal, the CEO of ARY Group.

Hassan Rana: Hassan Rana (born Hassan Waqas Rana), also known as Doc, is a Pakistani film director, producer and screenwriter.  He is best known for his debut production "Waar", for which he won 3 awards at 1st ARY Film Awards.  On 7 December 2013 Hassan Waqas Rana signed an MoU (Memorandum of Understanding) with Salman Iqbal (founder and president ARY), for the production of two action thrillers, Yalghaar & "Waar 2" to be produced and released in 2017-19.  "Yalghaar was released across Pakistan on the 28th of June 2017, and was well receieved by the audiences.  He has to his credit the production of the highest grossing Films in the hsitory of Pakistan by setting the record with "Waar" in 2013, and later breaking his own record with "Yalghaar" in 2017.  He is founder of MindWorks Media.

Dobara Phir Se: Dobara Phir Se is a 2016 Pakistani romantic drama film directed by Mehreen Jabbar and a production of ARY Films.  The film is produced by Salman Iqbal and co-produced by Mohammad Jerjees Seja.  The film stars Ali Kazmi, Hareem Farooq, Adeel Hussain, Tooba Siddiqui, Sanam Saeed, Atiqa Odho, Shaz Khan, and child actor, Musa Khan.  The film was released on 25 November 2016.

Question: Who is the coach of the Karachi kings, owned by Salman Iqbal?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The name of the cricket team."
    },
    "owner_name": {
      "type": "string",
      "description": "The name of the owner of the team."
    },
    "coach": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the team's coach."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the coach."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "team_name",
    "owner_name",
    "coach"
  ],
  "additionalProperties": false
}

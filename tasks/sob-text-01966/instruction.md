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
Eight Mile Style v New Zealand National Party: A controversy was caused in New Zealand in 2014 when the National Party allegedly used the song "Lose Yourself" by the American rapper Eminem in a campaign advertisement during that year's election.

Comeback Kid (song): "Comeback Kid" is a song written and performed by noise pop duo Sleigh Bells, issued as the official lead single for their second album "Reign of Terror" (following the promotional single “Born to Lose”).  The song was released January 17, 2012.  On February 18, the band performed the song on "Saturday Night Live".

Not Tonight: "Not Tonight" is a song performed by American rap artist Lil' Kim, featuring Jermaine Dupri, for her debut studio album "Hard Core" (1996).  A remix was conducted the next year, featuring Lil' Kim with other female rappers including Da Brat, Missy "Misdeameanor" Elliott, Angie Martinez, and Lisa "Left Eye" Lopes from the "Nothing to Lose" soundtrack.  The song became a hit in the U.S., peaking at number 6 on the "Billboard" Hot 100, and became Lil' Kim's third consecutive number 1 hit on the Rap Songs chart, becoming the first female rapper to do so.  The single was certified platinum by the RIAA.

Eminem: Marshall Bruce Mathers III (born October 17, 1972), known professionally as Eminem (often stylized as EMINƎM), is an American rapper, record producer, and actor.

Josh Holliday: Josh Holliday (born September 14, 1976) is an American college baseball coach and former professional player in Minor League Baseball.  Currently the head coach of the Oklahoma State Cowboys baseball team, he was hired to this position prior to the 2013 season.  In 2014, Holliday was the Big 12 Conference Baseball Coach of the Year as OSU claimed the conference regular season championship.  Hollidays' Cowboys pulled OSU a little Cowboy baseball tradition out of the fire and faced Oklahoma on the final weekend of 2017.  The team was in danger of missing out of the postseason for the 1st time in Hollidays tenure at Oklahoma State.  The Cowboys swept the instate rival Oklahoma Sooners (#2 seed going into region play) to claim the last and final spot as the 8th seed in the BigXII Championship.  The Cowboys went back to their traditionion and won just the 2nd Big 12 tournament in schools rich baseball history.  The Cowboys won 16 straight Big 8 tournaments before the formation of the Big12.  The Cowboys became the 1st eight seed (last seed) to win the conference championship and by doing so Holliday got his team in the NCAA postseason for the 5th time in his 5 years at the school.  The season was full of injuries from top to bottom Holliday and is associated Head Coach and current (2016) assistant coach of the year Rob Walton put together a pitching staff that was nothing short of magical.  The Cowboys luck would run out as the were sent to the Arkansas Regional and went 0-2 losing game one to Regional champions Missouri State Bears on a two out bottom of the 9th walk off HR.  Garrett Benge hit for the cycle for Hollidays Cowboys but it wasn't enough.  Garrett McCain would be named 1st team all-American the 25th in Cowboys history he would one of five current Cowboys drafted in 2017 preceded by 11 from the 2016 College World Series club.  Giving Holliday 16 in 2 years.  The Cowboys went on the end of the year run the had seen them lose six games in a row and face being the 1st Oklahoma State team to finish under .500 in 40 years.The Cowboys finished 30-27 on the year.  The 6-5 victory of the Texas Longhorns would be Hollidays' 200th victory as the head man of Oklahoma State.

Luis Resto (musician): Luis Edgardo Resto (born July 22, 1961) is an American musician, producer and keyboardist who has worked closely with rapper Eminem since his third major-label album "The Eminem Show".  He is of Puerto Rican descent, with both of his parents from Puerto Rico, and was raised in Detroit (Garden City), Michigan.  His career in recorded music began in the early 1980s in Detroit, with Michael Henderson and Was (Not Was).  He continued playing keyboards and co-writing songs for a wide variety of artists (including many produced by Don Was), ranging from Anita Baker to Patti Smith to The Highwaymen to Vertical Horizon to Fuel, before beginning a prolific and lengthy collaboration with Eminem in 2001.  He has played the keyboard for several Eminem-produced tracks and is credited for additional production on most Eminem-produced tracks on "Encore".  Resto released his own solo LP titled "Combo De Momento", and was released under his own imprint Resto World Music on May 18, 2010.  He co-wrote the Oscar-winning song, "Lose Yourself", featured in the movie "8 Mile" with Jeff Bass and Eminem.

Tru Collins: Tru Collins is an American actress and indie-pop singer.  She is known for her role of Julie on MTV's original high school comedy, Awkward.  Tru was born in Richmond, Virginia to five-time Emmy Award winning television journalist Reid Collins and choreographer Lindy Fisher.  She attended Manhattan's Professional Performing Arts School at 15 while studying classical piano and training with Elaine Kudo of American Ballet Theatre.  Collins began college with a songwriting scholarship from Universal and studied at New York University and The New School in New York City.  In 2014, she guest starred on Showtime's period drama Masters of Sex opposite Michael Sheen and had a supporting role in Spring Awakening, an indie film set in the late 1800s.  Tru has recurred as mean girl Julie on MTV's Awkward seasons 2 - 5.  As a singer, she performed with Grammy-winning soul singer Latrice Varrett, opening for Aretha Franklin at the Nokia Theatre Times Square in 2009.  In 2010, she joined Atlantic Records' multi-platinum progressive rock band Trans-Siberian Orchestra as a vocalist, touring arenas across North America and promoting the band performing acoustic guitar/vocal solos live on numerous rock radio stations.  That year, TSO reached #12 on the Billboard charts for American Arena Tours, beating Taylor Swift and Justin Bieber.  The tour grossed $47,395,108 and sold out 51 arenas.  She has co-written songs with Rostrum Records artist Vali and Three 6 Mafia's Juicy J, and her work has been featured on various recordings and television soundtracks.  In 2012, Collins performed with DJ Ravi Drums, Kitara player Craig Dobbin, and rapper Wes Period at the Air Canada Centre Arena in Toronto.  In 2015, Tru joined Steven Seagal's blues band Thunderbox for a European tour and performed with ten-time Grammy Award winner George Benson at the Cognac Blues Passion Festival in Cognac, France.  Her debut solo EP, "Story of A Gypsy Child", from producer Jonny on the Rocks of Brooklyn bands Shinobi Ninja and Rocky Business, is set for 2015 release.  Her music video for the first single, "Party Dress", was released via YouTube in February 2015.

Just Lose It: "Just Lose It" is a song by American rapper Eminem from his fifth studio album "Encore" (2004).  It was released as the lead single from "Encore", and was later included on his greatest hits compilation album "" (2005).  The song caused controversy as its lyrics and music video parodies Michael Jackson, who was being accused of child molestation at the time.  The song also pokes fun at Beavis/Cornholio, MC Hammer, Madonna, and others.  It also heavily spoofs Pee-wee Herman, going as far as imitating his signature shout during the chorus and Eminem dressing like him in the video.

Back to the Crib: "Back to the Crib" was the second single by American rapper Juelz Santana for his third album "Born to Lose, Built to Win".  It features American singer-songwriter Chris Brown in their second collaboration since Chris Brown's "Run It! " in 2005.  The song was produced by Polow Da Don.

Juelz Santana: LaRon Louis James (born February 18, 1982), better known by his stage name Juelz Santana, is an American rapper and actor.  He is from the Harlem neighborhood in New York City, and is a member of East Coast hip hop group The Diplomats.  He appeared on Cam'ron's 2002 singles, "Oh Boy" and "Hey Ma".  In 2003, his debut album "From Me to U" was released by Roc-A-Fella Records; his next album "What the Game's Been Missing! " contained the top-ten single "There It Go (The Whistle Song)".  He is currently working on his third studio album "Born to Lose, Built to Win".

Question: In what year was the rapper who performed "Just Lose It" born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song in question."
    },
    "performing_artist": {
      "type": "string",
      "description": "The name of the artist who performed the song."
    },
    "artist_birth_year": {
      "type": "integer",
      "description": "The birth year of the performing artist."
    }
  },
  "required": [
    "song_title",
    "performing_artist",
    "artist_birth_year"
  ],
  "additionalProperties": false
}

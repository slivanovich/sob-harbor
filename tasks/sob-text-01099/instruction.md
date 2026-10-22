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
I Know (Luther Vandross album): I Know is the eleventh studio album (sixteenth overall) by American R&B/soul singer Luther Vandross, released in August 1998 (see 1998 in music), and his only one for Virgin Records (after leaving his longtime home label Epic Records the previous year; three years later, he would sign with Clive Davis' then-new J Records, where he recorded his final two albums).  It was nominated for a Grammy Award for Best Traditional R&B Vocal Performance and the song "I Know" was nominated for a Grammy Award for Best Male R&B Vocal Performance in 1999.  In early 2005 (four months before his death), Dutch EMI affiliate Disky Records reissued the album in Europe with a different order of tracks as part of the budget series "The Ultra Selection".  It features a cover of "When I Need You", originally recorded by Leo Sayer.  Guest artists on this album include Stevie Wonder (who played harmonica on the title track), Cassandra Wilson (who performed the female vocals on "I'm Only Human", which originally appeared on the soundtrack to the film "Down in the Delta", which was also released in 1998), the rappers Precise and Guru (who performed on the original and remixed versions of "Nights in Harlem", respectively, with the former's vocals also appearing on "Get It Right") and Brandy (a future Epic signee whose background vocals appear on the remixed version of "Nights in Harlem", though uncredited).

Prashant Naik: Prashant Naik (born 2 September 1986, full name Prashant Tukuram Naik) is an Indian cricketer who plays for Mumbai.  He was born in Pune, Maharashtra.  He was brought by Delhi Daredevils for the 2011 and the 2012 Indian Premier League.  Prashant was selected for India Under 19 in the year 2005. He is natural attacking batsman and brilliant fielder.  He started playing cricket in Pune under coach Anna Nevrekar From SSPMS day school.  He Shifted to Mumbai in the 9th grade to further develop his cricket.  He has missed out many big events due to injuries.

Rahul Ranade: Rahul Ranade (born 23 May 1966 in Pune, Maharashtra) is an Indian singer and music composer in Marathi and Hindi movies.  His work in music spans from composing music for films, television, drama to events, concerts in Hindi and Marathi, composing music for ballets, advertisements, and also albums.  He is currently settled at Pune.

Washington Sundar: Washington Sundar (born 5 October 1999) is an Indian cricketer.  He is a left-handed batsman and right-arm off-spinner.  He has played for the India national under-19 cricket team as a Batsman.  He made his first-class debut for Tamil Nadu in the 2016–17 Ranji Trophy on 6 October 2016.  In 2017 he was selected by Rising Pune Supergiant as a replacement for Ravichandran Ashwin.  He made his Twenty20 debut for Rising Pune Supergiants in the 2017 Indian Premier League on 22 April 2017.  He was man of the match in IPL 2017 played between Mumbai Indians and Pune Supergiants, in which he took 3 wickets for 16 runs.  He holds the record for the best bowling figures in an IPL final 2017.

Abhay Jodhpurkar: Abhay Jodhpurkar is an Indian singer born in Madhya Pradesh on July 31.  He is best known for his song "Moongil Thottam", a duet with Harini for the Tamil film "Kadal" and "E Sanje Eke Jaruthide" for the Kannada Film "RangiTaranga".

Jaspal Singh (singer): Jaspal Singh is an Indian singer who lent his voice to various Bollywood Actors of 1970's and 1980's.  He was born in Amritsar and during his school and colleges days, he used to sing in various singing competitions.  To further pursue his passion for singing he went to Mumbai where his sister used to stay.  His talent was first and foremost recognised by well known female singer Usha Khanna during 1968.  He was provided a chance to sing at a Professional level, however he did not get the recognition which he deserved.  He struggled to make a career in singing and would often visit Amritsar, Delhi and Mumbai time and again.  Due to pressure from his father he started practising law and started living in Mumbai.  In spite of the hardships he never gave up.  And then, a well known Music Composer, Ravindra Jain gave him the big break for a song in the movie called 'Geet Gata Chal' of 1975.  After this song, he became a household name.  His voice was unique and was unlike any other and he sang for hit movies like 'Nadiya ke paar', Ankhiyon ke jharokhon se','Sawan ko aane do' amongst others.

Hamsika Iyer: Hamsika Iyer is an Indian singer based in Mumbai—born in Pune and brought up in Mumbai.  She studied at the SIES college of Arts and Science in Sion.  She is a regular voice with ad world jingles, Marathi tele-serials, and has sung songs in Kannada, Tamil, Hindi, Malayalam and Bengali movies.

Chammak Challo: "Chammak Challo" is a song composed by music director duo Vishal-Shekhar and Gobind Singh as a part of the soundtrack for the 2011 Bollywood film "Ra.One".  The female vocals were provided by Hamsika Iyer while male vocals were provided by Akon.  It is his first musical collaboration with Indian artists.  There are four other versions of the song in the album, including a remix by Abhijit Vaghani, another remix by DJ Khushi and an international version sung solely by Akon.  The song, along with the rest of the soundtrack, was officially released on 12 September 2011.  However, the song faced controversy when the rough version was leaked on the Internet on 31 May 2011.

Jai Ho (song): "Jai Ho" is a song composed by A. R. Rahman for the 2008 film, "Slumdog Millionaire".  When Danny Boyle, the director of "Slumdog Millionaire", approached Rahman to compose its soundtrack, he included the song.  "Jai Ho" accompanies a choreographed dance sequence at the end credits of "Slumdog Millionaire".  The song features vocals from Sukhvinder Singh, Mahalaxmi Iyer and Vijay Prakash in Hindi, Urdu and Punjabi.  Indian singer Tanvi Shah wrote and provided vocals for a Spanish section of the song.  "Jai Ho" is a Hindi phrase which can be roughly translated as "Let [the] victory prevail", "Let there be victory", or "May there always be victory".

Kaushal Inamdar: Kaushal S. Inamdar (born 2 October 1971 in Pune, Maharashtra) is an Indian singer and music composer in Marathi and Hindi movies.  His work in music spans from composing music for films, television, drama to events, concerts in Hindi and Marathi, composing music for ballets, advertisements, and also albums.  He is currently settled at Goregaon, a Mumbai suburb.

Question: Which movie's soundtrack has a song in which female vocals were provided by an Indian singer born in Pune and brought up in Mumbai?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie whose soundtrack contains the specified song."
    },
    "soundtrack_song_title": {
      "type": "string",
      "description": "The title of the song on the movie's soundtrack."
    },
    "female_vocalist": {
      "type": "object",
      "properties": {
        "singer_name": {
          "type": "string",
          "description": "The name of the Indian singer who provided female vocals."
        },
        "birth_city": {
          "type": "string",
          "description": "The city where the singer was born."
        },
        "upbringing_city": {
          "type": "string",
          "description": "The city where the singer was brought up."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the singer."
        }
      },
      "required": [
        "singer_name",
        "birth_city",
        "upbringing_city",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "movie_title",
    "soundtrack_song_title",
    "female_vocalist"
  ],
  "additionalProperties": false
}

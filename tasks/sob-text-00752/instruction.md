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
Guinness World Records – Ab India Todega: Guinness World Records – Ab India Todega (English: "Guinness World Records – Now India will Break") is a reality TV show based on the Guinness Book of World Records.  The show, which was hosted by Preity Zinta and Shabbir Ahluwalia, premiered on 18 March 2011 to an audience measurement of 3.3 rating points.  Each episode presents different individuals trying to break official world records.

Dave Farrow: David Andrew Farrow (born January 10, 1975) is a two-time Canadian Guinness World Record Holder for Most Decks of Playing Cards Memorized in a Single Sighting, entrepreneur, memory coach, speed reader and keynote speaker.  He is best known for winning the Guinness World Records for Most Decks of Playing Cards Memorized in a Single Sighting in 1996 and again in 2007 when he set out to reclaim his record after it was beaten in 2002.  The initial record was set at the Guinness World Records museum in Niagara Falls, Ontario, Canada while the latter was performed for Discovery Channel Canada at CTV Television Network studios.  Both records were accomplished under the controlled supervision of multiple cameras and multiple independent witnesses.

One Dance: "One Dance" is a song by Canadian rapper Drake from his fourth studio album, "Views" (2016).  It features guest vocals from Nigerian Afrobeat artist Wizkid and British singer Kyla.  The artists co-wrote the dancehall and afrobeat song with its co-producers Nineteen85, DJ Maphorisa, and Noah "40" Shebib, with production assistance from Wizkid.  Crazy Cousinz and Kyla also received songwriting credits for the sampling of their 2008 UK funky song "Do You Mind".

Wizkid (musician): Ayodeji Ibrahim Balogun (born 16 July 1990), better known by his stage name Wizkid (sometimes stylised as WizKid), is a Nigerian singer and songwriter who became the first Afro Pop artist to feature in "Guinness World Records" for his contribution on the hit song "One Dance".  He started recording music at age 11 and managed to release a collaborative album with the Glorious Five, a group he and a couple of his church friends formed.  In 2009, he signed a record deal with Banky W.'s record label Empire Mates Entertainment (E.M.E).  He rose to prominence in 2010 with the release of the song "Holla at Your Boy" from his debut studio album, "Superstar" (2011). " Tease Me/Bad Guys", "Don't Dull", "Love My Baby", "Pakurumo" and "Oluwa Lo Ni" were also released as singles from the "Superstar" album.  Wizkid's self-titled second studio album, "Ayo", was released in September 2014 and was preceded by six singles: "Jaiye Jaiye", "On Top Your Matter", "One Question", "Joy", "Bombay" and "Show You the Money".

Twin Galaxies: Twin Galaxies is an American organization that tracks "retro" and "old-school" video game world records and conducts a program of electronic-gaming promotions.  It operates the Twin Galaxies website and publishes the "Twin Galaxies' Official Video Game & Pinball Book of World Records", with the Arcade Volume released on June 2, 2007.  "The Guinness World Records - Gamers Edition 2008" was released in March, 2008 in conjunction with Twin Galaxies, who Guinness World Records considers to be the official supplier of verified world records to the annual volume.

George Hood (athlete): George E. Hood is an ultra athlete, certified personal trainer (NESTA) and a Group-X instructor.  Hood also owns and operates a successful business known as Oceanside Paddleboard in Oceanside, CA.www.OceansidePaddleboard.com.  George holds 7 world records.  He has set a total of 6 Guinness World Records and one independent world record for the plank set in Beijing, China in June, 2014 which was certified in the media and by the Assist World Records organization in India.http://www.china.org.cn/wap/2014-06/24/content_32752425.htm George previously held the Guinness World Record for the prone hold, or plank at 3 hours, 7 minutes, and 15 seconds set on 20 April 2013. http://www.thepostgame.com/blog/eye-performance/201304/george-hood-sets-planking-record-again

Guinness World Records Gone Wild: Guinness World Records Gone Wild, also known as "Guinness World Records Unleashed", is an American reality television series on truTV.  The series debuted on February 7, 2013 and is hosted by Dan Cortese.  The series' first season averaged more than 1.3 million viewers and ranked as one of ad-supported cable's Top 3 programs in the Thursday 8 p.m. timeslot with key adult and male demos.  It was also cable's No.1 unscripted entertainment program in the timeslot with men 18-49 and adults 18-34.  It was announced in April 2013 that truTV has ordered an additional ten episodes.  Season 2 premiered on November 7, 2013, and features a title change to "Guinness World Records Unleashed".

List of best-selling singles: According to "Guinness World Records", "White Christmas" (1942) by Bing Crosby is the best-selling single worldwide, with estimated sales of over 50 million copies.  The song recognized as "the best-selling single of all time" was released before the pop/rock singles-chart era and "was listed as the world's best-selling single in the first-ever "Guinness Book of Records" (published in 1955) and—remarkably—still retains the title more than 50 years later."  "Guinness World Records" states that double A-side charity single "Candle in the Wind 1997"/"Something About the Way You Look Tonight" (1997) by Elton John, a tribute to the late Diana, Princess of Wales, is "the biggest-selling single since UK and US singles charts began in the 1950s, having accumulated worldwide sales of 33 million copies," making it the second-best-selling single of all time.

Ashrita Furman: Ashrita Furman (born Keith Furman, September 16, 1954, Brooklyn, New York) is a Guinness World Records record-breaker.  As of 2017, Furman has set more than 600 official Guinness Records and currently holds 200 records, including the record for holding the most Guinness world records.  He has been breaking records since 1979.

The Journey (Sean Tizzle album): The Journey is the first studio album by Nigerian Afro Pop artist Sean Tizzle.  It was released on April 17, 2014 on Difference Entertainment.  which was released in 2014.  The album features guest appearances from Olamide, Reminisce, 9ice, Ice Prince, Naeto C, Kcee and Tiwa Savage.  The album was supported by four official singles— "Mama Eh", "Komole", "Kilogbe" and "Kilogbe (Remix)" along with the promotional singles "Mama Eh".

Question: This singer became the first Afro Pop artist to feature in "Guinness World Records" for his contribution on a song by which Canadian rapper?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the Afro Pop artist who featured in Guinness World Records."
    },
    "record_achievement": {
      "type": "string",
      "description": "Description of the record achieved by the artist."
    },
    "song_details": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song for which the record was achieved."
        },
        "contributing_artist_type": {
          "type": "string",
          "description": "The type of the contributing artist (e.g., rapper)."
        },
        "contributing_artist_nationality": {
          "type": "string",
          "description": "The nationality of the contributing artist."
        },
        "contributing_artist_name": {
          "type": "string",
          "description": "The name of the contributing artist."
        }
      },
      "required": [
        "song_title",
        "contributing_artist_type",
        "contributing_artist_nationality",
        "contributing_artist_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "record_achievement",
    "song_details"
  ],
  "additionalProperties": false
}

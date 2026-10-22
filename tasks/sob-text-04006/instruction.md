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
Sylvain Cossette: Sylvain Cossette (born May 8, 1963) is a French-Canadian singer-songwriter from Grand-Mère, Quebec (located in the Mauricie region).  Sylvain was a founding member of the Quebec-based English language band Paradox in 1984, before becoming a French language solo artist by 1994.  During his career he has sold over one million albums (12 Gold and Platinum), recorded thirty-two #1 hit songs and eight Number 1 albums, earned six Silver, Gold and Platinum Tickets, won 10 Quebec Felix Music Awards, six Socan awards and four Juno nominations, and performed in Canada and Europe in the hit stage musicals "Notre Dame De Paris" and "Dracula".  Cossette's 2001 album "Rendez-vous" was certified Platinum by the CRIA in November 2002.  His 2007 album "70s" (#1 Quebec, #2 Canada) is his first all English release and produced four Number 1 hit singles and two Number 1 hit videos.  The album went Gold (50,000 CDs sold) in 27 days and Platinum (100,000 CDs sold) in 15 weeks.  The 70s concert tour went Silver Ticket (25,000 tickets sold) in three months and Gold Ticket (50,000 tickets sold) within a year.  On October 21, 2008, he released the album "70s Volume 2" and produced three Number 1 hit singles and one Number 1 hit video.  The album went Gold (50,000 CDs sold) in 19 days and Platinum (100,000 CDs sold) in 11 weeks.  On October 25, 2010, the album 70s Volume 3 was released and quickly went Gold.  The 70s project has so far sold almost 400,000 albums, 150,000 concert tickets and been seen by over a 650,000 people at outdoor festivals.  In September 2011 he launched his new one-year tour «The Best of the 70s».  In October 2011, two compilation albums were released of his greatest French language hits.  On October 1, 2012, he release his first original French language album in 12 years called "Le jour d'après" (4 number one hit songs) which he wrote, co-arranged and co-produced.  His next album RETROSPECTIVE spawned a tour throughout French Canada in 2013-2014.  In April 2014 he released an album "Les numérous 1" of his career #1 hit songs that he composed.  A new trilogy project (album/photobiography book/tour) called ACCORDS was released in October 2014 and spawned three Number 1 hit singles followed by a tour throughout French Canada in 2015.  In 2014-16 he was the creative force behind two children projects (albums and live shows): Lily et le Lutin & Pyjama Party.  In 2017 he released his first instrumental album Café et Guitares in over 200 countries.

Kenny Young: Kenny Young is an American songwriter, producer and environmentalist who has been an active writer, artist, and producer from 1963 to the present.  His most famous songs are "Under the Boardwalk," co-written with Arthur Resnick, "Ai No Corrida", "Just a Little Bit Better", "SSSingle Bed', "Captain of Your Ship", Just One More Night",and "Only You Can".  "Under the Boardwalk" was recorded by The Drifters in 1964 and also by The Rolling Stones, The Beach Boys, John Mellencamp, Ricky Lee Jones, The Undertones, Aaron Neville, Bette Midler and many other artists.  Young also wrote or produced Top 40 hit songs for Herman's Hermits, Quincy Jones, Ben E. King, Mark Lindsay, Reparata and the Delrons, Clodagh Rodgers, Kenny Rogers, The Shirelles, and Nancy Sinatra.

Save the Last Dance for Me (album): Save the Last Dance for Me was Ben E. King's 15th album and 14th studio album.  It was released under the EMI-Manhattan label.  The album was released in 1987 and was King's first release in six years.  All the tracks are new recordings of hits by King's old group The Drifters, originally recorded between 1959 and 1964.  Note that King did not originally sing lead on all the Drifters versions of these songs, having left the Drifters in 1960.

Ben E. King: Benjamin Earl King (born Benjamin Earl Nelson, September 28, 1938 – April 30, 2015), known as Ben E. King, was an American soul and R&B singer and record producer.  He was perhaps best known as the singer and co-composer of "Stand by Me"— a US Top 10 hit, both in 1961 and later in 1986 (when it was used as the theme to the film of the same name), a number one hit in the UK in 1987, and no. 25 on the RIAA's list of Songs of the Century—and as one of the principal lead singers of the R&B vocal group the Drifters notably singing the lead vocals of one of their biggest global hit singles (and only U.S. #1 hit) "Save the Last Dance for Me".

This Magic Moment: "This Magic Moment" is a song composed by lyricist Doc Pomus and pianist Mort Shuman, and is one of their best-known songs.  It was recorded first by Ben E. King and the Drifters.  The Drifters version spent 11 weeks on the "Billboard" Hot 100 and reached No. 16 on April 2, 1960.

The Very Best of Ben E. King: The Very Best Of Ben E. King is a Ben E. King compilation album covering his entire recording history dating to 1975.  Longtime classics such as Spanish Harlem and Don't Play That Song as well as King's most influential hit Stand By Me are all on this album, among 13 additional hits.

Please Stay (Burt Bacharach song): "Please Stay" (also known as "(Don't Go) Please Stay") is an early hit of The Drifters featuring the new lead singer Rudy Lewis, who replaced Ben E. King.  It is one of songwriter Burt Bacharach's early pop hits, featuring Dionne Warwick's sister Dee Dee Warwick and Doris Troy on background vocals.  This song, along with "Some Kind of Wonderful" and "Sweets for My Sweet", were recorded in the same session.  The musicians who backed the Drifters on this record include George Barnes and Allan Hanlon on guitar, Abie Baker on bass, Bobby Rosengarden and Ray Kessler on percussion and Ed Shaughnessy and Gary Chester on drums.

There Goes My Baby (The Drifters song): "There Goes My Baby" is a song written by Ben E. King (Benjamin Nelson), Lover Patterson, George Treadwell, Jerry Leiber, and Mike Stoller, and produced by Jerry Leiber and Mike Stoller for The Drifters.  This was the first single by the second incarnation of the Drifters (previously known as the 5 Crowns), who assumed the group name in 1958 after manager George Treadwell fired the remaining members of the original lineup.

Save the Last Dance for Me: "Save the Last Dance for Me" is the title of a popular song written by Doc Pomus and Mort Shuman, first recorded in 1960 by The Drifters, with Ben E. King on lead vocals.

Don't Play That Song (You Lied): "Don't Play That Song (You Lied)" is a song written by Ahmet Ertegün and by the wife of Ben E. King, Betty Nelson.  It was first recorded by soul singer Ben E. King.  The title track on King's third album "Don't Play That Song! ", it reached number 2 on the U.S. R&B singles chart and number 11 on the pop chart when released as a single on Atco Records in 1962.

Question: In what year was the Drifters' only U.S. #1 hit featuring Ben E. King as lead vocalist recorded?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "artist": {
      "type": "string",
      "description": "The artist who recorded the song."
    },
    "lead_vocalist": {
      "type": "string",
      "description": "The lead vocalist for the specified recording."
    },
    "recording_year": {
      "type": "integer",
      "description": "The year the song was first recorded."
    },
    "us_chart_peak": {
      "type": "string",
      "description": "The peak chart position in the U.S."
    }
  },
  "required": [
    "song_title",
    "artist",
    "lead_vocalist",
    "recording_year",
    "us_chart_peak"
  ],
  "additionalProperties": false
}

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
How Your Love Makes Me Feel: "How Your Love Makes Me Feel" is a song written by Trey Bruce and Max T. Barnes, and recorded by American country music group Diamond Rio that reached the top of the "Billboard" Hot Country Singles & Tracks chart.  It was released in May 1997 as the first single from their "Greatest Hits" album.  Having held the Number One position for three weeks in the United States, it is the band's longest-lasting Number One hit.  It became the band's second number one hit and their first since "Meet in the Middle" in 1991.  It also reached number one in Canada.

Jim Kerr discography: This is a discography of the Scottish musician Jim Kerr which includes one studio album and three hit singles.  Kerr rose to fame during the 1980s as frontman of the popular rock group Simple Minds, who achieved their number one hit single with "Ballad of the Streets EP" and also achieved five number one studio albums.  In 2010 Kerr embarked on a solo career and released his debut solo album "Lostboy!  AKA Jim Kerr" which spawned three singles "Shadowland", "Refugee" and "She Fell In Love With Silence".

She Ain't Worth It: "She Ain't Worth It" is a song recorded by Glenn Medeiros with a rap verse from singer Bobby Brown.  It hit number one for two weeks on the "Billboard" Hot 100 on July 21, 1990, becoming Medeiros' only number one hit in America and Brown's second and last number one hit after "My Prerogative".  The single also reached the Top 20 in the UK Singles Chart where Medeiros had previously reached number 1 with his hit "Nothing's Gonna Change My Love for You".

Untasted Honey: Untasted Honey is the fourth studio album by American country music artist Kathy Mattea.  It was released in 1987 on Mercury Records.  The album produced Mattea's first Number One hit on the "Billboard" country charts in its lead-off single "Goin' Gone".  Following this song was another Number One hit, "Eighteen Wheels and a Dozen Roses", then "Untold Stories" and "Life as We Knew It", both of which reached #4.  "The Battle Hymn of Love" was later released as a single from Mattea's 1990 album "A Collection of Hits".  Like "Walk the Way the Wind Blows" before it, this album includes a cut originally found on Nanci Griffith's 1986 album "The Last of the True Believers", this time in the track "Goin' Gone".  "Untasted Honey" was certified gold by the RIAA.

The Streets Made Me: The Streets Made Me is the second studio album by American rapper Soulja Slim, released on No Limit Records.  The album wasn't as successful as his previous album.It was his last release with No Limit Records.  Production from the album is from Donald XL Robertson.  It features guest appearances from Slay Sean & Traci among others., " Soulja Slim soon left to start his own label, Cut Throat Comitty.

Soulja Slim: James Adarryl Tapp Jr. (September 9, 1977 – November 26, 2003), better known by his stage name Soulja Slim, was an American rapper and songwriter.  He is known for writing the U.S. number one hit "Slow Motion".

Sylvain Cossette: Sylvain Cossette (born May 8, 1963) is a French-Canadian singer-songwriter from Grand-Mère, Quebec (located in the Mauricie region).  Sylvain was a founding member of the Quebec-based English language band Paradox in 1984, before becoming a French language solo artist by 1994.  During his career he has sold over one million albums (12 Gold and Platinum), recorded thirty-two #1 hit songs and eight Number 1 albums, earned six Silver, Gold and Platinum Tickets, won 10 Quebec Felix Music Awards, six Socan awards and four Juno nominations, and performed in Canada and Europe in the hit stage musicals "Notre Dame De Paris" and "Dracula".  Cossette's 2001 album "Rendez-vous" was certified Platinum by the CRIA in November 2002.  His 2007 album "70s" (#1 Quebec, #2 Canada) is his first all English release and produced four Number 1 hit singles and two Number 1 hit videos.  The album went Gold (50,000 CDs sold) in 27 days and Platinum (100,000 CDs sold) in 15 weeks.  The 70s concert tour went Silver Ticket (25,000 tickets sold) in three months and Gold Ticket (50,000 tickets sold) within a year.  On October 21, 2008, he released the album "70s Volume 2" and produced three Number 1 hit singles and one Number 1 hit video.  The album went Gold (50,000 CDs sold) in 19 days and Platinum (100,000 CDs sold) in 11 weeks.  On October 25, 2010, the album 70s Volume 3 was released and quickly went Gold.  The 70s project has so far sold almost 400,000 albums, 150,000 concert tickets and been seen by over a 650,000 people at outdoor festivals.  In September 2011 he launched his new one-year tour «The Best of the 70s».  In October 2011, two compilation albums were released of his greatest French language hits.  On October 1, 2012, he release his first original French language album in 12 years called "Le jour d'après" (4 number one hit songs) which he wrote, co-arranged and co-produced.  His next album RETROSPECTIVE spawned a tour throughout French Canada in 2013-2014.  In April 2014 he released an album "Les numérous 1" of his career #1 hit songs that he composed.  A new trilogy project (album/photobiography book/tour) called ACCORDS was released in October 2014 and spawned three Number 1 hit singles followed by a tour throughout French Canada in 2015.  In 2014-16 he was the creative force behind two children projects (albums and live shows): Lily et le Lutin & Pyjama Party.  In 2017 he released his first instrumental album Café et Guitares in over 200 countries.

One of a Kind (G-Dragon song): "One of a Kind" is a song by South Korean rapper G-Dragon.  Released on August 24, 2012 through YG Entertainment, it served as the lead single from the extended play of the same name.  Written solely by G-Dragon, the rapper also worked with long-time collaborator Choice37 to produce the music.  The song was well received by music critics, that considered it one of his best work and one of the most influential Korean hip hop tracks.  "One of a Kind" peaked at number nine on the Gaon Music Chart in South Korea.

Twisted Black: Twisted Black (born Tommy Burns, October 18, 1976) is a rapper from Detroit, Michigan and settled in Fort Worth, Texas as a teen.  He is on the 3R Entertainment/Scarred 4 Life Records label, and has also gone under the pseudonym "145".  His debut album with the duo One Gud Cide, "Look What The Streets Made", sold 10,000 copies in less than 30 days.  In 1998, he was incarcerated for a period of time.  In July 2006, Twisted Black was arrested and charged by officers with the Drug Enforcement Administration in Midland, Texas, shortly after signing a deal with New York-based independent record label TVT Records.  His TVT debut album, "Street Fame", was released on March 6, 2007.  Due out on the album release date is a DVD titled "The Rise Of Twisted Black" which was released through Twisted Black's own imprint Scarred For Life.

The Tide Is High: "The Tide Is High" is a 1966 song written by John Holt, originally produced by Duke Reid and performed by the Jamaican group The Paragons, with John Holt as lead singer.  The song gained international attention in 1980, when a version by the American band Blondie became a US/UK number one hit.  The British girl group Atomic Kitten also had a number one hit with their version of the song in 2002, and a version of the song was a minor hit for Canadian rapper Kardinal Offishall in 2008.

Question: What is the number one hit released by the rapper also known for his The Streets Made Me album?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "rapper_name": {
      "type": "string",
      "description": "The name of the rapper."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album associated with the rapper."
    },
    "number_one_hit_song": {
      "type": "string",
      "description": "The title of the number one hit song by the rapper."
    },
    "hit_type": {
      "type": "string",
      "description": "The type of hit (e.g., song, album)."
    },
    "chart_location": {
      "type": "string",
      "description": "The country or region where the song was a number one hit."
    }
  },
  "required": [
    "rapper_name",
    "album_name",
    "number_one_hit_song",
    "hit_type",
    "chart_location"
  ],
  "additionalProperties": false
}

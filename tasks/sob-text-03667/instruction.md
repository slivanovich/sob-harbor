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
PGA Tour Latinoamérica: PGA Tour Latinoamérica is a third level professional golf tour formed in 2012 and operated by the PGA Tour.  It was formed in concert with the now defunct Tour de las Américas.  Executives from the Tour de las Américas became employees of the new tour.  The initial 2012 season runs from September to December and consists of 11 tournaments in seven Latin American countries.  Subsequent years' schedules will run in two swings, March to May (Southern Hemisphere autumn) and October to December (spring).

Stray from the Path: Stray from the Path is an American metalcore band formed in 2001 in Long Island, New York.  They have released seven full-length albums total.  First three records independently released entitled "People Over Profit" in 2002, "Audio Prozac" in 2003, "Our Oceania" in 2004.  Stray From The Path signed with Sumerian Records and have released six records with them; "Villains" in 2008, "Make Your Own History" in 2009, "Rising Sun" in 2011, "Anonymous" in 2013, "Subliminal Criminals" in 2015, and "Only Death Is Real" in 2017.  They are currently signed to Sumerian Records.  They have been seen on tour with bands such as: Architects, Every Time I Die, The Acacia Strain, Terror, Norma Jean, Underoath, The Ghost Inside, For Today, Stick to Your Guns, Bleeding Through, Comeback Kid, and Counterparts.  They were also featured on the All Stars Tour in 2012 and 2013.  The band also played on the entire Vans Warped Tour in 2014.

Because We Can (concert tour): Because We Can was a concert tour by American rock band, Bon Jovi.  The tour was in support of the band's twelfth studio album "What About Now".  The tour was named after the lead single from "What About Now".  All five major continents were visited during the 2013 tour.  The tour saw the band travel to Wales for the first time since their 2001 One Wild Night Tour and was also the first time since their 1995 These Days Tour that the band returned to Africa for two dates in South Africa.  Furthermore, this tour was the first time in the band's 30-year history that they visited Bulgaria and Poland.  The tour ranked 1st on Pollstar's annual "Top 100 Mid Year Worldwide Tours".  It earned $142.1 million from 60 shows.  At the end of 2013, the tour placed 1st on Pollstar's "Top 100 Worldwide Tours", grossing $259.5 million from 102 shows.

Pop Punks Not Dead Tour: The Pop Punk's Not Dead Tour is a concert tour headlined by American rock band New Found Glory.  The initial US leg was sponsored by "Rockstar" energy drink, with the band supported by Set Your Goals, The Wonder Years, Man Overboard, and This Time Next Year.  The band wanted to showcase young talent from within the pop punk scene, following in the footsteps of bands such as Less Than Jake, Blink-182 and Green Day, who had in turn helped them out by offering support roles early in their career.  It was announced on 1 August 2011 that the tour would commence on 6 October in Santa Cruz, California, running through 20 November in San Diego following the release of the band's seventh studio album "Radiosurgery".  AbsolutePunk ran an exclusive competition on their website, with five pairs of free tickets available for the tour including a meet-and-greet with the band back stage.  During the band's stint on the 2012 "Kerrang!"  Tour, it was announced they would be bringing the tour to UK shores later in the year.

Psycho Circus World Tour: Psycho Circus World Tour was a Kiss concert tour in 1998–2000.  It was the first concert tour in history to have 3-D visual effects.  The Smashing Pumpkins opened at the Dodger Stadium show only, in costume as The Beatles for the Halloween night performance.  The Dodger Stadium show was streamed live on the internet as well as a radio broadcast.  Two songs, "Psycho Circus" and "Shout It Out Loud", were screened live on Fox television as part of the "Kiss Live: The Ultimate Halloween Party" special.  The vast majority of songs in the setlist were played on the previous Alive/Worldwide concert dates, leading to some frustration from fans expecting the return of classic songs not played on the previous tour.  Peter Criss was quoted in Metal Edge magazine at the time as wanting to add "Parasite" to the setlist.  The tour was initially hyped as having circus-style acts as pre-show entertainment.  This ultimately happened only at the first concert at Dodger Stadium.  Peter Criss later said that it didn't work out because the circus performers wanted equal billing and that some had even wanted to use KISS' backstage dressing room.  "2,000 Man" was played to bring in the new Millennium at the 1999/2000 New Year's Eve show at Vancouver, advertised at the time as being recorded for Alive IV.  The Vancouver show was also notable as being the first time the original members had played non-original band era material live in concert – "I Love It Loud", "Lick It Up" and "Heaven's on Fire" were added to the setlist and subsequently played on the Farewell Tour.  "Forever" was listed on concert setlists at the Vancouver show but was not played.  It was thought at the time it may have been intended as a Paul Stanley solo version prior to "Black Diamond".  One notable show on the tour was the March 12 Bremen, Germany, show.  After the opening song, Paul Stanley announced that the local fire marshall had banned Kiss from using any pyrotechnics during the show.  They used a translator on stage to let the crowd understand exactly what Stanley was saying.  At the end of the performance, the band ignited all of the pyrotechnics at once; as a result, they were banned from performing in Bremen.  Ticket sales for this tour were notably slower than the previous Reunion Tour, with many of the smaller market shows underselling and a second North American leg for the summer of 1999 cancelled all together, the band ultimatly decided on embarking on a Farewell tour in the new millennium.

Rush (band): Rush is a Canadian rock band composed of Geddy Lee (bass guitar, lead vocals, keyboards), Alex Lifeson (guitars, backing vocals) and Neil Peart (drums, percussion, lyrics).  Forming in 1968, the band went through several configurations until arriving at its current line-up when Peart replaced original drummer John Rutsey in July 1974, two weeks before the group's first United States tour.

Different Stages (Rush album): Different Stages is a live album by Canadian rock band Rush, released in 1998.  The bulk of the first and second discs were recorded at the World Amphitheater in suburban Chicago during the 1997 "Test for Echo" tour, along with three songs from the 1994 "Counterparts" tour.  The third disc is taken from a performance at the Hammersmith Odeon in London during the "A Farewell to Kings" tour in 1978.

Maya Tour: The Maya Tour (stylized as /\/\ /\ Y /\ Tour) is a 2010 global M.I.A. concert tour performed in support of her third studio album "Maya" (see 2010 in music).  It began on 21 September 2010 in North America and was M.I.A.'s third major global performing tour following the birth of her first child.  The tour was announced on 8 September 2010, with dates for Canadian, American and European venues revealed.  According to photo albums on the musician's official Facebook page, the North American leg was branded the Reboot/Reboost Tour 2010, while the Sexynsofistic8d Tour formed the European leg of her 2010 concerts.  M.I.A. handled costumes and stage direction, which departed from the productions of the preceding 2007-2008 Kala Tour and People Vs. Money Tours.

The Uplift Mofo Party Tour: The Uplift Mofo Party Tour (also known during 1988 dates as the Monsters Of Funk Tour) was a concert tour by Red Hot Chili Peppers to support their third studio album "The Uplift Mofo Party Plan".  Founding drummer, Jack Irons returned the band the previous year to finish out the band's tour and record the next album, The Uplift Mofo Party Plan, which ended up being the only album and full tour to feature the four founding band members: Anthony Kiedis, Flea, Hillel Slovak and Irons.  It was the band's biggest tour at the time and featured their first trip to Europe.  Kiedis, who started to develop a major drug problem on the previous tour, started to fall deeper into his addiction and Slovak's addiction to heroin only grew stronger as well.  Slovak died of a heroin overdose a few weeks after the end of the tour on June 25, 1988.  The surviving three members regrouped for a small boat trip with then manager, Lindy Goetz.  It was there that Irons decided he could no longer deal with being in the band and Slovak's death was too hard for him to handle so he decided to quit the band again, this time for good.

Counterparts Tour: Rush's Counterparts Tour was in support of the band's studio album "Counterparts".  The tour kicked off January 22, 1994 at the Civic Center in Pensacola, Florida and culminated on May 7, 1994 at Maple Leaf Gardens in Toronto.  Opening acts for this tour were Candlebox, The Melvins, Primus, The Doughboys, and I Mother Earth.

Question: What year was the band who had a Counterparts Tour formed?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that had the tour."
    },
    "tour_name": {
      "type": "string",
      "description": "The name of the tour mentioned in the question."
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "tour_name",
    "formation_year"
  ],
  "additionalProperties": false
}

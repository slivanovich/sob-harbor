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
Katastrophy Wife: Katastrophy Wife is an American rock band formed by Kat Bjelland and her former husband Glenn Mattson in 1998.  Bjelland also fronted the punk rock band Babes in Toyland between 1987 and 2001.  The band currently consists of Bjelland on lead vocals and guitar and her boyfriend, Adrian Johnson, on drums. <ref name="MissB, "Katastrophy Wife's Kat Bjelland gets her Heart-On on FasterLouder.com.au" http://www.fasterlouder.com.au/features/8900/Katastrophy_Wifes_Kat_Bjelland_gets_her_HeartOn Fasterlouder.com Retrieved on June 12, 2010."> MissB, "Katastrophy Wife's Kat Bjelland gets her Heart-On on FasterLouder.com.au" http://www.fasterlouder.com.au/features/8900/Katastrophy_Wifes_Kat_Bjelland_gets_her_HeartOn Fasterlouder.com Retrieved on June 12, 2010. </ref> The band released two albums, "Amusia" (2001) and "All Kneel" (2004).  A third album was due for release in 2008, but, as of 2015, has yet to surface.  In May 2014, a 10th anniversary reissue of "All Kneel" was released as part of Record Store Day.  Kat Bjelland has since joined fellow Babes in Toyland band member Lori Barbero and new bass player, Clara Salyer in a reunion tour.

Cher: Cher ( ; born Cherilyn Sarkisian; May 20, 1946) is an American singer and actress.  Sometimes referred to as the Goddess of Pop, she has been described as embodying female autonomy in a male-dominated industry.  She is known for her distinctive contralto singing voice and for having worked in numerous areas of entertainment, as well as adopting a variety of styles and appearances during her five-decade-long career.

Welcome to the Blacklist Club: Welcome to the Blacklist Club<ref name="http://evantaubenfeld.com/">http://evantaubenfeld.com/</ref> (originally titled With a Wink and a Smile) is the debut album by American singer/songwriter Evan Taubenfeld, ex-guitarist of Avril Lavigne.  The album was expected to be released on September 15, 2009,<ref name="https://www.amazon.com/Welcome-Blacklist-Club-Evan-Taubenfeld/dp/B002JCYSNM/ref=sr_1_3?ie=UTF8&qid=1250375110&sr=8-3">https://www.amazon.com/dp/B002JCYSNM</ref> but was rescheduled to a later date.  During Taubenfeld's UStream chat on March 28, 2010, he confirmed that the album would be released on iTunes worldwide on May 18, 2010.  On February 24, a promotional single, "Cheater of the Year" was released on iTunes, and a lyric video was made available on MySpace.  The first official single, "Boy Meets Girl" was released on March 31.

Primitivity: Primitivity is an American instrumental cello rock band consisting of three cellists and a percussionist. <ref name="http://www.primitivity.com"> http://www.primitivity.com, February 2010. </ref><ref name="http://www.metalunderground.com/news/details.cfm?newsid=57088"> http://www.metalunderground.com/news/details.cfm?newsid=57088, June 2010. </ref> Primitivity began primarily as a cover band playing songs by the thrash metal band Megadeth and the cello rock band Apocalyptica. <ref name="http://www.strathmore.org/media/pdf/pressreleases/232010_41255371.pdf"> http://www.strathmore.org/media/pdf/pressreleases/232010_41255371.pdf, February 2010. </ref><ref name="http://www.metalinjection.net/tv/view/4821/cello-cover-of-symphony-of-destruction-megadeth"> http://www.metalinjection.net/tv/view/4821/cello-cover-of-symphony-of-destruction-megadeth, April 2010. </ref><ref name="http://www.metalinjection.net/tv/view/4822/cello-cover-of-master-of-puppets-metallica"> http://www.metalinjection.net/tv/view/4822/cello-cover-of-master-of-puppets-metallica, April 2010. </ref> The band has released one album entirely of Megadeth covers titled "Plays Megadeth For Cello". <ref name="http://www.roadrunnerrecords.com/blabbermouth.net/news.aspx?mode=Article&newsitemID=138712"> http://www.roadrunnerrecords.com/blabbermouth.net/news.aspx?mode=Article&newsitemID=138712, April 2010. </ref> Primitivity has also composed and performed original songs for cello rock ensemble. <ref name="http://www.metalunderground.com/news/details.cfm?newsid=57088"> http://www.metalunderground.com/news/details.cfm?newsid=57088, June 2010. </ref> The group was selected as a 2010 Artist In Residence at Strathmore Hall in Bethesda, Maryland. <ref name="http://www.strathmore.org/eventstickets/calendar/view.asp?id=5231"> http://www.strathmore.org/eventstickets/calendar/view.asp?id=5231, February 2010. </ref>

Strangers to Ourselves: Strangers to Ourselves is the sixth album by American alternative rock band Modest Mouse, which was released on March 17, 2015, two weeks after its initially announced release date of March 3.  The album was leaked to the internet on March 7, 2015.  On March 16, 2015, the day before the album's official release date, "Strangers to Ourselves" was prematurely made available for download on Amazon.com (free for Prime) and the iTunes Store.

Miss Potter: Miss Potter is a 2006 Anglo-American biographical fiction family drama film directed by Chris Noonan.  It is a biographical film of children's author and illustrator Beatrix Potter, and combines stories from her own life with animated sequences featuring characters from her stories, such as Peter Rabbit.  Scripted by Richard Maltby, Jr., the director of the Tony-winning Broadway revue, "Fosse", the film stars Renée Zellweger in the title role; Ewan McGregor as her publisher and fiancé, Norman Warne; and Lloyd Owen as solicitor William Heelis.  Emily Watson stars as Warne's sister, Millie.  Lucy Boynton also stars as the young Beatrix Potter.  It was filmed in St. Peter's Square Hammersmith, Cecil Court, Osterley Park, Covent Garden, the Isle of Man, Scotland and the Lake District.  "Miss Potter" was released on 29 December 2006 so that the film could compete for the 2007 Academy Awards.  The film was intended to be released generally on 12 January 2007, but Variety.com reported that the Weinstein Company had decided to push a wider release date until after the Academy Awards on 25 February 2007.  The date seemed to fluctuate a number of times, but the Weinstein Company website ultimately listed its release date as 9 March.  The film received generally positive reviews and earned Zellweger her sixth Golden Globe nomination.

Further Adventures Of: Further Adventures Of is the eighth studio album by Canadian singer/songwriter Bruce Cockburn.  The album was released in 1978 by True North Records.  Contrary to information on some websites (e.g. AllMusic.com, ArtistDirect.com, CDUniverse.com, Yahoo.com), the title of the album is not "Further Adventures of Bruce Cockburn".  As per Cockburn's official website and the original album cover the title is simply "Further Adventures Of".  The album cover displays a picture of a small globe of the Earth after the title, implying that the adventures referred to are those of the planet Earth, not of Cockburn.

Not.com.mercial: not.com.mercial is the twenty-third studio album by American singer-actress Cher.  It was released on November 8, 2000, exclusively through Cher.com and Artist Direct.  Cher wrote the album in 1994 while attending a semiannual songwriters' workshop hosted by entertainment executive Miles Copeland III in his castle in France.  Upon returning to the United States, Cher enlisted members of David Letterman's CBS Orchestra to record the album.  After completing it, she presented the album to her recording company, which declined the material for being "not commercial".  Cher kept the album for six years before deciding to release it through the Internet only.

Www.thug.com: Www.thug.Com (stylized as www.thug.com) is the second studio album by rapper Trick Daddy, who previously released his debut album known at the time under the name as Trick Daddy Dollars coming on the heels of "Based on a True Story".  It was released on September 22, 1998 by Warlock Records and Slip-n-Slide Records.  The album managed to peak at number thirty on the "Billboard" 200, the fifth-highest peak of any Trick Daddy album.  On July 2, 1999, less than a year after its release, the album achieved Gold status.  www.thug.com was also the URL of Trick Daddy's official website.

Www.tism.wanker.com: www.tism.wanker.com is the fifth album by Australian alternative rock group TISM (This Is Serious Mum), released in 1998.  The album title references an internet URL which, at the time of release, was a subdomain (of wanker.com) provided by a friendly person overseas who had registered wanker.com, as TISM were not able to obtain their preferred domain, wanker.com.au, due to Australian domain regulations.  However, the web hosting fees were not paid, subsequently it was taken down by the hosting ISP several months after launch and has not been available since.

Question: Cherilyn Sarkisian released her album "not.com.mercial" on what date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who released the album."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "release_date": {
      "type": "string",
      "format": "date",
      "description": "The date the album was released in YYYY-MM-DD format."
    }
  },
  "required": [
    "artist_name",
    "album_title",
    "release_date"
  ],
  "additionalProperties": false
}

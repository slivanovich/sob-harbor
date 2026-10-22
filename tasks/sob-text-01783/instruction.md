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
1984 San Francisco 49ers season: The 1984 San Francisco 49ers season was their 39th season in the National Football League.  The season was highlighted by their second Super Bowl victory.  The franchise had their best season ever with a record of 15 wins and only 1 loss.  Quarterback Joe Montana would be awarded the Super Bowl's Most Valuable Player Award for the second time in his career, joining Bart Starr and Terry Bradshaw as the only two time Super Bowl MVP's.

The 440 Alliance: The 440 Alliance is an American cello rock band from Arlington, Texas consisting of five cellists and a percussionist.  The group formed in 2004 and is known for their diverse approach to the cello, incorporating electric effects, turntables, piano, and mallet percussion.  They received national exposure on NPR's "All Songs Considered", the Drew Pearson Show on Fox Sports, and on Fox's musical reality show, "The Next Great American Band".  The group has performed at a number of private parties for celebrities including Troy Aikman (Former NFL Quarterback for the Dallas Cowboys), Jerry Jones (Dallas Cowboys owner), John Kirtland (Former drummer for Deep Blue Something and owner of Kirtland Records), Janine Turner (from Northern Exposure), members of the Dallas Symphony Orchestra, as well as the Dallas, TX movie premier for the film 'The Soloist' (starring Jamie Foxx and Robert Downey Jr.).

Troy Aikman: Troy Kenneth Aikman (born November 21, 1966) is a former American football quarterback who played for the Dallas Cowboys in the National Football League (NFL).  The number one overall draft pick in 1989, Aikman played twelve consecutive seasons as quarterback with the Cowboys.  During his career he was a six-time Pro Bowl selection, led the team to three Super Bowl victories, and was the Super Bowl XXVII MVP.  Aikman was elected to the Pro Football Hall of Fame in 2006 and to the College Football Hall of Fame on December 9, 2008 in New York City.

Greg Harden: Greg Harden is a life coach, motivational speaker and executive consultant who is best known for his work with 5-time Super Bowl champion quarterback Tom Brady, Heisman Trophy winner and Super Bowl MVP Desmond Howard, and 23-time Olympic gold medalist Michael Phelps.  Brady, Howard and other athletes credit Harden with inspiring them to overcome obstacles and achieve success in their professional and personal lives.  Harden has created a personal improvement program that is unique in sports.  In 2014, he was profiled in a segment on 60 Minutes.

Carlton Williamson: Carlton Williamson (born June 12, 1958) is a former college and NFL football player who was selected by the San Francisco 49ers in the 3rd round of the 1981 NFL Draft.  A 6'0", 200 lbs.  safety from the University of Pittsburgh, Williamson was a 2-time Pro Bowl selection in 1984 and 1985 and a 3-time Super Bowl winner.  He played in eight NFL seasons and his entire career with the 49ers from 1981-1988.  In his career, he recorded 17 interceptions for 294 yards and 1 touchdown.

Break of Reality: Break of Reality (BoR) is an American cello rock band consisting of three cellists and a percussionist.  The group is associated with the terms "cinematic rock", "cello rock", and "indie classical".  Break of Reality's current members are Patrick Laird, Ivan Trevino, Laura Metcalf, and Adrian Daurov.  The band's sound consists of many musical influences, such as rock, classical, and indie rock.

Super Bowl XLVIII: Super Bowl XLVIII was an American football game between the American Football Conference (AFC) champion Denver Broncos and National Football Conference (NFC) champion Seattle Seahawks to decide the National Football League (NFL) champion for the 2013 season.  The Seahawks defeated the Broncos 43–8, the largest margin of victory for an underdog and tied for the third largest point differential overall (35) in Super Bowl history with Super Bowl XXVII (1993).  It was the first time the winning team scored over 40 points, while holding their opponent to under 10.  This became the first Super Bowl victory for the Seahawks and the fifth Super Bowl loss for the Broncos, the most of any team.  The game was played on February 2, 2014, at MetLife Stadium at the Meadowlands Sports Complex in East Rutherford, New Jersey, the first Super Bowl played outdoors in a cold-weather city and the first Super Bowl to be played on a February 2.

The Pregnant Concert: The Pregnant Concert is a live recording of a recital by American cello rock band Rasputina held at the Knitting Factory in Williamsburg, Brooklyn on September 13, 2009 (although the album cover claims it to have been 1909).  It contains songs from previous Rasputina albums, as well as covers from a variety of other musicians and both "Holocaust of Giants" and "Kinderhook Hoopskirt Works" from their upcoming album "Sister Kinderhook".

Primitivity: Primitivity is an American instrumental cello rock band consisting of three cellists and a percussionist. <ref name="http://www.primitivity.com"> http://www.primitivity.com, February 2010. </ref><ref name="http://www.metalunderground.com/news/details.cfm?newsid=57088"> http://www.metalunderground.com/news/details.cfm?newsid=57088, June 2010. </ref> Primitivity began primarily as a cover band playing songs by the thrash metal band Megadeth and the cello rock band Apocalyptica. <ref name="http://www.strathmore.org/media/pdf/pressreleases/232010_41255371.pdf"> http://www.strathmore.org/media/pdf/pressreleases/232010_41255371.pdf, February 2010. </ref><ref name="http://www.metalinjection.net/tv/view/4821/cello-cover-of-symphony-of-destruction-megadeth"> http://www.metalinjection.net/tv/view/4821/cello-cover-of-symphony-of-destruction-megadeth, April 2010. </ref><ref name="http://www.metalinjection.net/tv/view/4822/cello-cover-of-master-of-puppets-metallica"> http://www.metalinjection.net/tv/view/4822/cello-cover-of-master-of-puppets-metallica, April 2010. </ref> The band has released one album entirely of Megadeth covers titled "Plays Megadeth For Cello". <ref name="http://www.roadrunnerrecords.com/blabbermouth.net/news.aspx?mode=Article&newsitemID=138712"> http://www.roadrunnerrecords.com/blabbermouth.net/news.aspx?mode=Article&newsitemID=138712, April 2010. </ref> Primitivity has also composed and performed original songs for cello rock ensemble. <ref name="http://www.metalunderground.com/news/details.cfm?newsid=57088"> http://www.metalunderground.com/news/details.cfm?newsid=57088, June 2010. </ref> The group was selected as a 2010 Artist In Residence at Strathmore Hall in Bethesda, Maryland. <ref name="http://www.strathmore.org/eventstickets/calendar/view.asp?id=5231"> http://www.strathmore.org/eventstickets/calendar/view.asp?id=5231, February 2010. </ref>

Doug Williams (quarterback): Douglas Lee "Doug" Williams (born August 9, 1955) is a former American football quarterback and former head coach of the Grambling State Tigers football team.  Williams is known for his remarkable performance in Super Bowl XXII.  Williams, who was named the Super Bowl MVP, passed for a Super Bowl record 340 yards and four touchdowns, with one interception.  He was the first African-American starting quarterback to win a Super Bowl.  Williams also became the first player in Super Bowl history to pass for four touchdowns in a single quarter, and four in a half.  Williams is now a team executive for the Redskins, being hired for that role in 2014.

Question: Which American cello rock band was hired by a three time Super Bowl winner to perform at his private party?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the American cello rock band."
    },
    "band_origin": {
      "type": "string",
      "description": "The country of origin for the band."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event the band performed at."
    },
    "host_details": {
      "type": "object",
      "properties": {
        "host_name": {
          "type": "string",
          "description": "The name of the individual who hired the band."
        },
        "host_profession": {
          "type": "string",
          "description": "The profession or role of the host."
        },
        "super_bowl_wins": {
          "type": "integer",
          "description": "The number of Super Bowl victories achieved by the host."
        }
      },
      "required": [
        "host_name",
        "host_profession",
        "super_bowl_wins"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "band_origin",
    "event_type",
    "host_details"
  ],
  "additionalProperties": false
}

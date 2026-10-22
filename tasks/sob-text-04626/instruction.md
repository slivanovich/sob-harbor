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
OhBoy!: OhBoy!  are an English indie-pop band from Northampton formed in 2012.  The band is composed of Jonathan 'Jay' Brook, Lee Irons, Mark Nicholas, Meg Amirghiasvand and Dan Battison.  Lee Irons previously played in the band The Departure while Dan Battison previously played in New Cassettes.  OhBoy!  signed to independent record label Alcopop!  in January 2016 and released their first single on the label, 'Carrot & The Stick', in the same month.  'Carrot & The Stick' received radio airplay from the likes of Huw Stephens on BBC Radio 1, as well as Radio X, BBC Radio 6 Music and Amazing Radio.  The band were selected to perform at Glastonbury Festival 2016 on The BBC Introducing Stage having been championed by BBC Introducing since their formation in 2012.

Vietnamese Prodigy: Vietnamese prodigy (Vietnamese : "Thần đồng đất Việt") is a comic series of Vietnam, the first volume called 'Shaman calls grapefruit' published by Tre Publishing House in February 16, 2002.  Initially the work was carried out by Le Linh and Phan Thi company.  After writing the story for a while, Le Linh stopped writing this comic, and now writing stories as well as related work are in charge by Phan Thi company.  The series previously published by Tre Publishing House, followed Van Hoa Sai Gon Publishing House, Thoi Dai Publishing House(from episode 130 to episode 153), Dai Hoc Su Pham Ho Chi Minh City Publishing House (from episode 154 to episode of 168) and now the Dan Tri Publishing House (from episode 169 onwards).  With over 100 novels, along with related comic Vietnamese Science prodigy, Vietnamese Fine Arts Prodigy and the Vietnam Mathematics prodigy, Vietnamese Prodigy Hoang Sa-Truong Sa, which is considered the Vietnam comics longest and most successful until the present time.  Average one volume per month of Vietnamese Prodigy (printed in black and white) and three new color comics related Vietnamese Prodigy (including Science, Mathematics and Fine Arts) was released.

The Sense of an Ending: The Sense of an Ending is a 2011 novel written by British author Julian Barnes.  The book is Barnes' eleventh novel written under his own name (he has also written crime fiction under the pseudonym Dan Kavanagh) and was released on 4 August 2011 in the United Kingdom.  "The Sense of an Ending" is narrated by a retired man named Tony Webster, who recalls how he and his clique met Adrian Finn at school and vowed to remain friends for life.  When the past catches up with Tony, he reflects on the paths he and his friends have taken.  In October 2011, "The Sense of an Ending" was awarded the Man Booker Prize.  The following month it was nominated in the novels category at the Costa Book Awards.

Combat Zone: True Tales of G.I.s in Iraq: Combat Zone: True Tales of GI's in Iraq is a graphic novel written by Karl Zinsmeister.  Penciller Dan Jurgens illustrated the graphic novel with cover art contributed by Esad Ribic.  The title was released as a single volume trade paperback in 2005.  The graphic novel depicted Zinsmeister's journalistic reports on his time with the 82nd Airborne.  Zinsmeister's initial account of his time with the 82nd Airborne was recounted in his book "Boots on the Ground: a month with the 82nd Airborne in the battle for Iraq"

Cat Run 2: Cat Run 2 is a 2014 direct-to-video American comedy action film sequel of "Cat Run" directed by John Stockwell starring Scott Mechlowicz, Winter Ave Zoli, Alphonso McAuley and Dan Bilzerian.

Extraction (film): Extraction is a 2015 American action-thriller film directed by Steven C. Miller and written by Umair Aleem.  The film stars Kellan Lutz, Bruce Willis, Gina Carano, D. B. Sweeney, Dan Bilzerian and Steve Coulter.  The film was released on December 18, 2015, in a limited release, and through video on demand by Lionsgate Premiere.

Dan Johnson (American football): Dan Johnson (born May 17, 1960) is a former professional American football player who played tight end for seven seasons for the Miami Dolphins.  Johnson told ESPN's John Barr on January 28, 2011 that he took about 1000 pain killers per month during his playing days, as a result of the numerous injuries and broken bones he suffered.  Teammates nicknamed him "King of Pain" as a result of all the broken bones he had during his career.

Second String: Second String is a direct-to-TV film from 2002 about the Buffalo Bills football team who find its first string (led by real-life Bills quarterback Doug Flutie, who had left the team by the time the film was released) out for a month after a food poisoning incident, leading the team's head coach, "Chuck Dichter" (portrayed by Jon Voight), to hire an insurance salesman named Dan Heller (played by Gil Bellows) as the team's backup quarterback.  Teri Polo also appeared as Heller's wife; Flutie, Mike Ditka, Chris Berman, Van Miller, Bills cornerback Donovan Greer and Ken "Pinto Ron" Johnson appear as themselves.  The film originally aired on TNT.

Blameshift: Blameshift is a four-piece rock band from Long Island, New York that started in 2005.  The band consists of Jenny Mann, Tim Barbour, Mike Sarkissian and Dan Scofield.  The band is recognized for their work ethic, extensive touring history and high energy live show.  In 2006 they recorded a self released album, “Drop Down”.  The release was followed by over 150 tour dates including three dates on the Warped Tour.  In 2007 Blameshift recorded their second album.  “The Test” with Michael Birnbaum and Chris Bittner.  The album was nationally released through Smart Punk, F.Y.E, Hot Topic, and iTunes.  Alternative Press named Blameshift as “Unsigned Band Of The Month” in August 2008.  Blameshift won a contest through Taco Bell called “Feed The Beat” in 2008.  Michael Birnbaum and Chris Bittner also produced the single, The Sirens Are Set in 2008.  Blameshift toured through all of 2008 in the U.S. and Canada with And Then There Was You, and The Material on the Everlasting Sound Tour.  At the start of 2009 producer Mike Watts demoed the bands’ Self Titled EP.  With touring in between with Sky Tells All and The Material, the release of the EP was put on hold until February 2010.  In May 2010 the band raised $5500 through Kickstarter to record with producer / engineer Erik Ron in Hollywood, California.  In June 2010 the band signed with Restless Management out of Venice Beach, California.

Dan Bilzerian: Dan Brandon Bilzerian (born December 7, 1980) is an American professional poker player.

Question: Dan Bilzerian was born the same month that Extraction was released. What month was it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "month_name": {
      "type": "string",
      "description": "The name of the month."
    },
    "person_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the person."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_date": {
          "type": "string",
          "description": "The full release date of the film."
        }
      },
      "required": [
        "title",
        "release_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "month_name",
    "person_details",
    "film_details"
  ],
  "additionalProperties": false
}

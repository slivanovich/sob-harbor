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
RuPaul's Drag Race: RuPaul's Drag Race is an American reality competition television series produced by World of Wonder for Logo TV and, beginning with the ninth season, VH1.  The show documents RuPaul in the search for "America's next drag superstar."  RuPaul plays the role of host, mentor, and head judge for this series, as contestants are given different challenges each week.  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage, Ross Mathews, Carson Kressley, and a host of other guest judges, who critique contestants' progress throughout the competition.  The title of the show is a play on drag queen and drag racing, and the title sequence and song "Drag Race" both have a drag-racing theme.

Todrick Hall: Todrick Hall (born April 4, 1985 in Plainview, Texas) is an American rapper, singer, actor, dancer, director, choreographer, and YouTuber.  He rose to prominence on the ninth season of "American Idol," where he made it to the semi-finals.  Since then, Hall has become notable as a Broadway veteran, YouTube star, and judge on "RuPaul's Drag Race".

RuPaul's Drag U: RuPaul's Drag U (as in "Drag University") is an American reality television series that debuted July 19, 2010, on Logo TV.  Its final episode aired in August 2012.  It was hosted by RuPaul and a team of drag queen "professors".  "Drag U" was a spin-off of "RuPaul's Drag Race".  RuPaul confirmed on May 8, 2013 via Twitter that the series had been cancelled.

List of RuPaul's Drag Race contestants: This is a list of contestants who have appeared on the American television show "RuPaul's Drag Race".  Contestants compete against each other and are progressively eliminated, until just a winner remains, who is crowned "next drag superstar".  They are judged by drag queen RuPaul and her panel of judges.  The series first aired in 2009 and as of 2017, there have been nine seasons of the show.  A total of 113 different participants have been selected as finalists in the show in its eight years running, with nine drag queens — BeBe Zahara Benet, Tyra Sanchez, Raja, Sharon Needles, Jinkx Monsoon, Bianca Del Rio, Violet Chachki, Bob the Drag Queen, and Sasha Velour being crowned so far as "America's Next Drag Superstar".  In addition, an season aired in 2012 featuring twelve returning contestants from the first four seasons, each competing for a place in the "Drag Race Hall of Fame".  The season was won by Chad Michaels, previously a runner-up in season four.  In 2015, it was announced "All Stars" had been renewed and a premiered on August 25, 2016.  The second season was won by Alaska, who was previously a runner-up in season 5.

Straight Outta Oz: Straight Outta Oz is the third solo studio album and original musical written and produced by American singer-songwriter and YouTube celebrity Todrick Hall, released on 23 June 2016.  Featured artists include Nicole Scherzinger, Jordin Sparks, Perez Hilton, Joseph Gordon-Levitt, and Amber Riley.  It is based on the Wizard Of Oz whilst being a semi-autobiographical account of his rise to fame in Los Angeles (Oz).

Carmen Carrera: Carmen Roman (born Christopher Roman; April 13, 1985), better known by her stage name Carmen Carrera, is an American reality television personality, model, burlesque performer, and actress, known for appearing on the third season of the Logo reality television series "RuPaul's Drag Race", as well as its spin-off series "RuPaul's Drag U".  Although she presented as male during the third season of "RuPaul's Drag Race", on May 1, 2012, ABC News reported that Carrera is a transgender woman.

List of RuPaul's Drag Race episodes: "RuPaul's Drag Race" is an American reality competition television series produced by World of Wonder for Logo TV.  The show documents RuPaul in his search for "America's next drag superstar."  Queen RuPaul plays the roles of host, mentor, and source of inspiration for this series, as contestants are given different challenges each week.  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage and a host of other guest judges, who critique contestants' progress throughout the competition.  The title of the show is a play on drag queen and drag racing, and the title sequence and song "Drag Race" both have a drag-racing theme.

Jealous of My Boogie: "Jealous of My Boogie" is the second single from RuPaul's album "Champion".  It was released to iTunes June 16, 2009 as part of an EP titled "Jealous of My Boogie - The RuMixes", and released again as track two of the "Champion" album.  The single include ringtones of catchphrases from RuPaul's Drag Race as well as a new version of "Cover Girl" with a rap by Bebe Zahara Benet, winner of the first season of "RuPaul's Drag Race".

RuPaul's Drag Race: All Stars: RuPaul's Drag Race All Stars is an American reality competition television series produced by World of Wonder for Logo TV.  The show is a spin-off of "RuPaul's Drag Race" where RuPaul allows past contestants to come back and compete for a spot in the Drag Race Hall of Fame.  RuPaul plays the roles of host, mentor, and source of inspiration for this series, as contestants are given different challenges each week.  "RuPaul's Drag Race" employs a panel of judges, including RuPaul, Michelle Visage and a host of other guest judges, who critique contestants' progress throughout the competition.

RuPaul's Drag Race (season 1): The first season of "RuPaul's Drag Race", later referred to as "The Lost Season", premiered in the United States on February 2, 2009, on VH-1.  Nine contestants were selected to compete in the running of becoming "America's Next Drag Superstar."  The first season was filmed during the summer of 2008.  The winner of the first season won a lifetime supply of MAC Cosmetics, was featured in an LA Eyeworks campaign, joined the Logo Drag Race tour, and won a cash prize of $20,000.  One of the nine contestants to compete on "RuPaul's Drag Race" was determined by an audience vote via the show's official website.  The results were announced in early September 2008.  The theme song playing during the runway every episode was "Cover Girl" from RuPaul's album "Champion".  This season and season one of All-Stars are the only seasons to not feature the "Snatch Game."

Question: on which day the album written by the you tube star, one of the semi finalists of "American Idol" and judge on "RuPaul's Drag Race" was released?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "role_on_rupauls_drag_race": {
          "type": "string",
          "description": "The artist's role on RuPaul's Drag Race."
        },
        "american_idol_achievement": {
          "type": "string",
          "description": "The artist's achievement on American Idol."
        },
        "other_prominent_roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other notable roles or professions of the artist."
        }
      },
      "required": [
        "name",
        "role_on_rupauls_drag_race",
        "american_idol_achievement",
        "other_prominent_roles"
      ],
      "additionalProperties": false
    },
    "album_information": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the album."
        },
        "type": {
          "type": "string",
          "description": "The type of album (e.g., solo studio album, original musical)."
        }
      },
      "required": [
        "title",
        "release_date",
        "type"
      ],
      "additionalProperties": false
    },
    "release_date_answer": {
      "type": "string",
      "description": "The final answer to the question: the release date of the album."
    }
  },
  "required": [
    "artist_information",
    "album_information",
    "release_date_answer"
  ],
  "additionalProperties": false
}

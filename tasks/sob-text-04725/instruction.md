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
Radio personality: A radio personality (American English) or radio presenter (British English), commonly referred to as a "disc jockey" or "DJ" for short, is a person who has an on-air position in radio broadcasting.  A radio personality that hosts a radio show is also known as a radio host, and in India and Pakistan as a radio jockey.  Radio personalities who introduce and play individual selections of recorded music are known as disc jockeys.  The term has evolved to also describe a person who mixes a continuous flow of recorded music in real time.  Broadcast radio personalities may include talk radio hosts, AM/FM radio show hosts, and satellite radio program hosts.  Notable radio personalities include pop music radio hosts Martin Block, Alan Freed, Dick Clark, Delilah Luke, Ameen Sayani, Wolfman Jack, and Casey Kasem, shock jocks such as Don Imus and Howard Stern, as well as sports talk hosts such as Mike Francesa and political talk hosts such as Rush Limbaugh.

Jim Norton (comedian): James Joseph Norton Jr. (born July 19, 1968) is an American comedian, radio personality, author, and actor.  He is best known as the former co-host of the "Opie and Anthony" radio show with Gregg "Opie" Hughes and Anthony Cumia from 2001 to 2014.  He is the co-host of "Jim Norton and Sam Roberts" on Sirius XM Satellite Radio which launched in 2016 with Sam Roberts.

Radioresepsjonen: Radioresepsjonen (Eng.  "lit."  "The radio reception") is a Norwegian radio show.  From 2006 to 2013, it was broadcast on NRK P3, a radio station targeting the youth.  Since 2014, it has been broadcast on NRK P13, which is aimed at a more adult audience than NRK P3.  The show is hosted by brothers Steinar Sagen (host) and Tore Sagen (technician), and Bjarte Tjøstheim (sidekick).  The show is very popular in Norway, and has developed cult status amongst a broad audience.  The show is the most podcasted radio show in Norway, with over 200.000 downloads each month.  Besides their radio show the trio has also had success with other live shows, TV-shows and podcasts.

Stephanie Miller's Happy Hour: Stephanie Miller's Happy Hour is a once a week podcast hosted by American radio host, comedian, and political commentator Stephanie Miller.  The podcast consists of approximately 45 minutes to an hour of original uncensored NSFW material, and is available via paid subscription from Miller’s website.  The "Happy Hour" features many of the sidekicks ("mooks") and guests who appear on Miller's daily radio show, "The Stephanie Miller Show", as well as other comedians, celebrities, and personalities.  During the podcast, the hosts and guests often consume alcohol while they chat as one typically does during a happy hour.  New episodes of the "Happy Hour" are usually recorded on Thursdays in Miller's home studio, and released each Friday.  Video versions of the "Happy Hour" are also available by paid subscription.  Audio and video versions of previous "Happy Hour's" are available to subscribers in the archive section of Miller's website.  Vanessa Rumbles, Miller’s radio Executive Producer appears on each episode.  Miller's radio show Associate Producer Sean Comiskey, who handles the "Happy Hour" video production, also appears on occasion, as does Miller’s radio co-host Jim Ward.  While there are usually guests on the "Happy Hour", periodically the episode is titled "Old Home Week" or "Family Week" with just Miller's radio co-hosts and producers.

Ed Schultz: Edward Andrew "Ed" Schultz (born January 27, 1954) is an American television and radio host, a progressive political commentator and a former sports broadcaster.  Schultz currently hosts a daily primetime weekday show on RT America TV channel based in Washington, D.C., that is part of the RT network.  Schultz has hosted a nationally syndicated podcast, "Ed Schultz News and Commentary", since 2015 and a nightly television show, "News with Ed Schultz", since 2016.  He was the host of "The Ed Show", a weekday news talk program on MSNBC, and "The Ed Schultz Show", a talk radio show, nationally syndicated by Dial Global.  The radio show ended on May 23, 2014, and was replaced by a one-hour podcast.

Anthony Cumia: Anthony Cumia (born April 26, 1961) is an American radio personality and broadcaster who is best known as the co-host of the "Opie and Anthony" radio show with Gregg "Opie" Hughes that aired from 1995 to 2014, alongside comedian Jim Norton from 2001.

Cranked Up Live: Cranked Up Live"®" - Is a syndicated weekly 3 hour hard rock radio show and 1 hour hard rock video show hosted by Curtis McKinney and Brad Hennington.  The radio show is a combination of music, comedy, talk, and interviews along with the 'Advice from the Desk of Mr. Holland', the 'Cranked Up Five', 'Psycho Picks', 'Block of Rock', and the 'Joke of the Week'.  The video show is a compressed version of the radio show made from video recorded while making the radio show.  Cranked Up Live is heard on over 50 FM, AM, and Digital Broadcasting stations.

Jesse Thorn: Jesse Thorn (born April 24, 1981) is an American public radio show host/creator.  He is the host and producer of the radio show and podcast "Bullseye" (formerly "The Sound of Young America"), which is distributed by National Public Radio to 69 public terrestrial radio stations in 29 states and is also broadcast weekly on XM Radio's "XM Public Radio" channel.  He is the owner and founder of the Maximum Fun podcast network, where he hosts the podcasts "Judge John Hodgman" and "Jordan, Jesse, Go! ."  In addition to his work in radio and podcasts, Jesse Thorn also hosts the television program The Grid, which formerly aired on IFC, and runs a blog and web video series devoted to men's fashion called Put This On.

2016 HappyBet Cup: The 2016 HappyBet Cup is an upcoming summer football friendly tournament organized by Alemannia Aachen, La Liga and Match IQ.  It will be hosted by Alemannia Aachen at the New Tivoli in Aachen, on 24 July 2016.  Köln (Germany), Málaga (Spain) and Marseille (France) will take part alongside hosts Alemannia.  It will be sponsored by HappyBet.

Cranked Up Country Radio: Cranked Up Country Radio"®" - Is a syndicated weekly 3 hour country music show radio show and 1 hour country music video show hosted by Curtis McKinney and Brad Hennington.  The radio show is a combination of music, comedy, talk, and interviews along with the 'Advice from the Desk of Mr. Holland', the 'Cranked Up Five', 'Hick Picks', and the 'Joke of the Week'.  The video show is a compressed version of the radio show made from video recorded while making the radio show.  Cranked Up Country Radio is heard on over 20 FM, AM, and Digital Broadcasting stations.

Question: What hosted a radio show from 1995 to 2014 alongside hosts born in 1961 and 1968?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "radio_show_name": {
      "type": "string",
      "description": "The name of the radio show."
    },
    "broadcast_period": {
      "type": "object",
      "properties": {
        "start_year": {
          "type": "integer",
          "description": "The start year of the radio show's broadcast."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the radio show's broadcast."
        }
      },
      "required": [
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    },
    "hosts_involved": {
      "type": "array",
      "description": "A list of hosts involved with the radio show.",
      "items": {
        "type": "object",
        "properties": {
          "host_name": {
            "type": "string",
            "description": "The name of the host."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the host, if available."
          }
        },
        "required": [
          "host_name"
        ],
        "additionalProperties": false
      }
    },
    "identified_host_name": {
      "type": "string",
      "description": "The name of the host identified by the question."
    }
  },
  "required": [
    "radio_show_name",
    "broadcast_period",
    "hosts_involved",
    "identified_host_name"
  ],
  "additionalProperties": false
}

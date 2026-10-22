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
Mash Off: "Mash Off" is the sixth episode of the third season of the American musical television series "Glee", and the fiftieth overall.  The episode was written by Michael Hitchcock and directed by Eric Stoltz, and originally aired on Fox in the United States on November 15, 2011.  Special guest star Idina Menzel is featured as rival glee club director Shelby Corcoran, and she and Will Schuester (Matthew Morrison) hold a mash-up competition between the Troubletones and the New Directions.  Santana (Naya Rivera) mercilessly taunts rival glee club member Finn (Cory Monteith), who ultimately responds by publicly accusing her of cowardice in her relationship with Brittany, thereby revealing to their fellow students that she is a lesbian.  Sue Sylvester (Jane Lynch) starts a propaganda campaign against Burt Hummel (Mike O'Malley), her chief rival in the special election for congress.

New Directions (Glee): "New Directions" is the thirteenth episode of the fifth season of the American musical television series "Glee", and the one-hundred-first episode overall.  Written and directed by series co-creator Brad Falchuk, it aired on Fox in the United States on March 25, 2014, and is the second part of a two-part anniversary episode that features the apparent end of New Directions after the club is shut down by principal Sue Sylvester (Jane Lynch).  Many graduates of the glee club have returned, as do special guest stars Kristin Chenoweth as April Rhodes and Gwyneth Paltrow as Holly Holliday.  This is Melissa Benoist latest appearance on the show.

Bronwyn Lundberg: Bronwyn Lundberg is an American digital artist and painter specializing in graphic art.  She is notable for her painting of the "Lesbian Last Supper" of Sandra Bernhard, Ellen DeGeneres, Melissa Etheridge, k.d. Lang, Jane Lynch, Rachel Maddow, Heather Matarazzo, Kate Moennig, Rosie O'Donnell, Linda Perry, Portia de Rossi, Wanda Sykes, and Lily Tomlin.  Lundberg also collaborates with Sarah Zucker as the Pop Art team YoMeryl.

Funeral (Glee): "Funeral" is the twenty-first episode of the second season of the American musical television series "Glee", and the forty-third overall.  It first aired May 17, 2011 on Fox in the United States, and was written by series creator Ryan Murphy and directed by Bradley Buecker.  The episode featured Jonathan Groff guest starring as Jesse St. James, who is brought in as a consultant to help the New Directions glee club prepare for the National Show Choir competition.  Sue Sylvester's (Jane Lynch) sister Jean (Robin Trocki) dies unexpectedly, and the glee club helps Sue plan her funeral.

100 (Glee): "100" is the twelfth episode of the fifth season of the American musical television series "Glee", and the special one-hundredth episode of the show.  Written by series co-creators Ryan Murphy, Brad Falchuk and Ian Brennan, and directed by Paris Barclay, it aired on Fox in the United States on March 18, 2014.  This is a two-part episode, with the second part airing on March 25, 2014, and features the apparent end of New Directions after the club is shut down by principal Sue Sylvester (Jane Lynch).  Many graduates of the glee club return, as do special guest stars Kristin Chenoweth as April Rhodes and Gwyneth Paltrow as Holly Holliday.

Furt: "Furt" is the eighth episode of the second season of the American musical television series "Glee", and the thirtieth episode overall.  It was written by series creator Ryan Murphy, directed by Carol Banker, and premiered on Fox in the United States on November 23, 2010.  The episode features a guest appearance by actress Carol Burnett as a Nazi hunter and mother of cheerleading coach Sue Sylvester (Jane Lynch), who shows up for the first time in years, just in time to attend Sue's wedding to herself.  The long-anticipated wedding of Burt Hummel (Mike O'Malley) and Carole Hudson (Romy Rosemont) is also featured, and the bullying storyline reaches a climax that results in Kurt (Chris Colfer) transferring from McKinley High to Dalton Academy at the end of the episode.

Sue Sylvester: Susan Sylvester is a fictional character of the Fox musical comedy-drama series, "Glee".  Known as Sue Sylvester, the character is portrayed by actress Jane Lynch, and appears in "Glee" from its pilot episode, first broadcast on May 19, 2009, through the show's final episode, first broadcast on March 25, 2015.  Sue was developed by "Glee" creators Ryan Murphy, Brad Falchuk, and Ian Brennan.  For the show's first four seasons, Sue is the track-suit wearing coach of the William McKinley High School cheerleading squad, and a ruthless bully to both students and faculty members alike.  Because her cheerleading squad competes with the glee club for the school's limited funding, she is often at odds with the club and more particularly its director Will Schuester (Matthew Morrison).  Sue is the main antagonist throughout the series' run.  In the show's fifth season, Sue is made the school's new principal, though she is ultimately fired late in the show's sixth and final season.

Comeback (Glee): "Comeback" is the thirteenth episode of the second season of the American musical television series "Glee", and the thirty-fifth overall.  It was written by series creator Ryan Murphy, directed by Bradley Buecker, and premiered on Fox on February 15, 2011.  In the episode, glee club director Will Schuester (Matthew Morrison) allows cheerleading coach Sue Sylvester (Jane Lynch) to join the McKinley High glee club in an attempt to ease her depression.  Club member Sam (Chord Overstreet) creates a tribute band to teen singer Justin Bieber in order to win the heart of Quinn (Dianna Agron), and is later joined by the group's other male members, minus co-captain Finn (Cory Monteith), to recreate Bieber's "Somebody to Love" and woo their significant others.

Jane Lynch: Jane Marie Lynch (born July 14, 1960) is an American actress, singer, and comedian.  She is best known for her role as Sue Sylvester in the musical television series "Glee".  She also gained fame in Christopher Guest's improv mockumentary pictures such as "Best in Show".

The Sue Sylvester Shuffle: "The Sue Sylvester Shuffle" is the eleventh episode of the second season of the American musical television series "Glee", and the thirty-third episode overall.  It was written by Ian Brennan, directed by Brad Falchuk, and was broadcast immediately following Super Bowl XLV on February 6, 2011.  In the episode, an effort to dispel student rivalry forces the McKinley High football team and glee club to unite.  When cheerleading coach Sue Sylvester (Jane Lynch) withdraws her squad from the halftime show of a championship football game, the disparate groups must come together to perform a routine and win the game.

Question: Bronwyn Lundberg is an American digital artist and painter specializing in graphic art, she is notable for her painting of the "Lesbian Last Supper" of various women, including Jane Lynch, best known for her role as Sue Sylvester in which musical television series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "specialization": {
          "type": "string",
          "description": "The artistic specialization of the artist."
        },
        "notable_artwork": {
          "type": "string",
          "description": "The name of a notable artwork by the artist."
        }
      },
      "required": [
        "name",
        "specialization",
        "notable_artwork"
      ],
      "additionalProperties": false
    },
    "featured_person_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person featured in the artwork and question."
        },
        "known_role": {
          "type": "string",
          "description": "The specific role the person is best known for."
        }
      },
      "required": [
        "name",
        "known_role"
      ],
      "additionalProperties": false
    },
    "musical_tv_series": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the musical television series where the person played the known role."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_info",
    "featured_person_info",
    "musical_tv_series"
  ],
  "additionalProperties": false
}

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
America's Got Talent (season 6): Season six of "America's Got Talent", a reality television series, premiered on May 31, 2011, on NBC.  The show was hosted by Nick Cannon, while Piers Morgan, Sharon Osbourne and Howie Mandel returned as judges.  On September 14, 2011, Landau Eugene Murphy, Jr. was announced as the winner of season six.  This season was the last with Morgan as a judge, as he did not return for season 7, where Howard Stern replaced him.

Seinfeld (season 6): Season six of "Seinfeld", an American comedy television series created by Jerry Seinfeld and Larry David, began airing on September 22, 1994, and concluded on May 18, 1995, on NBC.  Season six placed first in the Nielsen ratings, above "Home Improvement" and "ER".

Stargate SG-1 (season 6): Season six of "Stargate SG-1", an American-Canadian television series, began airing on June 7, 2002 on Sci Fi.  The sixth season concluded after 22 episodes on February 19, 2003 on British Sky One, which overtook the Sci-Fi Channel in mid-season.  The series was developed by Brad Wright and Jonathan Glassner.  Season six regular cast members include Richard Dean Anderson, Amanda Tapping, Christopher Judge, Corin Nemec, and Don S. Davis.

Smallville (season 6): Season six of "Smallville", an American television series, began airing on September 28, 2006.  The series recounts the early adventures of Kryptonian Clark Kent as he adjusts to life in the fictional town of Smallville, Kansas, during the years before he becomes Superman.  The sixth season comprises 22 episodes and concluded its initial airing on May 17, 2007, marking the first season to air on the newly formed The CW television network.  Regular cast members during season six include Tom Welling, Kristin Kreuk, Michael Rosenbaum, Allison Mack, Annette O'Toole, John Glover, and Erica Durance.

South Park (season 6): Season six of "South Park", an American animated television series created by Trey Parker and Matt Stone, began airing on March 6, 2002.  The sixth season concluded after 17 episodes on December 11, 2002.  This season is notable for being the only one without Kenny as a main character, as he was written off in the previous season.  Kenny, however, plays a part in some episodes without appearing and returns at the conclusion of the final episode.

Drop Dead Diva (season 6): Drop Dead Diva season six and last season premiered March 23, 2014, and concluded on June 22, 2014, on Lifetime.  Season six aired on Sundays at 9:00 pm ET (6:00 pm PT) and consisted of 13 episodes.

South Park Let's Go Tower Defense Play!: South Park Let's Go Tower Defense Play!  is a 2009 video game based on the American animated television series "South Park", released on the Xbox Live Arcade service for the Xbox 360 video game console.  The game was developed by Doublesix in collaboration with South Park Digital Studios and Xbox Live Productions.  "Let's Go Tower Defense Play" is a tower defense game, with the added element of being a fast-paced action game as well.  Thus, players do not only build towers to eliminate destructive forces, but they also have to control multiple characters in order to successfully protect the town of South Park.  "South Park Let's Go Tower Defense Play!"  is the first "South Park" video game released after three early titles released between 1998 and 2000.

Trey Parker: Randolph Severn "Trey" Parker III (born October 19, 1969) is an American actor, animator, writer, director, producer, singer, and songwriter.  He is known for co-creating "South Park" (1997–present) along with his creative partner Matt Stone, as well as co-writing and co-directing the Tony Award-winning musical "The Book of Mormon" (2011).  Parker was interested in film and music as a child, and attended the University of Colorado, Boulder following high school, where he met Stone.  The two collaborated on various short films, and starred in a feature-length musical, titled "Cannibal!  The Musical" (1993).

So You Think You Can Dance (U.S. season 6): So You Think You Can Dance, also known as SYTYCD, is a United States television reality program and dance competition airing on the Fox Broadcasting Company network.  Season six premiered on Wednesday, September 9, 2009, with Nigel Lythgoe and Mary Murphy returning as permanent judges and Cat Deeley returning to host.  Season six is the first to air during the fall season, immediately following the summer airing of season five.  Live shows began airing October 26 and the season finale aired on December 16.  Russell Ferguson, the first krumper to make it to the Las Vegas auditions, won the title of "America's Favorite Dancer" and the $250,000 prize.  Also in the finale were Jakob Karr in second place, Kathryn McCormick in third place, Ellenore Scott in fourth place, Ashleigh Di Lello in fifth place and Ryan Di Lello in sixth place.

Full Circle (Stargate SG-1): "Full Circle" is the season finale for season six of the Canadian-American military science fiction television series "Stargate SG-1".  It was originally intended to be the last episode of "Stargate SG-1". The episode was written by executive producer Robert C. Cooper and directed by Martin Wood.  The episodes received an average Nielsen household rating and a low syndication rating compared to other season six episodes.  The episode got strong reviews from major media publishers worldwide.

Question:  Season six of "South Park" was created by the actor and animator of what nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tv_series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "season_number": {
      "type": "integer",
      "description": "The specific season number being referred to."
    },
    "creator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the creator who is an actor and animator."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the creator."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Key roles of the creator mentioned in the context."
        }
      },
      "required": [
        "name",
        "nationality",
        "roles"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "tv_series_name",
    "season_number",
    "creator_details"
  ],
  "additionalProperties": false
}

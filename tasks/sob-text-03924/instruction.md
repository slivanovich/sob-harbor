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
Peter Rabbit (TV series): Peter Rabbit (TV Series; 2012-2016) is a British/American CGI animated children's preschool television series that debuted on Nick Jr. on December 14, 2012 in the United States and on the CBeebies channel and BBC One on December 25, 2012 in the United Kingdom.  It is based on the character of the same name from the Beatrix Potter children's books.  The series debuted in 2012 with a holiday special, "Peter Rabbit's Christmas Tale", which was watched by three million viewers in the U.S.  The first official DVD of "Peter Rabbit" came out on May 28, 2013, as a Walmart exclusive.  it contains the show's first eight episodes on a single disc.  On October 11, 2013, Nickelodeon ordered a second season of 26 episodes.  The series is also dubbed in Welsh on the S4C channel as "Guto Gwningen".  The show ran for two seasons from 2012-2016 and was produced for Nickelodeon in the US by Brown Bag Films and Silvergate Media.  The show also aired on CBeebies in the UK.  There are currently no plans for a third season, and the show has not been worked on since its second season conclusion, with the final episode being released on May 6, 2016.

The World of Peter Rabbit and Friends: The World of Peter Rabbit and Friends is a British animated anthology television series based on the works of Beatrix Potter, featuring Peter Rabbit and other anthropomorphic animal characters created by Potter.  It was originally shown in the U.K. on the BBC between 1992 and 1995 and subsequently broadcast in the U.S. on Family Channel from 1993-1995 and ABC in Australia (29 September 1997 - 13 April 2009) (with some of the characters' voices dubbed by actors with more American-like accents).  The series has also been released on VHS by Carlton Home Entertainment in 1997 and again in 1999 and DVD in 2003, on DVD by BBC Home Media in 2006 and by Abbey Home Media in 2016.

Harrison Cady: Walter Harrison Cady (1877–1970) was an American illustrator and author, best known for his "Peter Rabbit" comic strip which he wrote and drew for 28 years.

Llewellynn Jewitt: Llewellynn Frederick William Jewitt (or Llewellyn) (24 November 1816 – 5 June 1886) was a noted illustrator, engraver, natural scientist and author of "The Ceramic Art of Great Britain" (1878).  His output was prodigious and covered a large range of interests.

Peter Rabbit: Peter Rabbit is a fictional animal character in various children's stories by Beatrix Potter.  He first appeared in "The Tale of Peter Rabbit" in 1902 and subsequently in five more books between 1904 and 1912.  Spinoff merchandise includes dishes, wallpaper, and dolls.  He appears as a character in a number of adaptations.

Brown Bag Films: Brown Bag Films, or Brown Bag, is an Irish-Canadian television animation production studio, based in Dublin, Ireland with a 2D facility based in Manchester, UK.  Best known for its character CGI-animated television series' and short films, including the Oscar nominated "Give Up Yer Aul Sins" and "Granny O'Grimm's Sleeping Beauty".  Brown Bag Films was established in 1994 by Cathal Gaffney and Darragh O'Connell and the studio has garnered a number of awards, including Academy Award nominations for "Give Up Yer Aul Sins" (Best Animated Short Film 2001) and "Granny O'Grimm's Sleeping Beauty" (Best Animated Short Film 2010), six Emmy Award wins for "Peter Rabbit", an Emmy award for "Bing" and a number of BAFTA, Emmy and Annie nominations for their shows "Octonauts", "Doc McStuffins" and "Henry Hugglemonster".

Beatrix Potter: Helen Beatrix Potter (28 July 186622 December 1943) was an English writer, illustrator, natural scientist, and conservationist best known for her children's books featuring animals, such as those in "The Tale of Peter Rabbit".

The Tales of Beatrix Potter: The Tales of Beatrix Potter (US title: "Peter Rabbit and Tales of Beatrix Potter") is a 1971 ballet film based on the children's stories of English author and illustrator Beatrix Potter.  The film was directed by Reginald Mills, choreographed by Sir Frederick Ashton (who danced the role of Mrs. Tiggy-Winkle), and featured dancers from the Royal Ballet.  The musical score was arranged by John Lanchbery from various sources, such as the operas of Michael Balfe and of Sir Arthur Sullivan, and performed by the Orchestra of the Royal Opera House.  It was designed and co-written by Christine Edzard.

Peter Rabbit (film): Peter Rabbit is an upcoming 2018 3D live-action/CGI animated adventure comedy film written, directed and produced by Will Gluck and co-written by Rob Lieber, based on the stories of the character of the same name created by Beatrix Potter.  The film features voice roles played by James Corden, Margot Robbie, Daisy Ridley and Elizabeth Debicki, and live-action roles played by Domhnall Gleeson, Rose Byrne and Sam Neill.  The film is scheduled to be released on February 9, 2018.  It is not, however, based on the recent British/American CGI-animated TV Series of the same name.

Miss Potter: Miss Potter is a 2006 Anglo-American biographical fiction family drama film directed by Chris Noonan.  It is a biographical film of children's author and illustrator Beatrix Potter, and combines stories from her own life with animated sequences featuring characters from her stories, such as Peter Rabbit.  Scripted by Richard Maltby, Jr., the director of the Tony-winning Broadway revue, "Fosse", the film stars Renée Zellweger in the title role; Ewan McGregor as her publisher and fiancé, Norman Warne; and Lloyd Owen as solicitor William Heelis.  Emily Watson stars as Warne's sister, Millie.  Lucy Boynton also stars as the young Beatrix Potter.  It was filmed in St. Peter's Square Hammersmith, Cecil Court, Osterley Park, Covent Garden, the Isle of Man, Scotland and the Lake District.  "Miss Potter" was released on 29 December 2006 so that the film could compete for the 2007 Academy Awards.  The film was intended to be released generally on 12 January 2007, but Variety.com reported that the Weinstein Company had decided to push a wider release date until after the Academy Awards on 25 February 2007.  The date seemed to fluctuate a number of times, but the Weinstein Company website ultimately listed its release date as 9 March.  The film received generally positive reviews and earned Zellweger her sixth Golden Globe nomination.

Question: Peter Rabbit is a 2018 film based on the character by what English writier, illustrator, natural scientist, and conservationist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The scheduled release year of the film."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character the film is based on."
    },
    "creator": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the character's creator."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the creator."
        },
        "occupations": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of occupations held by the creator."
        }
      },
      "required": [
        "full_name",
        "nationality",
        "occupations"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "character_name",
    "creator"
  ],
  "additionalProperties": false
}

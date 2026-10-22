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
List of Catfish episodes: "" is an American television series that began airing on MTV on November 12, 2012.  The second series began airing on June 25, 2013.  Season 3 and Season 4 were premiered on May 7, 2014 and February 25, 2015, respectively.  Season 5 began airing on February 24, 2016.

List of Hank Zipzer episodes: "Hank Zipzer" is a children's television series which stars Nick James in the titular role as a 12-year-old dyslexic schoolboy.  The show is based on the series of books by Henry Winkler, who plays the character of Mr. Rock, Hank's music teacher.  The first series premiered in January 2014 on CBBC and a second and third series have been commissioned.  Unlike the books that took place in America, the series takes place in Britain.  The second series began airing on 13 August 2015.  Javone Prince made his first appearance as Mr Joy in series 2, episode 5, "Hank's Hero".  The third series began airing on 26 May 2016, which was followed by an 84-minute Christmas movie on 12 December 2016.  A fourth series has been confirmed by Winkler.

Chop Socky Chooks: Chop Socky Chooks is a computer-animated series that ran on Cartoon Network from March 7, 2008 until January 31, 2010.  produced by Aardman Animations, Decode Entertainment, and Cartoon Network that debuted on 7 March 2008.  It was created by animator Sergio Delfino, a prominent animator at Sony Pictures Imageworks.  Reruns of the show currently air in Eastern Europe on Cartoon Network and on Teletoon, and previously aired in the USA on Cartoon Network.  The name is from "chop socky," which is slang for the Asian martial arts film genre, and "chook", which is Australian and New Zealand slang for chicken.

Lark Rise to Candleford (TV series): Lark Rise to Candleford is a British television costume drama series, adapted by the BBC from Flora Thompson's trilogy of semi-autobiographical novels about the English countryside, published between 1939 and 1943.  The first episode aired on 13 January 2008 on BBC One and BBC HD in the UK.  In the U.S., the series began airing on select PBS stations in the spring of 2009.  A third series began airing in the UK on 10 January 2010.  The fourth and final series began on 9 January 2011 on BBC One and BBC One HD, and was filmed during August 2010.

It Takes a Church: It Takes a Church is an American dating game show hosted by Natalie Grant and broadcast by Game Show Network.  The show travels to multiple churches across the country looking for single members of congregations looking for a partner.  The congregation of the church is primarily in charge of looking at potential daters and judging which one would be the best match.  The first season, sponsored by Christian Mingle, began airing on June 5, 2014.  The series was later renewed for a second season, which began airing March 26, 2015.

Turf War: Turf War is a reality television series that is a spinoff from Yard Crashers.  The show is hosted by licensed contractor Matt Blashaw and began airing March 8, 2010 on the DIY Network.  Season two began airing on April 11, 2011.  Ahmed Hassan, the original host of the show, was replaced at the end of 2011 by Matt Blashaw.

List of 4 O'Clock Club episodes: "4 O'Clock Club" is a British children's television series, which premiered on 13 January 2012 on CBBC and BBC HD.  A second series began airing on 4 January 2013, and the third series premiered on 20 December 2013.  Series 4 began airing on 29 January 2015.  A fifth series was commissioned, and was filmed between June 2015 and August 2015, and began airing on 25 February 2016.

The Glee Project: The Glee Project is an American reality television series from Oxygen.  It served as an audition for the Fox musical comedy series "Glee", and the prize for the winner was a minimum seven-episode arc in the following season of the show.  The show's first season premiered in the US on June 12, 2011, and concluded on August 21, 2011.  In Canada, the series began airing on Slice on June 26, 2011, and in the UK, the series began airing on Sky 1 on July 14, 2011.  A second season aired in the US from June 5 to August 14, 2012.  In July 2013, it was announced that "The Glee Project" would not return for a third season.

Ed, Edd n Eddy's Big Picture Show: Ed, Edd n Eddy's Big Picture Show is a 2009 animated road television film based on the animated series "Ed, Edd n Eddy".  It was produced by a.k.a. Cartoon and premiered on Cartoon Network in the United States, and Teletoon in Canada on November 8, 2009.  It serves as the series finale of "Ed, Edd n Eddy".  The film was directed by series creator Danny Antonucci, who co-wrote the film with Jono Howard, Mike Kubat, Rachel Connor, and Stacy Warnick.  The movie centers on Ed, Edd and Eddy's journey to find Eddy's unnamed (and previously unseen) older brother.

Mike Kubat: Mike Kubat is a Canadian television writer and story editor.  He has worked on such animated series as "Atomic Betty", "Chop Socky Chooks", and "Ed, Edd n Eddy".  In 2005, he received a Leo Award nomination for Best Screenwriter in an Animation Program or Series for the "Atomic Betty" episode "Spindly Tam Kanushu".  Kubat originally started out wanting to be in a rock band, later becoming an accountant, and finally settling comfortably in his career writing for animation.

Question: What Mike Kubat series began airing March 7, 2008

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_title": {
      "type": "string",
      "description": "The title of the television series."
    },
    "premiere_date": {
      "type": "string",
      "format": "date",
      "description": "The date the series began airing."
    },
    "person_involved": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person involved with the series."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the series (e.g., writer, story editor)."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "network": {
      "type": "string",
      "description": "The network on which the series premiered."
    }
  },
  "required": [
    "series_title",
    "premiere_date",
    "person_involved",
    "network"
  ],
  "additionalProperties": false
}

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
Jerry Springer: The Opera: Jerry Springer: The Opera is a British musical written by Richard Thomas and Stewart Lee, based on the television show "The Jerry Springer Show".  The musical contains irreverent treatment of Christian themes, extensive profanity, and surreal images, such as a troupe of tap-dancing Ku Klux Klan members.  The musical is completely sung through, with only two exceptions: the title character, Jerry, who speaks throughout the production; and Steve Wilkos, who has a brief speech.

CBS Television Distribution: CBS Television Distribution (CTD) is an American television distribution company, formed from the merger of CBS Corporation's domestic television distribution arms CBS Paramount Domestic Television and King World Productions, including its home entertainment arm CBS Home Entertainment.  The division, the main distribution arm of CBS Television Studios (formerly CBS Paramount Network Television) and of the CBS and CW television networks, was formed on September 26, 2006 by CBS Corporation and was headed by Roger King, the CEO of King World until his death in 2007.  The current president is Paul Franklin.

Don't Forget the Lyrics! (U.S. game show): Don't Forget the Lyrics!  is a game show that originally aired on Fox from July 11, 2007 to June 19, 2009, hosted by Wayne Brady and produced by RDF USA, part of RDF Media.  The launch of this show prompted NBC to move up the launch of their similar game show "The Singing Bee".  The show's contestants compete to win $1,000,000 by correctly recalling song lyrics from a variety of genres.

NBCUniversal Television Distribution: NBCUniversal Television Distribution (NUTD) is the television distribution arm of the NBCUniversal Television Group in the United States, and is a subsidiary of Comcast.  Its predecessors include NBC Enterprises, Universal Domestic Television, MCA Television, Avco Embassy Television, Multimedia Entertainment, PolyGram Television and Studios USA Television.

Steve Wilkos: Steven John "Steve" Wilkos ( ; born March 9, 1964) is an American television personality, a veteran of the United States Marine Corps and a former law enforcement officer with the Chicago Police Department.  He has been hosting "The Steve Wilkos Show" since 2007, and was director of security on "The Jerry Springer Show" from 1994 to 2007.  He had previously substituted for Springer as host on several occasions before being given his own talk show.

Kwik Witz: Kwik Witz is an American syndicated comedy program which aired in syndication, mainly on numerous NBC affiliate stations—usually in the time-slot following "Saturday Night Live".  The show originated from the NBC Tower studios of WMAQ-TV in Chicago, Illinois and was produced by Beau & Arrow Productions.  The show shared studio space with The Jenny Jones Show, which was located immediately across from The Jerry Springer Show studio.

Hardcore Pawn: Hardcore Pawn is an American reality television series produced by RDF USA (later Zodiak USA) and Richard Dominick Productions for truTV about the day-to-day operations of American Jewelry and Loan, a family-owned and operated Pawn shop and broker in Detroit, Michigan's 8 Mile Road corridor.

The Jerry Springer Show: The Jerry Springer Show (also known as Jerry Springer, or simply Springer) is an American syndicated tabloid talk show hosted by Jerry Springer, a former politician.  The program tapes at the Rich Forum in Stamford, Connecticut, which is alternately known as the Stamford Media Center and is distributed by NBCUniversal Television Distribution.

Richard Dominick: Richard Dominick was the executive producer of NBC Universal Domestic Television Distribution's "The Jerry Springer Show" for almost 18 years.  Dominick also served in the same capacity on "The Steve Wilkos Show" for its first season, as well as the truTV police series "Bait Car".  He now produces (and created) another popular truTV series, "Hardcore Pawn".

Team Knight Rider: Team Knight Rider (TKR) is a syndicated television series that was adapted from the "Knight Rider" franchise and ran between 1997 and 1998.  "TKR" was created by writer/producers Rick Copp and David A. Goodman, based on the original series created by Glen A. Larson, who was an executive producer.  "TKR" was produced by Gil Wadsworth and Scott McAboy and was distributed by Universal Domestic Television and ran only a single season of 22 one-hour episodes before it was canceled due to poor ratings.

Question: Richard Dominick was the executive producer of NBC Universal Domestic Television Distribution's "The Jerry Springer Show" for almost 18 years, and he now produces (and created) another popular which truTV series, produced by RDF USA (later Zodiak USA) and Richard Dominick Productions?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the truTV series."
    },
    "network": {
      "type": "string",
      "description": "The television network on which the series airs."
    },
    "richard_dominick_involvement": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "description": "Richard Dominick's role in the series (e.g., creator, producer)."
        },
        "production_company": {
          "type": "string",
          "description": "Richard Dominick's associated production company."
        }
      },
      "required": [
        "role",
        "production_company"
      ],
      "additionalProperties": false
    },
    "other_production_companies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "The name of another production company."
          },
          "notes": {
            "type": "string",
            "description": "Any additional notes about the company, such as name changes."
          }
        },
        "required": [
          "company_name"
        ],
        "additionalProperties": false
      },
      "description": "A list of other production companies involved in the series."
    }
  },
  "required": [
    "series_name",
    "network",
    "richard_dominick_involvement",
    "other_production_companies"
  ],
  "additionalProperties": false
}

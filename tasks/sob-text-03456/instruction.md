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
List of awards and nominations received by Feist: Feist is a Canadian singer-songwriter from Amherst, Nova Scotia.  She has released four studio albums as a member of the indie rock supergroup Broken Social Scene: "Feel Good Lost" (2001), "You Forgot It in People" (2002), "Bee Hives" (2004), and "Broken Social Scene" (2005).  All four albums were released with the Arts & Crafts record label.  She has also released four studio albums as a solo artist: "Monarch (Lay Your Jewelled Head Down)" (1999), "Let It Die" (2004), "Open Season" (2006), and "The Reminder" (2007).  These four albums were also released with the Arts & Crafts record label, with the exception of her first album, which was released by the Bobby Dazzler record label.

Justin Peroff: Justin Peter Papadimitriou (born October 13, 1977), family name changed to Peroff, is best known as the drummer for the Toronto based indie rock collective Broken Social Scene.  He is a credited actor, appearing in the major motion picture "How to Lose a Guy in 10 Days" and the Canadian television shows "Straight Up" and "Our Hero".  Peroff is a known DJ, spinning Broken Social Scene after parties worldwide and when stationed in his home town of Toronto.  He also fulfills bi-weekly and monthly DJ gigs at clubs and bars citywide.  Peroff is also an event promoter and artist manager, managing Toronto based producer / musician and Last Gang artist Harrison and Toronto based neo-soul singer / artist and film maker M.I. Blue.

Something for All of Us...: Something for All of Us... is the debut solo album by Broken Social Scene co-founder Brendan Canning.  The album is the second in a series entitled "Broken Social Scene Presents:", with each album in the series being a particular member's solo efforts, assisted by fellow Broken Social Scene members—the first being Kevin Drew's "Spirit If...".

Andrew Kenny: Andrew Kenny is the main singer/songwriter of The Wooden Birds, which released their debut LP "Magnolia" in May 2009.  Their second album, "Two Matchsticks", was released June 2011.  He was the frontman for the American indie/lo-fi band The American Analog Set.  In 2004, he released a split EP in the Home Series (Vol.  V) with Benjamin Gibbard.  In 2005, he contributed towards Broken Social Scene's 2005 self-titled album.  Andrew Kenny toured briefly with Broken Social Scene in 2007 and with Ola Podrida in 2008 before moving back home to Austin to work on his own recordings.

The Happiness Project: The Happiness Project is the title of Charles Spearin's debut album.  Best known for his work with Toronto-based bands Do Make Say Think and Broken Social Scene, Charles Spearin has been performing samples of The Happiness Project live during Broken Social Scene concerts this past year, offering insight into the inspiration and concept of the album, which has been long-listed for the 2009 Polaris Music Prize.  On April 17, 2010, Spearin won a Juno Award for the Best Contemporary Jazz Album for the "The Happiness Project".

Spirit If...: Spirit If... is the debut solo album by Broken Social Scene co-founder Kevin Drew.  It was released on September 18, 2007.  The album is the first in a series entitled "Broken Social Scene Presents:", with each album in the series being a particular member's solo efforts, assisted by fellow Broken Social Scene members.  Brendan Canning's album "Something for All of Us", the second in the series, was released in 2008.

Kevin Drew: Kevin Drew (born September 9, 1976) is a Canadian musician and songwriter who, together with Brendan Canning, founded the expansive Toronto baroque-pop collective Broken Social Scene.  He was also part of the lesser-known KC Accidental, which consisted of Drew and Charles Spearin, another current member of Broken Social Scene.

Broken Social Scene: Broken Social Scene is a Canadian indie rock band, a musical collective including as few as six and as many as nineteen members, formed by Kevin Drew and Brendan Canning.  Most of its members play in various other groups and solo projects, mainly in the city of Toronto.  These associated acts include Metric, Feist, Stars, Apostle of Hustle, Do Make Say Think, KC Accidental, Emily Haines & The Soft Skeleton, Amy Millan, and Jason Collett.

Daniel Amos: Daniel Amos (aka D. A., Dä) is an American Christian rock band formed in 1974 by Terry Scott Taylor on guitars and vocals, Marty Dieckmeyer on bass guitar, Steve Baxter on guitars and Jerry Chamberlain on lead guitars.  Current members include bassist Tim Chandler, guitarist Greg Flesch and drummer Ed McTaggart.  Over the band's career, they have experimented with country rock, rock, new wave, and alternative rock.

Broken Social Scene (album): Broken Social Scene is the third studio album by Broken Social Scene, released on October 4, 2005.  In addition to the musicians who contributed to the band's prior release "You Forgot It in People", new contributors on "Broken Social Scene" include k-os, Jason Tait (The Weakerthans) and Murray Lightburn (The Dears).

Question: Which band has more members, Broken Social Scene or Daniel Amos?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_summary": {
      "type": "string",
      "description": "A summary of the comparison between the two bands' member counts."
    },
    "bands_data": {
      "type": "array",
      "description": "Details about each band compared.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "member_details": {
            "type": "object",
            "properties": {
              "member_count_description": {
                "type": "string",
                "description": "A textual description of the band's member count from the context."
              },
              "min_members": {
                "type": "integer",
                "description": "The minimum number of members, if specified as a range."
              },
              "max_members": {
                "type": "integer",
                "description": "The maximum number of members, if specified as a range."
              },
              "founding_members_count": {
                "type": "integer",
                "description": "The number of founding members, if specified."
              },
              "current_members_count": {
                "type": "integer",
                "description": "The number of current members, if specified."
              }
            },
            "required": [
              "member_count_description"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "band_name",
          "member_details"
        ],
        "additionalProperties": false
      }
    },
    "band_with_more_members": {
      "type": "string",
      "description": "The name of the band identified as having more members."
    }
  },
  "required": [
    "comparison_summary",
    "bands_data",
    "band_with_more_members"
  ],
  "additionalProperties": false
}

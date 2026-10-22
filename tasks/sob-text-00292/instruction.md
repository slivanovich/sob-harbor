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
Simon M. Woods: Simon M. Woods is a British entrepreneur and former record producer.  Woods was the manager for the band UB40 after having seen them play at a pub, and turned down two offers on their behalf to release under 2 Tone Records, opting to release "Food For Thought" through another label, Graduate, before setting up Dep International that recorded and released UB40 internationally with enormous success.  Woods left the band in 1983 and started his own label, to which he signed Swans Way.  Woods ran his own marketing company before being hired on by the Birmingham School of Acting, and founded the European Drama Network, a film production company which makes movies based on classic plays.  Their first movie was "The Mandrake Root"; it was directed by Malachi Bogdanov and is based on a comedy written in 1512 by Niccolò Machiavelli.  In a co-production with Warwick Business School he wrote and directed "The Inferno Show presents Machiavelli The Prince of Comedy", a short comedy to celebrate the 500th anniversary of the writing of "The Prince".  Currently he is developing a movie, "From Ithaca With Love The Odyssey", a modern version of Homer's "The Odyssey" set in the modern day but made in Ancient Greek and Latin, loosely based on a play of the same name he produced in 2006 with director Malachi Bogdanov as part of the New Generation Arts Festival.

Gramercy Pictures: Gramercy Pictures is a currently-inactive American film production label of Universal Studios' Focus Features division.  It was originally launched as a film distributor in May 1992 as a joint venture of PolyGram Filmed Entertainment and Universal Pictures.  Gramercy was the distributor of PolyGram movies in the United States and Canada, and also served as Universal's art-house division.  After Seagram's buyout on PolyGram, Gramercy, along with October Films, was merged by Barry Diller, to form USA Films in 1999.  In 2015, Focus Features (the current art-house division for Universal) revived the name as a label for action, horror and sci-fi genre films.

Charlee Johnson: Charlee Johnson (also Charlee Johnsson) is an American drummer, guitarist and songwriter, originally from San Bernardino, California.  Johnson was a founding member and chief songwriter of Utah punk band Deviance / 3½ Girls.  The band relocated to Boston, Massachusetts and signed with Curve of the Earth Records for their sole EP, "Rule".  Johnson then left to form Halfcocked (then known as Half Cocked) with guitarist Tommy O'Neil, bassist/backing vocalist Jhen Kobran and lead vocalist Sarah Reitkopp, later adding guitarist Johnny Rock Heatley who guested on debut album Sell Out (Halfcocked album) and joined as a full member with second album .  Halfcocked relocated to Los Angeles and signed with DreamWorks in early 2000 by Powerman 5000 frontman Spider One, released final album The Last Star in 2001 (produced by Ulrich Wild), then folded after a brief tour.  Johnsson went on to join childhood hero Danzig for a brief stint as "Charlee X", before joining award-winning Nirvana tribute band, Pennyroyal.

Reconcile (rapper): Ronald Stephen "Ronnie" Lillard, Jr. (born March 20, 1989), known by the stage name Reconcile, is an American hip hop recording artist.  Reconcile gained notoriety after releasing a free project entitled "Abandoned Hope" in 2012 on Full Ride Music, a label founded by rapper Thi'sl.  His second album, "Sacrifice", was released in 2014 on the Frontline Movement label.  "Sacrifice" was his first album to chart on the "Billboard" charts.  Reconcile signed a production contract with Street Symphony's Track or Die production label in 2015.  His follow-up release, "Catchin' Bodies" was released on September 18, 2015.

Prince Entertainment P4: Prince Entertainment P4 is an Indian film production company operating from Kolkata, West Bengal.  "Prince Entertainment P4" is doing full length Bengali feature film production and distribution.  Pijush Saha is the head of the company.  Along with film production, this company is doing production of various Bengali television serials.

New Line Cinema: New Line Cinema is an American film production label of Warner Bros.  Entertainment that was founded in 1967 by Robert Shaye as a film distribution company, later becoming an independent film studio.  It became a subsidiary of the Turner Broadcasting System in 1994 before Turner merged with Time Warner in 1996, and was later merged with its larger sister studio Warner Bros.  Entertainment in 2008.  Currently, its films are distributed by Warner Bros.

Hollywood Pictures: Hollywood Pictures was an American film production label of The Walt Disney Studios, a division of The Walt Disney Company.  Similar to Disney's Touchstone Pictures and former Miramax and Dimension film labels, it produced films for a more mature adult audience than Walt Disney Pictures and Disneynature.  The label's metonym was the Sphinx.

DreamWorks: DreamWorks Pictures (also known as DreamWorks SKG or DreamWorks Studios, commonly referred to as DreamWorks, trading as Storyteller Distribution Co., LLC) is an American film production label of Amblin Partners.  The studio was formerly distributing its own and third-party films by itself.  It has produced or distributed more than ten films with box-office grosses of more than $100 million each.  As of October 2016, DreamWorks' films are marketed and distributed by Universal Pictures.

Dark Castle Entertainment: Dark Castle Entertainment is an American film production label, it is a division of Silver Pictures, a production house formally affiliated with Warner Bros., now affiliated with Universal Studios.  It was formed in 1999 by Joel Silver, Robert Zemeckis, and Gilbert Adler.  Susan Downey was the Vice President of Development until February 2009, a term running congruent to her tenure as a VP of Production at parent company Silver Pictures.

Fox Atomic: Fox Atomic was a production label of film studio 20th Century Fox created in 2006 to generate comedy and genre films.

Question: Charlee Johnson was part of a band that signed with a film production label of what company in 2000?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band the musician was part of."
    },
    "signing_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the band signed with the label."
        },
        "label_name": {
          "type": "string",
          "description": "The name of the production label the band signed with."
        },
        "label_type": {
          "type": "string",
          "description": "The type of label (e.g., film production label)."
        }
      },
      "required": [
        "year",
        "label_name",
        "label_type"
      ],
      "additionalProperties": false
    },
    "parent_company": {
      "type": "string",
      "description": "The name of the parent company of the production label."
    }
  },
  "required": [
    "musician_name",
    "band_name",
    "signing_details",
    "parent_company"
  ],
  "additionalProperties": false
}

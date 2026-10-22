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
Jericho (missile): Jericho is a general designation given to a loosely related family of deployed ballistic missiles developed by Israel from the 1960s forward.  The name is taken from the first development contract for the Jericho I signed between Israel and Dassault in 1963, with the codename as a reference to the Biblical city of Jericho.  As with most Israeli unconventional weapons systems, exact details are classified, though there are observed test data, public statements by government officials, and details in open literature especially about the Shavit satellite launch vehicle.  The later Jericho family development is related to the Shavit and Shavit II space launch vehicles believed to be derivatives of the Jericho II IRBM and which preceded the development of the Jericho III ICBM.  The Lawrence Livermore National Laboratory concluded that the Shavit could be adapted as an ICBM carrying 500 kg warhead over 7500 km.  Additional insight into the Jericho program was revealed by the South African series of missiles, of which the RSA-3 are believed to be licensed copies of the Jericho II/Shavit, and the RSA-4 that used part of these systems in their stack with a heavy first stage.  Subsequent to the declaration and disarming of the Nuclear programme of South Africa, the RSA series missiles were offered commercially as satellite launch vehicles, resulting in the advertised specifications becoming part of the public knowledge.  The civilian space launch version of the Jericho, the Shavit, has been studied in an air launched version piggybacked on a Boeing 747 similar to a US experimental launch of the Minuteman ICBM from a C-5 Galaxy.

List of Fozzy band members: The following is a list of musicians who have been members of American heavy metal band Fozzy since their formation in San Antonio, Texas in 1999.  The current lineup consists of three of the original members of the band: vocalist Chris Jericho, guitarist Rich Ward, and drummer Frank Fontsere.

A Lion's Tale: A Lion's Tale: Around the World in Spandex is an autobiography of professional wrestler, Chris Jericho.  It details his life from his early years, to his début for World Wrestling Entertainment (WWE), on August 9, 1999.  The book is followed by a sequel, "", which was released in 2011.  A second sequel, "Best in the World (At What I Have No Idea)", was released in 2014.

Chris Jericho: Christopher Keith Irvine (born November 9, 1970), better known by the ring name Chris Jericho, is a Canadian-American professional wrestler, musician, media personality, actor, author, podcaster, and businessman signed to WWE on the SmackDown brand, where he is currently on a hiatus due to an expected tour with Fozzy.  He is known for his over-the-top, rockstar persona.

King of the Ring (2001): King of the Ring (2001) was the ninth annual King of the Ring professional wrestling pay-per-view (PPV) event produced by the World Wrestling Federation (WWF).  It was the final King of the Ring tournament held under the WWF name.  It was presented by Mars' Combos and took place on June 24, 2001, at the Continental Airlines Arena in East Rutherford, New Jersey.  The main event was a Triple threat match, a match involving three competitors, for the WWF Championship.  Stone Cold Steve Austin defeated Chris Benoit and Chris Jericho to retain the title.  The undercard featured the 2001 King of the Ring tournament won by Edge.

Robbie Brookside: Robert Edward Brooks (born 11 March 1966), better known by his ring name Robbie Brookside, is an English retired professional wrestler.  He is signed to WWE, where he works as a trainer in its developmental territory NXT.  He has toured all over the world during his career, wrestling in the United States, Japan, Germany, and Mexico.  He was a regular tag partner of Steve Regal in the United Kingdom and has competed in New Japan Pro Wrestling's annual tournament, the Super J, in 1997, where he picked up a victory over Chris Jericho.

Hart wrestling family: The Hart wrestling family, sometimes known as the Hart dynasty is a mainly Canadian family with a significant history within professional wrestling.  The patriarch of the family was wrestling legend Stu Hart (1915–2003).  An amateur and professional wrestling performer, promoter and trainer, Stu not only owned and operated his own wrestling promotion, Stampede Wrestling, but also trained some of the most well known and successful stars in wrestling history including Superstar Billy Graham, Fritz Von Erich, Edge, Chris Jericho, Chris Benoit, Christian and his sons Bret Hart and Owen Hart.  All of Stu's eight sons were wrestlers and two of them, Bret and Owen, achieved considerable fame and success in the World Wrestling Federation (WWF, now WWE), with many of the WWF's biggest storylines in the mid-1990s being built around Bret and Owen and their brothers-in-law.

Fozzy: Fozzy is an American heavy metal band formed in Atlanta, Georgia, in 1999 by lead singer Chris Jericho and guitarist Rich Ward.  The band is currently signed to Century Media Records and has released two studio albums through this label.  The band's current lineup consists of Chris Jericho, Rich Ward, Frank Fontsere, Billy Grey and Paul Di Leo.  Jericho has characterized the band by saying, "If Metallica and Journey had a bastard child, it would be Fozzy."  As of July 2014, the band has released six studio albums and one live album.

The Rise and Fall of ECW: The Rise and Fall of ECW is a 2004 direct-to-video documentary produced by World Wrestling Entertainment.  It chronicles the history of Philadelphia-based professional wrestling promotion Extreme Championship Wrestling.  The documentary features interviews with various performers who worked in the promotion including co-founder and former owner Paul Heyman as well as performers Tazz, Tommy Dreamer, Dawn Marie, Stevie Richards, Mick Foley, Chris Jericho, Lance Storm, Rey Mysterio, Eddie Guerrero, Chris Benoit, Rob Van Dam, Rhyno, Nunzio, Spike Dudley, Bubba Ray Dudley and D'Von Dudley.  A book with the same title was published by WWE and Pocket Books in 2006 with much of the same information and interviews from the DVD transcribed and included.

Jeri-Show: Jeri-Show was a villianous professional wrestling tag team consisting of Big Show and Chris Jericho, which competed in the World Wrestling Entertainment (WWE) promotion.

Question:  Where were both Chris Jericho and Robbie Brookside signed to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "wrestlers_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the wrestlers mentioned in the question."
    },
    "common_organization": {
      "type": "string",
      "description": "The organization to which both wrestlers were signed."
    },
    "organization_type": {
      "type": "string",
      "description": "The type of organization (e.g., wrestling promotion)."
    }
  },
  "required": [
    "wrestlers_involved",
    "common_organization",
    "organization_type"
  ],
  "additionalProperties": false
}

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
Maintenance of Religious Harmony Act: The Maintenance of Religious Harmony Act ("MRHA") is a Singapore statute which, according to its long title, provides for the maintenance of religious harmony, for the establishment of a Presidential Council for Religious Harmony ("PCRH"), and for matters connected therewith.  The Act, which was passed on 9 November 1990 and came into force on 31 March 1992, empowers the Minister for Home Affairs to make a restraining order against a person who is in a position of authority in any religious group or institution if the Minister is satisfied that the person has committed or is attempting to commit any of the following acts: causing feelings of enmity, hatred, ill-will or hostility between different religious groups; or promoting a political cause, carrying out subversive activities, or exciting disaffection against the President or the Government under the guise of propagating or practising a religious belief.  A restraining order may also be made against a person who incites, instigates or encourages any religious leader or any religious group or institution to commit the above acts; or a person who is not a religious leader who causes or attempts to cause feelings of enmity, hatred, ill-will or hostility between different religious groups.  A restraining order made against a religious leader may direct that he or she must obtain the permission of the Minister before addressing members of any religious group or institution, assisting or contributing to religious publications, or holding office in the editorial board or committee of such publications.  Breaching a restraining order is a criminal offence.

Prejudgment writ of attachment: A prejudgment writ of attachment may be ordered in a legal action where a plaintiff has demonstrated meritorious allegations, fraud in the underlying action, or that defendant may attempt to dispose of or hide assets from the court.  In this context, a prejudgment writ of attachment functions much like a temporary restraining order (TRO), which preserves the status quo pending a final resolution of the dispute.  However, unlike a TRO, a prejudgment writ of attachment provides a source of financial recovery for a plaintiff.  Usually, a plaintiff seeking a prejudgment writ of attachment must post a surety bond of up to two times the amount of the damages claimed by the plaintiff.

Harassment Restraining Order: A Harassment Restraining Order (HRO) is a form of restraining order or order of protection used in the state of Wisconsin and enforceable nationwide under invocation of the Full Faith and Credit Clause in the Violence Against Women Act ( /2265 § 2265  ).  It is a legal intervention in which a person who is deemed to be harassing, threatening or stalking another person is ordered to stop, with the goal of reducing risk of further threat or harm to the person being harassed.  It is not limited to any particular type of relationship between the parties.  However, a closely related form of injunction, a Domestic Abuse Restraining Order (DARO) has slightly more restrictive conditions but is only granted to petitioners in specific relationships with their abusers.

Civil Harassment Restraining Order: A Civil Harassment Restraining Order (CHO) is a form of restraining order or order of protection used in the state of California.  It is a legal intervention in which a person who is deemed to be harassing, threatening or stalking another person is ordered to stop, with the goal of reducing risk of further threat or harm to the person being harassed.  Some restraining orders are limited to domestic partners, but the CHO is not.  It is frequently used with the purpose of preventing harassment by co-workers, neighbours, strangers and acquaintances.

Provisional measure of protection: A provisional measure of protection is the term that the International Court of Justice (ICJ, World Court) uses to describe a procedure "roughly equivalent" to an interim order (which can be either a temporary restraining order or a temporary directive order) in national legal systems.  The carrying out of the procedure is termed "indicating" the provisional measure of protection.  Requests for the indication of provisional measures of protection take priority over all other cases before the ICJ due to their urgency.

Protests against Executive Order 13769: During the protests against Executive Order 13769, also referred to as the protests against Trump's travel ban or protests against Trump's Muslim ban, thousands of people gathered at various airports in the United States and around the world to prevent the returning of refugees and other visitors from seven countries considered unsafe.  According to various sources, more than 2,000 people were at the protest at John F. Kennedy International Airport in Queens, New York City with other protests appearing at significant international airports and other important sites around the United States.  Protests continued daily and internationally through February 6.  Protests also continued after a federal judge issued a temporary restraining order against parts of the travel ban.

Richard Farley: Richard Wade Farley (born July 25, 1948) is an American convicted mass murderer.  A former employee of ESL Incorporated in Sunnyvale, California, he stalked co-worker Laura Black for four years beginning in 1984.  Black obtained a temporary restraining order against him on February 2, 1988, with a court date set for February 17, 1988 to make the order permanent.

Restraining order: A restraining order or protective order is an order used by a court to protect a person, business, company, establishment, or entity, and the general public, in a situation involving alleged domestic violence, harassment, stalking, or sexual assault.  In the United States, every state has some form of domestic violence restraining order law, and many states also have specific restraining order laws for stalking and sexual assault.

I Can Make You Love Me: I Can Make You Love Me, also known as Stalking Laura, is an American made-for-television film starring Richard Thomas and Brooke Shields.  The film is based on the real-life story of American mass murderer Richard Farley, a former employee of ESL Incorporated whose romantic obsession and subsequent stalking of co-worker Laura Black culminated in the mass murder of several co-workers at ESL's headquarters in California, resulting in the first anti-stalking laws to be enacted in the United States.  The first half of the film covers the events of the stalking and Black's unrequited love that led to the shootings, while the second half deals with Farley's rampage on the ESL offices.

GSIS-Meralco bribery case: The GSIS-Meralco case is a political controversy and pending legal case being heard by the Supreme Court of the Philippines.  This complex case began with a complaint filed by the Philippines' Government Service Insurance System (GSIS) with the Securities and Exchange Commission of the Philippines (SEC) questioning the unvalidated proxy votes used by the Lopez family in a board election of the Manila Electric Company (Meralco).  The SEC issued a cease and desist order (CDO) against Meralco, which was ignored by the latter.  A show cause order (SCO) was then issued by the SEC, whereupon Meralco petitioned the Court of Appeals, questioning the jurisdiction of the SEC.  The Court of Appeals issued a temporary restraining order (TRO) to the SEC while the Special 9th Division composed of Associate Justices Vicente Q. Roxas, Jose L. Sabio Jr. and Myrna Dimaranan Vidal heard the case.  Roxas was assigned as the ponente while Sabio was the acting chairman.

Question: When did Laura Black get a temporary restraining order against the person "I Can Make You Love Me" is based on?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "restraining_order_details": {
      "type": "object",
      "properties": {
        "order_type": {
          "type": "string",
          "description": "The type of restraining order issued."
        },
        "issue_date": {
          "type": "string",
          "format": "date",
          "description": "The date the restraining order was obtained."
        }
      },
      "required": [
        "order_type",
        "issue_date"
      ],
      "additionalProperties": false
    },
    "parties_involved": {
      "type": "object",
      "properties": {
        "petitioner": {
          "type": "string",
          "description": "The person who obtained the restraining order."
        },
        "respondent": {
          "type": "string",
          "description": "The person against whom the restraining order was issued."
        }
      },
      "required": [
        "petitioner",
        "respondent"
      ],
      "additionalProperties": false
    },
    "related_media": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film based on the events."
        }
      },
      "required": [
        "film_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "restraining_order_details",
    "parties_involved",
    "related_media"
  ],
  "additionalProperties": false
}

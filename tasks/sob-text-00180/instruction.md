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
Protestant Revolution (Maryland): The Protestant Revolution of 1689, sometimes called "Coode's Rebellion" after one of its leaders, John Coode, took place in the Province of Maryland when Puritans, by then a substantial majority in the colony, revolted against the proprietary government led by the Roman Catholic Charles Calvert, 3rd Baron Baltimore.  The rebellion followed the "Glorious Revolution" in England of 1688, which saw the Protestant Monarchs William III and Mary II, replace the English, Catholic monarch, King James II.  The Lords Baltimore lost control of their proprietary colony, and for the next 25 years, Maryland would be ruled directly by the British Crown.  The Protestant Revolution also saw the effective end of Maryland's early experiments with religious toleration, as Catholicism was outlawed, and Roman Catholics forbidden from holding public office.  Religious toleration would not be restored in Maryland until after the American Revolution.

Glorious Revolution: The Glorious Revolution, also called the Revolution of 1688, was the overthrow of King James II of England (James VII of Scotland) by a union of English Parliamentarians with the Dutch stadtholder William III, Prince of Orange.  William's successful invasion of England with a Dutch fleet and army led to his ascension to the throne as William III of England jointly with his wife, Mary II, James's daughter, after the Declaration of Right, leading to the Bill of Rights 1689.

Leisler's Rebellion: Leisler's Rebellion was an uprising in late 17th century colonial New York in which German American merchant and militia captain Jacob Leisler seized control of the colony's south and ruled it from 1689 to 1691.  The uprising took place in the aftermath of Britain's Glorious Revolution and the 1689 Boston revolt in the Dominion of New England, which had included New York.  The rebellion reflected colonial resentment against the policies of deposed King James II.

Saur Revolution: The Saur Revolution (Dari: إنقلاب ثور Pashto: د ثور انقلاب‎ ) (also Sawr Revolution) was a revolution led by the People's Democratic Party of Afghanistan (PDPA) against the rule of self-proclaimed Afghan President Mohammed Daoud Khan on 27–28 April 1978.  The government at the time was led by Daoud, who had previously overthrown his cousin King Mohammed Zahir in 1973.  "Saur" is the Dari name of the second month of the Persian calendar, the month in which the uprising took place.  The revolution led to the 1979 intervention by the Soviets and the 1979–1989 Soviet–Afghan War against the Mujahideen.

Irish Fright: The Irish Fright was a mass panic that took place in England in December 1688, during the Glorious Revolution.  It accompanied the final days of King James II's regime after his initially thwarted attempt to flee into exile in France.  Troops of the Jacobite Irish Army were stationed in England to prop up James II's authority but were widely detested by the predominately Protestant population of England.

Jacobite Peerage: After the deposition by the English parliament in February 1689 of King James II and VII from the thrones of England and Ireland (the Scottish Estates followed suit on 11 April 1689), he and his successors continued to create peers and baronets, which they believed was their right.  These creations were not recognised by James's "de facto" successors or British law, but the titles were used in Jacobite circles in Continental Europe and recognised by France, Spain and the Papacy.  The following tables list the peerages and baronetcies created by the Stuart claimants in exile.  The tables present the situation from the Jacobite perspective, and so titles granted after 1689 by King James II & VII's "de facto" successors to the throne, whose authority was not recognised by Jacobites, are represented in inverted commas.

Argyll's Rising: Argyll's Rising or Argyll's Rebellion was a 1685 attempt by a group of largely Scottish exiles, led by Archibald Campbell, 9th Earl of Argyll, to overthrow King James II and VII.  It took place shortly before and in support of the Monmouth Rebellion, led by James Scott, 1st Duke of Monmouth.  Argyll's Rising was intended to tie down Royal forces in Scotland while Monmouth's army marched on London.  Both rebellions were backed by Protestants opposed to the kingship of James, a Roman Catholic.

Francis Nicholson: Francis Nicholson (12 November 1655 – March 16, 1728 [O.S. March 5, 1727] ) was a British military officer and colonial administrator.  His military service included time in Africa and Europe, after which he was sent to North America as leader of the troops supporting Governor, Sir Edmund Andros in the Dominion of New England.  There he distinguished himself, and was appointed lieutenant governor of the Dominion in 1688.  After news of the Glorious Revolution and the overthrow of King James II reached the colonies in 1689, Andros was himself overthrown in the Boston Revolt.  Nicholson himself was soon caught up in the civil unrest from Leisler's Rebellion in New York Town, and afterwards fled to England.

Monmouth Rebellion: The Monmouth Rebellion, also known as The Revolt of the West or The West Country rebellion, was an attempt to overthrow James II, the Duke of York who had become King of England, Scotland, and Ireland upon the death of his elder brother Charles II on 6 February 1685.  James II was a Roman Catholic, and some Protestants under his rule opposed his kingship.  James Scott, 1st Duke of Monmouth, an illegitimate son of Charles II, claimed to be rightful heir to the throne and attempted to displace James II.

Gove's Rebellion: Gove's Rebellion was a short uprising in 1683 in the Province of New Hampshire, in which men of the towns of Exeter and Hampton took up arms against the Royal Governor, Edward Cranfield.  The rebels were arrested while attempting to muster more rebels.  The leader, Edward Gove, was sentenced to death for high treason, and shipped off to London for sentencing.  He was pardoned three years later by James II and returned to New Hampshire.  The rebellion took place during a period when many American colonists were rebelling against their respective provincial governments, including Bacon's Rebellion, Coode's Rebellion, Leisler's Rebellion, Culpeper's Rebellion, and the Boston Revolt.

Question: what revolution led to the overthrow of King James II of England and its news led to overthrow of androws in the Boston Revolt

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "revolution_name": {
      "type": "string",
      "description": "The name of the revolution that led to the overthrow of King James II."
    },
    "overthrown_monarch": {
      "type": "string",
      "description": "The name of the monarch overthrown by the revolution."
    },
    "related_colonial_event": {
      "type": "string",
      "description": "The name of the colonial event that occurred after news of the revolution."
    },
    "colonial_governor_overthrown": {
      "type": "string",
      "description": "The name of the colonial governor overthrown during the related colonial event."
    }
  },
  "required": [
    "revolution_name",
    "overthrown_monarch",
    "related_colonial_event",
    "colonial_governor_overthrown"
  ],
  "additionalProperties": false
}

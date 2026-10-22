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
Sir John Baker, 2nd Baronet: Sir John Baker, 2nd Baronet (c. 1608 – 15 January 1653) was an English politician who sat in the House of Commons of England in 1640.  He supported the Royalist side in the English Civil War.

English Civil War: The English Civil War (1642–1651) was a series of armed conflicts and political machinations between Parliamentarians ("Roundheads") and Royalists ("Cavaliers") over, principally, the manner of England's government.  The first (1642–1646) and second (1648–1649) wars pitted the supporters of King Charles I against the supporters of the Long Parliament, while the third (1649–1651) saw fighting between supporters of King Charles II and supporters of the Rump Parliament.  The war ended with the Parliamentarian victory at the Battle of Worcester on 3 September 1651.

John Harrison (died 1669): Sir John Harrison (c. 1590 – 28 September 1669) was an English politician who sat in the House of Commons variously between 1640 and 1669.  He supported the Royalist side in the English Civil War.

John Strangways (died 1666): Sir John Strangways (27 September 1585 – 30 December 1666) was an English politician who sat in the House of Commons variously between 1614 and 1666.  He supported the Royalist side in the English Civil War

Sir John Jacob, 1st Baronet: Sir John Jacob, 1st Baronet of Bromley (c. 1597 –1666), was an English politician who sat in the House of Commons in 1640 and 1641.  He supported the Royalist side in the English Civil War.

Richard Harrison (Royalist): Sir Richard Harrison (31 August 1583 – 5 May 1655) was an English politician who sat in the House of Commons variously between 1621 and 1640.  He supported the Royalist side in the English Civil War.

First English Civil War: The First English Civil War (1642–1646) began the series of three wars known as the English Civil War (or "Wars").  "The English Civil War" was a series of armed conflicts and political machinations that took place between Parliamentarians and Royalists from 1642 until 1651, and includes the Second English Civil War (1648–1649) and the Third English Civil War (1649–1651).

Battle of Hopton Heath: The Battle of Hopton Heath, in Staffordshire, was a battle of the First English Civil War, fought on Sunday 19 March 1643 between Parliamentarian forces led by Sir John Gell, 1st Baronet and Sir William Brereton and a Royalist force under Spencer Compton, 2nd Earl of Northampton.  The battle ended at nightfall, with the victory remaining a matter of opinion: that the Parliamentarian foot were still in position at nightfall when, as the Royalists themselves admitted, they drew back a little; or that next morning the Royalists occupied the field after the Parliamentarians retreated in the night.  The Royalists had captured eight guns, but the Parliamentarians considered their killing of the enemy commander, the Earl of Northampton, of equal significance.

Sir John Stepney, 3rd Baronet: Sir John Stepney, 3rd Baronet (1618c.  1676) was a Welsh politician who sat in the House of Commons from 1640 to 1643.  He supported the Royalist side in the English Civil War.

Sir John Wolstenholme, 1st Baronet: Sir John Wolstenholme, 1st Baronet (died 1670) was an English politician who sat in the House of Commons in 1640.  He supported the Royalist side in the English Civil War.

Question: Sir John Harrison supported the Royalist side of the English Civil War and these Royalists were also known by what other name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "supported_side": {
      "type": "string",
      "description": "The side supported by the person in the conflict."
    },
    "conflict_name": {
      "type": "string",
      "description": "The name of the historical conflict."
    },
    "alternative_name_for_supported_side": {
      "type": "string",
      "description": "The alternative name for the supported side as found in the context."
    }
  },
  "required": [
    "person_name",
    "supported_side",
    "conflict_name",
    "alternative_name_for_supported_side"
  ],
  "additionalProperties": false
}

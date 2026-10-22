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
Régiment de La Fère: Le Régiment de La Fère was a regiment of infantry of the Kingdom of France, formed in 1645 as the Régiment de Mazarin-Français.  It was renamed in 1661, and during the French Revolution it became the 52nd Line Infantry Regiment ("52e régiment d’infanterie de ligne").  In 1794, its 2nd Battalion became part of the "104e demi-brigade de bataille", and it ceased to exist when its 1st Battalion was made part of the "103e demi-brigade de bataille".  Its traditions are continued by the 52nd Infantry Regiment.

Queen's Own Royal West Kent Regiment: The Queen's Own Royal West Kent Regiment was a line infantry regiment of the British Army in existence from 1881 to 1961.  The regiment was created on 1 July 1881 as part of the Childers Reforms, originally as the Queen's Own (Royal West Kent Regiment), by the amalgamation of the 50th (Queen's Own) Regiment of Foot and the 97th (The Earl of Ulster's) Regiment of Foot.  In January 1921, the regiment was renamed the Royal West Kent Regiment (Queen's Own) and, in April of the same year, was again renamed, this time as the Queen's Own Royal West Kent Regiment.

Worcestershire Regiment: The Worcestershire Regiment was a line infantry regiment in the British Army, formed in 1881 under the Childers Reforms by the amalgamation of the 29th (Worcestershire) Regiment of Foot and the 36th (Herefordshire) Regiment of Foot.  The regiment fought in many conflicts, including both the First and Second World Wars, until 1970, when it was amalgamated with the Sherwood Foresters (Nottinghamshire and Derbyshire Regiment) to form the Worcestershire and Sherwood Foresters Regiment (29th/44th Foot).  In September 2007, the regiment amalgamated with the Cheshire Regiment and the Staffordshire Regiment (Prince of Wales's) to form the Mercian Regiment.

Gordon Holmes Alexander MacMillan: General Sir Gordon Holmes Alexander MacMillan of MacMillan and Knap, (7 January 1897 – 21 January 1986) was a professional soldier who rose to become a general in the British Army.  As a young officer during the First World War, he displayed outstanding bravery and was awarded a Military Cross and two Bars.  At the age of 19 and while still a second lieutenant, he was appointed acting adjutant of the 2nd Battalion, Argyll and Sutherland Highlanders.  Between the World Wars, MacMillan remained in the army, occupying posts of increasing seniority.  He married Marian Blakiston Houston in 1929, and they had one daughter and four sons.

Argyll and Sutherland Highlanders: The Argyll and Sutherland Highlanders (Princess Louise's) was a line infantry regiment of the British Army that existed from 1881 until amalgamation into the Royal Regiment of Scotland in March 2006.

Queen's Royal Regiment (West Surrey): The Queen's Royal Regiment (West Surrey) was a line infantry regiment of the English and later the British Army from 1661 to 1959.  It was the senior English line infantry regiment of the British Army, behind only the Royal Scots in the British Army line infantry order of precedence.

Royal Sussex Regiment: The Royal Sussex Regiment was a line infantry regiment of the British Army that was in existence from 1881 to 1966.  The regiment was formed in 1881 as part of the Childers Reforms by the amalgamation of the 35th (Royal Sussex) Regiment of Foot and the 107th Regiment of Foot (Bengal Light Infantry).  The regiment saw service in the Second Boer War, and both World War I and World War II.

East Lancashire Regiment: The East Lancashire Regiment was, from 1881 to 1958, a line infantry regiment of the British Army.  The regiment was formed in 1881 under the Childers Reforms by the amalgamation of the 30th (Cambridgeshire) Regiment of Foot and 59th (2nd Nottinghamshire) Regiment of Foot with the militia and rifle volunteer units of eastern Lancashire.  In 1958 the regiment was amalgamated with the South Lancashire Regiment to form the Lancashire Regiment which was, in 1970, merged with the Loyal Regiment (North Lancashire) to form the Queen's Lancashire Regiment.  However, in 2006, the Queen's Lancashire were amalgamated with the King's Own Royal Border Regiment and the King's Regiment (Liverpool and Manchester) to form the present Duke of Lancaster's Regiment (King's, Lancashire and Border).

York and Lancaster Regiment: The York and Lancaster Regiment was a line infantry regiment of the British Army that existed from 1881 until 1968.  The regiment was created in the Childers Reforms of 1881 by the amalgamation of the 65th (2nd Yorkshire, North Riding) Regiment of Foot and the 84th (York and Lancaster) Regiment of Foot.  The regiment saw service in many small conflicts and both World War I and World War II until 1968 when the regiment chose to be disbanded rather than amalgamated with another regiment, one of only two infantry regiments in the British Army to do so, with the other being the Cameronians (Scottish Rifles).

Royal Hampshire Regiment: The Hampshire Regiment was a line infantry regiment of the British Army, created as part of the Childers Reforms in 1881 by the amalgamation of the 37th (North Hampshire) Regiment of Foot and the 67th (South Hampshire) Regiment of Foot.  The regiment existed continuously for 111 years and served in the Second Boer War, World War I and World War II.  In 1946, due to distinguished service in World War II, the regiment was retitled as the Royal Hampshire Regiment.

Question: When did the line infantry regiment that Gordon Holmes Alexander MacMillan was appointed acting adjunct to cease to exist due to amalgamation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "regiment_name": {
      "type": "string",
      "description": "The name of the line infantry regiment."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event that led to the regiment ceasing to exist."
    },
    "cessation_date": {
      "type": "string",
      "description": "The date when the regiment ceased to exist."
    },
    "amalgamated_into_regiment": {
      "type": "string",
      "description": "The name of the regiment it amalgamated into."
    }
  },
  "required": [
    "regiment_name",
    "event_type",
    "cessation_date",
    "amalgamated_into_regiment"
  ],
  "additionalProperties": false
}

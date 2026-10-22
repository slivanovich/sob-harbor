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
John W. King: John William King (October 10, 1918 – August 9, 1996) was an American lawyer, jurist, and Democratic politician from Manchester, New Hampshire.  He received his law degree from Columbia Law School in 1943.  He practiced law in Manchester and served in the New Hampshire House of Representatives.  In 1962 he was elected Governor of New Hampshire, becoming only the third Democratic Governor of the Granite State in 88 years, and the first since Fred Herbert Brown lost the 1924 election.  After his three terms as Governor of New Hampshire, he served on the New Hampshire Supreme Court from 1979, and as its Chief Justice from 1981 until 1986.

Chris Spirou: Chris Spirou is a politician in New Hampshire in the United States.  He was born in the town of Porti in the Prefecture of Karditsa, Province of Thessaly, Greece, and migrated in 1956, at the age of 13, to the United States of America.  He is a graduate of Saint Anselm College, Goffstown, New Hampshire, and holds a Master's Degree in Urban Studies and Social Change from Goddard College, Vermont.  Spirou lectured in many universities including Harvard University and Dartmouth College and has taught the course as an adjunct professor at New Hampshire College (now Southern New Hampshire University).  In 1970 he was elected to the New Hampshire House of Representatives.  He has been New Hampshire Democratic Party Chairman and was a Democratic nominee for governor.

Vesta M. Roy: Vesta M. Roy (née Coward ; March 26, 1925February 9, 2002) was a Republican New Hampshire politician.  She was the first woman to serve as both the President of the New Hampshire Senate and Governor of New Hampshire.  She began her brief time as Acting Governor of New Hampshire when the sitting governor fell ill and died prior to the end of his term.

List of colonial governors of New Hampshire: The territory of the present United States state of New Hampshire has a colonial history dating back to the 1620s.  This history is significantly bound to that of the neighboring Massachusetts, whose colonial precursors either claimed the New Hampshire territory, or shared governors with it.  First settled in the 1620s under a land grant to John Mason, the colony consisted of a small number of settlements near the seacoast before growing further inland in the 18th century.  Mason died in 1635, and the colonists appropriated a number of his holdings.  Thomas Roberts served as the last Colonial Governor of the Dover Colony before it became part of the Massachusetts Bay Colony.  In 1641 the New Hampshire colonists agreed to be ruled by Massachusetts Bay Colony, which also claimed the territory.  Massachusetts governed the New Hampshire settlements until 1680, when it became the royally chartered Province of New Hampshire.  In 1686 the territory became part of the Dominion of New England, which was effectively disbanded in 1689 following the 1688 Glorious Revolution in England.  After an interregnum under "de facto" rule from Massachusetts, Samuel Allen, who had acquired the Mason land claims, became governor.  From 1699 to 1741 the governorships of New Hampshire and the Province of Massachusetts Bay were shared.

Samuel Bell: Samuel Bell (February 9, 1770December 23, 1850) was an American politician and lawyer who served as the 14th Governor of New Hampshire from 1819 to 1823, and as the United States Senator for New Hampshire from 1823 to 1835.  Born in Londonderry in the Province of New Hampshire, Bell became a lawyer in the 1790s, and entered politics by becoming a member of the New Hampshire House of Representatives in 1804.  In 1806, the year he left the House, he became the head of a bank which during his tenure in that position became the only New Hampshire bank to fail between 1792 and 1840.  A member of the New Hampshire Senate from 1807 to 1809, and an associate justice of the New Hampshire Supreme Court from 1816 to 1819, Bell was elected to become the Governor of New Hampshire in 1819 as Democratic-Republican.  Re-elected in 1820, 1821, and 1822 against token opposition, Bell's victory in 1822 was accompanied by the largest share of votes cast for a governor candidate of New Hampshire since John Taylor Gilman's victory in 1795.  Whilst Governor, New Hampshire's crime level fell, and industry within the state prospered.  In 1823, declining to stand again for the governorship, he became a Senator for New Hampshire.  He won re-election in 1829, was the chairman of the United States Senate Committee on Claims, and left the Senate in 1835.  He retired from public life thereafter, and died in Chester, New Hampshire at the age of 80.  He is buried in Chester Village Cemetery, Rockingham, New Hampshire.

Frank W. Rollins: Frank West Rollins (February 24, 1860 – October 27, 1915) was an American lawyer, banker, and Republican politician from Concord, New Hampshire.  His father, Edward H. Rollins, had represented New Hampshire in the United States Senate.  Frank served New Hampshire in the state's Senate (as its president in 1895) and as governor.  Rollins and others founded the Society for the Protection of New Hampshire Forests in 1901, a private organization to protect the forests now known as the "Forest Society."  A shelter was built in his honor at Lost River in Kinsman Notch, New Hampshire in 1912, and remains there.  As Governor of New Hampshire, he invented and founded "Old Home Week" intended to remind New Hampshiremen to return to their hometowns.  This was in response to the large numbers of people moving to the Midwest (Minnesota in particular) because of the slow economy in the northeast at the time.  He and his father started the investment banking firm of E.H. Rollins and Sons, which became one of the largest in the country by the crash of 1929.  After the crash, it was very diminished and finally closed in the 1940s.  New research shows that Rollins and Senator John Weeks collaborated on the founding of the National Forest Act of 1911, signed by the President William Howard Taft.

Executive Council of New Hampshire: The Executive Council of the State of New Hampshire (commonly known as the Governor's Council) is the executive body of the U.S. state of New Hampshire.  The Executive Council advises the Governor on all matters and provides a check on the governor's power.  While the governor retains the right to veto legislation passed by the New Hampshire General Court, and commands the New Hampshire National Guard, the council has veto power over pardons, contracts with a value greater than $10,000, and nominations.  The Executive Council Chambers have been located in the New Hampshire State House since the chambers were added to the capitol in 1909.

Joseph Foster: Joseph A. Foster (born June 10, 1959) is the former Attorney General of the State of New Hampshire.  He was formerly a Democratic member of the New Hampshire Senate, representing the 13th District from 2002 until 2008 and served as the State Senate Majority Leader in 2007 and 2008.  Previously he was a member of the New Hampshire House of Representatives from 1994 through 1998.  On April 17, 2013 he was confirmed to the office of Attorney General.  He took office on May 15, 2013, succeeding Michael A. Delaney who decided not to seek reappointment by Governor Maggie Hassan at the end of his term, and instead took Foster's old position at his law firm.  Foster is considered a potential future Congressional candidate.

Michael Delaney (lawyer): Michael A. "Mike" Delaney (born July 19, 1969) is an American lawyer and former Attorney General of New Hampshire.  Delaney was appointed to the office of Attorney General by Governor John H. Lynch in August 2009.  He decided not to seek reappointment by Governor Maggie Hassan at the end of his term in 2013, instead taking a position at the McLane Law Firm.

Jack Delaney (musician): Jack Michael Delaney (August 27, 1930, New Orleans - September 22, 1975, New Orleans) was an American jazz trombonist, active principally in the New Orleans jazz scene.

Question: Which governor of New Hampshire attempted to reappoint Michael Delaney?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "governor_name": {
      "type": "string",
      "description": "The name of the New Hampshire governor."
    },
    "attorney_general_name": {
      "type": "string",
      "description": "The name of the Attorney General involved in the reappointment."
    },
    "reappointment_status": {
      "type": "string",
      "description": "The outcome of the reappointment attempt (e.g., 'declined', 'sought')."
    }
  },
  "required": [
    "governor_name",
    "attorney_general_name",
    "reappointment_status"
  ],
  "additionalProperties": false
}
